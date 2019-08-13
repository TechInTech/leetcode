#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (30.68%)
# Likes:    2154
# Dislikes: 0
# Total Accepted:    174.6K
# Total Submissions: 568.9K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        
        num, n = 1, len(s)
        for i, item1 in enumerate(s[0:n-1]):
            if s[i] == s[i+1]:
                continue
            item = item1
            for item2 in s[i+1:n]: 
                if item2 in item:
                    break
                item += item2
            if len(item) > num:
                num = len(item)
        return num

