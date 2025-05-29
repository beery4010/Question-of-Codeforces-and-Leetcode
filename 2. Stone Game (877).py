# 2. Approach (simple one)
# class Solution(object):
#     def stoneGame(self, piles):
#         """
#         :type piles: List[int]
#         :rtype: bool
#         """
#         return True

# 1. Approach
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alice_beg = 0
        alice_last = 0
        bob_beg = 0
        bob_last = 0
        count = 0

        while count < len(piles):
            if count%2 == 0:
                alice_beg += piles[count]
            else: 
                bob_beg += piles[count]
            count += 1
        
        count = len(piles) - 1

        while count >= 0:
            if count%2 == 0:
                bob_last += piles[count]
            else:
                alice_last += piles[count]
            count -= 1
        
        if (alice_beg > bob_beg) or (alice_last > bob_last):
            return True
        else: 
            return False
