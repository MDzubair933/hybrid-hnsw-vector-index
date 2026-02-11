def batch_insert(index, items):
    for doc_id, vec in items: index.insert(doc_id, vec)
