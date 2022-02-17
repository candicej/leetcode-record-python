class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 不返回任何东西，原地修改nums1
        if m == 0:
            nums1[m:] = nums2
        # 如果n是0 则直接不需要修改nums1

        # 这道题难在在nums1直接修改，如果前面的修改了后面的会移动，不好处理
        # 思路：从后往前处理
        # 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
        i = m - 1
        j = n - 1
        h = m + n - 1

        # 是j>=0 是因为如果已经遍历完了nums2那么就可以不用修改nums1了
        while j >= 0:
            # nums2的元素大
            # i<0 也就是说 nums1的数组已经遍历完了，直接把nums2放上去就可以了
            if i < 0 or nums1[i] < nums2[j]:
                nums1[h] = nums2[j]
                j -= 1
            # nums1的元素大
            else:
                nums1[h] = nums1[i]
                i -= 1
            h -= 1

# # 方法二： 作弊的方法 sort
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2
#         nums1.sort()

