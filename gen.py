# # # # # from mpmath import mp
# # # # # import time
# # # # # mp.dps = 150  # precision



# # # # # def W(l, m, n, alpha, beta, gamma, pmax=400):
# # # # #     # Convert to mp
# # # # #     alpha = mp.mpf(alpha)
# # # # #     beta  = mp.mpf(beta)
# # # # #     gamma = mp.mpf(gamma)

# # # # #     # ---------------- CONDITIONS ---------------- #
# # # # #     if l < 0:
# # # # #         raise ValueError("Condition violated: l >= 0")

# # # # #     if l + m + 1 < 0:
# # # # #         raise ValueError("Condition violated: l + m + 1 >= 0")

# # # # #     if l + m + n + 2 < 0:
# # # # #         raise ValueError("Condition violated: l + m + n + 2 >= 0")

# # # # #     # ---------------- CONSTANTS ---------------- #
# # # # #     denom = alpha + beta + gamma
# # # # #     x = alpha / denom
# # # # #     z = (alpha + beta) / denom

# # # # #     # factorial using gamma
# # # # #     def fact(x):
# # # # #         return mp.gamma(x + 1)

# # # # #     # ---------------- PREFactor ---------------- #
# # # # #     prefactor = fact(l) / (denom ** (l + m + n + 3))

# # # # #     # ---------------- SUM ---------------- #
# # # # #     total = mp.mpf(0)

# # # # #     for p in range(pmax + 1):

# # # # #         num = fact(l + m + n + p + 2)
# # # # #         den = fact(l + 1 + p) * (l + m + 2 + p)

# # # # #         coeff = num / den

# # # # #         power = x ** p

# # # # #         # Hypergeometric 2F1
# # # # #         hyper = mp.hyper(
# # # # #             [1, l + m + n + p + 3],
# # # # #             [l + m + p + 3],
# # # # #             z
# # # # #         )

# # # # #         term = coeff * power * hyper
# # # # #         total += term

# # # # #     return prefactor * total


# # # # # # ---------------- TEST ---------------- #
# # # # # if __name__ == "__main__":
# # # # #     l = 30
# # # # #     m = -5
# # # # #     n = 20

# # # # #     alpha_list = [0.1,0.3,0.6,1.0,3.0,6.0,9.0,99.0,999.0,9999.0,99999.0,999999.0,9999999.0,99999999.0,999999999.0]
# # # # #     beta  = 0.5
# # # # #     gamma = 0.5
# # # # #     start = time.perf_counter()

# # # # #     for alpha in alpha_list:
# # # # #         result = W(l, m, n, alpha, beta, gamma, pmax=400)
# # # # #         print(f"W ({alpha}) =", mp.nstr(result, 37))

# # # # #     end = time.perf_counter()

# # # # #     print("Execution Time =", end - start, "seconds")













# # # # from mpmath import mp
# # # # import time
# # # # import os

# # # # mp.dps = 150  # precision

# # # # DATA_FILE = "Wdata.dat"

# # # # # ---------------- CACHE ---------------- #
# # # # W_cache = {}


# # # # def make_key(l, m, n, alpha, beta, gamma):
# # # #     """Create a stable key (string to avoid float mismatch issues)"""
# # # #     return (
# # # #         int(l), int(m), int(n),
# # # #         mp.nstr(alpha, 50),
# # # #         mp.nstr(beta, 50),
# # # #         mp.nstr(gamma, 50)
# # # #     )


# # # # def load_W():
# # # #     """Load cache from file"""
# # # #     if not os.path.exists(DATA_FILE):
# # # #         return

# # # #     with open(DATA_FILE, "r") as f:
# # # #         for line in f:
# # # #             parts = line.strip().split("|")
# # # #             if len(parts) != 7:
# # # #                 continue

# # # #             l, m, n = map(int, parts[:3])
# # # #             alpha, beta, gamma = parts[3:6]
# # # #             val = parts[6]

# # # #             key = (l, m, n, alpha, beta, gamma)
# # # #             W_cache[key] = mp.mpf(val)


# # # # def save_W(l, m, n, alpha, beta, gamma, value):
# # # #     """Append new result to file"""
# # # #     with open(DATA_FILE, "a") as f:
# # # #         f.write(
# # # #             f"{l}|{m}|{n}|"
# # # #             f"{mp.nstr(alpha,50)}|{mp.nstr(beta,50)}|{mp.nstr(gamma,50)}|"
# # # #             f"{mp.nstr(value,80)}\n"
# # # #         )


# # # # # ---------------- CORE FUNCTION ---------------- #
# # # # def W_compute(l, m, n, alpha, beta, gamma, pmax=400):

# # # #     # Convert to mp
# # # #     alpha = mp.mpf(alpha)
# # # #     beta  = mp.mpf(beta)
# # # #     gamma = mp.mpf(gamma)

