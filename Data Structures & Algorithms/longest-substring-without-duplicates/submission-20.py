class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}  # stores last index of each character
        longest = 0
        left = 0  # start of current substring

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                # duplicate found, move left pointer past previous occurrence
                left = last_seen[char] + 1

            # update last seen index
            last_seen[char] = right

            # update longest substring length
            longest = max(longest, right - left + 1)

        return longest
