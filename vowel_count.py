#count vowels
str=input("enter the string:")
vowelcount=0
vowels="aeiouAEIOU"
for char in str:
        if char in vowels:
                vowelcount+=1
print(f"the vowel count in string is {vowelcount}")