import hashlib
import random
import string
import time

# Generate random strings as dataset
def generate_random_strings(n, length=32):
    """Generate a list of 'n' random strings with specified 'length'."""
    random_strings = []
    for _ in range(n):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_str)
    return random_strings

# Function to compute hash using a specified algorithm
def compute_hash(data, algorithm='md5'):
    """Compute hash using specified algorithm (md5, sha1, sha256)."""
    hash_func = getattr(hashlib, algorithm)()
    hash_func.update(data.encode())
    return hash_func.hexdigest()

# Function to measure the time taken to compute hashes
def measure_time_and_collision(random_strings, algorithm):
    """Measure time taken to compute hashes and detect collisions."""
    hash_set = set()
    collisions = []
    start_time = time.time()

    for string in random_strings:
        hash_value = compute_hash(string, algorithm)
        if hash_value in hash_set:
            collisions.append(string)  # Record the string causing a collision
        hash_set.add(hash_value)

    end_time = time.time()
    duration = end_time - start_time
    return duration, len(collisions)

# Main function to perform the experiment
def experiment(num_strings=100, string_length=32):
    random_strings = generate_random_strings(num_strings, string_length)

    algorithms = ['md5', 'sha1', 'sha256']
    results = {}

    for algo in algorithms:
        print(f"Running experiment for {algo.upper()}...")
        time_taken, collisions = measure_time_and_collision(random_strings, algo)
        results[algo] = {
            "time_taken": time_taken,
            "collisions": collisions
        }
        print(f"{algo.upper()} took {time_taken:.6f} seconds with {collisions} collisions.\n")

    return results

if __name__ == '__main__':
    # Experiment with 100 random strings of length 32
    results = experiment(num_strings=100, string_length=32)
    
    # Final results
    for algo, res in results.items():
        print(f"{algo.upper()} - Time taken: {res['time_taken']:.6f} seconds, Collisions: {res['collisions']}")
