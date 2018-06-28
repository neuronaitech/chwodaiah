# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
k =input("read the sentence:")

k=k.lower()
print(k)

#k=k.upper()
#print(k)

k=k.replace('a','A')
k=k.replace('e','E')
k=k.replace('i','I')
k=k.replace('o','O')
k=k.replace('u','U')
print(k)

 
#reverse order
  'chwodaiah'[::-1]
   
  
    
   
   
   
   k=input("Enter a sentence :")
   print(k.replace('v' , 'b'))
   print(k.replace('b' , 'v'))
   
  
    
   
   k={'Mexico':'Mexicocity','china':'Beijing','France':'Paris','Belguim':'Brussels','Argentina':'Buenos'}
   k3=sorted(k.keys())
   for key in k3:
       print("%s:%s" %(key, k[key]))