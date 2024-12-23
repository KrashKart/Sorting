import random

# feel free to change your generation settings here!

RANGE = range(-10_000, 10_001) # -10,000 to 10,000

XTRA_SMALL_SIZE = 10
SMALL_SIZE = 100
MEDIUM_SIZE = 1_000
LARGE_SIZE = 10_000
XTRA_LARGE_SIZE = 100_000

RANDOM_XTRA_SMALL = [random.choice(RANGE) for _ in range(XTRA_SMALL_SIZE)]
RANDOM_SMALL = [random.choice(RANGE) for _ in range(SMALL_SIZE)]
RANDOM_MEDIUM = [random.choice(RANGE) for _ in range(MEDIUM_SIZE)]
RANDOM_LARGE = [random.choice(RANGE) for _ in range(LARGE_SIZE)]
RANDOM_XTRA_LARGE = [random.choice(RANGE) for _ in range(XTRA_LARGE_SIZE)]

DISPLAY_LIMIT = 10

if __name__ == "__main__":
    print(f"Xtra-Small Random ({XTRA_SMALL_SIZE}): {RANDOM_XTRA_SMALL[:DISPLAY_LIMIT]}")
    print(f"Small Random ({SMALL_SIZE}): {RANDOM_SMALL[:DISPLAY_LIMIT]}")
    print(f"Medium Random ({MEDIUM_SIZE}): {RANDOM_MEDIUM[:DISPLAY_LIMIT]}")
    print(f"Large Random ({LARGE_SIZE}): {RANDOM_LARGE[:DISPLAY_LIMIT]}")
    print(f"Xtra-Large Random ({XTRA_LARGE_SIZE}): {RANDOM_XTRA_LARGE[:DISPLAY_LIMIT]}")