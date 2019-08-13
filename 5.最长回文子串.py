#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.43%)
# Likes:    1105
# Dislikes: 0
# Total Accepted:    86K
# Total Submissions: 324.7K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 0:
            return ''
        if len(s) == 1:
            return s
        
        # 回文子串首子串
        s1 = s[0]
        for i, item in enumerate(s[0:len(s)-1]):
            s2 = item
            for item1 in s[i+1::]:
                s2 += item1
                if s2 == s2[::-1] and len(s2) > len(s1):
                    s1 = s2
        return s1

