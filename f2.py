# import os
# from mpmath import mp

# mp.dps = 100

# # ---------------- FILES ---------------- #
# FAC_FILE = "facdata.dat"
# I_FILE   = "Idata.dat"

# # ---------------- CACHE ---------------- #
# fac_cache = {}
# I_cache   = {}

# # ---------------- FACTORIAL ---------------- #
# def load_factorials():
#     if not os.path.exists(FAC_FILE):
#         return
#     with open(FAC_FILE, "r") as f:
#         for line in f:
#             n, val = line.strip().split()
#             fac_cache[int(n)] = mp.mpf(val)


# def append_factorial(n, val):
#     with open(FAC_FILE, "a") as f:
#         f.write(f"{n} {val}\n")


# def get_factorial(n):
#     if n in fac_cache:
#         return fac_cache[n]

#     val = mp.mpf(1)
#     for i in range(2, n+1):
#         val *= i

#     fac_cache[n] = val
#     append_factorial(n, val)
#     return val


# # ---------------- LOAD I ---------------- #
# def load_I():
#     if not os.path.exists(I_FILE):
#         return
#     with open(I_FILE, "r") as f:
#         for line in f:
#             m, n, val = line.strip().split()
#             I_cache[(int(m), int(n))] = mp.mpf(val)


# def append_I(m, n, val):
#     with open(I_FILE, "a") as f:
#         f.write(f"{m} {n} {val}\n")


# # ---------------- BASE FUNCTIONS ---------------- #
# def I_10(alpha, beta, gamma):
#     denom = alpha + beta + gamma

#     term = mp.log((alpha + beta + gamma)/(beta + gamma))

#     s = mp.mpf(0)
#     for k in range(1, 100):
#         s += (1/k) * (alpha/denom)**k

#     return get_factorial(1)/(gamma**2) * (term - s)


# def I_1n(n, alpha, beta, gamma):
#     # Using equation (20) structure (simplified usable form)
#     denom = alpha + beta + gamma

#     val = mp.mpf(0)
#     for k in range(n+1):
#         val += (alpha/denom)**k / (k+1)

#     return val


# # ---------------- DP COMPUTATION ---------------- #
# def compute_all_I(m_max, n_max, alpha, beta, gamma):

#     denom = alpha + beta + gamma

#     # -------- STEP 1: m = 1 -------- #
#     for n in range(n_max+1):
#         if (1, n) in I_cache:
#             continue

#         if n == 0:
#             val = I_10(alpha, beta, gamma)
#         else:
#             val = I_1n(n, alpha, beta, gamma)

#         I_cache[(1, n)] = val
#         append_I(1, n, val)

#     # -------- STEP 2: build upward -------- #
#     for m in range(2, m_max+1):
#         for n in range(0, n_max+1):

#             if (m, n) in I_cache:
#                 continue

#             if n > m:  # invalid region
#                 continue

#             # SUM term from equation (16)
#             S = mp.mpf(0)
#             for k in range(n+1):
#                 num = get_factorial(l + k + 1 - m) * gamma**k
#                 den = get_factorial(k) * denom**(l + k + 2 - m)
#                 S += num / den

#             val = S / (m - 1)

#             # recursion
#             if (m-1, n) in I_cache:
#                 val -= (beta + gamma)/(m - 1) * I_cache[(m-1, n)]

#             if n-1 >= 0 and (m-1, n-1) in I_cache:
#                 val += gamma/(m - 1) * I_cache[(m-1, n-1)]

#             I_cache[(m, n)] = val
#             append_I(m, n, val)


# # ---------------- PARAMETERS ---------------- #
# alpha = mp.mpf('1.0')
# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')

# l = 25

# # ---------------- INIT ---------------- #
# load_factorials()
# load_I()

# # ---------------- RUN ---------------- #
# compute_all_I(m_max=5, n_max=20, alpha=alpha, beta=beta, gamma=gamma)

# # TEST OUTPUT
# for key in sorted(I_cache.keys()):
#     print(key, "->", mp.nstr(I_cache[key], 20))















# import os
# from mpmath import mp

# mp.dps = 100

# # ---------------- FILES ---------------- #
# FAC_FILE = "facdata.dat"
# I_FILE   = "Idata.dat"

# # ---------------- CACHE ---------------- #
# fac_cache = {}
# I_cache   = {}

# # ---------------- FACTORIAL ---------------- #
# def load_factorials():
#     if not os.path.exists(FAC_FILE):
#         return
#     with open(FAC_FILE, "r") as f:
#         for line in f:
#             n, val = line.strip().split()
#             fac_cache[int(n)] = mp.mpf(val)


# def append_factorial(n, val):
#     with open(FAC_FILE, "a") as f:
#         f.write(f"{n} {val}\n")


# def get_factorial(n):
#     if n in fac_cache:
#         return fac_cache[n]

#     val = mp.mpf(1)
#     for i in range(2, n+1):
#         val *= i

#     fac_cache[n] = val
#     append_factorial(n, val)
#     return val


