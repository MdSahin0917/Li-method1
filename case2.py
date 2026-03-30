# # # # from mpmath import mp, mpf, quad, power, exp, sqrt

# # # # # Set high precision (adjust as needed)
# # # # mp.dps = 150   # 50 decimal places for multiple precision
# # # # # l = 30
# # # # # m = 5
# # # # # n = 20
# # # # # alpha = 0.1
# # # # # beta = 0.5
# # # # # gamma = 0.5

# # # # # l = mpf(l)
# # # # # m = mpf(m)
# # # # # n = mpf(n)
# # # # # alpha = mpf(alpha)
# # # # # beta = mpf(beta)
# # # # # gamma = mpf(gamma)


# # # # def I(l,m,n,alpha,beta,gamma):
# # # #     sum1 = 0
# # # #     for k in range(0,19):
# # # #         sum1 += (mp.factorial(l+k+1-m)*gamma**k)/(mp.factorial(k)*(alpha+beta+gamma)**(l+k+2-m))
# # # #     if m>2 and n>1:
# # # #         return ((sum1 - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma) ) + (gamma/(m-1)*I(l,m-1,n-1,alpha,beta,gamma)))

# # # #     elif m == 2 and n>1:
# # # #         return ((sum1 - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_1n(l,n-1,alpha,beta,gamma)))

# # # #     elif m>2 and n==1:
# # # #         return ((sum1 - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_m0(l,m-1,alpha,beta,gamma)))
# # # #     elif m == 2 and n==1:
# # # #         return ((sum1 - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_10(l,alpha,beta,gamma)))

# # # # def I_1n(l,n,alpha,beta,gamma):
# # # #     sum2 = 0
# # # #     for k1 in range(1,l+1):
# # # #         sum2 += (alpha/(alpha+beta+gamma))**k1
# # # #     sum3 = 0
# # # #     for k2 in range(1,n+1):
# # # #         for q in range(0,k2):
# # # #             sum3 += (mp.factorial(l+q)/mp.factorial(q)) * (1/k2) *(1/(alpha+beta+gamma)**(l+1)) * ((gamma/(beta+gamma))**k2) * (((beta+gamma)/(alpha+beta+gamma))**q)

# # # #     return (((mp.factorial(l) * alpha**(l+1)) * (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum2)) + sum3)
    


# # # # def I_m0(l,m,alpha,beta,gamma):
# # # #     term1 = (1/(m-1)) * (mp.factorial(l+1-m)/(alpha+beta+gamma)**(l+2-m))
# # # #     if m>2:
# # # #         term2 = ((beta+gamma)/(m-1)) * I_m0(l,m-1,alpha,beta,gamma)
# # # #     elif m == 2:
# # # #         term2 = term2 = ((beta+gamma)/(m-1)) * I_10(l,alpha,beta,gamma)
# # # #     return term1 - term2

# # # # def I_10(l,alpha,beta,gamma):
# # # #     sum4 = 0
# # # #     for k in range(1,l+1):
# # # #         sum4 += (alpha/(alpha+beta+gamma))**k
# # # #     return ((mp.factorial(l) * alpha**(l+1)) * (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum4))

# # # # l = 30
# # # # m = 5
# # # # n = 20
# # # # alpha = 0.1
# # # # beta = 0.5
# # # # gamma = 0.5
# # # # W = (mp.factorial(n)/gamma**(n+1)) * I(l,m,n,alpha,beta,gamma)
# # # # print(W)












# # # from mpmath import mp, mpf, quad, power, exp, sqrt

# # # mp.dps = 150

# # # def I(l,m,n,alpha,beta,gamma):
# # #     sum1 = mp.mpf(0)
# # #     for k in range(0,19):
# # #         sum1 += (mp.factorial(l+k+1-m)*gamma**k)/(mp.factorial(k)*(alpha+beta+gamma)**(l+k+2-m))

# # #     if m>2 and n>1:
# # #         return ((sum1 - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma) ) + (gamma/(m-1)*I(l,m-1,n-1,alpha,beta,gamma)))

# # #     elif m == 2 and n>1:
# # #         return ((sum1 - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_1n(l,n-1,alpha,beta,gamma)))

# # #     elif m>2 and n==1:
# # #         return ((sum1 - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_m0(l,m-1,alpha,beta,gamma)))

# # #     elif m == 2 and n==1:
# # #         return ((sum1 - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma) ) + (gamma/(m-1)*I_10(l,alpha,beta,gamma)))


# # # def I_1n(l,n,alpha,beta,gamma):
# # #     sum2 = mp.mpf(0)
# # #     for k1 in range(1,l+1):
# # #         sum2 += (alpha/(alpha+beta+gamma))**k1

