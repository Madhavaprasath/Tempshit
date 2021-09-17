def add_numbers(*num):
 sum=0
 total_numbers=0
 for i in sum:
     sum+=i
     total_numbers+=1
 return [sum,total_numbers]

def main():
  numbers=[]
  total=int(input("total_numbers"))
  for i in range(0,total):
      num=int(input("enter the num"))
      numbers.append(num)
  print(numbers)
  aver=add_numbers(numbers)
  final=aver[0]/aver[1]
  print("The average of numbers are ",final)
         

main()
print("hello world")


