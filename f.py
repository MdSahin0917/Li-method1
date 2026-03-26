
import time
import json
import os
from mpmath import mp

mp.dps = 150  # precision

# FIXED PARAMETERS
beta = mp.mpf('0.5')
gamma = mp.mpf('0.5')

l = 25
m = 10
n = 20

DATA_FILE = "factorial_data.json"


def mpf_to_str(val):
    """Convert mpf to string with full precision."""
    return mp.nstr(val, mp.dps)


def str_to_mpf(s):
    """Convert string to mpf."""
    return mp.mpf(s)


def load_or_create_factorial_data():
    """Load factorial data from JSON file if exists, otherwise create and save it."""
    
    if os.path.exists(DATA_FILE):
        print(f"Loading factorial data from {DATA_FILE}...")
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            
            # Convert string keys back to integers and mpf strings to mpf
            factorials = {int(k): str_to_mpf(v) for k, v in data['factorials'].items()}
            
            # Load rising factorials
            rising_factorials = {}
            if 'rising_factorials' in data:
                for key, value in data['rising_factorials'].items():
                    # Parse key format: "x_n"
                    parts = key.split('_')
                    if len(parts) >= 2:
                        x_str = '_'.join(parts[:-1])
                        n_str = parts[-1]
                        x = str_to_mpf(x_str)
                        n = int(n_str)
                        rising_factorials[(x, n)] = str_to_mpf(value)
            
            print(f"Loaded {len(factorials)} factorials and {len(rising_factorials)} rising factorials")
            return factorials, rising_factorials
            
        except Exception as e:
            print(f"Error loading data file: {e}")
            print("Creating new factorial data...")
            return create_and_save_factorial_data()
    else:
        print(f"Data file {DATA_FILE} not found. Creating new factorial data...")
        return create_and_save_factorial_data()


def create_and_save_factorial_data():
    """Create factorial and rising factorial data and save to JSON file."""
    
    global l, m, n, beta, gamma
    
    factorials = {}
    rising_factorials = {}
    
    # Calculate needed factorial values
    print("Calculating factorials...")
    max_factorial = max(n, m + n, l + m + n)
    
    # Pre-compute all factorials up to max needed
    for i in range(max_factorial + 1):
        factorials[i] = mp.factorial(i)
        if i % 1000 == 0 and i > 0:
            print(f"  Computed factorials up to {i}")
    
    # Calculate rising factorials
    print("Calculating rising factorials...")
    
    max_k = n
    max_p = m + n
    
    # (m+k)!/m! = (m+1)_k
    print("  Computing (m+1)_k rising factorials...")
    m_plus_1 = m + 1
    for k in range(max_k + 1):
        key = (m_plus_1, k)
        if k == 0:
            rising_factorials[key] = mp.mpf('1')
        else:
            result = mp.mpf('1')
            for i in range(k):
                result *= (m_plus_1 + i)
            rising_factorials[key] = result
    
    # (l+p)!/l! = (l+1)_p
    print("  Computing (l+1)_p rising factorials...")
    l_plus_1 = l + 1
    for p in range(max_p + 1):
        key = (l_plus_1, p)
        if p == 0:
            rising_factorials[key] = mp.mpf('1')
        else:
            result = mp.mpf('1')
            for i in range(p):
                result *= (l_plus_1 + i)
            rising_factorials[key] = result
    
    # Pre-compute rising factorials for constant gamma
    print("  Computing gamma rising factorials...")
    for k in range(max_k + 1):
        key = (gamma, k)
        if k == 0:
            rising_factorials[key] = mp.mpf('1')
        else:
            result = mp.mpf('1')
            for i in range(k):
                result *= (gamma + i)
            rising_factorials[key] = result
    
    # Pre-compute rising factorials for constant beta
    print("  Computing beta rising factorials...")
    for k in range(max_k + 1):
        key = (beta, k)
        if k == 0:
            rising_factorials[key] = mp.mpf('1')
        else:
            result = mp.mpf('1')
            for i in range(k):
                result *= (beta + i)
            rising_factorials[key] = result
    
    # Pre-compute rising factorials for constant beta+gamma
    print("  Computing (beta+gamma) rising factorials...")
    beta_plus_gamma = beta + gamma
    for k in range(max_k + 1):
        key = (beta_plus_gamma, k)
        if k == 0:
            rising_factorials[key] = mp.mpf('1')
        else:
            result = mp.mpf('1')
            for i in range(k):
                result *= (beta_plus_gamma + i)
            rising_factorials[key] = result
    
    # Save to JSON file
    print(f"Saving factorial data to {DATA_FILE}...")
    
    # Convert to JSON-serializable format
    serializable_data = {
        'factorials': {str(k): mpf_to_str(v) for k, v in factorials.items()},
        'rising_factorials': {},
        'metadata': {
            'l': l,
            'm': m,
            'n': n,
            'beta': mpf_to_str(beta),
            'gamma': mpf_to_str(gamma),
            'precision': mp.dps,
            'description': 'This file contains precomputed factorials and rising factorials'
        }
    }
    
    # Convert rising factorials to string keys
    for (x, k), val in rising_factorials.items():
        x_str = mpf_to_str(x)
        key_str = f"{x_str}_{k}"
        serializable_data['rising_factorials'][key_str] = mpf_to_str(val)
    
    # Save with pretty formatting for readability
    with open(DATA_FILE, 'w') as f:
        json.dump(serializable_data, f, indent=2, sort_keys=True)
    
    file_size = os.path.getsize(DATA_FILE) / (1024 * 1024)  # Size in MB
    print(f"Saved {len(factorials)} factorials and {len(rising_factorials)} rising factorials")
    print(f"File size: {file_size:.2f} MB")
    print(f"File location: {os.path.abspath(DATA_FILE)}")
    
    return factorials, rising_factorials


