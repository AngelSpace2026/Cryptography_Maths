import random

def encode_until_one(number):
    original = number
    path = []
    step = 0

    print(f"Encoding {number} with optimized steps until it becomes 1...\n")

    while number > 1:
        found_divisor = False
        for divisor in range(2, number + 1):
            if number % divisor == 0:
                path.append((number, divisor))
                number //= divisor
                step += 1
                print(f"Step {step}: {path[-1][0]} ÷ {divisor} = {number}")
                found_divisor = True
                break

        if not found_divisor:
            print(f"No divisor found for {number} (shouldn't happen)")
            break

    step += 1
    path.append((1, None))
    print(f"Step {step}: Reached 1")

    return path, original, step

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

    encoded_path, original, total_steps = encode_until_one(start_number)

    print("\nEncoded path:")
    for i, (num, div) in enumerate(encoded_path):
        if div:
            print(f"Step {i+1}: {num} ÷ {div} = {num // div}")
        else:
            print(f"Step {i+1}: Reached 1")

    decoded = decode_path(encoded_path)
    print(f"\nDecoded number: {decoded}")
    print("Yes" if decoded == original else "No")

    print(f"\nFinal Result:")
    if len(encoded_path) >= 2:
        last_before_one = encoded_path[-2][0] // encoded_path[-2][1]
        print(f"{last_before_one}")
    else:
        print("1")
    print(f"Divided in {total_steps} steps from {original}")