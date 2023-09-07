def two_num_sum(points, sumOfnums):
    num_dict = {}

    for i in range(len(points)):
        num = points[i]
        complement = sumOfnums - num

        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

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
