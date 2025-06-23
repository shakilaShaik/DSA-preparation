class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict={"I":1, "V":5,"X":10,"L":50, "C":100, "D":500, "M":1000}
        number=0
        prev_nbr=0
        for char in reversed(s):
            value=symbol_dict[char]
            if prev_nbr >value:
                number=number-value
            else:
                number +=value
                prev_nbr=value
        return number
