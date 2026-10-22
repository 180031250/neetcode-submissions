class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numbers=defaultdict(list)
        rest=[]
        final=[]
        for i in strs:
            key = tuple(sorted(i))
            numbers[key].append(i)
        return list(numbers.values())
