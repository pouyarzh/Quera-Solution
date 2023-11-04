class Foo:
    def __init__(self):
        self._x = 0

    # using property decorator
    # a getter function
    @property
    def x(self):
        # print("getter method called")
        return self._x

    # a setter function
    @x.setter
    def x(self, a):
        if (a >= 0):
            self._x = abs(a) % 100
        else:
            self._x = -1
        # print("setter method called")



if __name__ == "__main__":
    test = Foo()
    test.x = 6874
    print(test.x)
