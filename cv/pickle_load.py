import pickle

with open('font_pca_model.pkl', 'rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)

print(V)
