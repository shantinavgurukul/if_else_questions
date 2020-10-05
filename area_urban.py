# age=int(input("enter the age="))
# sex=input("enter the sex=")
# marry=input("you are married or not=")
# if(sex=='f'):
#     print("urban areas only")
# elif(sex=='m'and age>=20 and age<=40):
#     print("you are work anywhere")
# elif(sex=='m' and age>=40 and age<=60):
#     print("urban areas ")
# else:
#     print("error")


print ("Enter age")
age = int(input())
print ("SEX? (M or F)")
sex =input()
print ("MARRIED? (Y or N)")
marry = input()
if sex == "F" :
  print ("Urban areas only:-")
elif sex == "M" and age>=20 and age<=40:
  print ("You can work anywhere")
elif sex == "M" and age>40 and age<=60:
  print( "Urban areas only")
else:
  print ("ERROR")