# # ---------------- LOAD I ---------------- #
# def load_I():
#     if not os.path.exists(I_FILE):
#         return
#     with open(I_FILE, "r") as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 4:
#                 alpha, m, n, val = parts
#                 key = (mp.mpf(alpha), int(m), int(n))
#                 I_cache[key] = mp.mpf(val)


# def append_I(alpha, m, n, val):
#     with open(I_FILE, "a") as f:
#         f.write(f"{alpha} {m} {n} {val}\n")


# # ---------------- BASE FUNCTIONS ---------------- #
# def I_10(alpha, beta, gamma):
#     denom = alpha + beta + gamma

#     term = mp.log((alpha + beta + gamma)/(beta + gamma))

#     s = mp.mpf(0)
#     for k in range(1, 100):
#         s += (1/k) * (alpha/denom)**k

#     return get_factorial(1)/(gamma**2) * (term - s)


# def I_1n(n, alpha, beta, gamma):
#     denom = alpha + beta + gamma

#     val = mp.mpf(0)
#     for k in range(n+1):
#         val += (alpha/denom)**k / (k+1)

#     return val


# # ---------------- DP COMPUTATION ---------------- #
# def compute_all_I(m_max, n_max, alpha, beta, gamma):

#     denom = alpha + beta + gamma

#     # -------- STEP 1: m = 1 -------- #
#     for n in range(n_max+1):

#         key = (alpha, 1, n)

#         if key in I_cache:
#             continue

#         if n == 0:
#             val = I_10(alpha, beta, gamma)
#         else:
#             val = I_1n(n, alpha, beta, gamma)

#         I_cache[key] = val
#         append_I(alpha, 1, n, val)

#     # -------- STEP 2: DP build -------- #
#     for m in range(2, m_max+1):
#         for n in range(0, n_max+1):

#             if n > m:
#                 continue

#             key = (alpha, m, n)

#             if key in I_cache:
#                 continue

#             # SUM term
#             S = mp.mpf(0)
#             for k in range(n+1):
#                 num = get_factorial(l + k + 1 - m) * gamma**k
#                 den = get_factorial(k) * denom**(l + k + 2 - m)
#                 S += num / den

#             val = S / (m - 1)

#             # recursion
#             key1 = (alpha, m-1, n)
#             key2 = (alpha, m-1, n-1)

#             if key1 in I_cache:
#                 val -= (beta + gamma)/(m - 1) * I_cache[key1]

#             if n-1 >= 0 and key2 in I_cache:
#                 val += gamma/(m - 1) * I_cache[key2]

#             I_cache[key] = val
#             append_I(alpha, m, n, val)


# # ---------------- PARAMETERS ---------------- #
# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')
# l = 25

# # ---------------- INIT ---------------- #
# load_factorials()
# load_I()

# # ---------------- MULTIPLE ALPHAS ---------------- #
# alpha_values = [
#     0.1, 0.3, 0.6, 1.0, 3.0, 6.0,
#     9.0, 99.0, 999.0
# ]

# for a in alpha_values:
#     alpha = mp.mpf(a)
#     print(f"\n===== alpha = {a} =====")

#     compute_all_I(m_max=5, n_max=20, alpha=alpha, beta=beta, gamma=gamma)

#     # print some results
#     for m in range(1, 6):
#         for n in range(0, min(5, m)+1):
#             key = (alpha, m, n)
#             if key in I_cache:
#                 print(f"I({m},{n}) =", mp.nstr(I_cache[key], 20))



















# import os
# from mpmath import mp

# mp.dps = 100

# # ---------------- FILES ---------------- #
# FAC_FILE = "facdata.dat"
# I_FILE   = "Idata.dat"

# # ---------------- CACHE ---------------- #
# fac_cache = {}
# I_cache   = {}

# # ---------------- FACTORIAL ---------------- #
# def load_factorials():
#     if not os.path.exists(FAC_FILE):
#         return
#     with open(FAC_FILE, "r") as f:
#         for line in f:
#             n, val = line.strip().split()
#             fac_cache[int(n)] = mp.mpf(val)


# def append_factorial(n, val):
#     with open(FAC_FILE, "a") as f:
#         f.write(f"{n} {val}\n")


# def get_factorial(n):
#     if n in fac_cache:
#         return fac_cache[n]

#     val = mp.mpf(1)
#     for i in range(2, n+1):
#         val *= i

#     fac_cache[n] = val
#     append_factorial(n, val)
#     return val


# # ---------------- LOAD I ---------------- #
# def load_I():
#     if not os.path.exists(I_FILE):
#         return
#     with open(I_FILE, "r") as f:
#         for line in f:
#             m, n, val = line.strip().split()
#             I_cache[(int(m), int(n))] = mp.mpf(val)


# def append_I(m, n, val):
#     with open(I_FILE, "a") as f:
#         f.write(f"{m} {n} {val}\n")


# # ---------------- BASE FUNCTIONS ---------------- #
# def I_10():
#     denom = alpha + beta + gamma

#     term = mp.log((alpha + beta + gamma)/(beta + gamma))

#     s = mp.mpf(0)
#     for k in range(1, l+1):
#         s += (1/k) * (alpha/denom)**k

