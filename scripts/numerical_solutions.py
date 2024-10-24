
import numpy as np

def sol_diff_eq_ord(f, x0, t0, h, N, method="RK4"):
    t = np.arange(t0, t0 + (N + 1) * h, h)
    x = np.zeros(len(t))
    x[0] = x0
    
    if method == "Euler":
        for n in range(1, len(t)):
            x[n] = x[n-1] + h * f(t[n-1], x[n-1])
    
    elif method == "MidPoint":
        for n in range(1, len(t)):
            x[n] = x[n-1] + h * f(t[n-1] + 0.5 * h, x[n-1] + 0.5 * h * f(t[n-1], x[n-1]))
    
    elif method == "Ralston":
        for n in range(1, len(t)):
            k1 = f(t[n-1], x[n-1])
            k2 = f(t[n-1] + (2/3) * h, x[n-1] + (2/3) * h * k1)
            x[n] = x[n-1] + h * (0.25 * k1 + 0.75 * k2)
    
    elif method == "RK4":
        for n in range(1, len(t)):
            k1 = f(t[n-1], x[n-1])
            k2 = f(t[n-1] + 0.5 * h, x[n-1] + 0.5 * h * k1)
            k3 = f(t[n-1] + 0.5 * h, x[n-1] + 0.5 * h * k2)
            k4 = f(t[n-1] + h, x[n-1] + h * k3)
            x[n] = x[n-1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    return x, t

# Ejemplo de uso:
# def f(t, x):
#     return -x + t
# x, t = sol_diff_eq_ord(f, 1, 0, 0.1, 100, method="RK4")


