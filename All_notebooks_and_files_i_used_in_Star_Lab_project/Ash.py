import pickle

def afs_open(data_path: str):
    afs_labels = pickle.load(open(f"{data_path}", "rb"))


