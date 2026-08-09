class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        half_len = (m + n + 1) // 2

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = half_len - partition1

            if partition1 == 0:
                maxLeft1 = float('-inf')
            else:
                maxLeft1 = nums1[partition1 - 1]

            if partition1 == m:
                minRight1 = float('inf')
            else:
                minRight1 = nums1[partition1]

            if partition2 == 0:
                maxLeft2 = float('-inf')
            else:
                maxLeft2 = nums2[partition2 - 1]

            if partition2 == n:
                minRight2 = float('inf')
            else:
                minRight2 = nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                if (m + n) % 2 != 0:
                    return max(maxLeft1, maxLeft2)

                return (max(maxLeft1, maxLeft2) +
                        min(minRight1, minRight2)) / 2.0

            elif maxLeft1 > minRight2:
                right = partition1 - 1

            else:
                left = partition1 + 1