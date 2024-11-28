import torch
import torch.nn as nn
import torch.nn.functional as F
import os

# Hyperparameters
device = 'cuda' if torch.cuda.is_available() else 'cpu'
batch_size = 64
block_size = 256
max_iters = 2000 # max iterations of training loop
learning_rate = 3e-4
eval_interval = 100
n_embd = 256 # embedding_vector = [0.1,0.2,0.8,1.1,...(256 values)]
n_head = 8 # how many heads of attention
n_layer = 4 # 4 decoder blocks
dropout = 0.1 # rate at which random nodes in the network are dropped duringt training so we don't overfit

# Load and preprocess data
with open("source.txt", 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)

# Create encoding/decoding mappings
string_to_int = {ch: i for i, ch in enumerate(chars)}
int_to_string = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [string_to_int[c] for c in s]
decode = lambda l: ''.join([int_to_string[i] for i in l])

# Encode the entire text dataset
data = torch.tensor(encode(text), dtype=torch.long)

# Split data into training and validation sets
n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]

# Data loader function
def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i + block_size] for i in ix])
    y = torch.stack([data[i + 1:i + block_size + 1] for i in ix])
    return x.to(device), y.to(device)

# Define the GPT-like model
class GPTLanguageModel(nn.Module):
    def __init__(self, vocab_size, n_embd, n_head, n_layer):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, n_embd)
        self.position_embedding = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding(idx)
        pos_emb = self.position_embedding(torch.arange(T, device=device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            return logits, None
        B, T, C = logits.shape
        logits = logits.view(B * T, C)
        targets = targets.view(B * T)
        loss = F.cross_entropy(logits, targets)
        return logits, loss

    def generate(self, idx, max_new_tokens):
        # Ensure input is not longer than block_size
        if idx.shape[1] > block_size:
            idx = idx[:, -block_size:]

        for _ in range(max_new_tokens):
            # If the input exceeds block_size, truncate it
            if idx.shape[1] > block_size:
                idx = idx[:, -block_size:]

            # Get the logits from the model
            logits, _ = self(idx)

            # Extract the logits for the last token
            logits = logits[:, -1, :]

            # Convert logits to probabilities
            probs = F.softmax(logits, dim=-1)

            # Sample the next token
            idx_next = torch.multinomial(probs, num_samples=1)

            # Append the sampled token to the input sequence
            idx = torch.cat((idx, idx_next), dim=1)

        return idx

class Block(nn.Module):
    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x

class MultiHeadAttention(nn.Module):
    def __init__(self, n_head, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(n_head)])
        self.proj = nn.Linear(head_size * n_head, n_embd)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        return self.proj(out)

class Head(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.tril = torch.tril(torch.ones(block_size, block_size)).to(device)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        v = self.value(x)
        wei = q @ k.transpose(-2, -1) * (C ** -0.5)
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        wei = F.softmax(wei, dim=-1)
        return wei @ v

class FeedForward(nn.Module):
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
        )

    def forward(self, x):
        return self.net(x)

def load_trained_model():
    model = GPTLanguageModel(vocab_size,n_embd,n_head,n_layer).to(device)
    # loading trained weights
    model.load_state_dict(torch.load('gpt_model.pth', map_location=device))
    model.eval()
    return model

if __name__ == "__main__":
    # Initialize the model and optimizer
    model = GPTLanguageModel(vocab_size, n_embd, n_head, n_layer).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    # Training loop
    for iter in range(max_iters):
        if iter % eval_interval == 0:
            model.eval()
            optimizer.zero_grad()
            xb, yb = get_batch('validate')
            logits, loss = model(xb, yb)
            print(f"Step {iter}, Loss: {loss.item()}")
            model.train()
            continue
        xb, yb = get_batch('train')
        logits, loss = model(xb, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Save the trained model
    torch.save(model.state_dict(), 'gpt_model.pth')
    print("Model saved!")