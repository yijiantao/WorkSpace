/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */

// @lc code=start
#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        std::stack<char> test_s;
        for (int _index = s.size() - 1; _index >= 0; --_index)
            test_s.push(s[_index]);
        
        for (int _index = 0; _index < t.size(); ++_index) {
            if (test_s.empty()) return true;
            char temp_s = test_s.top();
            test_s.pop();
            if (temp_s == t[_index]) continue;
            else test_s.push(temp_s);
            
        }
        return test_s.empty();
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution test;
    std::string s = "axc", t = "ahbgdc";
    std::cout << test.isSubsequence(s, t) << std::endl;
    return 0;
}

