def two_num_sum(points, sumOfnums):
    num_dict = {}  # Create a dictionary to store the numbers we've seen and their indices

    # Iterate through the list
    for i in range(len(points)):
        num = points[i]
        complement = sumOfnums - num  # Calculate the complement required to reach the target

        # Check if the complement is already in the dictionary
        if complement in num_dict:
            # If found, return the indices of the two numbers
            return [num_dict[complement], i]

        # Otherwise, add the current number and its index to the dictionary
        num_dict[num] = i

    # If no solution is found, return an empty list
    return []

points1 = [2, 7, 11, 15]
sumOfnums1 = 9
result1 = two_num_sum(points1, sumOfnums1)
print("Output 1:", result1)

points2 = [3, 2, 4]
sumOfnums2 = 6
result2 = two_num_sum(points2, sumOfnums2)
print("Output 2:", result2)

points3 = [3, 3]
sumOfnums3 = 6
result3 = two_num_sum(points3, sumOfnums3)
print("Output 3:", result3)
