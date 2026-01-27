class ScalarQuantizer:
    def quantize(self, v):
        return [int(x * 127) for x in v]