#     return get_factorial(l)/(alpha**(l+1)) * (term - s)


# def I_1n(n):
#     denom = alpha + beta + gamma
#     denom2 = beta + gamma

#     val = mp.mpf(0)
#     for k in range(1,n+1):
#         for q in range(k):
#             val += (mp.factorial(l + q) * (gamma**k)*(beta+gamma)**q) / (mp.factorial(q) * k * denom**(l + 1) * (denom2**k)*(denom**q))

#     return val+I_10()


# # ---------------- LAZY COMPUTATION ---------------- #
# def compute_I(m, n):

#     # -------- CACHE -------- #
#     if (m, n) in I_cache:
#         return I_cache[(m, n)]

#     # -------- BASE CASES -------- #
#     if m == 1 and n == 0:
#         val = I_10()

#     elif m == 1:
#         val = I_1n(n)

#     elif n < 0 or m <= 0:
#         return mp.mpf(0)

#     else:
#         denom = alpha + beta + gamma

#         # SUM term
#         S = mp.mpf(0)
#         for k in range(n+1):
#             num = get_factorial(l + k + 1 - m) * gamma**k
#             den = get_factorial(k) * denom**(l + k + 2 - m)
#             S += num / den

#         val = S / (m - 1)

#         #  ONLY REQUIRED CALLS
#         if  m != 1:
#             val -= (beta + gamma)/(m - 1) * compute_I(m-1, n)
#             val += gamma/(m - 1) * compute_I(m-1, n-1)
#         elif m == 1 and n > 0:
#             val -= (beta + gamma)/(m - 1) * I_1n(n)
#             val += gamma/(m - 1) * I_1n(n-1)

#     # -------- STORE -------- #
#     I_cache[(m, n)] = val*mp.factorial(n)/gamma**(n+1)
#     append_I(m, n, val*mp.factorial(n)/gamma**(n+1))

#     return val*mp.factorial(n)/gamma**(n+1)


# # ---------------- PARAMETERS ---------------- #
# alpha = mp.mpf('9.0')
# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')

# l = 30

# # ---------------- INIT ---------------- #
# load_factorials()
# load_I()

# # ---------------- TARGET COMPUTATION ---------------- #
# # print("Result:", mp.nstr(compute_I(5, 20), 30))
# print("Result:", compute_I(5, 20))


# import os
# from mpmath import mp

# mp.dps = 100

# FAC_FILE = "facdata.dat"
# I_FILE   = "Idata.dat"

# fac_cache = {}
# J_cache   = {}   # store core J, not I


# # ---------------- FACTORIAL ---------------- #
# def load_factorials():
#     if not os.path.exists(FAC_FILE):
#         return
#     with open(FAC_FILE, "r") as f:
#         for line in f:
#             n, val = line.strip().split()
#             fac_cache[int(n)] = mp.mpf(val)


# def append_factorial(n, val):
#     with open(FAC_FILE, "a") as f:
#         f.write(f"{n} {val}\n")


# def get_factorial(n):
#     if n in fac_cache:
#         return fac_cache[n]

#     val = mp.mpf(1)
#     for i in range(2, n+1):
#         val *= i

#     fac_cache[n] = val
#     append_factorial(n, val)
#     return val


# # ---------------- LOAD J ---------------- #
# def load_J():
#     if not os.path.exists(I_FILE):
#         return
#     with open(I_FILE, "r") as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 3:
#                 m, n, val = parts
#                 J_cache[(int(m), int(n))] = mp.mpf(val)


# def append_J(m, n, val):
#     with open(I_FILE, "a") as f:
#         f.write(f"{m} {n} {val}\n")


# # ---------------- BASE CASES (J) ---------------- #
# def J_10():
#     denom = alpha + beta + gamma

#     term = mp.log((alpha + beta + gamma)/(beta + gamma))

#     s = mp.mpf(0)
#     for k in range(1, l+1):
#         s += (1/k) * (alpha/denom)**k

#     return get_factorial(l)/(alpha**(l+1)) * (term - s)


# def J_1n(n):
#     denom = alpha + beta + gamma
#     denom2 = beta + gamma

#     val = mp.mpf(0)
#     for k in range(1,n+1):
#         for q in range(k):
#             val += (mp.factorial(l + q) * (gamma**k)*(beta+gamma)**q) / (mp.factorial(q) * k * denom**(l + 1) * (denom2**k)*(denom**q))

#     return val+J_10()


# # ---------------- CORE RECURSION ---------------- #
# def compute_J(m, n):

#     if (m, n) in J_cache:
#         return J_cache[(m, n)]

#     if m == 1 and n == 0:
#         val = J_10()

#     elif m == 1:
#         val = J_1n(n)

#     elif n < 0 or m <= 0:
#         return mp.mpf(0)

#     else:
#         denom = alpha + beta + gamma

#         S = mp.mpf(0)
#         for k in range(n+1):
#             num = get_factorial(l + k + 1 - m) * gamma**k
#             den = get_factorial(k) * denom**(l + k + 2 - m)
#             S += num / den

#         val = S / (m - 1)

