class AdaptiveSearch:
    def compute_ef(self, target_recall):
        return max(32, int(target_recall * 100))
