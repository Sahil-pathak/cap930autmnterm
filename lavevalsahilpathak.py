FirstName="Sahil P Pathak "

FinalName=FirstName.split()

print(FinalName)
print("First Name : ",FinalName[0])
print("Middle Name : ",FinalName[1])
print("Last Name : ",FinalName[2])

Name= FinalName[0]+" "+FinalName[1]+" "+FinalName[2]
print("Name is ",Name)

print("Reverse of the string is :",Name[::-1])

print("Length of Name is : ",len(Name))

print("Name in UpperCase is :",Name.upper())
print("Name in UpperCase is :",Name.lower())

print("Threee characters from begenning are : ",FirstName[0:3])

print("Threee characters from last are : ",FirstName[11:])