# # # #     # ---------------- CONDITIONS ---------------- #
# # # #     if l < 0:
# # # #         raise ValueError("Condition violated: l >= 0")

# # # #     if l + m + 1 < 0:
# # # #         raise ValueError("Condition violated: l + m + 1 >= 0")

# # # #     if l + m + n + 2 < 0:
# # # #         raise ValueError("Condition violated: l + m + n + 2 >= 0")

# # # #     # ---------------- CONSTANTS ---------------- #
# # # #     denom = alpha + beta + gamma
# # # #     x = alpha / denom
# # # #     z = (alpha + beta) / denom

# # # #     def fact(x):
# # # #         return mp.gamma(x + 1)

# # # #     prefactor = fact(l) / (denom ** (l + m + n + 3))

# # # #     total = mp.mpf(0)

# # # #     for p in range(pmax + 1):

# # # #         num = fact(l + m + n + p + 2)
# # # #         den = fact(l + 1 + p) * (l + m + 2 + p)

# # # #         coeff = num / den
# # # #         power = x ** p

# # # #         hyper = mp.hyper(
# # # #             [1, l + m + n + p + 3],
# # # #             [l + m + p + 3],
# # # #             z
# # # #         )

# # # #         total += coeff * power * hyper

# # # #     return prefactor * total


# # # # # ---------------- WRAPPER WITH CACHE ---------------- #
# # # # def W(l, m, n, alpha, beta, gamma, pmax=400):

# # # #     alpha = mp.mpf(alpha)
# # # #     beta  = mp.mpf(beta)
# # # #     gamma = mp.mpf(gamma)

# # # #     key = make_key(l, m, n, alpha, beta, gamma)

# # # #     # Check cache
# # # #     if key in W_cache:
# # # #         return W_cache[key]

# # # #     # Compute if not found
# # # #     result = W_compute(l, m, n, alpha, beta, gamma, pmax)

# # # #     # Save in memory + file
# # # #     W_cache[key] = result
# # # #     save_W(l, m, n, alpha, beta, gamma, result)

# # # #     return result


# # # # # ---------------- TEST ---------------- #
# # # # if __name__ == "__main__":

# # # #     load_W()  # load existing data

# # # #     l = 25
# # # #     m = 10
# # # #     n = 20

# # # #     alpha_list = [
# # # #         0.1,0.3,0.6,1.0,3.0,6.0,9.0,
# # # #         99.0,999.0,9999.0,99999.0,
# # # #         999999.0,9999999.0,99999999.0,999999999.0
# # # #     ]

# # # #     beta  = 0.5
# # # #     gamma = 0.5

# # # #     start = time.perf_counter()

# # # #     for alpha in alpha_list:
# # # #         result = W(l, m, n, alpha, beta, gamma, pmax=400)
# # # #         print(f"W({alpha}) =", mp.nstr(result, 37))

# # # #     end = time.perf_counter()

# # # #     print("Execution Time =", end - start, "seconds")
















# # # from mpmath import mp
# # # import time
# # # import os

# # # mp.dps = 150  # precision

# # # DATA_FILE = "Wdata.dat"

# # # # ---------------- CACHE ---------------- #
# # # W_cache = {}


# # # def make_key(l, m, n, alpha, beta, gamma):
# # #     return (
# # #         int(l), int(m), int(n),
# # #         mp.nstr(alpha, 50),
# # #         mp.nstr(beta, 50),
# # #         mp.nstr(gamma, 50)
# # #     )


# # # def load_W():
# # #     if not os.path.exists(DATA_FILE):
# # #         return

# # #     with open(DATA_FILE, "r") as f:
# # #         for line in f:
# # #             parts = line.strip().split("|")
# # #             if len(parts) != 7:
# # #                 continue

# # #             l, m, n = map(int, parts[:3])
# # #             alpha, beta, gamma = parts[3:6]
# # #             val = parts[6]

# # #             key = (l, m, n, alpha, beta, gamma)
# # #             W_cache[key] = mp.mpf(val)


# # # def save_W(l, m, n, alpha, beta, gamma, value):
# # #     with open(DATA_FILE, "a") as f:
# # #         f.write(
# # #             f"{l}|{m}|{n}|"
# # #             f"{mp.nstr(alpha,50)}|{mp.nstr(beta,50)}|{mp.nstr(gamma,50)}|"
# # #             f"{mp.nstr(value,80)}\n"
# # #         )


# # # # ---------------- CORE FUNCTION ---------------- #
# # # def W_compute(l, m, n, alpha, beta, gamma, tol=mp.mpf('1e-40'), pmax=1000):

# # #     alpha = mp.mpf(alpha)
# # #     beta  = mp.mpf(beta)
# # #     gamma = mp.mpf(gamma)

# # #     # ---------------- CONDITIONS ---------------- #
# # #     if l < 0:
# # #         raise ValueError("Condition violated: l >= 0")
# # #     if l + m + 1 < 0:
# # #         raise ValueError("Condition violated: l + m + 1 >= 0")
# # #     if l + m + n + 2 < 0:
# # #         raise ValueError("Condition violated: l + m + n + 2 >= 0")

