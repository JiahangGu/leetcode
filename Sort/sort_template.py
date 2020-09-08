#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/29 10:03
# @Author:JiahangGu


class Solution:
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(n-1-i):
                # 发现不符合序列要求的数字对，将大的冒泡到后面
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    def select_sort(self, nums):
        n = len(nums)
        for i in range(n-1):
            index = i
            # 选择当前趟最小的元素放入数组首
            for j in range(i+1, n):
                if nums[j] < nums[index]:
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
        return nums

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            j = i - 1
            key = nums[i]
            # 查找第一个小于等于待插入元素的数字，插入到其后，这里的等于保证了排序稳定性
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

    def shell_sort(self, nums):
        n = len(nums)
        # 设定下标增量
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                key = nums[i]
                j = i - gap
                # 同插排，但是是在由下标增量决定的数组分区之间进行插入排序
                while j >= 0 and nums[j] > key:
                    nums[j+gap] = nums[j]
                    j -= gap
                nums[j+gap] = key
            gap = gap // 2
        return nums

    def merge_sort(self, nums):
        def merge(nums, l, mid, r):
            i = l
            j = mid + 1
            k = l
            # 取出更小的值赋到临时数组
            while i <= mid and j <= r:
                if nums[i] > nums[j]:
                    tmp[k] = nums[j]
                    j += 1
                else:
                    tmp[k] = nums[i]
                    i += 1
                k += 1
            # 将剩余数组的全部元素拷贝到临时数组
            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1
            while j <= r:
                tmp[k] = nums[j]
                k += 1
                j += 1
            # 临时数组的更新结果拷贝到原始数组中
            nums[l:r+1] = tmp[l:r+1]

        def _merge_sort(nums, l, r):
            if l < r:
                # 找到mid，将数组划分为两部分，递归排序得到两个均内部有序的子数组，然后合并
                mid = (l + r) // 2
                _merge_sort(nums, l, mid)
                _merge_sort(nums, mid+1, r)
                merge(nums, l, mid, r)

        tmp = [0] * len(nums)
        _merge_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums):
        def _partition(nums, l, r):
            """
            l和r是当前分区的左右端点
            :param nums:
            :param l:
            :param r:
            :return:
            """
            pivot = nums[l]
            start = l
            end = r
            while start < end:
                # 因为基准是取的左边，所以要先从右边开始查找第一个小于基准的元素，如果范围符合则交换
                while start < end and nums[end] > pivot:
                    end -= 1
                if start < end:
                    nums[start] = nums[end]
                # 从左边开始查找第一个大于基准的元素，如果符合范围交换
                while start < end and nums[start] <= pivot:
                    start += 1
                if start < end:
                    nums[end] = nums[start]
            # start的位置是预留给基准的，直接赋值，因为此前基准的位置已被小于基准元素覆盖
            nums[start] = pivot
            return start

        def _quick_sort(nums, l, r):
            if l < r:
                # 分区后可以确定[l,mid-1]<[mid]<[mid+1,r]，所以继续对左右两侧排序
                mid = _partition(nums, l, r)
                _quick_sort(nums, l, mid-1)
                _quick_sort(nums, mid+1, r)
        _quick_sort(nums, 0, len(nums)-1)
        return nums

    def heap_sort(self, nums):
        def max_heapify(start, end):
            # 指向当前节点和子节点
            father = start
            son = 2 * start + 1
            # 保证子节点有效，即没有超过数组范围
            while son <= end:
                # 选择左右子节点中最大的值代替父节点位置
                if son + 1 <= end and nums[son] < nums[son+1]:
                    son += 1
                # 已经满足最大堆性质返回
                if nums[father] > nums[son]:
                    return
                # 调整节点满足最大堆，并继续向下调整
                nums[father], nums[son] = nums[son], nums[father]
                father = son
                son = 2 * father + 1

        n = len(nums)
        # 建立最大堆的过程，对所有非叶子节点进行调整，并且从下向上遍历，保证对于某一非叶子节点，其子节点均满足最大堆性质
        for i in range((n-1)//2, -1, -1):
            max_heapify(i, n-1)
        # 每次将根节点（最大值）换到当前数组最后一位，并将最右元素放入根节点进行调整，保证根节点为最大值
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heapify(0, i-1)
        return nums

    def count_sort(self, nums):
        # 得到最大最小值确定计数数组的范围
        min_value, max_value = nums[0], nums[0]
        ans = [-1] * len(nums)
        for i in range(1, len(nums)):
            if min_value > nums[i]:
                min_value = nums[i]
            elif max_value < nums[i]:
                max_value = nums[i]
        count = [0] * (max_value - min_value + 1)
        # 计数
        for i in nums:
            count[i-min_value] += 1
        # 根据计数结果计算数字在结果数组中的位置
        for i in range(1, len(count)):
            count[i] += count[i-1]
        # 根据位置拷贝数字
        for num in nums:
            count[num-min_value] -= 1
            ans[count[num-min_value]] = num
        return ans

    def bucket_sort(self, nums):
        # 得到最大最小值确定桶的个数
        max_value, min_value = max(nums), min(nums)
        buckets = [[] for _ in range(max_value//10 - min_value//10 + 1)]
        # 根据划分桶的方式映射数字并存入桶
        for num in nums:
            index = num//10 - min_value//10
            buckets[index].append(num)
        nums.clear()
        # 按顺序合并，内部采用插入排序
        for l in buckets:
            nums.extend(self.insert_sort(l))
        return nums

    def radix_sort(self, nums, radix=10):
        import math
        # 求出数组中最大数的位数，用于确定排序循环次数
        max_digit = math.ceil(math.log(max(nums), radix))
        # 构造存储数字的桶
        bucket = [[] for _ in range(radix)]
        for i in range(max_digit):
            # 将数字根据规则放入对应桶中，这里是取最低位最高位的顺序
            for num in nums:
                bucket[num % (radix ** (i+1)) // (radix ** i)].append(num)
            nums.clear()
            # 按顺序合并
            for l in bucket:
                nums.extend(l)
            bucket = [[] for _ in range(radix)]
        return nums


s = Solution()
nums = [5,3,6,87,89,3,5,5,7,1,9,6,5,3]
print(s.radix_sort(nums))
