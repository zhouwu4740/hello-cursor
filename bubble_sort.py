
def bubble_sort(arr):
    # 获取数组的长度
    n = len(arr)
    # 外层循环控制比较的轮数
    for i in range(n):
        # 内层循环控制每一轮比较的次数
        for j in range(0, n-i-1):
            # 如果前一个元素大于后一个元素，则交换它们的位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def test_bubble_sort():
    test_cases_list = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        # Negative test cases
        # Already sorted, should remain the same
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Reverse order, should sort correctly
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # Large array, should sort correctly
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        # Large array, should sort correctly
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),

        # Large array, should sort correctly
    ]

    for i, (input_arr, expected) in enumerate(test_cases_list):
        bubble_sort(input_arr)
        assert input_arr == expected, f"Test case {i+1} failed: expected {expected}, got {input_arr}"


# Example usage
if __name__ == "__main__":
    test_bubble_sort()