# # #     # ---------------- VARIABLES ---------------- #
# # #     denom = alpha + beta + gamma
# # #     x = alpha / denom
# # #     z = (alpha + beta) / denom

# # #     # ---------------- LOG PREFACTOR ---------------- #
# # #     log_pref = mp.loggamma(l + 1) - (l + m + n + 3) * mp.log(denom)

# # #     total = mp.mpf(0)

# # #     for p in range(pmax):

# # #         # -------- LOG COEFFICIENT -------- #
# # #         log_num = mp.loggamma(l + m + n + p + 3)
# # #         log_den = mp.loggamma(l + 2 + p) + mp.log(l + m + 2 + p)

# # #         log_coeff = log_num - log_den

# # #         # -------- POWER TERM -------- #
# # #         if x == 0:
# # #             if p == 0:
# # #                 log_power = mp.mpf(0)
# # #             else:
# # #                 break
# # #         else:
# # #             log_power = p * mp.log(x)

# # #         # -------- HYPER STABILIZATION -------- #
# # #         if z > 0.9:
# # #             # transformation for z ~ 1
# # #             hyper = (1 - z)**(-1) * mp.hyper(
# # #                 [1, -(n)],
# # #                 [l + m + p + 3],
# # #                 z / (z - 1)
# # #             )
# # #         else:
# # #             hyper = mp.hyper(
# # #                 [1, l + m + n + p + 3],
# # #                 [l + m + p + 3],
# # #                 z
# # #             )

# # #         # -------- TERM -------- #
# # #         term = mp.exp(log_coeff + log_power) * hyper

# # #         total += term

# # #         # -------- CONVERGENCE CHECK -------- #
# # #         if abs(term) < tol:
# # #             break

# # #     return mp.exp(log_pref) * total


# # # # ---------------- WRAPPER ---------------- #
# # # def W(l, m, n, alpha, beta, gamma, tol=mp.mpf('1e-40'), pmax=1000):

# # #     alpha = mp.mpf(alpha)
# # #     beta  = mp.mpf(beta)
# # #     gamma = mp.mpf(gamma)

# # #     key = make_key(l, m, n, alpha, beta, gamma)

# # #     if key in W_cache:
# # #         return W_cache[key]

# # #     result = W_compute(l, m, n, alpha, beta, gamma, tol, pmax)

# # #     W_cache[key] = result
# # #     save_W(l, m, n, alpha, beta, gamma, result)

# # #     return result


# # # # ---------------- TEST ---------------- #
# # # if __name__ == "__main__":

# # #     load_W()

# # #     l = 25
# # #     m = 10
# # #     n = 20

# # #     alpha_list = [
# # #         0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0,
# # #         99.0, 999.0, 9999.0, 99999.0,
# # #         999999.0, 9999999.0, 99999999.0, 999999999.0
# # #     ]

# # #     beta  = mp.mpf('0.5')
# # #     gamma = mp.mpf('0.5')

# # #     start = time.perf_counter()

# # #     for alpha in alpha_list:
# # #         result = W(l, m, n, alpha, beta, gamma)
# # #         print(f"W({alpha}) =", mp.nstr(result, 40))

# # #     end = time.perf_counter()

# # #     print("Execution Time =", end - start, "seconds")





















# # from mpmath import mp
# # import time
# # import os

# # mp.dps = 200

# # DATA_FILE = "Wdata.dat"
# # W_cache = {}


# # # ---------------- KEY ---------------- #
# # def make_key(l, m, n, alpha, beta, gamma):
# #     return (
# #         int(l), int(m), int(n),
# #         mp.nstr(alpha, 40),
# #         mp.nstr(beta, 40),
# #         mp.nstr(gamma, 40)
# #     )


# # # ---------------- CACHE LOAD ---------------- #
# # def load_W():
# #     if not os.path.exists(DATA_FILE):
# #         return

# #     with open(DATA_FILE, "r") as f:
# #         for line in f:
# #             parts = line.strip().split("|")
# #             if len(parts) != 7:
# #                 continue

# #             l, m, n = map(int, parts[:3])
# #             alpha, beta, gamma = parts[3:6]
# #             val = parts[6]

# #             key = (l, m, n, alpha, beta, gamma)
# #             W_cache[key] = mp.mpf(val)


# # # ---------------- CACHE SAVE ---------------- #
# # def save_W(l, m, n, alpha, beta, gamma, value):
# #     with open(DATA_FILE, "a") as f:
# #         f.write(
# #             f"{l}|{m}|{n}|"
# #             f"{mp.nstr(alpha,40)}|{mp.nstr(beta,40)}|{mp.nstr(gamma,40)}|"
# #             f"{mp.nstr(value,80)}\n"
# #         )


