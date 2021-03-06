/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */

// @lc code=start
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        // auto 循环会创建副本，auto 推导会重开地址？
        for (int _index = 0; _index < A.size(); ++_index) 
            A[_index] *= A[_index];
        std::sort(A.begin(), A.end());
        return A;
    }
};
// @lc code=end

