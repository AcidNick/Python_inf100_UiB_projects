import matplotlib.pyplot as plt
def plot_polynomial(a: int, b: int, c:int, xs: list) -> None:
    ys = []
    for x in xs:
        ys.append(a*x**2 + b*x + c)
    plt.plot(xs, ys)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'f(x) ={coeff_string(a)}x^2{coeff_string(b)}x{coeff_string(c)}')

def coeff_string(coefficient):
    if coefficient == 1:
        return " + "
    elif coefficient == 0:
        return None
    elif coefficient >= 0:
        return f" + {coefficient}"
    elif coefficient < 0:
        return f" - {abs(coefficient)}"




if __name__ == "__main__":
    plot_polynomial(1, -5, 100, [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.show()  # ha gjerne plt.show() utenfor plot_polynomial