
# # # import os

# # # FACDATA_FILE = "facdata.dat"


# # # # ---------------- LOAD DATA ---------------- #
# # # def load_facdata():
# # #     data = {}

# # #     if not os.path.exists(FACDATA_FILE):
# # #         return data

# # #     with open(FACDATA_FILE, "r") as f:
# # #         for line in f:
# # #             parts = line.strip().split()
# # #             if len(parts) == 2:
# # #                 n, val = parts
# # #                 data[int(n)] = int(val)

# # #     return data

# # # # ---------------- SAVE NEW DATA ---------------- #
# # # def append_data(n, value):
# # #     with open(DATA_FILE, "a") as f:
# # #         f.write(f"{n} {value}\n")


# # # # ---------------- COMPUTE (example: factorial) ---------------- #
# # # def compute_factorial(n):
# # #     result = 1
# # #     for i in range(2, n + 1):
# # #         result *= i
# # #     return result


# # # # ---------------- MAIN FUNCTION ---------------- #
# # # def get_factorial(n):
# # #     data = load_data()

# # #     # If exists → return
# # #     if n in data:
# # #         print(f"[FROM FILE] {n}! = {data[n]}")
# # #         return data[n]

# # #     # Else → compute
# # #     print(f"[COMPUTE] {n}! not found. Computing...")
# # #     value = compute_factorial(n)

# # #     # Save to file
# # #     append_data(n, value)
# # #     print(f"[SAVED] {n}! = {value}")

# # #     return value


# # # # ---------------- TEST ---------------- #
# # # if __name__ == "__main__":
# # #     nums = [5, 6, 10, 5, 10]

# # #     for n in nums:
# # #         res = get_factorial(n)
# # #         print(f"Result: {res}\n")



# # # # # ---------------- TEST ---------------- #
# # # # alphas = [0.1, 0.3, 1, 6, 9, 99]

# # # # start = time.perf_counter()

# # # # for a in alphas:
# # # #     res = compute_W_fast(a)
# # # #     print(f"alpha = {a} → {mp.nstr(res, 25)}")

# # # # end = time.perf_counter()
# # # # print("Time:", end - start)



























# # import os

# # DATA_FILE = "facdata.dat"


# # # ---------------- LOAD DATA ---------------- #
# # def load_data():
# #     data = []

# #     if not os.path.exists(DATA_FILE):
# #         return data

# #     with open(DATA_FILE, "r") as f:
# #         for line in f:
# #             parts = list(map(int, line.strip().split()))
# #             if len(parts) in (2, 3):
# #                 data.append(parts)

# #     return data


# # # ---------------- APPEND DATA ---------------- #
# # def append_data(entry):
# #     with open(DATA_FILE, "a") as f:
# #         f.write(" ".join(map(str, entry)) + "\n")


# # # ---------------- SEARCH ---------------- #
# # def search_data(data, key, dim):
# #     if dim == 1:
# #         for row in data:
# #             if len(row) == 2:
# #                 n, val = row
# #                 if n == key:
# #                     return val

# #     elif dim == 2:
# #         n1, n2 = key
# #         for row in data:
# #             if len(row) == 3:
# #                 a, b, val = row
# #                 if a == n1 and b == n2:
# #                     return val

# #     return None


# # # ---------------- COMPUTE ---------------- #
# # def compute_value(key, dim):
# #     if dim == 1:
# #         n = key
# #         result = 1
# #         for i in range(2, n + 1):
# #             result *= i
# #         return result

# #     elif dim == 2:
# #         n, r = key
# #         from math import comb
# #         return comb(n, r)


# # # ---------------- MAIN FUNCTION ---------------- #
# # def get_value(key):
# #     data = load_data()

# #     # determine dimension ONLY from input
# #     if isinstance(key, int):
# #         dim = 1
# #     elif isinstance(key, tuple) and len(key) == 2:
# #         dim = 2
# #     else:
# #         raise ValueError("Invalid key format")

# #     result = search_data(data, key, dim)

# #     if result is not None:
# #         print("[FROM FILE]", key, "->", result)
# #         return result

# #     print("[COMPUTE]", key, "not found")
# #     result = compute_value(key, dim)

# #     if dim == 1:
# #         append_data([key, result])
# #     else:
# #         append_data([key[0], key[1], result])

# #     print("[SAVED]", key, "->", result)
# #     return result


# # # ---------------- TEST ---------------- #
# # if __name__ == "__main__":
# #     # 1D test

# #     for n in range(1,100):
# #         print(get_value(n))


# #     # 2D test
# #     print(get_value((5, 2)))
# #     print(get_value((6, 3)))





























# import os
# from mpmath import mp

# mp.dps = 50  # set precision

# DATA_FILE = "facdata.dat"


# # ---------------- LOAD DATA ---------------- #
# def load_data():
#     data = []

#     if not os.path.exists(DATA_FILE):
#         return data

#     with open(DATA_FILE, "r") as f:
#         for line in f:
#             parts = line.strip().split()

