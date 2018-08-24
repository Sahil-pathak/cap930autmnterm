empty_set=set()
set_from_list=set(["a","b","c","d"])
print(type(set_from_list))

a={"a","a","b","c"}
print(len(a))


b=set("mississippi")
b.add('r')
print(b)

b.remove('m')
print(b)


print(b.pop())

b.clear()

a=set("missisippi")
b=set("uganda")
print(a)
print(b)

#iset difference

print("set difference : ",a-b) #elements in a but not in b
print("set difference : ",b-a) #elements in b but not in a

#union

print("union  :: ",a|b)

#intersection

print("intersection   ::  ",a&b)


#symmetric difference

print("Symmetric difference a^b :: ",a^b)
print("Symmetric difference  b^a :: ",b^a)



efficient_letters={}
