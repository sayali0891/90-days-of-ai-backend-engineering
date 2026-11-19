def accumulator():
    N = int(input("Enter no : "))
    total_sum = 0

    for i in range(N + 1):
        total_sum += i

    print(f"total_Sum of nos is : {total_sum}")

def accumulator_final():
    n = int(input("Enter no : "))
    
    # sum() handles the internal looping automatically at C-speed
    total_sum = sum(range(n + 1))

    print(f"Sum of nos is : {total_sum}")


if __name__ == "__main__":
    accumulator()
    accumulator_final()