#             # convert numbers safely
#             if len(parts) == 2:
#                 n = int(parts[0])
#                 val = mp.mpf(parts[1])
#                 data.append([n, val])

#             elif len(parts) == 3:
#                 x = int(parts[0])
#                 n = int(parts[1])
#                 val = mp.mpf(parts[2])
#                 data.append([x, n, val])

#     return data


# # ---------------- APPEND DATA ---------------- #
# def append_data(entry):
#     with open(DATA_FILE, "a") as f:
#         f.write(" ".join(str(x) for x in entry) + "\n")


# # ---------------- SEARCH ---------------- #
# def search_data(data, key, dim):
#     if dim == 1:
#         for row in data:
#             if len(row) == 2:
#                 n, val = row
#                 if n == key:
#                     return val

#     elif dim == 2:
#         x1, n1 = key
#         for row in data:
#             if len(row) == 3:
#                 x, n, val = row
#                 if x == x1 and n == n1:
#                     return val

#     return None


# # ---------------- COMPUTE ---------------- #
# def compute_value(key, dim):
#     if dim == 1:
#         n = key
#         result = mp.mpf(1)
#         for i in range(2, n + 1):
#             result *= i
#         return result

#     elif dim == 2:
#         x, n = key
#         # rising factorial using mpmath (BEST method)
#         return mp.rf(x, n)


# # ---------------- MAIN FUNCTION ---------------- #
# def get_value(key):
#     data = load_data()

#     # determine dimension from input
#     if isinstance(key, int):
#         dim = 1
#     elif isinstance(key, tuple) and len(key) == 2:
#         dim = 2
#     else:
#         raise ValueError("Invalid key format")

#     # search in file
#     result = search_data(data, key, dim)

#     if result is not None:
#         print("[FROM FILE]", key, "->", result)
#         return result

#     # compute if missing
#     print("[COMPUTE]", key, "not found")
#     result = compute_value(key, dim)

#     # save to file (store as string for precision safety)
#     if dim == 1:
#         append_data([key, str(result)])
#     else:
#         append_data([key[0], key[1], str(result)])

#     print("[SAVED]", key, "->", result)
#     return result


# # ---------------- TEST ---------------- #
# if __name__ == "__main__":

#     print("----- 1D: Factorials -----")
#     for n in range(1, 15):
#         print(get_value(n))

#     print("\n----- 2D: Rising Factorials -----")
#     print(get_value((5, 2)))   # (5)_2 = 30
#     print(get_value((6, 3)))   # (6)_3 = 336
#     print(get_value((2, 5)))   # (2)_5 = 720































import os
import time
from mpmath import mp

mp.dps = 150  # precision

# ---------------- FILE ---------------- #
DATA_FILE = "facdata.dat"

# ---------------- MEMORY CACHE ---------------- #
fac_cache = {}   # super important (RAM cache)


# ---------------- LOAD FILE INTO CACHE ---------------- #
def load_factorials():
    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                n = int(parts[0])
                val = mp.mpf(parts[1])
                fac_cache[n] = val


# ---------------- APPEND TO FILE ---------------- #
def append_factorial(n, value):
    with open(DATA_FILE, "a") as f:
        f.write(f"{n} {value}\n")


# ---------------- FACTORIAL WITH CACHE ---------------- #
def get_factorial(n):
    # check RAM first (fast)
    if n in fac_cache:
        return fac_cache[n]

    # compute if not found
    result = mp.mpf(1)
    for i in range(2, n + 1):
        result *= i

    # store in RAM
    fac_cache[n] = result

    # store in file
    append_factorial(n, result)

    return result


# ---------------- MAIN COMPUTATION ---------------- #
def compute_result(alpha):
    alpha = mp.mpf(alpha)

    denom = alpha + beta + gamma
    denom2 = beta + gamma

    # PART 1 (using cached factorial)
    part1_val = get_factorial(n) / (
        gamma**(n+1) * denom2**(m+1) * denom**(l+1)
    )

    total = mp.mpf('0')

    for k in range(n + 1):

        fk = get_factorial(k)
        fmk = get_factorial(m + k)

        for p in range(m + k + 1):

            fp = get_factorial(p)
            flp = get_factorial(l + p)

            term = (fmk * flp) / (fk * fp)
            term *= (gamma / denom2) ** k * (denom2 / denom) ** p

            total += term

    return part1_val * total


# ---------------- PARAMETERS ---------------- #
beta  = mp.mpf('0.5')
gamma = mp.mpf('0.5')

l = 25
m = 10
n = 20


# ---------------- RUN ---------------- #
if __name__ == "__main__":

    # 🔥 load file once
    load_factorials()

    alpha_values = [
        0.1, 0.3, 0.6, 1.0, 3.0, 6.0,
        9.0, 99.0, 999.0, 9999.0,
        99999.0, 999999.0, 9999999.0,
        99999999.0, 999999999.0
    ]

    start = time.perf_counter()

    for a in alpha_values:
        result = compute_result(a)
        print(f"alpha = {a} -> {mp.nstr(result, 40)}")

    end = time.perf_counter()

    print("Execution Time =", end - start, "seconds")