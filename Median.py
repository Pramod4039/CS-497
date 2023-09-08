def findMedian(points1, points2):
    if len(points1) > len(points2):
        points1, points2 = points2, points1

    m, n = len(points1), len(points2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and points2[j - 1] > points1[i]:

            imin = i + 1
        elif i > 0 and points1[i - 1] > points2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = points2[j - 1]
            elif j == 0:
                max_of_left = points1[i - 1]
            else:
                max_of_left = max(points1[i - 1], points2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = points2[j]
            elif j == n:
                min_of_right = points1[i]
            else:
                min_of_right = min(points1[i], points2[j])

            return (max_of_left + min_of_right) / 2.0

points1 = [1, 3]
points2 = [2]
print("Output 1:", findMedian(points1, points2))

points3 = [1, 2]
points4 = [3, 4]
print("Output 2:", findMedian(points3, points4))
