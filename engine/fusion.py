def reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=60):
    rrf_score = {}
    for rank, doc_id in enumerate(dense_ranks):
        rrf_score[doc_id] = rrf_score.get(doc_id, 0.0) + (1.0 / (k + rank + 1))
    for rank, doc_id in enumerate(sparse_ranks):
        rrf_score[doc_id] = rrf_score.get(doc_id, 0.0) + (1.0 / (k + rank + 1))
    return sorted(rrf_score.items(), key=lambda x: x[1], reverse=True)
