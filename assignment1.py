#Q1 to print the square of a number in the list given if it is greater than 50. 

l1 = [1 ,12,34,53,65,77,34] 
for i in l1 :
  if (i**2  > 50):
    print(i**2) 
#now by using list comprehension we have 
l1 = [1 ,12,34,53,65,77,34] 
[i**2 for i in l1 if i**2 > 50 ]


#Q2 for a given list if value is greate than 5 print hi else print bye 

 L1 = [24,4,56,65,7,2]
 for i in l1:
   if(i > 5):
     print(hi)
    else :
      print(bye)
      
      #or 
L = [24 ,4,56,65,7,2]
['hi' if (i>5) else 'bye' for i in L ]


#Q3 find all the numbers from 1 to 1000 that have 3 in them 
[i  for i in range(1,1001) if '3' in str(i)]

#Q4 count the number of spaces in a given string
s = '   my   name   is   parth  '
l1 = [i for i in s  if s == ' ']
print(len(l1))

#Q5 count the number of consonants in a given string 
s ='fgrgoehebvevwufwyrawoxmcn bzwnk   mvmbitvv'
S=['a'  'e' 'i' 'o' 'u' ' ']
l1 = [i for i in s if i not in S  ]
print(len(l1))

#Q6 If x**2 <= excute 27*x foe values in range 1-20
l=[27*i for i in range(1,21) if(i**2<=10)]
print(l)

#Q7 Print all the even no. in the range 1-20
[i for i in range(1,21) if i%2==0 ]

#Q8 Find all the no . that can be divided by 2 and 5 in some range 
l=[i for i in range(1,1001) if (i%2==0) and (i%5==0)]
print(l)
