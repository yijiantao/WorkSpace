/*
 * @lc app=leetcode.cn id=201 lang=cpp
 *
 * [201] 数字范围按位与
 */

// @lc code=start
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int mask = 1 << 30;    // 获取最高位
        int ans = 0;
        while (mask > 0 && (m&mask) == (n&mask)) {    // 寻找相同的前缀
            ans |= m & mask;
            mask >>= 1;
        }
        return ans;
    }
};
// @lc code=end

