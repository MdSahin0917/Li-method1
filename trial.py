






# # # # from mpmath import mp

# # # # mp.dps = 200


# # # # # ---------------- FAST 2F1 ---------------- #
# # # # def hyp2f1_fast(a, b, c, x, tol=1e-30, max_iter=10000):
# # # #     term = mp.mpf(1)
# # # #     s = term

# # # #     for k in range(1, max_iter):
# # # #         term *= (a + k - 1)*(b + k - 1) / ((c + k - 1)*k) * x
# # # #         s += term

# # # #         if abs(term) < tol:
# # # #             break

# # # #     return s


# # # # # ---------------- MAIN FUNCTION ---------------- #
# # # # def W(l, m, n, alpha, beta, gamma, tol=1e-30, pmax=10000):

# # # #     alpha = mp.mpf(alpha)
# # # #     beta  = mp.mpf(beta)
# # # #     gamma = mp.mpf(gamma)

# # # #     if l < 0 or (l+m+1) < 0 or (l+m+n+2) < 0:
# # # #         raise ValueError("Conditions violated")

# # # #     denom = alpha + beta + gamma
# # # #     x1 = alpha / denom
# # # #     x2 = (alpha + beta) / denom

# # # #     pref = mp.factorial(l) / (denom ** (l+m+n+3))

# # # #     # ---------------- p = 0 ---------------- #
# # # #     p = 0

# # # #     C = mp.factorial(l+m+n+2) / (
# # # #         mp.factorial(l+1) * (l+m+2)
# # # #     )

# # # #     x1_power = mp.mpf(1)

# # # #     term = C * hyp2f1_fast(
# # # #         1,
# # # #         l+m+n+3,
# # # #         l+m+3,
# # # #         x2,
# # # #         tol=tol
# # # #     )

# # # #     S = term

# # # #     # ---------------- LOOP ---------------- #
# # # #     for p in range(0, pmax-1):

# # # #         # update coefficient (CORRECTED)
# # # #         C *= ((l+m+n+p+3)/(l+2+p)) * ((l+m+2+p)/(l+m+3+p))

# # # #         # update power
# # # #         x1_power *= x1

# # # #         term = C * x1_power * hyp2f1_fast(
# # # #             1,
# # # #             l+m+n+p+4,
# # # #             l+m+p+4,
# # # #             x2,
# # # #             tol=tol
# # # #         )

# # # #         S += term

# # # #         if abs(term) < tol:
# # # #             break

# # # #     return pref * S

# # # # print(W(25,10,20,0.1,0.5,0.5))







# # # from mpmath import mp

# # # mp.dps = 200


# # # # ---------------- FAST 2F1 ---------------- #
# # # def hyp2f1_fast(a, b, c, x, tol=1e-30, max_iter=10000):
# # #     term = mp.mpf(1)
# # #     s = term

# # #     for k in range(1, max_iter):
# # #         term *= (a + k - 1)*(b + k - 1) / ((c + k - 1)*k) * x
# # #         s += term

# # #         if abs(term) < tol:
# # #             break

# # #     return s


# # # # ---------------- MAIN FUNCTION ---------------- #
# # # def W(l, m, n, alpha, beta, gamma, tol=1e-30, pmax=10000):

# # #     alpha = mp.mpf(alpha)
# # #     beta  = mp.mpf(beta)
# # #     gamma = mp.mpf(gamma)

# # #     if l < 0 or (l+m+1) < 0 or (l+m+n+2) < 0:
# # #         return mp.nan  # skip invalid

# # #     denom = alpha + beta + gamma
# # #     x1 = alpha / denom
# # #     x2 = (alpha + beta) / denom

# # #     pref = mp.factorial(l) / (denom ** (l+m+n+3))

# # #     C = mp.factorial(l+m+n+2) / (
# # #         mp.factorial(l+1) * (l+m+2)
# # #     )

# # #     x1_power = mp.mpf(1)

# # #     term = C * hyp2f1_fast(
# # #         1,
# # #         l+m+n+3,
# # #         l+m+3,
# # #         x2,
# # #         tol=tol
# # #     )

# # #     S = term

# # #     for p in range(0, pmax-1):

# # #         C *= ((l+m+n+p+3)/(l+2+p)) * ((l+m+2+p)/(l+m+3+p))
# # #         x1_power *= x1

# # #         term = C * x1_power * hyp2f1_fast(
# # #             1,
# # #             l+m+n+p+4,
# # #             l+m+p+4,
# # #             x2,
# # #             tol=tol
# # #         )

# # #         S += term

# # #         if abs(term) < tol:
# # #             break

# # #     return pref * S


