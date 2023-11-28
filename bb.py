def find_max_alternating_subsequence_sum(sequence):
    max_positive = 0
    max_negative = 0

    for num in sequence:
        if num > 0:
            max_positive = max(max_positive, max_negative + num)
        else:
            max_negative = max(max_negative, max_positive + num)

    return max(max_positive, max_negative)

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the length of the sequence
    n = int(input())

    # Read the sequence
    sequence = list(map(int, input().split()))

    # Find the maximum sum of the maximum alternating subsequence
    max_sum = find_max_alternating_subsequence_sum(sequence)

    # Print the result
    print(max_sum)