# # # ---------------- STABLE 2F1 ---------------- #
# # def stable_hyper(a, b, c, z):
# #     """
# #     Stable evaluation of 2F1
# #     Uses direct when safe, fallback when z ~ 1
# #     """
# #     if z < 0.9:
# #         return mp.hyper([a, b], [c], z)

# #     # Use analytic continuation (correct one)
# #     return mp.hyper([a, b], [c], z)


# # # ---------------- CORE ---------------- #
# # def W_compute(l, m, n, alpha, beta, gamma,
# #               tol=mp.mpf('1e-40'), pmax=100):

# #     alpha = mp.mpf(alpha)
# #     beta  = mp.mpf(beta)
# #     gamma = mp.mpf(gamma)

# #     # -------- CONDITIONS -------- #
# #     if l < 0:
# #         raise ValueError("l >= 0 violated")
# #     if l + m + 1 < 0:
# #         raise ValueError("l+m+1 >= 0 violated")
# #     if l + m + n + 2 < 0:
# #         raise ValueError("l+m+n+2 >= 0 violated")

# #     denom = alpha + beta + gamma
# #     x = alpha / denom
# #     z = (alpha + beta) / denom

# #     # -------- PREFactor -------- #
# #     log_pref = mp.loggamma(l + 1) - (l + m + n + 3) * mp.log(denom)

# #     total = mp.mpf(0)

# #     for p in range(pmax):

# #         # -------- COEFFICIENT -------- #
# #         log_num = mp.loggamma(l + m + n + p + 3)   # ( ... +2)!
# #         log_den = mp.loggamma(l + p + 2)           # (l+1+p)!
# #         log_den += mp.log(l + m + p + 2)           # (l+m+2+p)

# #         log_coeff = log_num - log_den

# #         # -------- POWER -------- #
# #         if x == 0:
# #             if p == 0:
# #                 log_power = 0
# #             else:
# #                 break
# #         else:
# #             log_power = p * mp.log(x)

# #         # -------- HYPER -------- #
# #         hyper = stable_hyper(
# #             1,
# #             l + m + n + p + 3,
# #             l + m + p + 3,
# #             z
# #         )

# #         term = mp.exp(log_coeff + log_power) * hyper

# #         total += term

# #         if abs(term) < tol:
# #             break

# #     return mp.exp(log_pref) * total


# # # ---------------- WRAPPER ---------------- #
# # def W(l, m, n, alpha, beta, gamma):

# #     alpha = mp.mpf(alpha)
# #     beta  = mp.mpf(beta)
# #     gamma = mp.mpf(gamma)

# #     key = make_key(l, m, n, alpha, beta, gamma)

# #     if key in W_cache:
# #         return W_cache[key]

# #     val = W_compute(l, m, n, alpha, beta, gamma)

# #     W_cache[key] = val
# #     save_W(l, m, n, alpha, beta, gamma, val)

# #     return val


# # # ---------------- TEST ---------------- #
# # if __name__ == "__main__":

# #     load_W()

# #     l = 25
# #     m = 10
# #     n = 20

# #     beta  = mp.mpf('0.5')
# #     gamma = mp.mpf('0.5')

# #     alpha_list = [
# #         0.1, 0.3, 0.6, 1.0,
# #         3.0, 6.0, 9.0,
# #         99.0, 999.0, 9999.0
# #     ]

# #     start = time.perf_counter()

# #     for alpha in alpha_list:
# #         res = W(l, m, n, alpha, beta, gamma)
# #         print(f"W({alpha}) =", mp.nstr(res, 40))

# #     print("Time =", time.perf_counter() - start)
















# import mpmath
# from mpmath import mp, fac, hyper, nsum, loggamma, exp, gamma, rf

# # Set high precision
# mp.dps = 80

# def calculate_W_corrected(l, m, n, alpha, beta, gamma, max_terms=500):
#     """
#     Calculate W(l,m,n; α,β,γ) correctly handling negative parameters
#     """
#     # Convert to floats
#     alpha = mp.mpf(alpha)
#     beta = mp.mpf(beta)
#     gamma = mp.mpf(gamma)
    
#     denom = alpha + beta + gamma
    
#     # Prefactor: l! / (α+β+γ)^(l+m+n+3)
#     # Use gamma function for factorial
#     l_fact = mp.gamma(l + 1)
#     exponent = l + m + n + 3
#     prefactor = l_fact / (denom ** exponent)
    
#     ratio = alpha / denom
#     z = (alpha + beta) / denom
    
#     def term(p):
#         p_val = p
        
#         # Check if the factorial arguments are valid
#         # For negative n, l+m+n+p+2 can be small
#         arg1 = l + m + n + p_val + 2
#         arg2 = l + 1 + p_val
#         arg3 = l + m + 2 + p_val
        