# # # # ---------------- PARAMETERS ---------------- #
# # # alpha_values = [
# # #     0.1,0.3,0.6,1.0,3.0,6.0,9.0,
# # #     99.0,999.0,9999.0,99999.0,
# # #     999999.0,9999999.0,99999999.0
# # # ]

# # # cases = [
# # #     (25,10,20),
# # #     (30,-5,20),
# # #     (25,10,-20),
# # #     (30,-3,-20)
# # # ]

# # # beta  = mp.mpf('0.5')
# # # gamma = mp.mpf('0.5')


# # # # ---------------- TABLE ---------------- #
# # # for (l,m,n) in cases:
# # #     print("\n" + "="*80)
# # #     print(f"CASE: l={l}, m={m}, n={n}")
# # #     print("="*80)
# # #     print(f"{'alpha':>15} {'x=alpha/(a+b+g)':>25} {'W':>40}")
# # #     print("-"*80)

# # #     for a in alpha_values:
# # #         alpha = mp.mpf(a)
# # #         denom = alpha + beta + gamma
# # #         x = alpha / denom

# # #         try:
# # #             val = W(l,m,n,alpha,beta,gamma)
# # #             val_str = mp.nstr(val, 20)
# # #         except:
# # #             val_str = "ERROR"

# # #         print(f"{mp.nstr(alpha,8):>15} {mp.nstr(x,12):>25} {val_str:>40}")


















from mpmath import mp
import time
# target precision (final output ~35 digits safe)
mp.dps = 120


# ---------------- BASIC 2F1 (recurrence) ---------------- #
def hyp2f1_fast(a, b, c, x, tol=mp.mpf('1e-40'), max_iter=100000):
    term = mp.mpf(1)
    s = term

    for k in range(1, max_iter):
        term *= (a + k - 1)*(b + k - 1) / ((c + k - 1)*k) * x
        s += term

        if abs(term) < tol * abs(s):
            break

    return s


# ---------------- STABLE 2F1 ---------------- #
def hyp2f1_stable(a, b, c, x, tol=mp.mpf('1e-40')):

    # handle dangerous region x ~ 1
    if x > mp.mpf('0.9'):
        y = 1 - x

        return (y**(c-a-b)) * hyp2f1_fast(
            c-a,
            c-b,
            c,
            x,
            tol
        )

    return hyp2f1_fast(a, b, c, x, tol)


# ---------------- MAIN FUNCTION ---------------- #
def W(l, m, n, alpha, beta, gamma,
      tol=mp.mpf('1e-40'), pmax=100000):

    alpha = mp.mpf(alpha)
    beta  = mp.mpf(beta)
    gamma = mp.mpf(gamma)

    if l < 0 or (l+m+1) < 0 or (l+m+n+2) < 0:
        return mp.nan

    denom = alpha + beta + gamma
    x1 = alpha / denom
    x2 = (alpha + beta) / denom

    pref = mp.factorial(l) / (denom ** (l+m+n+3))

    # ---------------- p = 0 ---------------- #
    C = mp.factorial(l+m+n+2) / (
        mp.factorial(l+1) * (l+m+2)
    )

    x1_power = mp.mpf(1)

    term = C * hyp2f1_stable(
        1,
        l+m+n+3,
        l+m+3,
        x2,
        tol
    )

    S = term
    c_corr = mp.mpf(0)   # Kahan correction

    # ---------------- LOOP ---------------- #
    for p in range(0, pmax-1):

        # recurrence (CORRECT)
        C *= ((l+m+n+p+3)/(l+2+p)) * ((l+m+2+p)/(l+m+3+p))

        # power update
        x1_power *= x1

        term = C * x1_power * hyp2f1_stable(
            1,
            l+m+n+p+4,
            l+m+p+4,
            x2,
            tol
        )

        # -------- KAHAN SUMMATION -------- #
        y = term - c_corr
        t = S + y
        c_corr = (t - S) - y
        S = t

        # relative convergence
        if abs(term) < tol * abs(S):
            break

    return pref * S


# ---------------- DRIVER ---------------- #
# alpha_values = [
#     0.1,0.3,0.6,1.0,3.0,6.0,9.0,
#     99.0,999.0,9999.0,99999.0,
#     999999.0,9999999.0,99999999.0
# ]

alpha_values = [
    0.1,0.3,0.6,1.0,3.0,6.0,9.0,
]

cases = [
    (25,10,20),
    (30,-5,20),
    (25,10,-20),
    (30,-3,-20)
]

beta  = mp.mpf('0.5')
gamma = mp.mpf('0.5')


