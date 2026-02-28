
---

# 📁 backend/README.md


# Backend – DAG Validation Service

## Overview

This backend service validates whether a submitted directed graph is a Directed Acyclic Graph (DAG).

It receives:

- List of nodes
- List of edges

And returns:

```json
{
  "num_nodes": number,
  "num_edges": number,
  "is_dag": boolean
}