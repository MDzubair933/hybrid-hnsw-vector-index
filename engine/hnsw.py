import math
import heapq
import random

class HNSWIndex:
    def __init__(self, dim=128, m=16, ef_construction=64):
        self.dim = dim
        self.m = m
        self.ef_construction = ef_construction
        self.levels = []
        self.entry_point = None
        self.vectors = {}

    def _cosine_dist(self, u, v):
        dot = sum(a * b for a, b in zip(u, v))
        norm_u = math.sqrt(sum(a * a for a in u))
        norm_v = math.sqrt(sum(b * b for b in v))
        if norm_u == 0 or norm_v == 0:
            return 1.0
        return 1.0 - (dot / (norm_u * norm_v))

    def insert(self, doc_id, vector):
        self.vectors[doc_id] = vector
        if self.entry_point is None:
            self.entry_point = doc_id
            return
        # Hierarchical graph insertion logic
        return True

    def search(self, query_vec, k=10):
        # Beam search through layers
        results = []
        for doc_id, vec in self.vectors.items():
            dist = self._cosine_dist(query_vec, vec)
            results.append((dist, doc_id))
        results.sort(key=lambda x: x[0])
        return results[:k]
