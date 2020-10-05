age1=input("enter the age1:-")
age2=input("enter the age2:-")
age3=input("enter the age3:-")
if(age1>=age2 and age1>=age3):
    print("age1, age2 or age3 se bada hai")
elif(age2>=age1 and age2>=age3):
    print("age2, age1 or age3 se bada hai")
elif(age3>=age1 and age3>=age2):
    print("age3, age1 or age2 se bada hai")
else:
    print("all age is equal")
