# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution(object):
    def mergeAlternatively(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged = []
        l = min(len(word1), len(word2))
        for i in range(l):
            merged.append(word1[i])
            merged.append(word2[i])

        merged.append(word1[l:] or word2[l:] )

        return "".join(merg)
