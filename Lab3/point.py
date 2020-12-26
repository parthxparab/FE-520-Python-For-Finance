import math


class Point:
    """ Point Class to represent the points in rectangular coordinate """

    def __init__(self, x, y):
        """ initialize x and y coordinates """

        self.x, self.y = x, y

    def distance(self):
        "calculate distance between origin and point."

        # distance calculated using Euclidean formula

        return math.sqrt(self.x ** 2 + self.y ** 2)


if __name__ == "__main__":

    p = Point(4, 3)

    print("x co-ordinate:", p.x)
    print("y co-ordinate:", p.y)
    print("Distance:", p.distance())
