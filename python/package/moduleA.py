import sys

from subpackage1 import moduleX, moduleY
from subpackage2 import moduleZ


def main():
    print(sys.path)
    print('Module A')
    moduleX.main()
    moduleY.main()
    moduleZ.main()

    my_A = A(a=1, b=2)
    my_B = my_A.do()
    print(my_B.a)
    print(my_B.b)
    print(my_B.c)


class A(object):
    def __init__(self, **kwargs):
        # Non pythonic and a bit of a hack
        self.kwargs = kwargs
        vars(self).update(kwargs)

    def do(self):
        c = self.a + self.b
        return B(self.kwargs, c=c)


class B(A):
    def __init__(self, kwargs, c):
        self.c = c
        super(B, self).__init__(**kwargs)


if __name__ == "__main__":
    main()
