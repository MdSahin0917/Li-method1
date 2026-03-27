from mpmath import mp

mp.dps = 100  # high precision

# PARAMETERS
beta  = mp.mpf('0.5')
gamma = mp.mpf('0.5')

denom = beta + gamma

# CACHE
I_cache = {}

# BASE CASE
def I_base(n):
    # I(0,n) = n! / denom^(n+1)
    return mp.factorial(n) / (denom ** (n + 1))


# RECURSIVE FUNCTION
def I(m, n):
    # Check cache
    if (m, n) in I_cache:
        return I_cache[(m, n)]

    # Base case
    if m == 0:
        val = I_base(n)

    # Recursive step
    elif m > 0:
        val = (m + n) / denom * I(m - 1, n)

    else:
        raise ValueError("m must be >= 0")

    # Store in cache
    I_cache[(m, n)] = val
    return val


# ---------------- TEST ---------------- #
if __name__ == "__main__":
    m = 5
    n = 20

    result = I(m, n)
    print("I({}, {}) = {}".format(m, n, mp.nstr(result, 40)))