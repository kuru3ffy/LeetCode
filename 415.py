class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # リストに変換して逆順にする
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        
        sum_nums = []
        carry = 0
        longer_len = max(len(num1), len(num2))
        
        for i in range(longer_len):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            
            tmp = digit1 + digit2 + carry
            carry = tmp // 10
            sum_nums.append(str(tmp % 10))
        
        if carry:
            sum_nums.append(str(carry))
        
        return ''.join(sum_nums[::-1])

