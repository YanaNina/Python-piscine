class Vector:
    def __init__(self, arg):
        if isinstance(arg, list):
            self.values = arg
            self.size = len(self.values)
        elif isinstance(arg, int):
            self.size = arg
            self.values = list(range(arg))
            for i in self.values:
                self.values[i] = float(i)
        else:
            self.values = list(range(arg[0], arg[1]))
            self.size = len(self.values)

    def __str__(self):
        return f'(Vector {self.values})'


    def __add__(self, other):
        result = []
        if isinstance(other, float):
            for i in self.values:
                result.append(i + other)
            return Vector(result)
        elif isinstance(other, Vector) and other.size == self.size:
            for i in range(other.size):
                result.append(other.values[i] + self.values[i])
            return Vector(result)
        else:
            raise TypeError("Vectors are different size")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        result = []
        if isinstance(other, float):
            for i in self.values:
                result.append(i - other)
            return Vector(result)
        elif isinstance(other, Vector) and other.size == self.size:
            for i in range(other.size):
                result.append(self.values[i] - other.values[i])
            return Vector(result)
        else:
            raise TypeError("Vectors are different size")

    def __rsub__(self, other):
        a = self - other
        result = []
        for i in a.values:
            result.append(i * -1)
        return result

    def __truediv__(self, other):
        result = []
        if isinstance(other, float):
            for i in self.values:
                result.append(i / other)
            return Vector(result)
        elif isinstance(other, Vector) and other.size == self.size:
            for i in range(other.size):
                result.append(self.values[i] / other.values[i])
            return Vector(result)
        else:
            raise TypeError("Vectors are different size")




v = Vector((10,13))
t = Vector((5,8))
# print(v.size)

# print(v.__add__(t))
print(v / t)
# print(t + v)