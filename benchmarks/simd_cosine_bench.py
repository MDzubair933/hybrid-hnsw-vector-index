# HNSW Cosine Similarity Vectorization Benchmark
import time
import numpy as np

def benchmark_cosine_similarity(dim=1536, n_vectors=10000):
    vecs = np.random.randn(n_vectors, dim).astype(np.float32)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    normalized = vecs / norms
    query = np.random.randn(1, dim).astype(np.float32)
    query /= np.linalg.norm(query)
    
    start = time.perf_counter()
    scores = np.dot(normalized, query.T)
    duration_ms = (time.perf_counter() - start) * 1000.0
    print(f"Computed {n_vectors} cosine scores in {duration_ms:.2f}ms")

if __name__ == '__main__':
    benchmark_cosine_similarity()
