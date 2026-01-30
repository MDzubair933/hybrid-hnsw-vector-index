class MetadataFilter:
    def matches(self, meta, query):
        return all(meta.get(k) == v for k,v in query.items())
