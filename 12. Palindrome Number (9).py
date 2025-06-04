class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if x < 0:
            return False
        else:
            res_x = str_x[::-1]
            if res_x == str_x:
                return True
            else: 
                return False
        