#         val -= (beta + gamma)/(m - 1) * compute_J(m-1, n)
#         val += gamma/(m - 1) * compute_J(m-1, n-1)
#         if  m != 1:
#             val -= (beta + gamma)/(m - 1) * compute_J(m-1, n)
#             val += gamma/(m - 1) * compute_J(m-1, n-1)
#         elif m == 1 and n > 0:
#             val -= (beta + gamma)/(m - 1) * J_1n(n)
#             val += gamma/(m - 1) * J_1n(n-1)

#     J_cache[(m, n)] = val
#     append_J(m, n, val)

#     return val


# # ---------------- FINAL I ---------------- #
# def compute_I(m, n):
#     J = compute_J(m, n)
#     return (get_factorial(n) / gamma**(n+1)) * J


# # ---------------- PARAMETERS ---------------- #
# alpha = mp.mpf('1.0')
# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')
# l = 25

# # ---------------- INIT ---------------- #
# load_factorials()
# load_J()

# # ---------------- TEST ---------------- #
# res = compute_I(5, 20)
# print("I(5,20) =", mp.nstr(res, 25))
















# # # # # # import os
# # # # # # from mpmath import mp

# # # # # # mp.dps = 100

# # # # # # FAC_FILE = "facdata.dat"
# # # # # # I_FILE   = "Idata.dat"

# # # # # # fac_cache = {}
# # # # # # J_cache   = {}   # store core J, not I


# # # # # # # ---------------- FACTORIAL ---------------- #
# # # # # # def load_factorials():
# # # # # #     if not os.path.exists(FAC_FILE):
# # # # # #         return
# # # # # #     with open(FAC_FILE, "r") as f:
# # # # # #         for line in f:
# # # # # #             n, val = line.strip().split()
# # # # # #             fac_cache[int(n)] = mp.mpf(val)


# # # # # # def append_factorial(n, val):
# # # # # #     with open(FAC_FILE, "a") as f:
# # # # # #         f.write(f"{n} {val}\n")


# # # # # # def get_factorial(n):
# # # # # #     if n in fac_cache:
# # # # # #         return fac_cache[n]

# # # # # #     val = mp.mpf(1)
# # # # # #     for i in range(2, n+1):
# # # # # #         val *= i

# # # # # #     fac_cache[n] = val
# # # # # #     append_factorial(n, val)
# # # # # #     return val


# # # # # # # ---------------- LOAD J ---------------- #
# # # # # # def load_J():
# # # # # #     if not os.path.exists(I_FILE):
# # # # # #         return
# # # # # #     with open(I_FILE, "r") as f:
# # # # # #         for line in f:
# # # # # #             parts = line.strip().split()
# # # # # #             if len(parts) == 3:
# # # # # #                 m, n, val = parts
# # # # # #                 J_cache[(int(m), int(n))] = mp.mpf(val)


# # # # # # def append_J(m, n, val):
# # # # # #     with open(I_FILE, "a") as f:
# # # # # #         f.write(f"{m} {n} {val}\n")


# # # # # # # ---------------- BASE CASES (J) ---------------- #
# # # # # # def J_10():
# # # # # #     denom = alpha + beta + gamma

# # # # # #     term = mp.log((alpha + beta + gamma)/(beta + gamma))

# # # # # #     s = mp.mpf(0)
# # # # # #     for k in range(1, l+1):
# # # # # #         s += (1/k) * (alpha/denom)**k

# # # # # #     if alpha < 0.9 * beta or alpha < 0.9 * gamma:
# # # # # #         return get_factorial(l)/(alpha**(l+1)) * (s)
# # # # # #     else:
# # # # # #         return get_factorial(l)/(alpha**(l+1)) * (term - s)


# # # # # # def J_1n(n):
# # # # # #     denom = alpha + beta + gamma
# # # # # #     denom2 = beta + gamma

# # # # # #     val = mp.mpf(0)
# # # # # #     for k in range(1,n+1):
# # # # # #         for q in range(k):
# # # # # #             val += (mp.factorial(l + q) * (gamma**k)*(beta+gamma)**q) / (mp.factorial(q) * k * denom**(l + 1) * (denom2**k)*(denom**q))

# # # # # #     return val+J_10()


# # # # # # # ---------------- CORE RECURSION ---------------- #
# # # # # # def compute_J(m, n):

# # # # # #     if (m, n) in J_cache:
# # # # # #         return J_cache[(m, n)]

    
# # # # # #     denom = alpha + beta + gamma

# # # # # #     S = mp.mpf(0)
# # # # # #     for k in range(n+1):
# # # # # #         num = get_factorial(l + k + 1 - m) * gamma**k
# # # # # #         den = get_factorial(k) * denom**(l + k + 2 - m)
# # # # # #         S += (num / den)

# # # # # #     val = S 

# # # # # #     # val -= (beta + gamma)/(m - 1) * compute_J(m-1, n)
# # # # # #     # val += gamma/(m - 1) * compute_J(m-1, n-1)
# # # # # #     if  m > 1 and n >= 1:
# # # # # #         val -= val*(1/(m-1)) * (beta + gamma)/(m - 1) * compute_J(m-1, n)
# # # # # #         val += val*(1/(m-1)) * gamma/(m - 1) * compute_J(m-1, n-1)
# # # # # #     elif m == 1 and n >= 1:
# # # # # #         val -=  J_1n(n)
# # # # # #         val +=  J_1n(n-1)

