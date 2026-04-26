class ClassicalPair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def measure_A(self, basis):
        return self.a

    def measure_B(self, basis):
        return self.b