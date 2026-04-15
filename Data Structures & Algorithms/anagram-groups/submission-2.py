from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}
        for string in strs:
            freq = Counter(string)
            key = tuple(sorted(freq.items()))
            if key in anagram_group:
                anagram_group[key].append(string)
            else:
                anagram_group[key] = [string]
        result = []
        for key in anagram_group.keys():
            result.append(anagram_group[key])
        return result


       