# # # # # #     J_cache[(m, n)] = val
# # # # # #     append_J(m, n, val)

# # # # # #     return val


# # # # # # # ---------------- FINAL I ---------------- #
# # # # # # def compute_I(m, n):
# # # # # #     J = compute_J(m, n)
# # # # # #     return (get_factorial(n) / gamma**(n+1)) * J


# # # # # # # ---------------- PARAMETERS ---------------- #
# # # # # # alpha = mp.mpf('1.0')
# # # # # # beta  = mp.mpf('0.5')
# # # # # # gamma = mp.mpf('0.5')
# # # # # # l = 25

# # # # # # # ---------------- INIT ---------------- #
# # # # # # load_factorials()
# # # # # # load_J()

# # # # # # # ---------------- TEST ---------------- #
# # # # # # res = compute_I(5, 20)
# # # # # # print("I(5,20) =", mp.nstr(res, 25))




















# # # # # import os
# # # # # from mpmath import mp

# # # # # mp.dps = 100

# # # # # FAC_FILE = "facdata.dat"
# # # # # I_FILE   = "Idata.dat"

# # # # # fac_cache = {}
# # # # # J_cache   = {}


# # # # # # ---------------- FACTORIAL ---------------- #
# # # # # def load_factorials():
# # # # #     if not os.path.exists(FAC_FILE):
# # # # #         return
# # # # #     with open(FAC_FILE, "r") as f:
# # # # #         for line in f:
# # # # #             n, val = line.strip().split()
# # # # #             fac_cache[int(n)] = mp.mpf(val)


# # # # # def append_factorial(n, val):
# # # # #     with open(FAC_FILE, "a") as f:
# # # # #         f.write(f"{n} {val}\n")


# # # # # def get_factorial(n):
# # # # #     if n in fac_cache:
# # # # #         return fac_cache[n]

# # # # #     val = mp.mpf(1)
# # # # #     for i in range(2, n+1):
# # # # #         val *= i

# # # # #     fac_cache[n] = val
# # # # #     append_factorial(n, val)
# # # # #     return val


# # # # # # ---------------- LOAD J ---------------- #
# # # # # def load_J():
# # # # #     if not os.path.exists(I_FILE):
# # # # #         return
# # # # #     with open(I_FILE, "r") as f:
# # # # #         for line in f:
# # # # #             parts = line.strip().split()
# # # # #             if len(parts) == 3:
# # # # #                 m, n, val = parts
# # # # #                 J_cache[(int(m), int(n))] = mp.mpf(val)


# # # # # def append_J(m, n, val):
# # # # #     with open(I_FILE, "a") as f:
# # # # #         f.write(f"{m} {n} {val}\n")


# # # # # # ---------------- BASE CASES ---------------- #
# # # # # def J_10():
# # # # #     denom = alpha + beta + gamma

# # # # #     term = mp.log((alpha + beta + gamma)/(beta + gamma))

# # # # #     s = mp.mpf(0)
# # # # #     for k in range(1, l+1):
# # # # #         s += (1/k) * (alpha/denom)**k

# # # # #     if alpha < 0.9 * beta or alpha < 0.9 * gamma:
# # # # #         return get_factorial(l)/(alpha**(l+1)) * s
# # # # #     else:
# # # # #         return get_factorial(l)/(alpha**(l+1)) * (term - s)


# # # # # def J_1n(n):
# # # # #     denom = alpha + beta + gamma
# # # # #     denom2 = beta + gamma

# # # # #     val = mp.mpf(0)

# # # # #     for k in range(1, n+1):
# # # # #         for q in range(k):
# # # # #             num = get_factorial(l + q) * (gamma**k) * (denom2**q)
# # # # #             den = get_factorial(q) * k * (denom**(l + 1 + q)) * (denom2**k)
# # # # #             val += num / den

# # # # #     return val + J_10()


# # # # # # ---------------- CORE RECURSION ---------------- #
# # # # # def compute_J(m, n):

# # # # #     if (m, n) in J_cache:
# # # # #         return J_cache[(m, n)]

# # # # #     # BASE CASE
# # # # #     if m == 1:
# # # # #         val = J_1n(n)
# # # # #         J_cache[(m, n)] = val
# # # # #         append_J(m, n, val)
# # # # #         return val

# # # # #     denom = alpha + beta + gamma

# # # # #     # SUM PART
# # # # #     S = mp.mpf(0)
# # # # #     for k in range(n+1):
# # # # #         num = get_factorial(l + k + 1 - m) * gamma**k
# # # # #         den = get_factorial(k) * denom**(l + k + 2 - m)
# # # # #         S += num / den

# # # # #     val = S

