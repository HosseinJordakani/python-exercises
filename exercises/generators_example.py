# generators_example.py
def positive_numbers(seq):
    for x in seq:
        if x > 0:
            yield x

if __name__ == "__main__":
    nums = [-2, 0, 3, 5, -1]
    for n in positive_numbers(nums):
        print(n)
