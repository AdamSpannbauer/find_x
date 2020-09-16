from expressions import Sum


def print_simplify(expr):
    print("\nInput:")
    print(expr)
    expr.simplify()
    print("Simplified:")
    print(expr)


s = Sum([1, 2, Sum([3, 4, Sum([5, 6])])])
print_simplify(s)

s = Sum([1, 2, Sum([3, "x", Sum([5, 6])])])
print_simplify(s)
