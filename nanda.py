# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 05:28:41 2018

@author: nandavari
"""

#k= input('read the sentences:')
def rem_vowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
             
    # Print string without vowels
    print(string)
# Driver program
string = "hii friends my self chwodaiah"
rem_vowel(string)




c=input("enter data:")
wordcount=len(c)
print(wordcount)



time = float(input('enter the number of seconds:'))
time %=(24 * 3600)
hours = time // 3600
time %= (60 * 60)
mintues = time // 3600
time %= 60
seconds = time 
print("hh:mm:ss->%d:%d:%d" %(hours,mintues,seconds)) 


    #!/usr/bin/env python







Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print ("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C:")
#Convert Celsius to Fahrenheit
#!/usr/bin/env python
Celsius = int(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print ("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F:")