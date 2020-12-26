class LCG:
    """ Linear Congenital Generator algorithm """

    def __init__(self, seed, multiplier, increment, modulus):
        """ initialize variables """

        self.seed, self.multiplier, self.increment, self.modulus = seed, multiplier, increment, modulus
        self.initGen()

    def getSeed(self):
        """ get seed value """

        return self.seed

    def setSeed(self, val):
        """ set seed value """

        self.seed = val

    def initGen(self):
        """ initialize the generator (start from the seed) """

        self.start = self.seed

    def rand(self):
        """ generate next random number """

        self.start = (self.multiplier * self.start +
                      self.increment) % self.modulus

        return self.start / self.modulus

    # ref: https://stackoverflow.com/questions/19140589/linear-congruential-generator-in-python

    def rand_array(self, length):
        """ returns a sequence (list) of random number """
        return [self.rand() for val in range(length)]


class SCG(LCG):

    """ Recursive Congruential Generator """

    def __init__(self, seed, multiplier, increment, modulus):

        # seed value check
        if (seed % 4 != 2):
            raise ValueError(
                "the seed of this generator did not satisfy X to base 0 mod 4 = 2")

        # inherit LCG init
        super().__init__(seed, multiplier, increment, modulus)

    def rand(self):
        """ generate next random number """

        self.start = (self.start * (self.start + 1)) % self.modulus
        return self.start / self.modulus


if __name__ == "__main__":

    # LCG TEST 1
    r1 = LCG(1, 1103515245, 12345, 2**32)
    print("\nLCG TEST 1\n")
    print(r1.rand_array(3))

    # LCG TEST 2
    r2 = LCG(1, 1140671485, 128201163, 2**24)
    print("\nLCG TEST 2\n")
    print(r2.rand_array(3))

    # SCG TEST 1
    r1 = SCG(6, 1103515245, 12345, 2**32)
    print("\nSCG TEST 1\n")
    print(r1.rand_array(3))

    # SCG TEST 2
    r2 = SCG(6, 1140671485, 128201163, 2**24)
    print("\nSCG TEST 2\n")
    print(r2.rand_array(3))
