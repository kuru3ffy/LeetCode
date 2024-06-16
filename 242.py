class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_sorted_list = sorted(s_list)
        t_sorted_list = sorted(t_list)
        return s_sorted_list == t_sorted_list
