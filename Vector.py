class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        sum = []
        for i in range(len(self.coordinates)):
            sum.append(self.coordinates[i] + v.coordinates[i])
        return sum

    def __sub__(self, v):
        sum = []
        for i in range(len(self.coordinates)):
            sum.append(self.coordinates[i] - v.coordinates[i])
        return sum

    def __mul__(self, multiplier):
        return [dim * multiplier for dim in self.coordinates]


a = Vector([8.218, -9.341])
b = Vector([-1.129, 2.111])
print(a + b)


# a = Vector([7.119, 8.215])
# b = Vector([-8.223, 0.878])
# print(a - b)


# a = Vector([1.671, -1.012, -0.318])

# print(a * 7.41)