# ---------------- TABLE ---------------- #
start = time.perf_counter()
for (l,m,n) in cases:

    print("\n" + "="*90)
    print(f"CASE: l={l}, m={m}, n={n}")
    print("="*90)
    print(f"{'alpha':>15} {'x=alpha/(a+b+g)':>25} {'W ':>45}")
    print("-"*90)

    for a in alpha_values:

        alpha = mp.mpf(a)
        denom = alpha + beta + gamma
        x = alpha / denom

        with mp.workdps(250):   # 🔥 critical for accuracy
            try:
                val = W(l,m,n,alpha,beta,gamma)
                val_str = mp.nstr(val, 40)   # show ~40 digits
            except:
                val_str = "ERROR"

        print(f"{mp.nstr(alpha,8):>15} {mp.nstr(x,12):>25} {val_str:>45}")

end = time.perf_counter()






























# from mpmath import mp
# import time

# # Set high precision for accurate calculations
# mp.dps = 120

# def hyp2f1_series(a, b, c, x, tol=mp.mpf('1e-45'), max_iter=100000):
#     """
#     Direct series evaluation of 2F1 hypergeometric function
#     """
#     # For x close to 1, use transformation to improve convergence
#     if x > mp.mpf('0.95'):
#         # Use transformation: 2F1(a,b;c;x) = (1-x)^(c-a-b) * 2F1(c-a, c-b; c; x)
#         y = 1 - x
#         power = c - a - b
#         return (y ** power) * hyp2f1_series(c - a, c - b, c, x, tol, max_iter)
    
#     term = mp.mpf(1)
#     s = term
#     k = 1
    
#     while k < max_iter:
#         term *= (a + k - 1) * (b + k - 1) / ((c + k - 1) * k) * x
#         s += term
        
#         if abs(term) < tol * abs(s):
#             break
#         k += 1
    
#     return s

# def W(l, m, n, alpha, beta, gamma, tol=mp.mpf('1e-45'), max_p=100000):
#     """
#     Calculate W(l,m,n; α,β,γ) as defined in the formula:
    
#     W = [l! / (α+β+γ)^(l+m+n+3)] × Σ_{p=0}^∞ [ (l+m+n+p+2)! / ((l+1+p)!(l+m+2+p)) ] 
#         × (α/(α+β+γ))^p × ₂F₁(1, l+m+n+p+3; l+m+p+3; (α+β)/(α+β+γ))
#     """
    
#     # Convert inputs to mpmath numbers
#     alpha = mp.mpf(alpha)
#     beta = mp.mpf(beta)
#     gamma = mp.mpf(gamma)
    
#     # Check for valid indices
#     if l < 0 or m < 0 or n < 0:
#         return mp.nan
    
#     denom = alpha + beta + gamma
#     if denom == 0:
#         return mp.nan
    
#     # Precompute constants
#     x1 = alpha / denom          # First argument in the sum
#     x2 = (alpha + beta) / denom # Argument for hypergeometric function
    
#     # Prefactor: l! / (α+β+γ)^(l+m+n+3)
#     prefactor = mp.factorial(l) / (denom ** (l + m + n + 3))
    
#     # Initialize the series sum
#     total_sum = mp.mpf(0)
#     correction = mp.mpf(0)  # Kahan summation correction
    
#     # Calculate p=0 term first to initialize properly
#     p = 0
    
#     # Coefficient C(p) = (l+m+n+p+2)! / ((l+1+p)! * (l+m+2+p))
#     # For p=0:
#     C = mp.factorial(l + m + n + 2) / (mp.factorial(l + 1) * (l + m + 2))
    
#     # Power term (α/(α+β+γ))^p = x1^p, for p=0 it's 1
#     x1_power = mp.mpf(1)
    
#     # Hypergeometric term
#     hypergeom = hyp2f1_series(1, l + m + n + 3, l + m + 3, x2, tol)
    
#     term = C * x1_power * hypergeom
    
#     # Kahan summation
#     y = term - correction
#     t = total_sum + y
#     correction = (t - total_sum) - y
#     total_sum = t
    
#     # Loop over p from 1 to max_p
#     for p in range(1, max_p + 1):
#         # Update C(p) using recurrence relation
#         # C(p) = C(p-1) * [(l+m+n+p+2)/(l+1+p)] * [(l+m+2+p-1)/(l+m+2+p)]
#         # Actually derived from: C(p)/C(p-1) = (l+m+n+p+2)/(l+1+p) * (l+m+1+p)/(l+m+2+p)
#         # Let's derive carefully:
#         # C(p) = (l+m+n+p+2)! / ((l+1+p)! * (l+m+2+p))
#         # C(p-1) = (l+m+n+p+1)! / ((l+p)! * (l+m+1+p))
#         # Ratio = (l+m+n+p+2) / (l+1+p) * (l+p+1)!/(l+p)!? Wait, need to be careful
        
