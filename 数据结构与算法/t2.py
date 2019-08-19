def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

a=C()
print(a.f(1,2))
print(a.h())