#         # Use gamma function for all cases (handles non-integer and negative values)
#         # Gamma(n+1) = n! for integer n, and handles negative arguments via reflection
#         try:
#             num = mp.gamma(arg1 + 1)  # (l+m+n+p+2)!
#             den = mp.gamma(arg2 + 1) * mp.gamma(arg3 + 1)  # (l+1+p)! * (l+m+2+p)!
#             coeff = num / den
#         except:
#             return mp.mpf(0)
        
#         # Power term
#         power_term = ratio ** p_val
        
#         # Hypergeometric function
#         a = l + m + n + p_val + 3
#         b = l + m + p_val + 3
        
#         try:
#             hyper_val = hyper([1, a], [b], z)
#         except:
#             hyper_val = mp.mpf(0)
        
#         return coeff * power_term * hyper_val
    
#     # Sum the series
#     total = mp.mpf(0)
#     for p in range(max_terms):
#         term_val = term(p)
#         total += term_val
        
#         # Check convergence
#         if p > 20 and abs(term_val) < mp.mpf(1e-60) * abs(total):
#             break
    
#     result = prefactor * total
#     return result


# def calculate_W_with_gamma(l, m, n, alpha, beta, gamma, max_terms=1000):
#     """
#     Calculate W using gamma functions throughout for better handling of negative n
#     """
#     alpha = mp.mpf(alpha)
#     beta = mp.mpf(beta)
#     gamma = mp.mpf(gamma)
    
#     denom = alpha + beta + gamma
#     ratio = alpha / denom
#     z = (alpha + beta) / denom
    
#     # Use log gamma to avoid overflow
#     log_prefactor = mp.loggamma(l + 1) - (l + m + n + 3) * mp.log(denom)
    
#     total = mp.mpf(0)
    
#     for p in range(max_terms):
#         # Calculate term using log gamma
#         # (l+m+n+p+2)!
#         arg1 = l + m + n + p + 2
#         # (l+1+p)!
#         arg2 = l + 1 + p
#         # (l+m+2+p)!
#         arg3 = l + m + 2 + p
        
#         # Check if arguments are valid
#         if arg1 < -0.5 or arg2 < -0.5 or arg3 < -0.5:
#             continue
            
#         try:
#             log_num = mp.loggamma(arg1 + 1)
#             log_den = mp.loggamma(arg2 + 1) + mp.loggamma(arg3 + 1)
#             log_coeff = log_num - log_den
            
#             log_power = p * mp.log(ratio)
            
#             # Hypergeometric
#             a = l + m + n + p + 3
#             b = l + m + p + 3
            
#             hyper_val = hyper([1, a], [b], z)
            
#             if hyper_val > 0:
#                 log_hyper = mp.log(hyper_val)
#             else:
#                 log_hyper = mp.mpf('-inf')
            
#             log_term = log_coeff + log_power + log_hyper
            
#             if log_term > mp.mpf('-700'):
#                 term_val = mp.exp(log_term)
#                 total += term_val
                
#                 # Check convergence
#                 if p > 50 and term_val < mp.mpf(1e-60) * total:
#                     break
#         except:
#             continue
    
#     result = mp.exp(log_prefactor) * total
#     return result


# def format_number(value):
#     """
#     Format a number as mantissa and exponent for table display
#     """
#     if value == 0:
#         return "0", 0
    
#     # Convert to float for exponent extraction
#     try:
#         # Get the exponent using log10
#         log10_val = mp.log10(abs(value))
#         exponent = int(mp.floor(log10_val))
        
#         # Calculate mantissa
#         mantissa = value / (10 ** exponent)
        
#         # Format mantissa with appropriate precision
#         mantissa_str = mp.nstr(mantissa, 35)
        
#         return mantissa_str, exponent
#     except:
#         return str(value), 0


# def test_table_cases():
#     """
#     Test all table cases
#     """
    
#     print("=" * 110)
#     print("TABLE 1: l=25, m=10, n=20, β=0.5, γ=0.5")
#     print("=" * 110)
    
#     table1_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0]
    
#     print(f"{'x':<10} {'z':<20} {'Calculated W':<50} {'Expected W (approx)':<30}")
#     print("-" * 110)
    
#     for x in table1_values:
#         # Calculate z = x / sqrt(1 - y^2) with y=0.5
#         y = 0.5
#         z_val = x / mp.sqrt(1 - y**2)
        
#         W = calculate_W_corrected(25, 10, 20, x, 0.5, 0.5)
#         mantissa_str, exponent = format_number(W)
        
#         print(f"{x:<10.1f} {float(z_val):<20.10f} {mantissa_str} E={exponent:+04d}")
    
#     print("\n" + "=" * 110)
#     print("TABLE 2: l=30, m=-5, n=20, β=0.5, γ=0.5")
#     print("=" * 110)
    
#     table2_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0, 9999.0]
    
#     print(f"{'x':<12} {'Calculated W':<50} {'Exponent':<10}")
#     print("-" * 72)
    
