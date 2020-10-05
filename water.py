water=int(input("enter the water="))
if(water<=1):
    print("pani bharna hai")
elif(water>1 and water<10):
    print("or ni bhARANA HAI")
elif(water>10):
    print("overflow")
else:
    print("not overflow")