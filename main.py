from math import cos, exp


def f(x: float, y: float) -> float:
    return cos(x + y) * exp(x ** 2 + y ** 2)


def solve_based_euler(h: float, x_0: float, y_0: float, x_n: float) -> list[tuple[float, float]]:
    x_i: float = x_0
    y_i: float = y_0
    res: list[tuple[float, float]] = []
    while x_i <= x_n:
        res.append((x_i, y_i))
        y_i = y_i + h * f(x_i, y_i)
        x_i += h
    return res


def solve_based_predictor_corrector(h: float, x_0: float, y_0: float, x_n: float) -> list[tuple[float, float]]:
    x_i: float = x_0
    y_i: float = y_0
    res: list[tuple[float, float]] = []
    while x_i <= x_n:
        res.append((x_i, y_i))
        k_1: float = h * f(x_i, y_i)
        k_2: float = h * f(x_i + h, y_i + k_1)
        y_i = y_i + 0.5 * k_1 + 0.5 * k_2
        x_i += h
    return res

def main():
    print(solve_based_euler(0.02, 0, 1, 0.1))
    print(solve_based_predictor_corrector(0.02, 0, 1, 0.1))


if __name__ == '__main__':
    main()
