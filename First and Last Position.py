
def searchPoints(points, number):
    def findStartPoint(points, number):
        left, right = 0, len(points) - 1
        start = -1

        while left <= right:
            mid = left + (right - left) // 2

            if points[mid] == number:
                start = mid
                right = mid - 1
            elif points[mid] < number:
                left = mid + 1
            else:
                right = mid - 1

        return start

    def findEndPoint(points, number):
        left, right = 0, len(points) - 1
        end = -1

        while left <= right:
            mid = left + (right - left) // 2

            if points[mid] == number:
                end = mid
                left = mid + 1
            elif points[mid] < number:
                left = mid + 1
            else:
                right = mid - 1

        return end

    start = findStartPoint(points, number)
    end = findEndPoint(points, number)

    return [start, end]

points1 = [5, 7, 7, 8, 8, 10]
number1 = 8
print("Output 1:", searchPoints(points1, number1))  # Output: [3, 4]

points2 = [5, 7, 7, 8, 8, 10]
number2 = 6
print("Output 2:", searchPoints(points2, number2))  # Output: [-1, -1]

points3 = []
number3 = 0
print("Output 3:", searchPoints(points3, number3))  # Output: [-1, -1]
