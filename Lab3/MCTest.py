import generator
import point
import math
import time


def test(gen):
    num = 10 ** 7

    # selecting generator

    if (gen == "LCG"):
        rand = generator.LCG(1, 1103515245, 12345, 2**32)
    elif gen == "SCG":
        rand = generator.SCG(6, 1103515245, 12345, 2**32)

    # generating 2 * 10 ** 7 random numbers
    x, y = rand.rand_array(num), rand.rand_array(num)

    # re-scale points into [−1, 1]
    x, y = [(i-0.5) * 2 for i in x], [(i-0.5) * 2 for i in y]

    # pairing
    points = []

    for i, j in zip(x, y):
        points.append(point.Point(i, j))

    # calculate distance from origin
    count = 0

    for p in points:
        if p.distance() < 1:
            count += 1

    ratio = count/num

    # actual number
    real = math.pi / 4
    diff = abs(real - ratio)

    print("Estimate Ratio using", gen, ":", ratio)
    print("Theoretical value: ", real)
    print("Difference: ", diff)


if __name__ == "__main__":

    for gen in ("LCG", "SCG"):

        start = time.time()
        test(gen=gen)
        runtime = time.time() - start

        print("Time consumed: ", runtime, "seconds\n")
