import math
from collections import Counter

class BM25Index:
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = {}
        self.doc_lens = {}
        self.avg_len = 0

    def index_document(self, doc_id, text):
        tokens = text.lower().split()
        self.corpus[doc_id] = Counter(tokens)
        self.doc_lens[doc_id] = len(tokens)
        self.avg_len = sum(self.doc_lens.values()) / max(1, len(self.doc_lens))

    def search(self, query, k=10):
        query_tokens = query.lower().split()
        scores = {}
        for doc_id, tf_map in self.corpus.items():
            score = 0.0
            doc_len = self.doc_lens[doc_id]
            for token in query_tokens:
                if token in tf_map:
                    tf = tf_map[token]
                    idf = math.log((len(self.corpus) + 1) / (1 + 1))
                    term_score = idf * (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_len)))
                    score += term_score
            if score > 0:
                scores[doc_id] = score
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:k]
