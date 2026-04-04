





class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_arr = []
        hash_map = {}
        for i in strs:
            for char in i:
                char_arr.append(char)
            print(char_arr)
            char_arr.sort()
            joined = "".join(char_arr)
            get_hash = hash_map.get(joined, None)
            if get_hash:
                hash_map[joined].append(i)
            else:
                hash_map[joined] = [i]
            char_arr = []
        print(hash_map.values())
        return list(hash_map.values())
        
        