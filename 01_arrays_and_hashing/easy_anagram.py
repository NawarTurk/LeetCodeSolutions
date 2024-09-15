class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return Counter(s) == Counter(t)
        # Time Complexity: O(n) - Counter() traverses the string once
        # Space Complexity: O(1) - space depends on the character set, which is constant
        

        # return sorted(t) == sorted(s)
        # Time Complexity: O(n log n) - dominated by the sorting step
        # Space Complexity: O(n) - sorting usually requires storing a copy of the data

        if len(s) != len(t):
            return False

        freq_s, freq_t = {}, {}

        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        return freq_s == freq_t
        # Time Complexity: O(n) - Each string 's' and 't' is iterated once to build their frequency maps, 
        # each iteration taking O(n) time
        # Space Complexity: O(1) - depends on the size of the character set, not the input size

        