# # #     sum3 = mp.mpf(0)
# # #     for k2 in range(1,n+1):
# # #         for q in range(0,k2):
# # #             sum3 += (mp.factorial(l+q)/mp.factorial(q)) * (mp.mpf(1)/k2) * (mp.mpf(1)/(alpha+beta+gamma)**(l+1)) * ((gamma/(beta+gamma))**k2) * (((beta+gamma)/(alpha+beta+gamma))**q)

# # #     return (((mp.factorial(l) * alpha**(l+1)) * (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum2)) + sum3)
    


# # # def I_m0(l,m,alpha,beta,gamma):
# # #     term1 = (mp.mpf(1)/(m-1)) * (mp.factorial(l+1-m)/(alpha+beta+gamma)**(l+2-m))

# # #     if m>2:
# # #         term2 = ((beta+gamma)/(m-1)) * I_m0(l,m-1,alpha,beta,gamma)
# # #     elif m == 2:
# # #         term2 = ((beta+gamma)/(m-1)) * I_10(l,alpha,beta,gamma)

# # #     return term1 - term2


# # # def I_10(l,alpha,beta,gamma):
# # #     sum4 = mp.mpf(0)
# # #     for k in range(1,l+1):
# # #         sum4 += (alpha/(alpha+beta+gamma))**k

# # #     return ((mp.factorial(l) * alpha**(l+1)) * (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum4))


# # # # Convert inputs properly
# # # l = 30
# # # m = 5
# # # n = 20
# # # alpha = mp.mpf('1.0')
# # # beta = mp.mpf('0.5')
# # # gamma = mp.mpf('0.5')

# # # W = (mp.factorial(n)/gamma**(n+1)) * I(l,m,n,alpha,beta,gamma)

# # # print(mp.nstr(W, 50))


























# from mpmath import mp

# mp.dps = 150

# # ---------------- CACHE ---------------- #
# I_cache = {}

# def key(l,m,n,a,b,g):
#     return (l,m,n, mp.nstr(a,30), mp.nstr(b,30), mp.nstr(g,30))

# # ---------------- MAIN FUNCTION ---------------- #
# def I(l,m,n,alpha,beta,gamma):

#     kkey = key(l,m,n,alpha,beta,gamma)
#     if kkey in I_cache:
#         return I_cache[kkey]

#     # -------- adaptive sum1 -------- #
#     sum1 = mp.mpf(0)
#     k = 0
#     term = mp.mpf(1)

#     while True:
#         term = (mp.factorial(l+k+1-m) * gamma**k) / \
#                (mp.factorial(k) * (alpha+beta+gamma)**(l+k+2-m))

#         sum1 += term

#         if abs(term) < mp.mpf('1e-40'):
#             break
#         k += 1

#     # -------- recursion -------- #
#     if m>2 and n>1:
#         val = (sum1 
#                - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma)
#                + (gamma/(m-1))*I(l,m-1,n-1,alpha,beta,gamma))

#     elif m == 2 and n>1:
#         val = (sum1 
#                - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma)
#                + (gamma/(m-1))*I_1n(l,n-1,alpha,beta,gamma))

#     elif m>2 and n==1:
#         val = (sum1 
#                - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma)
#                + (gamma/(m-1))*I_m0(l,m-1,alpha,beta,gamma))

#     elif m == 2 and n==1:
#         val = (sum1 
#                - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma)
#                + (gamma/(m-1))*I_10(l,alpha,beta,gamma))

#     I_cache[kkey] = val
#     return val


# # ---------------- I(1,n) ---------------- #
# def I_1n(l,n,alpha,beta,gamma):

#     # geometric sum (closed form)
#     r = alpha/(alpha+beta+gamma)
#     sum2 = (r*(1-r**l))/(1-r)

#     sum3 = mp.mpf(0)
#     for k2 in range(1,n+1):
#         for q in range(0,k2):
#             sum3 += (mp.factorial(l+q)/mp.factorial(q)) \
#                     * (1/k2) \
#                     * (1/(alpha+beta+gamma)**(l+1)) \
#                     * ((gamma/(beta+gamma))**k2) \
#                     * (((beta+gamma)/(alpha+beta+gamma))**q)

#     return ((mp.factorial(l)*alpha**(l+1)) *
#             (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum2) + sum3)


# # ---------------- I(m,0) ---------------- #
# def I_m0(l,m,alpha,beta,gamma):

#     if m == 2:
#         return I_10(l,alpha,beta,gamma)

#     term1 = (1/(m-1)) * (mp.factorial(l+1-m) /
#                         (alpha+beta+gamma)**(l+2-m))

#     return term1 - ((beta+gamma)/(m-1)) * I_m0(l,m-1,alpha,beta,gamma)


# # ---------------- I(1,0) ---------------- #
# def I_10(l,alpha,beta,gamma):

#     r = alpha/(alpha+beta+gamma)
#     sum4 = (r*(1-r**l))/(1-r)

