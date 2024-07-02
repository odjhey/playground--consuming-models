import pickle
from model_1 import Model

model = Model()
model.some_state = "wataaa"

with open("out/model1.pkl", "wb") as f:
    pickle.dump(model, f)
