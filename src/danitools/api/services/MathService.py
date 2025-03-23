from danitools.framework.utils.MathUtils import MathUtils


class MathService:
    def __init__(self):
        self._math = MathUtils()

    def add(self, a, b):
        return self._math.add(a, b)

    def subtract(self, a, b):
        return self._math.sub(a, b)

    def multiply(self, a, b):
        return self._math.mul(a, b)
