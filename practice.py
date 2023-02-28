list=[2,5,6,9,3,3,23,45,65,22,87,94,54,12,15,27,50]
count=0
for i in list:
    if i >10:
      count+=1
       
print(count)

#num=int(input("enter number"))
#if num %2==0:
    #print("it's an even number")
#else: 
   # print("it's an odd number")

#num=int(input("enter number"))
#if num >0:
   # print("it's a postive number")
#elif num==0:
   # print("it's a zero")
#else:
    #print("it's a negative number")

num=int(input("enter number"))
for i in range (0,num):
    for t in range (0,i+1):
         print('#')
    print()