# # # # #     # RECURSION (CORRECT)
# # # # #     if n >= 1:
# # # # #         val -= (beta + gamma)/(m - 1) * compute_J(m-1, n)
# # # # #         val += gamma/(m - 1) * compute_J(m-1, n-1)
# # # # #     else:
# # # # #         val -= (beta + gamma)/(m - 1) * compute_J(m-1, 0)

# # # # #     J_cache[(m, n)] = val
# # # # #     append_J(m, n, val)

# # # # #     return val


# # # # # # ---------------- FINAL I ---------------- #
# # # # # def compute_I(m, n):
# # # # #     J = compute_J(m, n)
# # # # #     return (get_factorial(n) / gamma**(n+1)) * J


# # # # # # ---------------- PARAMETERS ---------------- #
# # # # # alpha = mp.mpf('1.0')
# # # # # beta  = mp.mpf('0.5')
# # # # # gamma = mp.mpf('0.5')
# # # # # l = 25


# # # # # # ---------------- INIT ---------------- #
# # # # # load_factorials()
# # # # # load_J()


# # # # # # ---------------- TEST ---------------- #
# # # # # res = compute_I(5, 20)
# # # # # print("I(5,20) =", mp.nstr(res, 30))








# # # # import os
# # # # from mpmath import mp

# # # # mp.dps = 100

# # # # FAC_FILE = "facdata.dat"
# # # # I_FILE   = "Idata.dat"

# # # # fac_cache = {}
# # # # J_cache   = {}


# # # # # ---------------- FACTORIAL ---------------- #
# # # # def load_factorials():
# # # #     if not os.path.exists(FAC_FILE):
# # # #         return
# # # #     with open(FAC_FILE, "r") as f:
# # # #         for line in f:
# # # #             n, val = line.strip().split()
# # # #             fac_cache[int(n)] = mp.mpf(val)


# # # # def append_factorial(n, val):
# # # #     with open(FAC_FILE, "a") as f:
# # # #         f.write(f"{n} {val}\n")


# # # # def get_factorial(n):
# # # #     if n in fac_cache:
# # # #         return fac_cache[n]

# # # #     val = mp.mpf(1)
# # # #     for i in range(2, n+1):
# # # #         val *= i

# # # #     fac_cache[n] = val
# # # #     append_factorial(n, val)
# # # #     return val


# # # # # ---------------- LOAD J ---------------- #
# # # # def load_J():
# # # #     if not os.path.exists(I_FILE):
# # # #         return
# # # #     with open(I_FILE, "r") as f:
# # # #         for line in f:
# # # #             parts = line.strip().split()
# # # #             if len(parts) == 3:
# # # #                 m, n, val = parts
# # # #                 J_cache[(int(m), int(n))] = mp.mpf(val)


# # # # def append_J(m, n, val):
# # # #     with open(I_FILE, "a") as f:
# # # #         f.write(f"{m} {n} {val}\n")


# # # # # ---------------- BASE CASES ---------------- #
# # # # def J_10():
# # # #     denom = alpha + beta + gamma

# # # #     term = mp.log((alpha + beta + gamma)/(beta + gamma))

# # # #     s = mp.mpf(0)
# # # #     for k in range(1, l+1):
# # # #         s += (1/k) * (alpha/denom)**k

# # # #     if alpha < 0.9 * beta or alpha < 0.9 * gamma:
# # # #         return get_factorial(l)/(alpha**(l+1)) * s
# # # #     else:
# # # #         return get_factorial(l)/(alpha**(l+1)) * (term - s)


# # # # def J_1n(n):
# # # #     denom = alpha + beta + gamma
# # # #     denom2 = beta + gamma

# # # #     val = mp.mpf(0)

# # # #     for k in range(1, n+1):
# # # #         for q in range(k):
# # # #             num = get_factorial(l + q) * (gamma**k) * (denom2**q)
# # # #             den = get_factorial(q) * k * (denom**(l + q + 1)) * (denom2**k)
# # # #             val += num / den

# # # #     return val + J_10()


# # # # # ---------------- CORE RECURSION ---------------- #
# # # # def compute_J(m, n):

# # # #     if (m, n) in J_cache:
# # # #         return J_cache[(m, n)]

# # # #     # BASE CASE
# # # #     if m == 1:
# # # #         val = J_1n(n)
# # # #         J_cache[(m, n)] = val
# # # #         append_J(m, n, val)
# # # #         return val

# # # #     denom = alpha + beta + gamma

# # # #     # ----------- CORRECT S TERM ----------- #
# # # #     S = mp.mpf(0)
# # # #     for k in range(n+1):
# # # #         num = get_factorial(l + k - m) * (gamma**k)
# # # #         den = get_factorial(k) * (denom**(l + k + 1 - m))
# # # #         S += num / den

# # # #     val = S

# # # #     # ----------- RECURSION ----------- #
# # # #     if n >= 1:
# # # #         val -= (beta + gamma)/(m - 1) * compute_J(m-1, n)
# # # #         val += gamma/(m - 1) * compute_J(m-1, n-1)
# # # #     else:
# # # #         val -= (beta + gamma)/(m - 1) * compute_J(m-1, 0)

# # # #     J_cache[(m, n)] = val
# # # #     append_J(m, n, val)

# # # #     return val


