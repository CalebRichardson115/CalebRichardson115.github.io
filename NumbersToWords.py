class Solution(object):
    '''Given a number n, returns the corresponding word form. Whole algorithm is developed
    on the idea that each place value in a number can be isolated with modulo and therefore have a correspinding value
    in one of the following arrays based on what place value is being operated on. Built on same idea as IntegerToRomanNumerals
    but allows for inputs lower than 10 billion.'''
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'

        oneList = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        TenList =["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        #no split between words as that occurs in the final step.
        hundredList = ["","OneHundred","TwoHundred","ThreeHundred","FourHundred",
        "FiveHundred", "SixHundred", "SevenHundred", "EightHundred", "NineHundred"]
        teenList = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
        "Seventeen","Eighteen","Nineteen"]

        Hundreds = hundredList[(num%1000)//100]
        if ((num%100)//10) == 1:
            Teens = teenList[num%10]
            solToHundreds = Hundreds + Teens
        else:
            Tens = TenList[(num%100)//10]
            Ones = oneList[num%10]
            solToHundreds = Hundreds + Tens + Ones
        
        HundredThousand = hundredList[(num%1000000)//100000]
        if((num%100000)//10000) ==1:
            TeenThous = teenList[(num%10000)//1000]
            Thousand = ""
            TenThous = ""
            soltoThous = HundredThousand + TeenThous
        else:
            TenThousand = TenList[(num%100000)//10000]
            Thousand = oneList[(num%10000)//1000]
            TeenThous = ""
            soltoThous = HundredThousand + TenThousand + Thousand

        if HundredThousand != "" or TeenThous != "" or TenThousand != "" or Thousand != "":
            soltoThous = soltoThous + "Thousand"

        HundredMill = hundredList[(num%1000000000)//100000000]
        if((num%100000000)//10000000) == 1:
            TeenMill = teenList[(num%10000000)//1000000]
            TenMillion = ""
            Million = ""
            soltoMill = HundredMill + TeenMill
        else:
            TeenMill = ""
            TenMill = TenList[(num%100000000)//10000000]
            Million = oneList[(num%10000000)//1000000]
            soltoMill = HundredMill + TenMill + Million
        if HundredMill != "" or TeenMill != "" or TenMill != "" or Million != "":
            soltoMill = soltoMill + "Million"

        Billion = oneList[(num%10000000000)//1000000000]
        if Billion != "":
            Billion = Billion + "Billion"

        #typecasts to ensure no error.
        solToHundreds = str(solToHundreds)
        solToThous = str(soltoThous)
        soltoMill = str(soltoMill)
        Billion = str(Billion)

        solution = Billion + soltoMill + soltoThous + solToHundreds

        #instruction to add spaces before uppercase letters
        solution = ''.join([' '+ s if s.isupper()  else s for s in solution]).lstrip()
        
        return solution
    
        """
        :type num: int
        :rtype: str
        """