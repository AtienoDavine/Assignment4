
maths = int(input("enter maths mark"))
physics = int(input("enter physics mark"))
geo = int(input("enter geo mark"))
chem = int(input("enter chem mark"))

average = (maths + physics + geo + chem) / 4

print(average)
if 0 <= average <= 30:

   'return' "D"

elif 31 <= average <= 50:

    print("D")



elif 51 <= average <= 70:
    print("B")

elif 71 <= average <= 100:
    print("A")
else:


 print("unrecognised marks/average")










