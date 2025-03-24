# https://leetcode.com/problems/merge-strings-alternately/description/
# Time & Space complexity: O(a + b)

class Solution(object):
    def mergeAlternatively(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged = []
        l = min(len(word1), len(word2)) # O(1)
        for i in range(l):
            merged.append(word1[i]) # O(1)
            merged.append(word2[i]) # O(1)

        merged.append(word1[l:] or word2[l:] ) # O(len(w1) - len(w2)) or vice-verse

        return "".join(merged) # O(w1 + w2)
