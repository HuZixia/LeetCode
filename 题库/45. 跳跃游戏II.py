# -*- coding: utf-8 -*-
# @Time      : 2024/6/21 02:03
# @Author    : huzixia
# @FileName  : Test
# @微信公众号  : AI Freedom
# @知乎       : RedHerring


# 贪心算法

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        # 记录当前的跳跃次数
        jumps = 0
        # 当前能达到的最远距离
        current_end = 0
        # 下一步能达到的最远距离
        farthest = 0

        # 遍历数组，最后一个元素不需要遍历
        for i in range(n - 1):
            # 更新能达到的最远距离
            farthest = max(farthest, i + nums[i])

            # 如果到达了当前的最远距离，说明需要一次跳跃
            # 如果当前遍历的位置 i 达到了 current_end，说明上一次跳跃所能到达的最远位置已经走完了，这时需要增加跳跃次数，并更新 current_end 为当前遍历过程中能达到的最远距离 farthest。
            if i == current_end:
                # 增加跳跃次数
                jumps += 1
                # 更新当前的最远距离
                current_end = farthest
                # 如果当前的最远距离已经超过或等于最后一个位置，则跳出循环
                if current_end > n - 1:
                    break
        return jumps


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))  # 2
# print(solution.jump([2, 3, 0, 1, 4]))  # 2
# print(solution.jump([1, 1, 1, 1, 1]))  # 4

# 为什么能够判断跳跃的步数：
#
# 	•	局部最优选择：每次在当前范围内选择能够跳到最远的地方。
# 	•	贪心策略：贪心算法总是做出在当前看来最好的选择（即选择跳跃最远的地方），最终保证全局最优解（即最少的跳跃次数）。
# 	•	遍历整个数组：遍历数组时，不断更新最远可达距离，当需要新的跳跃时才增加跳跃次数并更新跳跃范围。