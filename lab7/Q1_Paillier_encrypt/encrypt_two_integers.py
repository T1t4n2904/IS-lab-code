import random
from math import gcd
from sympy import mod_inverse

# Key generation for the Paillier cryptosystem
def generate_keypair(bit_length=512):
    # Choose two large primes p and q
    p = random_prime(bit_length // 2)
    q = random_prime(bit_length // 2)

    # Compute n = p * q
    n = p * q
    nsquare = n ** 2

    # Compute lambda (lcm(p-1, q-1))
    lcm_lambda = (p - 1) * (q - 1) // gcd(p - 1, q - 1)

    # Compute g, generally g = n + 1
    g = n + 1

    # Compute mu = (L(g^lambda mod n^2))^(-1) mod n
    mu = mod_inverse(L(pow(g, lcm_lambda, nsquare), n), n)

    # Public key (n, g) and private key (lambda, mu)
    public_key = (n, g)
    private_key = (lcm_lambda, mu)
    
    return public_key, private_key

# L(x) function in Paillier cryptosystem: L(x) = (x - 1) // n
def L(x, n):
    return (x - 1) // n

# Function to find a large random prime using sympy's prime generation
def random_prime(bit_length):
    from sympy import primerange
    lower_bound = 2 ** (bit_length - 1)
    upper_bound = 2 ** bit_length
    primes = list(primerange(lower_bound, upper_bound))
    return random.choice(primes)

# Paillier encryption function
def encrypt(public_key, plaintext):
    n, g = public_key
    nsquare = n ** 2

    # Choose a random r such that gcd(r, n) = 1
    r = random.randint(1, n - 1)
    while gcd(r, n) != 1:
        r = random.randint(1, n - 1)

    # Ciphertext = g^m * r^n mod n^2
    ciphertext = (pow(g, plaintext, nsquare) * pow(r, n, nsquare)) % nsquare
    return ciphertext

# Paillier decryption function
def decrypt(private_key, public_key, ciphertext):
    n, g = public_key
    lcm_lambda, mu = private_key
    nsquare = n ** 2

    # Decrypt ciphertext: m = L(c^lambda mod n^2) * mu mod n
    x = pow(ciphertext, lcm_lambda, nsquare)
    plaintext = (L(x, n) * mu) % n
    return plaintext

# Homomorphic addition of two encrypted values
def homomorphic_add(public_key, ciphertext1, ciphertext2):
    n, _ = public_key
    nsquare = n ** 2

    # Addition of encrypted values: c1 * c2 mod n^2
    return (ciphertext1 * ciphertext2) % nsquare

# Main experiment
def paillier_experiment():
    # Generate keypair
    public_key, private_key = generate_keypair()

    # Two integers to encrypt
    num1 = 15
    num2 = 25

    # Encrypt both numbers
    ciphertext1 = encrypt(public_key, num1)
    ciphertext2 = encrypt(public_key, num2)

    print(f"Ciphertext of {num1}: {ciphertext1}")
    print(f"Ciphertext of {num2}: {ciphertext2}")

    # Homomorphic addition of encrypted values
    ciphertext_sum = homomorphic_add(public_key, ciphertext1, ciphertext2)
    print(f"Ciphertext of sum (encrypted): {ciphertext_sum}")

    # Decrypt the result of the addition
    decrypted_sum = decrypt(private_key, public_key, ciphertext_sum)
    print(f"Decrypted sum: {decrypted_sum}")

    # Verify that decrypted sum matches the original sum
    assert decrypted_sum == num1 + num2, "Decryption result does not match the expected sum!"
    print("Homomorphic addition verified successfully.")

if __name__ == "__main__":
    paillier_experiment()
