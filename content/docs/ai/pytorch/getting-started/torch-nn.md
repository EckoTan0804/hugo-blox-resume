---
# Title, summary, and position in the list
# linktitle: ""
summary: "Important PyTorch modules and classes for creating and training neural networks."
weight: 140

# Basic metadata
title: "PyTorch Modules and Classes"
date: 2020-09-10
draft: false
 
authors: ["admin"]
tags: ["Deep Learning", "PyTorch"]
categories: ["Deep Learning"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true

comments: true  # Show comments?
disable_comment: false
commentable: true   # Allow visitors to comment?  

editable: false  # Allow visitors to edit the page?  

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""

---

## TL;DR

- `torch.nn`
  - `Module`: creates a callable which behaves like a function, but can also contain state(such as neural net layer weights). It knows what `Parameter` (s) it contains and can zero all their gradients, loop through them for weight updates, etc.
  - `Parameter`: a wrapper for a tensor that tells a `Module` that it has weights that need updating during backprop. Only tensors with the requires_grad attribute set are updated
  - `functional`: a module (usually imported into the `F` namespace by convention) which contains activation functions, loss functions, etc, as well as non-stateful versions of layers such as convolutional and linear layers.
- `torch.optim`: Contains optimizers such as `SGD`, which update the weights of `Parameter` during the backward step
- `Dataset`: An abstract interface of objects with a `__len__` and a `__getitem__`, including classes provided with Pytorch such as `TensorDataset`
- `DataLoader`: Takes any `Dataset` and creates an iterator which returns batches of data.

## Notebook

View in [nbviewer](https://nbviewer.jupyter.org/github/EckoTan0804/summay-pytorch/blob/master/pytorch-quick-start/06-what-is-torch_nn-exactly.ipynb)

## Reference

- [What is torch.nn *really*?](https://pytorch.org/tutorials/beginner/nn_tutorial.html#)