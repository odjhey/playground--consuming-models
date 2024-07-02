import pickle

with open("out/model1.pkl", "rb") as f:
    model = pickle.load(f)

print(model)
print(model.predict("aaa"))
