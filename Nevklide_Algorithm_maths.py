import random

def encode_until_one(number):
    original = number
    path = []
    step = 0

    print(f"Encoding {number} with infinite steps until it becomes 1...\n")

    while number > 1:
        divisor = random.randint(1, 2**24)
        if divisor != 0 and number % divisor == 0:
            path.append((number, divisor))
            number //= divisor
            step += 1
            print(f"Step {step}: {path[-1][0]} ÷ {divisor} = {number}")
        # Else: try another divisor (loop continues infinitely)

    path.append((1, None))  # Final step
    return path, original

def decode_path(path):
    number = 1
    print("\nDecoding path...")
    for num, divisor in reversed(path):
        if divisor:
            number *= divisor
            print(f"Decoding: {number // divisor} * {divisor} = {number}")
        else:
            print("Final step: Reached 1")
    return number

if __name__ == "__main__":
    start_number = int(input("Enter a number to encode: "))

    encoded_path, original = encode_until_one(start_number)

    print("\nEncoded path:")
    for i, (num, div) in enumerate(encoded_path):
        if div:
            print(f"Step {i+1}: {num} ÷ {div} = {num // div}")
        else:
            print("Final: 1 reached")

    decoded = decode_path(encoded_path)
    print(f"\nDecoded number: {decoded}")

    print("Yes" if decoded == original else "No")