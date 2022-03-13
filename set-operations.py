#using set data  type
#creating a set
set1={"pravalli","sandhya","varshini","usha","sam"}
print(set1)
print(type(set1))
#to find the length of the set
print(len(set1))
#use of in keyword in python
if "pravalli" in set1:
    print("she is a good girl")

#use of "not in" keyword in python
if "uday" not in set1:
    print("uday name is not in the set")
#creating an empty set
set2=set()
print(type(set2))
#adding string to the empty set
set2.add("youtube")
print(set2)
#creating two sets
set3={1,2,3,4}
set4={6,7,8,9,1}
print(set3)
print(set4)
#using union operation in set3 and set4
result=set3.union(set4)
print(result)
#using inetrsect operator in python
result=set3.intersection(set4)
print(result)