details={"Name":"sahil pathak","RollNo:" :15 , "Sec" : "d1710" ,"Nationality:" : "Indian", "Achievements:" : "National level shooter"}
print(details)

print("Name : ",details["Name"])
print("Achievements: ",details["Achievements:"])
print("RollNo. : ",details["RollNo:"])
print("Nationality ",details["Nationality:"])

details["Name"]="saar"
details["talent"]="Singer"
details["three"]=""
print(details)

#----------------------------------------------------------------------------------------------
#dictionary using list

d={"a":[1,2,3,4,5],"b":[5,6,7,8,9]}
print(d["a"])
print(d.get("c"))

#---------------------------------------------------------------------------------------------
english=d.get("h",[])
print(len(english))

#---------------------------------------------------------------------------------------------
#delete key from dictionary

del details["talent"]
print(details)

print(details.pop("three"))

details.popitem()
print(details.keys())
print(details.values())
print(details.items())

#length of keys
print(len(details.keys()))

#to check value in dictionary
print(("sex","male") in details.items())

#---------------------------------------------------------------------------------------------
#to print all values of dictionary

for value in details.values():
    print(value)
#---------------------------------------------------------------------------------------------
    # detail=details.copy()
    #   print("detail=",detail)
#---------------------------------------------------------------------------------------------





