class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for str in strs:
            char_map = {}
            for char in str:
                char_map[char] = char_map.get(char, 0) + 1
            c_sort = tuple(sorted(char_map.items()))
            group = string_map.get(c_sort, [])
            group.append(str)
            string_map[c_sort] = group
        return list(string_map.values())

            

            
        


                