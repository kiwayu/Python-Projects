def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return[num_map[complement], i]
        num_map[num] = i
               
        
def contains_duplicate(self, nums: list[int]) -> bool:
    dup_map = {}
    
    for i, num in enumerate(nums):
        if num in dup_map:
            return True
        dup_map[num] = i
        
    return False

def frequency_counter(self, nums: list[int]) -> dict:
    counter_map = {}
    for num in nums:
        if num in counter_map:
            counter_map[num] += 1
        else:
            counter_map[num] = 1
    return counter_map

def unique_char(self, s: str) -> int:
    count_map = {}
    for char in s:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1
            
    for i, char in enumerate(s):
        if count_map[char] == 1:
            return i
    
    return -1

def anagrams(self, s: str, t: str) -> bool:
    anagram_map = {}
    if len(s) != len(t):
        return False
    for char in s:
        anagram_map[char] = anagram_map.get(char, 0) + 1
    
    for char in t:
        if char not in anagram_map or anagram_map[char] == 0:
            return False
    
    return True

def find_missing_number(self, nums:list[int]) -> int:
    int_map = {}
    n = len(nums)

    for num in nums:
        int_map[num] == True
        
    for i in range(n+1)
        if i not in int_map:
            return i

    return -1
        
    
    
        