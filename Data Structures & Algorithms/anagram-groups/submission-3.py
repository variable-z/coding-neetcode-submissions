from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        for string in strs:
            alpha_array = [0]*26
            for s in string:
                alpha_array[ord('a')-ord(s)] += 1
            key = tuple(alpha_array)
            anagram_group[key].append(string)
        return [value for value in anagram_group.values()]
            

       
