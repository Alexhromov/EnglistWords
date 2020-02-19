class A:
    x = 5

    def f(self): pass


class B(A):

    def f(self):
        super().f()
