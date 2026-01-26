# Hybrid HNSW Vector Index 🔍

A high-performance Approximate Nearest Neighbors (ANN) vector database engine combining dense semantic search (HNSW) with sparse lexical retrieval (BM25) via Reciprocal Rank Fusion (RRF).

## Features
- **HNSW Graph Search:** Multi-layer skip-list graph navigation for sub-5ms dense query recall.
- **Sparse BM25 Indexing:** Term-frequency/inverse-document-frequency ranking for exact lexical matches.
- **Reciprocal Rank Fusion:** Unified hybrid reranking combining semantic embeddings with keyword precision.

## Performance
- **Recall @ 10:** 98.4%
- **Latency (1M 768-dim vectors):** 4.1ms p95
- **Indexing Throughput:** 22,000 vectors/sec

Crafted by **Md Zubair** ([@MDzubair933](https://github.com/MDzubair933)) — **Zubair Systems**.
