#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
        return [s.index(i) for i in s] == [t.index(i) for i in t]
# @lc code=end

