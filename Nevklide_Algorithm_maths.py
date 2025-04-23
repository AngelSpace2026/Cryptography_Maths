import random

def encode_until_one(number):
    original = number
    path = []
    step = 0
    last_divisor = None

    print(f"Encoding {number} with infinite steps until it becomes 1...\n")

    while number > 1:
        # If only 1 division left to reach 1, enforce divisor 1–255
        if number <= 255:
            divisor = random.randint(1, min(number, 255))
            while number % divisor != 0 or number // divisor != 1:
                divisor = random.randint(1, min(number, 255))
        else:
            divisor = random.randint(1, 2**24)
            while divisor == 0 or number % divisor != 0:
                divisor = random.randint(1, 2**24)

        path.append((number, divisor))
        number //= divisor
        step += 1
        last_divisor = divisor
        print(f"Step {step}: {path[-1][0]} ÷ {divisor} = {number}")

    path.append((1, None))  # Final state
    return path, original, step, last_divisor

def decode_path(path):
    number = 1
    print("\nDecoding path...")
    for num, divisor in reversed(path):
        if divisor:
            number *= divisor
            print(f"Decoding: {number // divisor} * {divisor} = {number}")
    return number

if __name__ == "__main__":
    start_number = int(input("Enter a number to encode: "))

    encoded_path, original, total_steps, last_divisor = encode_until_one(start_number)

    print("\nEncoded path:")
    for i, (num, div) in enumerate(encoded_path):
        if div:
            print(f"Step {i+1}: {num} ÷ {div} = {num // div}")
        else:
            print("Final: 1 reached")

    decoded = decode_path(encoded_path)
    print(f"\nDecoded number: {decoded}")
    print("Yes" if decoded == original else "No")

    # Final result output
    print(f"\nLast Three Values:")
    print(f"1 (Final result), Steps = {total_steps}, Last Divisor = {last_divisor}")