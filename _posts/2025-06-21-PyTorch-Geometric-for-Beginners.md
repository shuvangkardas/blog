---
title: "PyTorch Geometric for Beginners: Create, Visualize, and Train on Graph Data"
permalink: pyg-basics-create-visualize-train
date: 2025-06-21
excerpt: A beginner-friendly guide to get started with PyTorch Geometric. Learn how to create graphs, visualize them, prepare your dataset, and build a simple GCN model — all in one place.
type: Blog
categories: 
tags: 
status:
---

If you're just starting out with graph neural networks using PyTorch Geometric (PyG), it can feel overwhelming. This post shares my practical notes on how to create a graph, visualize it, set up the dataset, and build a simple model using PyG. I’ve kept it minimal and functional—just enough to get you up and running.

---

## 1. What `model.train()` and `model.eval()` Really Mean

```python
model.train()  # Tells the model you’re training (activates dropout, batch norm, etc.)
model.eval()   # Tells the model you’re evaluating (deactivates training-only layers)
```

These do not train or evaluate the model themselves. They only change the internal behavior of layers.

---

## 2. Create a Single Graph

```python
import torch
from torch_geometric.data import Data

# Define edges in COO format
edges = [[0, 1, 1, 2, 0, 2], [1, 0, 2, 1, 2, 0]]
edge_index = torch.tensor(edges, dtype=torch.long)

# Node features (3 nodes, 2 features each)
x = torch.tensor([[2, 3], [-1, 2], [-4, 1]], dtype=torch.float)

# Create the data object
data = Data(x=x, edge_index=edge_index)
print(data)
# Output: Data(x=[3, 2], edge_index=[2, 6])
```

You can freely add new attributes to the `Data` object as needed.

---
## 3. Visualize the Graph

```python
import networkx as nx
from torch_geometric.utils import to_networkx

G = to_networkx(data)
nx.draw(G, with_labels=True)
```

Visualizing the structure often helps understand how nodes are connected.

![Image](/assets/images/Pasted-image-20250621074703.png)

---
## 4. Generate Adjacency Matrix

```python
from torch_geometric.transforms import ToDense
import copy

dataTest = copy.deepcopy(data)
ToDense(num_nodes=3)(dataTest)
print(dataTest.adj)
```

Useful for checking consistency between the adjacency matrix and the feature matrix.

---

## 5. Random Train/Val/Test Split

```python
from torch_geometric.transforms import RandomNodeSplit

split = RandomNodeSplit(split="train_rest", num_val=0.3, num_test=0.6)
data = split(data)

print(torch.sum(data.train_mask).item())
print(torch.sum(data.val_mask).item())
print(torch.sum(data.test_mask).item())
```

Adds `train_mask`, `val_mask`, and `test_mask` to your `Data` object.

---

## 6. Build a Simple GCN Model

```python
from torch.nn import Linear
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, in_features, out_classes):
        super().__init__()
        self.conv1 = GCNConv(in_features, 4)
        self.conv2 = GCNConv(4, 4)
        self.conv3 = GCNConv(4, 2)
        self.classifier = Linear(2, out_classes)

    def forward(self, x, edge_index):
        h = self.conv1(x, edge_index).tanh()
        h = self.conv2(h, edge_index).tanh()
        h = self.conv3(h, edge_index).tanh()
        return self.classifier(h), h
```

---

## 7. Training Function

```python
import torch.nn.functional as F

def train(model, data, optimizer):
    model.train()
    optimizer.zero_grad()
    out, _ = model(data.x, data.edge_index)
    loss = F.cross_entropy(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    return loss.item()
```

Use `CrossEntropyLoss` if your model outputs raw logits.

---

## 8. Run Training Loop

```python
model = GCN(data.num_features, num_classes=4)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(200):
    loss = train(model, data, optimizer)
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")
```

---

## 9. Count Trainable Parameters

```python
print("Trainable params:", sum(p.numel() for p in model.parameters() if p.requires_grad))
```

---

## Final Thoughts

This note doesn't cover everything but touches the key steps: how to create a graph, visualize it, prepare data, and build a simple GCN model. If you're just starting out with PyG, I hope this helps get you past the initial barrier.



---
### 👋 About Me
Hi, I’m **Shuvangkar Das**, a power systems researcher with a Ph.D. in Electrical Engineering from Clarkson University. I work at the intersection of power electronics, DER, IBR, and AI — building greener, smarter, and more stable grids. Currently, I’m a Research Engineer at EPRI (though everything I share here reflects my personal experience, not my employer’s views).

Over the years, I’ve worked on real-world projects involving large scale EMT simulation and firmware development for  grid-forming and grid following inverter and reinforcement learning (RL). I also publish technical content and share hands-on insights with the goal of making complex ideas accessible to engineers and researchers.

📺 Subscribe to my [YouTube channel](https://www.youtube.com/@ShuvangkarDas), where I share tutorials, code walk-throughs, and research productivity tips.

<p><strong>Connect with me:<br></strong>
<a href="https://www.youtube.com/@ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube">
  </a>
  <a href="https://www.linkedin.com/in/ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
  </a>
  <a href="https://newsletter.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Newsletter-Subscribe-blue?style=for-the-badge">
  </a>
  <a href="https://twitter.com/shuvangkar_das" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-Follow-blue?style=for-the-badge&logo=twitter">
  </a>
  
  <a href="https://github.com/shuvangkardas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github">
  </a>
  <a href="https://blog.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Blog-Read-blueviolet?style=for-the-badge">
  </a>
  
</p>

### 📚References
[[PyG Fundamental]]
[[PyG Resource]]



