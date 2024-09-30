import random
from sympy import isprime, mod_inverse

# Key generation for RSA
def generate_keypair(bit_length=512):
    # Step 1: Generate two large prime numbers p and q
    p = generate_large_prime(bit_length // 2)
    q = generate_large_prime(bit_length // 2)

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute Euler's totient function phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # Step 4: Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Commonly used public exponent
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime!")

    # Step 5: Compute the private key d such that d * e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi)

    # Public key (e, n), private key (d, n)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Function to find the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate a large prime number
def generate_large_prime(bit_length):
    while True:
        prime_candidate = random.getrandbits(bit_length)
        if isprime(prime_candidate):
            return prime_candidate

# RSA encryption function
def encrypt(public_key, plaintext):
    e, n = public_key
    # Ciphertext = plaintext^e mod n
    ciphertext = pow(plaintext, e, n)
    return ciphertext

# RSA decryption function
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Plaintext = ciphertext^d mod n
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Main experiment
def rsa_homomorphic_multiplication():
    # Step 1: Generate keypair
    public_key, private_key = generate_keypair()

    # Step 2: Define two integers to encrypt
    num1 = 7
    num2 = 3

    # Step 3: Encrypt both numbers
    ciphertext1 = encrypt(public_key, num1)
    ciphertext2 = encrypt(public_key, num2)

    print(f"Ciphertext of {num1}: {ciphertext1}")
    print(f"Ciphertext of {num2}: {ciphertext2}")

    # Step 4: Homomorphic multiplication of encrypted values (ciphertext1 * ciphertext2)
    # This results in the encryption of num1 * num2
    ciphertext_product = (ciphertext1 * ciphertext2) % public_key[1]
    print(f"Ciphertext of the product (encrypted): {ciphertext_product}")

    # Step 5: Decrypt the result of the multiplication
    decrypted_product = decrypt(private_key, ciphertext_product)
    print(f"Decrypted product: {decrypted_product}")

    # Verify that the decrypted product matches num1 * num2
    assert decrypted_product == num1 * num2, "Decryption result does not match the expected product!"
    print("Homomorphic multiplication verified successfully.")

if __name__ == "__main__":
    rsa_homomorphic_multiplication()
