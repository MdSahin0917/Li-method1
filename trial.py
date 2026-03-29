






# # from mpmath import mp

# # mp.dps = 200


# # # ---------------- FAST 2F1 ---------------- #
# # def hyp2f1_fast(a, b, c, x, tol=1e-30, max_iter=10000):
# #     term = mp.mpf(1)
# #     s = term

# #     for k in range(1, max_iter):
# #         term *= (a + k - 1)*(b + k - 1) / ((c + k - 1)*k) * x
# #         s += term

# #         if abs(term) < tol:
# #             break

# #     return s


# # # ---------------- MAIN FUNCTION ---------------- #
# # def W(l, m, n, alpha, beta, gamma, tol=1e-30, pmax=10000):

# #     alpha = mp.mpf(alpha)
# #     beta  = mp.mpf(beta)
# #     gamma = mp.mpf(gamma)

# #     if l < 0 or (l+m+1) < 0 or (l+m+n+2) < 0:
# #         raise ValueError("Conditions violated")

# #     denom = alpha + beta + gamma
# #     x1 = alpha / denom
# #     x2 = (alpha + beta) / denom

# #     pref = mp.factorial(l) / (denom ** (l+m+n+3))

# #     # ---------------- p = 0 ---------------- #
# #     p = 0

# #     C = mp.factorial(l+m+n+2) / (
# #         mp.factorial(l+1) * (l+m+2)
# #     )

# #     x1_power = mp.mpf(1)

# #     term = C * hyp2f1_fast(
# #         1,
# #         l+m+n+3,
# #         l+m+3,
# #         x2,
# #         tol=tol
# #     )

# #     S = term

# #     # ---------------- LOOP ---------------- #
# #     for p in range(0, pmax-1):

# #         # update coefficient (CORRECTED)
# #         C *= ((l+m+n+p+3)/(l+2+p)) * ((l+m+2+p)/(l+m+3+p))

# #         # update power
# #         x1_power *= x1

# #         term = C * x1_power * hyp2f1_fast(
# #             1,
# #             l+m+n+p+4,
# #             l+m+p+4,
# #             x2,
# #             tol=tol
# #         )

# #         S += term

# #         if abs(term) < tol:
# #             break

# #     return pref * S

# # print(W(25,10,20,0.1,0.5,0.5))







# from mpmath import mp

# mp.dps = 200


# # ---------------- FAST 2F1 ---------------- #
# def hyp2f1_fast(a, b, c, x, tol=1e-30, max_iter=10000):
#     term = mp.mpf(1)
#     s = term

#     for k in range(1, max_iter):
#         term *= (a + k - 1)*(b + k - 1) / ((c + k - 1)*k) * x
#         s += term

#         if abs(term) < tol:
#             break

#     return s


# # ---------------- MAIN FUNCTION ---------------- #
# def W(l, m, n, alpha, beta, gamma, tol=1e-30, pmax=10000):

#     alpha = mp.mpf(alpha)
#     beta  = mp.mpf(beta)
#     gamma = mp.mpf(gamma)

#     if l < 0 or (l+m+1) < 0 or (l+m+n+2) < 0:
#         return mp.nan  # skip invalid

#     denom = alpha + beta + gamma
#     x1 = alpha / denom
#     x2 = (alpha + beta) / denom

#     pref = mp.factorial(l) / (denom ** (l+m+n+3))

#     C = mp.factorial(l+m+n+2) / (
#         mp.factorial(l+1) * (l+m+2)
#     )

#     x1_power = mp.mpf(1)

#     term = C * hyp2f1_fast(
#         1,
#         l+m+n+3,
#         l+m+3,
#         x2,
#         tol=tol
#     )

#     S = term

#     for p in range(0, pmax-1):

#         C *= ((l+m+n+p+3)/(l+2+p)) * ((l+m+2+p)/(l+m+3+p))
#         x1_power *= x1

#         term = C * x1_power * hyp2f1_fast(
#             1,
#             l+m+n+p+4,
#             l+m+p+4,
#             x2,
#             tol=tol
#         )

#         S += term

#         if abs(term) < tol:
#             break

#     return pref * S


# # ---------------- PARAMETERS ---------------- #
# alpha_values = [
#     0.1,0.3,0.6,1.0,3.0,6.0,9.0,
#     99.0,999.0,9999.0,99999.0,
#     999999.0,9999999.0,99999999.0
# ]

# cases = [
#     (25,10,20),
#     (30,-5,20),
#     (25,10,-20),
#     (30,-3,-20)
# ]

# beta  = mp.mpf('0.5')
# gamma = mp.mpf('0.5')


# # ---------------- TABLE ---------------- #
# for (l,m,n) in cases:
#     print("\n" + "="*80)
#     print(f"CASE: l={l}, m={m}, n={n}")
#     print("="*80)
#     print(f"{'alpha':>15} {'x=alpha/(a+b+g)':>25} {'W':>40}")
#     print("-"*80)

#     for a in alpha_values:
#         alpha = mp.mpf(a)
#         denom = alpha + beta + gamma
#         x = alpha / denom

#         try:
#             val = W(l,m,n,alpha,beta,gamma)
#             val_str = mp.nstr(val, 20)
#         except:
#             val_str = "ERROR"

#         print(f"{mp.nstr(alpha,8):>15} {mp.nstr(x,12):>25} {val_str:>40}")


















from mpmath import mp

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
    99.0
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
for (l,m,n) in cases:

    print("\n" + "="*90)
    print(f"CASE: l={l}, m={m}, n={n}")
    print("="*90)
    print(f"{'alpha':>15} {'x=alpha/(a+b+g)':>25} {'W (≈35+ digits)':>45}")
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