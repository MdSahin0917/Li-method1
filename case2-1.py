import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, factorial
from functools import partial

def W_integral(l, m, n, a, beta, gamma, gamma_prime, use_analytic=False):
    """
    Compute W(l, -m, n; x, l', y') where m is positive after substitution
    
    Parameters:
    -----------
    l, m, n : int
        Parameters where l >= 0, m > 0, n >= 0
    a, beta, gamma, gamma_prime : float
        Parameters in the exponents
    
    Returns:
    --------
    float : Value of the integral
    """
    
    if use_analytic:
        # Analytic solution based on the derived expression
        return analytic_W(l, m, n, a, beta, gamma, gamma_prime)
    else:
        # Numerical integration
        return numerical_W(l, m, n, a, beta, gamma, gamma_prime)


def numerical_W(l, m, n, a, beta, gamma, gamma_prime):
    """
    Numerical evaluation of the triple integral:
    W = ∫₀^∞ dx x^l e^{-ax} ∫_x^∞ dy y^{-m} e^{-βy} ∫_y^∞ dz z^n e^{-γz}
    """
    
    # Inner integral over z: ∫_y^∞ dz z^n e^{-γz}
    def inner_integral(y, n, gamma):
        if n == 0:
            return np.exp(-gamma * y) / gamma
        else:
            # Use integration for general n
            result, _ = quad(lambda z: z**n * np.exp(-gamma * z), y, np.inf)
            return result
    
    # Middle integral over y: ∫_x^∞ dy y^{-m} e^{-βy} * (inner integral)
    def middle_integral(x, n, m, gamma, beta):
        def integrand(y):
            if y <= 0:
                return 0
            inner = inner_integral(y, n, gamma)
            return y**(-m) * np.exp(-beta * y) * inner
        result, _ = quad(integrand, x, np.inf)
        return result
    
    # Outer integral over x: ∫_0^∞ dx x^l e^{-ax} * (middle integral)
    def outer_integrand(x, n, m, gamma, beta, l, a):
        middle = middle_integral(x, n, m, gamma, beta)
        return x**l * np.exp(-a * x) * middle
    
    # Perform the outer integral
    result, error = quad(outer_integrand, 0, np.inf, 
                        args=(n, m, gamma, beta, l, a))
    
    return result


def analytic_W(l, m, n, a, beta, gamma, gamma_prime):
    """
    Analytic evaluation based on equation (13):
    W = n! / γ^(n+1) * ∫₀^∞ dx x^l e^{-ax} ∫_x^∞ dy y^{-m} e^{-β(y + γ')} * Σ_{k=0}^n (γ^k y^k)/k!
    """
    
    # Precompute factorial for efficiency
    n_factorial = factorial(n)
    gamma_power = gamma ** (n + 1)
    
    # Summation over k
    def integrand_y_given_x(x, y):
        sum_term = 0
        for k in range(n + 1):
            sum_term += (gamma ** k) * (y ** k) / factorial(k)
        return y**(-m) * np.exp(-beta * (gamma + gamma_prime) * y) * sum_term
    
    # Integral over y from x to infinity
    def y_integral(x):
        result, _ = quad(lambda y: integrand_y_given_x(x, y), x, np.inf)
        return result
    
    # Outer integral over x
    def x_integrand(x):
        return x**l * np.exp(-a * x) * y_integral(x)
    
    result, error = quad(x_integrand, 0, np.inf)
    
    return (n_factorial / gamma_power) * result


def W_with_substitution(l, m_original, n, a, beta, gamma, gamma_prime):
    """
    Wrapper function for the case where original m is negative
    After substitution, we use m = -m_original (positive)
    """
    m = -m_original  # m becomes positive
    
    # Check conditions: l - m + 1 >= 0 and l - m + n + 2 >= 0
    if l - m + 1 < 0:
        print(f"Warning: l - m + 1 = {l - m + 1} < 0")
    if l - m + n + 2 < 0:
        print(f"Warning: l - m + n + 2 = {l - m + n + 2} < 0")
    
    return W_integral(l, m, n, a, beta, gamma, gamma_prime)


# Example usage
if __name__ == "__main__":
    # Set parameters
    l = 30         # l >= 0
    m_original = -5 # m < 0, so after substitution m = 3
    n = 20         # n >= 0
    
    a = 1.0
    beta = 0.5
    gamma = 0.5
    gamma_prime = 0.5
    
    # Compute using numerical integration
    result_num = W_with_substitution(l, m_original, n, a, beta, gamma, gamma_prime)
    print(f"Numerical result: {result_num:.6f}")
    
    # If we want to use the analytic form (based on equation 13)
    # Note: The analytic form assumes the specific structure in equation (13)
    # with the exponential term e^{-β(γ + γ')}
    # result_ana = W_with_substitution(l, m_original, n, a, beta, gamma, gamma_prime)
    # print(f"Analytic form result: {result_ana:.6f}")
    
    # Example with different parameters
    print("\n" + "="*50)
    print("Example with different parameters:")
    
    l = 30
    m_original = -5
    n = 20
    a = 0.1
    beta = 0.5
    gamma = 0.5
    gamma_prime = 0.5
    
    result = W_with_substitution(l, m_original, n, a, beta, gamma, gamma_prime)
    print(f"W({l}, {m_original}, {n}) = {result:.6f}")
    
    # Show intermediate calculations for small parameters
    print("\n" + "="*50)
    print("Testing with small parameters for verification:")
    
    l = 0
    m_original = -0
    n = 0
    a = 1.0
    beta = 1.0
    gamma = 1.0
    gamma_prime = 0.0
    
    # When n=0, the integral simplifies
    # ∫₀^∞ dx e^{-ax} ∫_x^∞ dy y^{-m} e^{-βy} ∫_y^∞ dz e^{-γz}
    # = ∫₀^∞ dx e^{-ax} ∫_x^∞ dy y^{-m} e^{-βy} * e^{-γy}/γ
    
    m = -m_original if m_original < 0 else m_original
    result = W_with_substitution(l, m_original, n, a, beta, gamma, gamma_prime)
    print(f"W({l}, {m_original}, {n}) = {result:.6f}")