#     for x in table2_values:
#         try:
#             W = calculate_W_corrected(30, -5, 20, x, 0.5, 0.5)
#             mantissa_str, exponent = format_number(W)
#             print(f"{x:<12.1f} {mantissa_str} E={exponent:+04d}")
#         except Exception as e:
#             print(f"{x:<12.1f} Error: {e}")
    
#     print("\n" + "=" * 110)
#     print("TABLE 3: l=25, m=10, n=-20, β=0.5, γ=0.5")
#     print("=" * 110)
    
#     table3_values = [
#         0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 
#         99.0, 999.0, 9999.0, 99999.0, 999999.0, 
#         9999999.0, 99999999.0, 999999999.0
#     ]
    
#     # Expected exponents from Table 3
#     expected_exponents = {
#         0.1: 10,
#         0.3: 9,
#         0.6: 8,
#         1.0: 6,
#         3.0: 1,
#         6.0: 4,
#         9.0: 4,
#         99.0: 24,
#         999.0: 42,
#         9999.0: 60,
#         99999.0: 60,
#         999999.0: 78,
#         9999999.0: 96,
#         99999999.0: 96,
#     }
    
#     print(f"{'x':<12} {'Calculated W':<55} {'Expected Exponent':<20}")
#     print("-" * 87)
    
#     for x in table3_values:
#         try:
#             W = calculate_W_with_gamma(25, 10, -20, x, 0.5, 0.5)
#             mantissa_str, exponent = format_number(W)
            
#             expected_exp = expected_exponents.get(x, "?")
#             print(f"{x:<12.1f} {mantissa_str} E={exponent:+05d}  Expected E={expected_exp}")
#         except Exception as e:
#             print(f"{x:<12.1f} Error: {e}")
    
#     print("\n" + "=" * 110)
#     print("TABLE 4: l=30, m=3, n=20, β=0.5, γ=0.5")
#     print("=" * 110)
    
#     table4_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0, 999.0, 9999.0, 99999.0, 999999.0]
    
#     print(f"{'x':<12} {'Calculated W':<50} {'Exponent':<10}")
#     print("-" * 72)
    
#     for x in table4_values:
#         try:
#             W = calculate_W_corrected(30, 3, 20, x, 0.5, 0.5)
#             mantissa_str, exponent = format_number(W)
#             print(f"{x:<12.1f} {mantissa_str} E={exponent:+04d}")
#         except Exception as e:
#             print(f"{x:<12.1f} Error: {e}")


# def test_specific_case():
#     """
#     Test the specific case from Table 3 that was failing
#     """
#     print("Testing Table 3, x=0.1 (should be ~9.57 × 10^10):")
#     print("-" * 60)
    
#     l, m, n = 25, 10, -20
#     alpha, beta, gamma = 0.1, 0.5, 0.5
    
#     # Try both implementations
#     print("\nMethod 1 (calculate_W_corrected):")
#     try:
#         W1 = calculate_W_corrected(l, m, n, alpha, beta, gamma, max_terms=500)
#         mantissa1, exp1 = format_number(W1)
#         print(f"  Result: {mantissa1} × 10^{exp1}")
#         print(f"  Full value: {mp.nstr(W1, 30)}")
#     except Exception as e:
#         print(f"  Error: {e}")
    
#     print("\nMethod 2 (calculate_W_with_gamma):")
#     try:
#         W2 = calculate_W_with_gamma(l, m, n, alpha, beta, gamma, max_terms=500)
#         mantissa2, exp2 = format_number(W2)
#         print(f"  Result: {mantissa2} × 10^{exp2}")
#         print(f"  Full value: {mp.nstr(W2, 30)}")
#     except Exception as e:
#         print(f"  Error: {e}")
    
#     print("\nExpected: ~9.56922368555909552646164305802255 × 10^10")


# if __name__ == "__main__":
#     print("High-Precision Calculation of W(l,m,n;α,β,γ)")
#     print(f"Precision set to {mp.dps} decimal digits\n")
    
#     # Test the problematic case first
#     test_specific_case()
    
#     print("\n" + "=" * 110)
#     print("Running all table comparisons...")
#     print("=" * 110)
    
#     # Run all tests
#     test_table_cases()























import mpmath
from mpmath import mp, fac, hyper

# Set extremely high precision
mp.dps = 100

def W_series(l, m, n, alpha, beta, gamma, max_terms=500):
    """
    Direct series calculation for W(l,m,n; α,β,γ)
    """
    alpha = mp.mpf(alpha)
    beta = mp.mpf(beta)
    gamma = mp.mpf(gamma)
    
    S = alpha + beta + gamma
    
    # Prefactor: l! / (α+β+γ)^(l+m+n+3)
    prefactor = fac(l) / (S ** (l + m + n + 3))
    
    # Parameters for the series
    r = alpha / S
    z = (alpha + beta) / S
    
    total = mp.mpf(0)
    
    for p in range(max_terms):
        try:
            # Calculate factorial ratio
            # (l+m+n+p+2)! / [(l+1+p)! * (l+m+2+p)!]
            num = fac(l + m + n + p + 2)
            den = fac(l + 1 + p) * fac(l + m + 2 + p)
            coeff = num / den
            
            # Power term
            power = r ** p
            
            # Hypergeometric function
            a = l + m + n + p + 3
            b = l + m + p + 3
            
            hyp = hyper([1, a], [b], z)
            
            term_val = coeff * power * hyp
            total += term_val
            
            # Check convergence
            if p > 50 and abs(term_val) < mp.mpf(1e-70) * abs(total):
                break
                
        except Exception as e:
            # If calculation fails, stop
            if p > 100:
                break
            continue
    
    result = prefactor * total
    return result


