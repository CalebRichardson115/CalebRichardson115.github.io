'''
Program that returns the Roman numeral form of a given number. Works by isolating place values
with modulo which corresponds to an index in an array. Allows for inputs lower than 3999.
'''
class Solution(object):
    def intToRoman(self, num):
        RomanOnes = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        RomanTens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        RomanHundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        RomanThousands = ["", "M", "MM", "MMM"]

        thousand = RomanThousands[num//1000]
        hundred = RomanHundreds[(num%1000)//100]
        ten = RomanTens[(num%100)//10]
        one = RomanOnes[num%10]
        solution = thousand + hundred + ten + one
        return solution