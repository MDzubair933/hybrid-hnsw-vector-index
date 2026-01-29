import pickle
def save_index(index, path):
    with open(path, 'wb') as f: pickle.dump(index, f)
