import math

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
        new_coords = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)

    def __sub__(self, v):
        new_coords = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coords)

    def __mul__(self, multiplier):
        print('multiplier', multiplier)
        new_coords = [dim * multiplier for dim in self.coordinates]
        return Vector(new_coords)

    def magnitude(self):
        return math.sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalized(self):
        try:
            return self.__mul__(1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


# a = Vector([8.218, -9.341])
# b = Vector([-1.129, 2.111])
# print(a + b)


# a = Vector([7.119, 8.215])
# b = Vector([-8.223, 0.878])
# print(a - b)


# a = Vector([1.671, -1.012, -0.318])
# print(a * 7.41)

# a = Vector([-0.221, 7.437])
# print(a.mag())

# a = Vector([8.813, -1.331, -6.247])
# print(a.mag())

a = Vector([1.996, 3.108, -4.554])
print(a.normalized())
