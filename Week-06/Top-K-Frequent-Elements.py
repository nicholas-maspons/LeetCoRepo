# 347. Top K Frequent Elements

class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
    
        freq_list = []
        for num in freq_map:
            freq_list.append((freq_map[num], num)) 

        freq_list.sort(reverse=True)
    
        result = []
        for i in range(k):
            result.append(freq_list[i][1])  

        return result