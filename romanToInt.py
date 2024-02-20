class Solution:
    def romanToInt(self, s: str) -> int:
        dictOfLetters = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":3, # readed I and + 3 from V
        "IX":8,
        "XL": 30,
        "XC": 80,
        "CD": 300,
        "CM": 800,
        "0":0
        }
        s = "0"+s
        number = 0
        for i in range(len(s)):
            if s[i] == "V":
                if s[i-1] == "I":
                    number+=dictOfLetters["IV"]
                else:
                    number+= dictOfLetters[s[i]]
            elif s[i] == "X":
                if s[i-1] == "I":
                    number+=dictOfLetters["IX"]
                else:
                    number+= dictOfLetters[s[i]]
            elif s[i] == "L":
                if s[i-1] == "X":
                    number+=dictOfLetters["XL"]
                else:
                    number+= dictOfLetters[s[i]]
            elif s[i] == "C":
                if s[i-1] == "X":
                    number+=dictOfLetters["XC"]
                else:
                    number+= dictOfLetters[s[i]]
            elif s[i] == "D":
                if s[i-1] == "C":
                    number+=dictOfLetters["CD"]
                else:
                    number+= dictOfLetters[s[i]]
            elif s[i] == "M":
                if s[i-1] == "C":
                    number+=dictOfLetters["CM"]
                else:
                    number+= dictOfLetters[s[i]]
            else:
                number += dictOfLetters[s[i]]
        return number




sol= Solution()
sol.romanToInt("III")
sol.romanToInt(s = "LVIII")
sol.romanToInt("MCMXCIV")