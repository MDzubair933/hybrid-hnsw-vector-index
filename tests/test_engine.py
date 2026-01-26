from engine.hnsw import HNSWIndex
from engine.bm25 import BM25Index
from engine.fusion import reciprocal_rank_fusion

def test_hybrid_flow():
    hnsw = HNSWIndex(dim=4)
    hnsw.insert("doc1", [0.1, 0.2, 0.3, 0.4])
    bm25 = BM25Index()
    bm25.index_document("doc1", "semantic search with vectors")
    assert len(hnsw.vectors) == 1
