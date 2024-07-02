class Model:
    def __init__(self):
        self.name = "Model2"
        self.version = 2

    def predict(self, data):
        return f"{self.name} v{self.version} prediction for {data}"
