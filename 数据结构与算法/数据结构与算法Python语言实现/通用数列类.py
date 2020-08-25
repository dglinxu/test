#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/6/7
# 开发工具：PyCharm   文件名称：通用数列类.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''


class Progression:
    """Iterator producing a generic progressoin.

    Default iterator produces the whole numbers 0,1,2,.....
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression.
        By convention,if current is set to None,this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element,or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention,an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """等差数列"""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment   the fixed constant to add to each term(default 1)
        start       the first term of the progresion (default 0)
        """

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment. """

        self._current += self._increment


class GeometricProgression(Progression):
    """等比数列"""

    def __init__(self, base=2, start=1):
        """Creat a new geometric progression.

        base     the fixed constant multiplied to each term(default 2)
        start    the first term of the progression(default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """斐波那契数列（模拟），是随机两个数产生类斐波那契数列"""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression

        first     the first term of the progression (default 0)
        second    the second term of the progression(default 1
        """
        super().__init__(first)
        self._prev = second - first  #为保证从第一个开始计数，计算第一前面那个值。

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
