from abc import abstractmethod


class Expression(list):
    infix = " ? "

    def __repr__(self):
        if not self.infix:
            raise NotImplementedError("infix class attribute must be defined")

        expr_str = self.infix.join(str(x) for x in self)
        return "(" + expr_str + ")"

    def __str__(self):
        return self.__repr__()

    def flatten(self):
        elems = []
        for elem in self:
            if isinstance(elem, type(self)):
                elems += list(elem)
            elif isinstance(elem, Expression) and len(elem) == 1:
                elems.append(elem[0])
            else:
                elems.append(elem)

        self.__init__(elems)

    def _simplify_if_possible(self, expr):
        """
        A helper function that guards against trying to simplify a non-Expression.
        """
        if isinstance(expr, Expression):
            return self._simplify(expr)
        else:
            return expr

    @abstractmethod
    def _simplify(self, expr):
        return self._simplify_if_possible(expr)

    def simplify(self):
        simplified = self._simplify(self)
        self.__init__(simplified)

    def _simplify_nums(self, output_class, operation):
        """
        Apply expression operator to numbers (i.e. simplify `Sum([1, 5])` to `Sum([6])`)
        """
        seen = set()
        simplified = output_class()
        for i, a in enumerate(self):
            if i in seen:
                continue
            else:
                seen.add(i)

            if isinstance(a, (int, float)):
                for j, b in enumerate(self[i + 1 :]):
                    if j + i + 1 in seen:
                        continue
                    else:
                        seen.add(j + i + 1)

                    if isinstance(b, (int, float)):
                        a = operation(a, b)
                    else:
                        simplified.append(b)

            simplified.append(a)

        self.__init__(simplified)
