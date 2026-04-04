class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}

        for i in nums:
            get = results.get(i, None)
            if get:
                results[i] += 1
            else:
                results[i] = 1
        
        sorted_dict = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

        
        return list(sorted_dict.keys())[0:k]