#         # Better: Direct recurrence based on factorial ratio
#         C *= (l + m + n + p + 2) / (l + 1 + p)
#         C *= (l + m + 1 + p) / (l + m + 2 + p)
        
#         # Update power term
#         x1_power *= x1
        
#         # Hypergeometric function with updated parameters
#         hypergeom = hyp2f1_series(1, l + m + n + p + 3, l + m + p + 3, x2, tol)
        
#         # Calculate term
#         term = C * x1_power * hypergeom
        
#         # Kahan summation for numerical stability
#         y = term - correction
#         t = total_sum + y
#         correction = (t - total_sum) - y
#         total_sum = t
        
#         # Check for convergence
#         if abs(term) < tol * abs(total_sum):
#             break
    
#     return prefactor * total_sum

# def test_calculation(l, m, n, alpha, beta, gamma):
#     """Test a single calculation with detailed output"""
#     result = W(l, m, n, alpha, beta, gamma)
#     denom = alpha + beta + gamma
#     x1 = alpha / denom
#     x2 = (alpha + beta) / denom
    
#     print(f"\n  l={l}, m={m}, n={n}")
#     print(f"  α={alpha}, β={beta}, γ={gamma}")
#     print(f"  Denom = {denom}")
#     print(f"  x1 = α/(α+β+γ) = {x1}")
#     print(f"  x2 = (α+β)/(α+β+γ) = {x2}")
#     print(f"  Result: {mp.nstr(result, 40)}")
#     return result

# def main():
#     """Main test routine"""
    
#     print("="*100)
#     print("CALCULATING W(l,m,n; α,β,γ) FROM THE FORMULA")
#     print("="*100)
    
#     # Test with simple values (all positive)
#     print("\n" + "="*100)
#     print("TEST 1: All positive indices")
#     print("="*100)
    
#     test_calculation(l=0, m=0, n=0, alpha=1.0, beta=1.0, gamma=1.0)
#     test_calculation(l=1, m=0, n=0, alpha=1.0, beta=1.0, gamma=1.0)
#     test_calculation(l=0, m=1, n=0, alpha=1.0, beta=1.0, gamma=1.0)
#     test_calculation(l=0, m=0, n=1, alpha=1.0, beta=1.0, gamma=1.0)
    
#     # Test with different alpha values
#     print("\n" + "="*100)
#     print("TEST 2: Varying alpha")
#     print("="*100)
    
#     alpha_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    
#     for alpha in alpha_values:
#         test_calculation(l=1, m=1, n=1, alpha=alpha, beta=1.0, gamma=1.0)
    
#     # Test with the original cases from the code
#     print("\n" + "="*100)
#     print("TEST 3: Original test cases")
#     print("="*100)
    
#     cases = [
#         (25, 10, 20),
#         (30, -5, 20),   # Negative m - should be handled carefully
#         (25, 10, -20),  # Negative n - may cause issues
#         (30, -3, -20)   # Both negative
#     ]
    
#     beta = 0.5
#     gamma = 0.5
#     alpha_values_small = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0]
    
#     for (l, m, n) in cases:
#         print(f"\n{'-'*100}")
#         print(f"CASE: l={l}, m={m}, n={n}")
#         print(f"{'-'*100}")
#         print(f"{'alpha':>15} {'x1 = α/(α+β+γ)':>25} {'W value':>50}")
#         print(f"{'-'*100}")
        
#         for alpha in alpha_values_small:
#             try:
#                 result = W(l, m, n, alpha, beta, gamma)
#                 denom = alpha + beta + gamma
#                 x1 = alpha / denom
#                 print(f"{alpha:>15.6f} {x1:>25.15f} {mp.nstr(result, 40):>50}")
#             except Exception as e:
#                 print(f"{alpha:>15.6f} {'ERROR':>25} {str(e):>50}")
    
#     # Test with very large alpha to check stability
#     print("\n" + "="*100)
#     print("TEST 4: Large alpha values (stability test)")
#     print("="*100)
    
#     large_alphas = [99.0, 999.0, 9999.0]
#     for alpha in large_alphas:
#         try:
#             result = W(5, 5, 5, alpha, 1.0, 1.0)
#             print(f"α={alpha:>10.1f}, W = {mp.nstr(result, 35)}")
#         except Exception as e:
#             print(f"α={alpha:>10.1f}, ERROR: {e}")

# if __name__ == "__main__":
#     start_time = time.perf_counter()
#     main()
#     end_time = time.perf_counter()
#     print(f"\n{'='*100}")
#     print(f"Total execution time: {end_time - start_time:.2f} seconds")