def Add(numbers):
    if not numbers:
        return 0

    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Invalid input format")

    numbers_uni = numbers.replace("\n", ",")
    num_split = numbers_uni.split(",")

    try:
        return sum(int(n) for n in num_split if n.strip())
    except ValueError:
        raise ValueError("Invalid input format")


