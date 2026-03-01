from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Models
# -----------------------------

class Edge(BaseModel):
    source: str
    target: str


class Node(BaseModel):
    id: str


class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


# -----------------------------
# DAG Logic
# -----------------------------

from collections import defaultdict, deque

def is_dag(nodes, edges):
    adjacency = defaultdict(list)
    indegree = defaultdict(int)

    for node in nodes:
        indegree[node.id] = 0

    for edge in edges:
        adjacency[edge.source].append(edge.target)
        indegree[edge.target] += 1

    queue = deque([node.id for node in nodes if indegree[node.id] == 0])

    visited_count = 0

    while queue:
        current = queue.popleft()
        visited_count += 1

        for neighbor in adjacency[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count == len(nodes)


# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.post("/pipelines/parse")
def parse_pipeline(pipeline: Pipeline):

    print("NODES:", [n.id for n in pipeline.nodes])
    print("EDGES:", pipeline.edges)

    node_count = len(pipeline.nodes)
    edge_count = len(pipeline.edges)

    dag_result = is_dag(pipeline.nodes, pipeline.edges)

    return {
        "num_nodes": node_count,
        "num_edges": edge_count,
        "is_dag": dag_result
    }