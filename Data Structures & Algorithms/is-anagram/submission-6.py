class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s),len(t)
        if n != m:
            return False
        anagram = [0]*26
        for i in range(n):
            anagram[ord(s[i])-ord('a')] += 1
            anagram[ord(t[i])-ord('a')] -= 1
        for a in anagram:
            if a != 0:
                return False
        return True


        

        



        