from abc import ABC
from .expression import Expression


class Sum(Expression, ABC):
    infix = " + "

    def _simplify(self, expr):
        if len(expr) == 1:
            simplified = self._simplify_if_possible(expr[0])
        else:
            simplified = Sum([self._simplify_if_possible(elem) for elem in expr])

        simplified.flatten()
        simplified._simplify_sum_nums()

        return simplified

    def _simplify_sum_nums(self):
        self._simplify_nums(Sum, operation=lambda a, b: a + b)