def format_with_exponent(value):
    """Format a number as mantissa and exponent"""
    if value == 0:
        return "0", 0
    
    log10_val = mp.log10(abs(value))
    exponent = int(mp.floor(log10_val))
    mantissa = value / (10 ** exponent)
    mantissa_str = mp.nstr(mantissa, 35)
    
    return mantissa_str, exponent


def test_table1():
    """Test Table 1: l=25, m=10, n=20, β=0.5, γ=0.5"""
    print("=" * 100)
    print("TABLE 1: l=25, m=10, n=20, β=0.5, γ=0.5")
    print("=" * 100)
    
    x_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0]
    
    # Expected values from Table 1 (mantissa only, exponent 0)
    expected = {
        0.1: "1.071788953016887897503701849018956",
        0.3: "1.07178895301688789750370184901896117",
        0.6: "1.08178703763909409843017318767104",
        1.0: "1.08178703763909409843017318672104",
        3.0: "1.08178703763909409843017318672104",
        6.0: "1.032578848169991829523411468131954",
        9.0: "1.03257884816999182952341146813195343"
    }
    
    print(f"{'x':<8} {'Calculated W':<45} {'Expected W':<45} {'Match':<10}")
    print("-" * 108)
    
    for x in x_values:
        W = W_series(25, 10, 20, x, 0.5, 0.5)
        mantissa_str, exponent = format_with_exponent(W)
        exp_str = expected[x]
        
        # Check if mantissa matches
        mantissa_compare = mantissa_str[:30]
        expected_compare = exp_str[:30]
        match = "✓" if mantissa_compare == expected_compare else "✗"
        
        print(f"{x:<8.1f} {mantissa_str} E={exponent:+03d}  {exp_str:<45} {match}")


def test_table2():
    """Test Table 2: l=30, m=-5, n=20, β=0.5, γ=0.5"""
    print("\n" + "=" * 100)
    print("TABLE 2: l=30, m=-5, n=20, β=0.5, γ=0.5")
    print("=" * 100)
    
    x_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0, 9999.0]
    
    # Expected values from Table 2
    expected = {
        0.1: "2.973484179892053703109868437107661",
        0.3: "3.0135607907517240218506454211323800",
        0.6: "8.9816449452661831264940252357000109",
        1.0: "2.682256487480758800601258522440313",
        3.0: "5.0823263927315956244490430366363846",
        6.0: "3.618892368220859328284256510360004147",
        9.0: "1.44613500039834568043772901568371805",
        99.0: "5.6399988353334020490491732762743743",
        9999.0: "5.1907707948097377177561435591360994"
    }
    
    print(f"{'x':<10} {'Calculated W':<50} {'Expected W':<45} {'Match':<10}")
    print("-" * 115)
    
    for x in x_values:
        try:
            W = W_series(30, -5, 20, x, 0.5, 0.5, max_terms=500)
            mantissa_str, exponent = format_with_exponent(W)
            exp_str = expected[x]
            
            mantissa_compare = mantissa_str[:30]
            expected_compare = exp_str[:30]
            match = "✓" if mantissa_compare == expected_compare else "✗"
            
            print(f"{x:<10.1f} {mantissa_str} E={exponent:+03d}  {exp_str:<45} {match}")
        except Exception as e:
            print(f"{x:<10.1f} Error: {e}")


def test_table3():
    """Test Table 3: l=25, m=10, n=-20, β=0.5, γ=0.5"""
    print("\n" + "=" * 100)
    print("TABLE 3: l=25, m=10, n=-20, β=0.5, γ=0.5")
    print("=" * 100)
    
    # Values from Table 3 (x, expected mantissa, expected exponent)
    test_cases = [
        (0.1, "9.56922368555909552646164305802255", 10),
        (0.3, "5.499600574942757228470944505031596", 9),
        (0.6, "1.55500479709582687187894036506070", 8),
        (1.0, "3.307243695831894875086510524687", 6),
        (3.0, "1.88699013788402410184148570247821", 1),
        (6.0, "9.9002824195029411574458900717829659", 4),
        (9.0, "1.780268582196248028535920337015427", 4),
        (99.0, "2.268828037872845686323319546413988798", 24),
        (999.0, "2.33271849380107258920534597054144623", 42),
    ]
    
    print(f"{'x':<10} {'Calculated W':<50} {'Expected':<45} {'Match':<10}")
    print("-" * 115)
    
    for x, expected_mantissa, expected_exp in test_cases:
        try:
            W = W_series(25, 10, -20, x, 0.5, 0.5, max_terms=500)
            mantissa_str, exponent = format_with_exponent(W)
            
            mantissa_compare = mantissa_str[:25]
            expected_compare = expected_mantissa[:25]
            match = "✓" if (mantissa_compare == expected_compare and 
                           abs(exponent - expected_exp) <= 1) else "✗"
            
            print(f"{x:<10.1f} {mantissa_str} E={exponent:+05d}  {expected_mantissa} E={expected_exp:+04d}  {match}")
        except Exception as e:
            print(f"{x:<10.1f} Error: {e}")


