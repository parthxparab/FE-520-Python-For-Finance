import numpy as np


class Rectangular:
    """ Class Rectangular to calculate area and perimeter """

    def __init__(self, length, width):
        """ initialization of length and width variable """
        self.length, self.width = length, width

    def area(self):
        """ function to return area of rectangle """

        return self.length * self.width

    def perimeter(self):
        """ function to return perimeter of rectangle """

        return (self.length + self.width) * 2


class Time:
    """ Class Time for simple time operations """

    def __init__(self, hours, minutes, seconds):
        """ initialization of hours, minutes and seconds """

        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def addTime(self, val):
        """ function to add two time objects """

        newHours, newMinutes, newSeconds = self.hours + \
            val.hours, self.minutes + val.minutes, self.seconds + val.seconds

        # minutes and seconds correction

        newMinutes, newSeconds = (
            newMinutes + newSeconds // 60), (newSeconds % 60)
        newHours, newMinutes = (newHours + newMinutes // 60), (newMinutes % 60)

        return Time(newHours, newMinutes, newSeconds)

    def displayTime(self):
        """ display time """

        print(self.hours, "hour(s)", self.minutes,
              "minute(s)", self.seconds, "second(s)")

    def displaySecond(self):
        """ display time in seconds"""

        print(self.hours * 3600 + self.minutes * 60 + self.seconds, "seconds")


if __name__ == "__main__":

    # REACTANGULAR TEST 1
    myRec = Rectangular(10, 20)
    print("REACTANGULAR TEST 1\n")
    print("Area: ", myRec.area())
    print("Perimeter: ", myRec.perimeter())

    # REACTANGULAR TEST 2
    length = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    width = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    myRec = Rectangular(length, width)
    print("\nREACTANGULAR TEST 2\n")
    print("Area: ", myRec.area())
    print("Perimeter: ", myRec.perimeter())

    # TIME TEST 1

    t1 = Time(2, 50, 10)
    t2 = Time(1, 20, 5)

    print("\nTIME TEST 1\n")
    res = t1.addTime(t2)
    res.displayTime()
    res.displaySecond()
