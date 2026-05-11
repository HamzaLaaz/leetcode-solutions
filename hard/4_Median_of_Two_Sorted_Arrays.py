def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total = nums1 + nums2
    total = sorted(total)
    if len(total) % 2:
        return total[len(total) // 2]
    else:
        i = int(len(total) / 2)
        return (total[i - 1] + total[i]) / 2


print(f"{findMedianSortedArrays([1, 2], [3]):4f}")
