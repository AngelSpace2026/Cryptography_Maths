import random

def encode_until_one(number):
    original = number
    path = []
    step = 0

    print(f"Encoding {number} with optimized steps until it becomes 1...\n")

    # Keep track of each step where the number is divided by a divisor
    while number > 1:
        found_divisor = False
        # Try divisors from 2 up to 10 (or a higher number for better reduction)
        for divisor in range(2, 11):
            if number % divisor == 0:
                path.append((number, divisor))
                number //= divisor
                step += 1
                print(f"Step {step}: {path[-1][0]} ÷ {divisor} = {number}")
                found_divisor = True
                break

        if not found_divisor:
            # If no small divisor is found, try a random large divisor
            divisor = random.randint(11, 2**24)
            if number % divisor == 0:
                path.append((number, divisor))
                number //= divisor
                step += 1
                print(f"Step {step}: {path[-1][0]} ÷ {divisor} = {number}")
    
    path.append((1, None))  # Final step
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
            print("Final: 1 reached")

    decoded = decode_path(encoded_path)
    print(f"\nDecoded number: {decoded}")

    print("Yes" if decoded == original else "No")

    # Print 1 to indicate the final step reached
    print("1")

    # Print the number of steps
    print(f"Divided {total_steps} steps")