#     return ((mp.factorial(l)*alpha**(l+1)) *
#             (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum4))


# # ---------------- INPUT ---------------- #
# l = 30
# m = 5
# n = 20
# alpha = mp.mpf('1.0')
# beta = mp.mpf('0.5')
# gamma = mp.mpf('0.5')

# W = (mp.factorial(n)/gamma**(n+1)) * I(l,m,n,alpha,beta,gamma)

# print(mp.nstr(W, 50))

























from mpmath import mp
import os
import json

mp.dps = 150

DATA_FILE = "data.dat"

# ---------------- LOAD CACHE ---------------- #
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        I_cache = json.load(f)
else:
    I_cache = {}

# ---------------- SAVE CACHE ---------------- #
def save_cache():
    with open(DATA_FILE, "w") as f:
        json.dump(I_cache, f)

# ---------------- KEY ---------------- #
def key(l,m,n,a,b,g):
    return (
        int(l), int(m), int(n),
        mp.nstr(a,80),  # 🔥 increased precision
        mp.nstr(b,80),
        mp.nstr(g,80)
    )

# ---------------- MAIN FUNCTION ---------------- #
def I(l,m,n,alpha,beta,gamma):

    kkey = str(key(l,m,n,alpha,beta,gamma))

    if kkey in I_cache:
        return mp.mpf(I_cache[kkey])

    # -------- adaptive sum1 -------- #
    sum1 = mp.mpf(0)
    k = 0

    while True:
        term = (mp.factorial(l+k+1-m) * gamma**k) / \
               (mp.factorial(k) * (alpha+beta+gamma)**(l+k+2-m))

        sum1 += term

        # 🔥 stricter convergence
        if abs(term) < mp.power(10, -mp.dps + 20):
            break

        k += 1
        if k > 500:   # safety cap
            break

    # -------- recursion -------- #
    if m>2 and n>1:
        val = (sum1 
               - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma)
               + (gamma/(m-1))*I(l,m-1,n-1,alpha,beta,gamma))

    elif m == 2 and n>1:
        val = (sum1 
               - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma)
               + (gamma/(m-1))*I_1n(l,n-1,alpha,beta,gamma))

    elif m>2 and n==1:
        val = (sum1 
               - ((beta+gamma)/(m-1))*I(l,m-1,n,alpha,beta,gamma)
               + (gamma/(m-1))*I_m0(l,m-1,alpha,beta,gamma))

    elif m == 2 and n==1:
        val = (sum1 
               - ((beta+gamma)/(m-1))*I_1n(l,n,alpha,beta,gamma)
               + (gamma/(m-1))*I_10(l,alpha,beta,gamma))

    # store
    I_cache[kkey] = mp.nstr(val, 80)
    return val


# ---------------- I(1,n) ---------------- #
def I_1n(l,n,alpha,beta,gamma):

    r = alpha/(alpha+beta+gamma)

    # stable geometric
    if abs(1-r) < mp.mpf('1e-40'):
        sum2 = l * r
    else:
        sum2 = (r*(1-r**l))/(1-r)

    sum3 = mp.mpf(0)

    for k2 in range(1,n+1):
        inner = mp.mpf(0)

        for q in range(0,k2):
            inner += (mp.factorial(l+q)/mp.factorial(q)) * \
                     (((beta+gamma)/(alpha+beta+gamma))**q)

        sum3 += inner * (1/k2) * \
                ((gamma/(beta+gamma))**k2) * \
                (1/(alpha+beta+gamma)**(l+1))

    return ((mp.factorial(l)*alpha**(l+1)) *
            (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum2) + sum3)


# ---------------- I(m,0) ---------------- #
def I_m0(l,m,alpha,beta,gamma):

    if m == 2:
        return I_10(l,alpha,beta,gamma)

    term1 = (1/(m-1)) * (mp.factorial(l+1-m) /
                        (alpha+beta+gamma)**(l+2-m))

    return term1 - ((beta+gamma)/(m-1)) * I_m0(l,m-1,alpha,beta,gamma)


# ---------------- I(1,0) ---------------- #
def I_10(l,alpha,beta,gamma):

    r = alpha/(alpha+beta+gamma)

    if abs(1-r) < mp.mpf('1e-40'):
        sum4 = l * r
    else:
        sum4 = (r*(1-r**l))/(1-r)

    return ((mp.factorial(l)*alpha**(l+1)) *
            (mp.log((alpha+beta+gamma)/(beta+gamma)) - sum4))


# ---------------- INPUT ---------------- #
l = 30
m = 5
n = 20
alpha = mp.mpf('1.0')
beta = mp.mpf('0.5')
gamma = mp.mpf('0.5')

W = (mp.factorial(n)/gamma**(n+1)) * I(l,m,n,alpha,beta,gamma)

print(mp.nstr(W, 50))

# save cache at end
save_cache()


