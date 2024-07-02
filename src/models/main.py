from model_1 import Model


def main():
    model = Model()
    data = "some data"
    prediction = model.predict(data)
    print(prediction)


if __name__ == "__main__":
    main()
