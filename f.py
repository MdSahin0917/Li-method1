import time
from scipy.special import hyp2f1
from mpmath import mp

# Set precision if necessary
mp.dps = 100 # Set decimal place
start = time.perf_counter()

# ---------------- PARAMETERS ---------------- #
alpha = 9.0
beta  = 0.5
gamma = 0.5
l = 25
m = 10
n = 20
pmax = 100

# ---------------- PRECOMPUTE CONSTANTS ---------------- #
denom = alpha + beta + gamma
denom2 = (beta+gamma)



# ---------------- PART 1 ---------------- #
part1_val = mp.factorial(n) / (gamma**(n+1)*(denom2**(m+1)) * denom**(l+1))

# ---------------- FAST SUM ---------------- #
total = 0.0
for k in range(n+1):
    for p in range(m+k+1):
        total += ((mp.factorial(m+k) * mp.factorial(l+p))/(mp.factorial(k)*mp.factorial(p)))*((gamma/denom2)**k)*((denom2/denom)**p)
        
result = part1_val*total
end = time.perf_counter()

print("Final Result =", result)
print("Execution Time =", end - start, "seconds")