def get_factorial(n_val, factorials):
    """Retrieve factorial from cache."""
    n_int = int(n_val)
    if n_int not in factorials:
        factorials[n_int] = mp.factorial(n_int)
    return factorials[n_int]


def get_rising_factorial(x, n_val, rising_factorials):
    """Retrieve rising factorial (x)_n from cache or calculate."""
    if isinstance(x, mp.mpf):
        x_val = x
    else:
        x_val = mp.mpf(x)
    
    n_int = int(n_val)
    key = (x_val, n_int)
    
    if key in rising_factorials:
        return rising_factorials[key]
    
    result = mp.mpf('1')
    for i in range(n_int):
        result *= (x_val + i)
    
    rising_factorials[key] = result
    return result


def compute_result(alpha, factorials, rising_factorials):
    """Compute result using cached factorial values."""
    alpha = mp.mpf(alpha)
    global beta, gamma, l, m, n
    
    denom = alpha + beta + gamma
    denom2 = beta + gamma
    
    part1_val = get_factorial(n, factorials) / (gamma**(n+1) * denom2**(m+1) * denom**(l+1))
    
    total = mp.mpf('0')
    
    for k in range(n+1):
        for p in range(m+k+1):
            fact_mk = get_factorial(m+k, factorials)
            fact_lp = get_factorial(l+p, factorials)
            fact_k = get_factorial(k, factorials)
            fact_p = get_factorial(p, factorials)
            
            term = (fact_mk * fact_lp) / (fact_k * fact_p)
            term *= (gamma/denom2)**k * (denom2/denom)**p
            total += term
    
    return part1_val * total


def view_data_file():
    """View the contents of the data file."""
    if os.path.exists(DATA_FILE):
        print(f"\n{'='*60}")
        print(f"CONTENTS OF {DATA_FILE}")
        print(f"{'='*60}")
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            
            # Display metadata if it exists
            if 'metadata' in data:
                print(f"\nMetadata:")
                for key, value in data['metadata'].items():
                    print(f"  {key}: {value}")
            else:
                print(f"\nNote: This file was created with an older version (no metadata)")
                print(f"File contains {len(data)} top-level keys: {list(data.keys())}")
            
            # Display factorials
            if 'factorials' in data:
                factorials = data['factorials']
                print(f"\nFactorials stored: {len(factorials)}")
                if factorials:
                    fact_keys = [int(k) for k in factorials.keys()]
                    print(f"  Range: {min(fact_keys)} to {max(fact_keys)}")
                    print(f"  First 10 factorials:")
                    sorted_facts = sorted([(int(k), v) for k, v in factorials.items()])[:10]
                    for k, v in sorted_facts:
                        print(f"    {k}! = {v[:50]}..." if len(v) > 50 else f"    {k}! = {v}")
            
            # Display rising factorials
            if 'rising_factorials' in data:
                rising = data['rising_factorials']
                print(f"\nRising factorials stored: {len(rising)}")
                if rising:
                    print(f"  First 10 rising factorials:")
                    sorted_rising = list(rising.items())[:10]
                    for key, value in sorted_rising:
                        print(f"    ({key}) = {value[:50]}..." if len(value) > 50 else f"    ({key}) = {value}")
            
            # File size
            file_size = os.path.getsize(DATA_FILE) / (1024 * 1024)
            print(f"\nFile size: {file_size:.2f} MB")
            print(f"File location: {os.path.abspath(DATA_FILE)}")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File {DATA_FILE} does not exist yet.")


# -------- MAIN EXECUTION -------- #
# Check if we need to recreate the data file with new format
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, 'r') as f:
            old_data = json.load(f)
        if 'metadata' not in old_data:
            print("Old data file detected (no metadata). Recreating with new format...")
            os.rename(DATA_FILE, DATA_FILE + ".old")
            print(f"Backed up old file to {DATA_FILE}.old")
    except:
        pass

# View existing data file if it exists
view_data_file()

# Load or create factorial data
factorials, rising_factorials = load_or_create_factorial_data()

# Multiple alpha values
alpha_values = [0.1, 0.3, 0.6, 1.0, 3.0, 6.0, 9.0, 99.0, 999.0, 9999.0, 
                99999.0, 999999.0, 9999999.0, 99999999.0, 999999999.0]

start = time.perf_counter()

print("\nComputing results for different alpha values...")
for i, a in enumerate(alpha_values, 1):
    result = compute_result(a, factorials, rising_factorials)
    print(f"alpha = {a:12.1f} -> {mp.nstr(result, 40)}")
    # if i % 5 == 0:
    #     print(f"  Progress: {i}/{len(alpha_values)} values computed")

end = time.perf_counter()

print("\n" + "="*50)
print(f"Execution Time = {end - start:.4f} seconds")
print("="*50)