# # # # # ---------------- FINAL I ---------------- #
# # # # def compute_I(m, n):
# # # #     J = compute_J(m, n)
# # # #     return (get_factorial(n) / (gamma**(n+1))) * J


# # # # # ---------------- PARAMETERS ---------------- #
# # # # alpha = mp.mpf('1.0')
# # # # beta  = mp.mpf('0.5')
# # # # gamma = mp.mpf('0.5')
# # # # l = 25


# # # # # ---------------- INIT ---------------- #
# # # # load_factorials()
# # # # load_J()


# # # # # ---------------- TEST ---------------- #
# # # # res = compute_I(5, 20)
# # # # print("I(5,20) =", mp.nstr(res, 40))
















# # # from mpmath import mp

# # # mp.dps = 100  # precision

# # # # ---------------- PARAMETERS ---------------- #
# # # alpha = mp.mpf('0.1')
# # # beta  = mp.mpf('0.5')
# # # gamma = mp.mpf('0.5')

# # # A = alpha + beta + gamma
# # # B = beta + gamma

# # # # ---------------- CACHE ---------------- #
# # # I_cache = {}

# # # # ---------------- STABLE SERIES ---------------- #
# # # def stable_series(n):
# # #     x = alpha / A

# # #     s = mp.mpf('0')
# # #     k = n + 1

# # #     # infinite sum (truncate safely)
# # #     while True:
# # #         term = (x**k) / k
# # #         s += term
# # #         if abs(term) < mp.mpf('1e-40'):
# # #             break
# # #         k += 1

# # #     return s


# # # # ---------------- I(1,n) ---------------- #
# # # def I_1n(n):
# # #     # first part
# # #     term1 = mp.factorial(n) / (alpha**(n+1)) * (
# # #         mp.log((A)/(B)) - sum((1/k)*(alpha/A)**k for k in range(1, n+1))
# # #     )

# # #     # stable correction (VERY IMPORTANT)
# # #     stable = mp.factorial(n) / (alpha**(n+1)) * stable_series(n)

# # #     # second part
# # #     term2 = mp.mpf('0')
# # #     for k in range(1, n+1):
# # #         for q in range(0, k+1):
# # #             term2 += (
# # #                 mp.binomial(k, q)
# # #                 * mp.factorial(q)
# # #                 / (k * (A**(q+1)))
# # #                 * (gamma/B)**k
# # #                 * (B/A)**q
# # #             )

# # #     return term1 + stable + term2


# # # # ---------------- I(m,0) ---------------- #
# # # def I_m0(m):
# # #     if (m, 0) in I_cache:
# # #         return I_cache[(m, 0)]

# # #     if m == 1:
# # #         val = I_1n(0)
# # #     else:
# # #         val = (
# # #             mp.factorial(2 - m) / ((m - 1) * (A ** (2 - m)))
# # #             + (B / (m - 1)) * I_m0(m - 1)
# # #         )

# # #     I_cache[(m, 0)] = val
# # #     return val


# # # # ---------------- MAIN RECURSION ---------------- #
# # # def I(m, n):
# # #     if (m, n) in I_cache:
# # #         return I_cache[(m, n)]

# # #     if m == 1:
# # #         val = I_1n(n)

# # #     elif n == 0:
# # #         val = I_m0(m)

# # #     else:
# # #         val = (
# # #             (B / (m - 1)) * I(m - 1, n)
# # #             + (gamma / (m - 1)) * I(m - 1, n - 1)
# # #         )

# # #     I_cache[(m, n)] = val
# # #     return val


# # # # ---------------- TEST ---------------- #
# # # if __name__ == "__main__":
# # #     m = 5
# # #     n = 20

# # #     result = I(m, n)
# # #     print(f"I({m},{n}) = {mp.nstr(result, 40)}")























# # from mpmath import mp

# # mp.dps = 100

# # # ---------------- PARAMETERS ---------------- #
# # alpha = mp.mpf('0.1')
# # beta  = mp.mpf('0.5')
# # gamma = mp.mpf('0.5')
# # l = 30   # MUST be defined

# # A = alpha + beta + gamma
# # B = beta + gamma

# # # ---------------- CACHE ---------------- #
# # I_cache = {}

# # # ---------------- STABLE SERIES ---------------- #
# # def stable_series(n):
# #     x = alpha / A
# #     s = mp.mpf('0')
# #     k = n + 1

# #     while True:
# #         term = (x**k) / k
# #         s += term
# #         if abs(term) < mp.mpf('1e-40'):
# #             break
# #         k += 1

# #     return s


# # # ---------------- I(1,n) ---------------- #
# # def I_1n(n):
# #     # ----- PART A -----
# #     if alpha < B:  # use stable form
# #         log_part = stable_series(n)
# #     else:
# #         log_part = mp.log(A/B) - sum((1/k)*(alpha/A)**k for k in range(1, n+1))

# #     partA = mp.factorial(l) / (alpha**(l+1)) * log_part

# #     # ----- PART B -----
# #     partB = mp.mpf('0')

