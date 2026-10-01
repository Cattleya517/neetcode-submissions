class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}

        for word in strs:
            processed = ''.join(sorted(word))
            if processed not in record:
                record[processed] = [word]
            else:
                record[processed].append(word)
        
        return list(record.values())