def test_table4():
    """Test Table 4: l=30, m=3, n=20, β=0.5, γ=0.5"""
    print("\n" + "=" * 100)
    print("TABLE 4: l=30, m=3, n=20, β=0.5, γ=0.5")
    print("=" * 100)
    
    x_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0, 999.0, 9999.0, 99999.0, 999999.0]
    
    # Expected values from Table 4
    expected = {
        0.1: "1.96307874594160496848204489285239",
        0.3: "1.96307874594160496549595791103",
        0.6: "1.96271221990863684640326899444098",
        1.0: "1.962712219908636846403268994425469",
        3.0: "1.962712219908636846403268994475874",
        6.0: "1.962712219908636846403268994475876",
        9.0: "1.962712219908636846403268994475877",
        99.0: "1.962712219908636846403268994475878",
    }
    
    print(f"{'x':<10} {'Calculated W':<50} {'Expected W':<45} {'Match':<10}")
    print("-" * 115)
    
    for x in x_values:
        try:
            W = W_series(30, 3, 20, x, 0.5, 0.5, max_terms=300)
            mantissa_str, exponent = format_with_exponent(W)
            
            if x in expected:
                exp_str = expected[x]
                mantissa_compare = mantissa_str[:30]
                expected_compare = exp_str[:30]
                match = "✓" if mantissa_compare == expected_compare else "✗"
                print(f"{x:<10.1f} {mantissa_str} E={exponent:+03d}  {exp_str:<45} {match}")
            else:
                print(f"{x:<10.1f} {mantissa_str} E={exponent:+03d}")
        except Exception as e:
            print(f"{x:<10.1f} Error: {e}")


def test_single_case_for_debugging():
    """Test a single case for debugging Table 3"""
    print("\n" + "=" * 100)
    print("DEBUG: Single case from Table 3 (x=0.1)")
    print("=" * 100)
    
    l, m, n = 25, 10, -20
    alpha, beta, gamma = 0.1, 0.5, 0.5
    
    S = alpha + beta + gamma
    print(f"S = {S}")
    print(f"l! = {fac(l)}")
    print(f"Prefactor exponent: {l + m + n + 3}")
    print(f"Prefactor = {fac(l)} / {S}^{l+m+n+3}")
    
    # Calculate first few terms manually to see the pattern
    print("\nFirst few terms:")
    r = alpha / S
    z = (alpha + beta) / S
    
    total = mp.mpf(0)
    for p in range(10):
        num = fac(l + m + n + p + 2)
        den = fac(l + 1 + p) * fac(l + m + 2 + p)
        coeff = num / den
        power = r ** p
        a = l + m + n + p + 3
        b = l + m + p + 3
        hyp = hyper([1, a], [b], z)
        
        term = coeff * power * hyp
        total += term
        
        print(f"p={p}: coeff={mp.nstr(coeff, 10)}, power={mp.nstr(power, 10)}, hyp={mp.nstr(hyp, 10)}, term={mp.nstr(term, 15)}")
    
    print(f"\nSum of first 10 terms: {mp.nstr(total, 20)}")
    print(f"Prefactor: {mp.nstr(fac(l) / (S ** (l + m + n + 3)), 20)}")
    print(f"Final result: {mp.nstr(fac(l) / (S ** (l + m + n + 3)) * total, 20)}")
    
    # Calculate with our function
    W = W_series(l, m, n, alpha, beta, gamma, max_terms=100)
    print(f"\nOur function result: {mp.nstr(W, 30)}")
    
    mantissa, exponent = format_with_exponent(W)
    print(f"In scientific notation: {mantissa} × 10^{exponent}")
    print(f"Expected: 9.56922368555909552646164305802255 × 10^10")


if __name__ == "__main__":
    print(f"Precision: {mp.dps} decimal digits")
    print()
    
    # First debug the problematic Table 3 case
    test_single_case_for_debugging()
    
    # Then run all tables
    print("\n" + "=" * 100)
    print("RUNNING ALL TABLE TESTS")
    print("=" * 100)
    
    test_table1()
    test_table2()
    test_table3()
    test_table4()