# exercise-01 Vowel or Consonant

alphabet = input("Please enter a letter from the alphabet (a-z or A-Z): ")
if alphabet in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
  print("The letter %s is a vowel."%alphabet)
else:
  print("The letter %s is a consonant."%alphabet)


# exercise-02 Length of Phrase

in_str = input("Please enter a word or a phrase: ")
while True:
  if in_str == "quit":
    break
  print("What you enetered is "+ str(len(in_str))+ " characters long")
  in_str = input("Please enter a word or a phrase: ")


# exercise-03 Calculate Dog Years

age_str = input("Input a dog's age in human years: ")
age_num = int(age_str)
if age_num == 1:
  dog_age = 10
elif age_num == 2:
  dog_age = 20
elif age_num > 2:
  dog_age = 20 + (age_num-2)*7
print("The dog's age in dog years is " +str(dog_age)+ " year(s).")


# exercise-04 What kind of Triangle?

print("Enter the lengths of three side of a triangle:")
a_str = input("a: ")
b_str= input("b: ")
c_str = input("c: ")
a = int(a_str)
b = int(b_str)
c = int(c_str)
if a==b and b==c :
  print(f'A triangle with sides of {a_str},  {b_str}  & {c_str} is an equilateral triangle')
elif a==b or a==c or b==c:
  print(f'A triangle with sides of {a_str},  {b_str}  & {c_str} is an scalene triangle')
else:
  print(f'A triangle with sides of {a_str},  {b_str}  & {c_str} is an isosceles triangle')


# exercise-05 Fibonacci sequence for first 50 terms

# def fibonacci(n):
#     if n==0 or n==1 :
#       term = n
#       y=1
#     else:
#       term = n
#       y = fibonacci(n-2)+fibonacci(n-1)
#     return y
# print(fibonacci(50))


fibo_0 = 1
fibo_1 = 1
for i in range(50):
  if i==0:
    fibo_0=0
    fibo_1=0
  if i==1:
    fibo_0=0
    fibo_1=1
  fibo = fibo_0+fibo_1
  fibo_0=fibo_1
  fibo_1 = fibo
  print("term: "+ str(i)+ "/ number: " + str(fibo))


  
# exercise-06 What's the  Season?

input_month_str = input("Enter the month of the year (Jan - Dec): ")
input_day_str =  input("Enter the day of the month: ")
input_month = input_month_str.upper()
input_day = int(input_day_str)
if (input_month == 'DEC' and input_day>=21) or (input_month == 'MAR' and input_day<=19) or  input_month in ('JAN', 'FEB'):
  print(input_month_str +" "+input_day_str+" is in Winter")
elif (input_month == 'MAR' and input_day>=20) or (input_month == 'JUN' and input_day<=20) or  input_month in ('APR', 'MAY'):
  print(input_month_str +" "+input_day_str+" is in Spring")
elif (input_month == 'JUN' and input_day>=21) or (input_month == 'SEP' and input_day<=21) or  input_month in ('JUL', 'AUG'):
  print(input_month_str +" "+input_day_str+" is in Summer")
elif (input_month == 'SEP' and input_day>=22) or (input_month == 'DEC' and input_day<=20) or  input_month in ('OCT', 'NOV'):
  print(input_month_str +" "+input_day_str+" is in Fall")


