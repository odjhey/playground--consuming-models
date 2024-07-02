class Model:
    def __init__(self):
        self.some_state = "some state"
        self.name = "Model1"
        self.version = 1

    def predict(self, data):
        return f"{self.name} v{self.version} prediction for {data} of {self.some_state}"