# #     for k in range(1, n+1):
# #         for q in range(0, k):
# #             partB += (
# #                 mp.factorial(l + q) / mp.factorial(q)
# #                 * (1 / (k * (A**(l + 1))))
# #                 * (gamma / B)**k
# #                 * (B / A)**q
# #             )

# #     return partA + partB


# # # ---------------- I(m,0) ---------------- #
# # def I_m0(m):
# #     if (m, 0) in I_cache:
# #         return I_cache[(m, 0)]

# #     if m == 1:
# #         val = I_1n(0)
# #     else:
# #         val = (
# #             mp.factorial(l + 1 - m)
# #             / ((m - 1) * (A ** (l + 2 - m)))
# #             + (B / (m - 1)) * I_m0(m - 1)
# #         )

# #     I_cache[(m, 0)] = val
# #     return val


# # # ---------------- MAIN ---------------- #
# # def I(m, n):
# #     # validity check (CRUCIAL)
# #     if (l - m + 1) < 0 or (l - m + n + 2) < 0:
# #         raise ValueError("Invalid (m,n) for given l")

# #     if (m, n) in I_cache:
# #         return I_cache[(m, n)]

# #     if m == 1:
# #         val = I_1n(n)

# #     elif n == 0:
# #         val = I_m0(m)

# #     else:
# #         val = (
# #             (B / (m - 1)) * I(m - 1, n)
# #             + (gamma / (m - 1)) * I(m - 1, n - 1)
# #         )

# #     I_cache[(m, n)] = val
# #     return val


# # # ---------------- TEST ---------------- #
# # if __name__ == "__main__":
# #     m = 5
# #     n = 20

# #     res = I(m, n)
# #     print(f"I({m},{n}) = {mp.nstr(res, 40)}")



























# from mpmath import mp

# mp.dps = 100

# # ---------------- PARAMETERS ---------------- #
# alpha = mp.mpf('9.0')
# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')
# l = 30

# A = alpha + beta + gamma
# B = beta + gamma

# # ---------------- CACHE ---------------- #
# I_cache = {}

# # ---------------- STABLE SERIES ---------------- #
# def stable_series_from_1():
#     x = alpha / A
#     s = mp.mpf('0')
#     k = 1

#     while True:
#         term = (x**k) / k
#         s += term
#         if abs(term) < mp.mpf('1e-40'):
#             break
#         k += 1

#     return s


# def stable_series_from_n(n):
#     x = alpha / A
#     s = mp.mpf('0')
#     k = n + 1

#     while True:
#         term = (x**k) / k
#         s += term
#         if abs(term) < mp.mpf('1e-40'):
#             break
#         k += 1

#     return s


# # ---------------- I(1,0) ---------------- #
# def I_10():
#     if alpha < B:
#         log_part = stable_series_from_1()
#     else:
#         log_part = mp.log(A / B) - sum((1/k)*(alpha/A)**k for k in range(1, l+1))

#     return mp.factorial(l) / (alpha**(l+1)) * log_part


# # ---------------- I(1,n) ---------------- #
# def I_1n(n):
#     if n == 0:
#         return I_10()

#     # ----- PART A -----
#     if alpha < B:
#         log_part = stable_series_from_n(n)
#     else:
#         log_part = mp.log(A/B) - sum((1/k)*(alpha/A)**k for k in range(1, l+1))

#     partA = mp.factorial(l) / (alpha**(l+1)) * log_part

#     # ----- PART B -----
#     partB = mp.mpf('0')

#     for k in range(1, n+1):
#         for q in range(0, l+1):
#             partB += (
#                 mp.factorial(l + q) / mp.factorial(q)
#                 * (1 / (k * (A**(l + q + 1))))
#                 * (gamma / B)**k
#                 * (B / A)**q
#             )

#     return partA + partB


# # ---------------- I(m,0) ---------------- #
# def I_m0(m):
#     if (m, 0) in I_cache:
#         return I_cache[(m, 0)]

#     if m == 1:
#         val = I_10()
#     else:
#         val = (
#             mp.factorial(l + 1 - m)
#             / ((m - 1) * (A ** (l + 2 - m)))
#             + (B / (m - 1)) * I_m0(m - 1)
#         )

#     I_cache[(m, 0)] = val
#     return val


# # ---------------- MAIN RECURSION ---------------- #
# def I(m, n):
#     # validity check
#     if (l - m + 1) < 0 or (l - m + n + 2) < 0:
#         raise ValueError("Invalid (m,n) for given l")

#     if (m, n) in I_cache:
#         return I_cache[(m, n)]

#     if m == 1:
#         val = I_1n(n)

#     elif n == 0:
#         val = I_m0(m)

#     else:
#         val = (
#             (B / (m - 1)) * I(m - 1, n)
#             + (gamma / (m - 1)) * I(m - 1, n - 1)
#         )

#     I_cache[(m, n)] = val
#     return val


# # ---------------- TEST ---------------- #
# if __name__ == "__main__":
#     print("I(1,0) =", mp.nstr(I_10(), 40))

#     m = 5
#     n = 20
#     res = I(m, n)

#     print(f"I({m},{n}) = {mp.nstr(res, 40)}")