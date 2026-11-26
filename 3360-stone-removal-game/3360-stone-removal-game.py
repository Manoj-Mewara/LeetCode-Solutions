class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_remove = 10
        turns = 0
        while n >= alice_remove:
            n = n - alice_remove
            alice_remove -= 1
            turns = turns + 1
        if turns % 2 != 0: #Because, Alice has the 1st turn & Bob has 2nd.So,Alice has odd turn
            return True
        else:
            return False 

     
            