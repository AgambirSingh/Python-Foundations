#W5 L2
#Access variable from nested list
f = [45,93,150.67,"Python","Programming","My","Name",['spam',45.67,95]]
print(f[3:6])
print([7]) # It will print whole nested list
print(f[7][0]) #to print specific word inside/from a nested list ^^^ 

# Merge- it will merge/add two list
l1=[1,2,'spam',3,4]
l2=[5,6,7,8,'rogers',11]
sum2=l1+l2
print(sum2)
# or
print(l1+l2)
# or

#EXTEND fn. - merge/add two variables
(l1.extend(l2)) # L1(list 1) extended to L2(list 2) so that it incudes list 2
print(l1)

#REPLACE- to repllace a variable in list
l3= [45,67,34,49,7]
l3[1]=100 #Element in the 1st index of l3 will become 100
print(l3)

#COPY- copy the item from list L3 to list L4
l4=[] #empty
l3=l4 #we copied empty list to list 3
print(l3)# since l3 has become l4 the l3 became empty
l4=l3 #compying the elements from L3 to L4
print(l4)

# to fix it we do 
l3= [45,67,34,49,7]
#copy the item from list L3 to list L4
l4=[] #empty
l4=l3 #compying the elements from L3 to L4
print(l4)

#ADD- add individual elements of  list
l5=[100,20,50,7,3]
l6=["sum1","Zoo","Agam","basketball"]
print(sum(l5)) #it will add all the elements in List "L6"
print(min(l5)) # it will find minumum value in List "L6"
print(max(l5)) # it will find maximum value in List "L6"
l5.sort() #Sort fn.-it will sort the list
l6.sort()
print(l5)
print(l6)
l6.sort(key=str.lower) #kEY fn.- gives condition to sort fn.
print(l6)

#REVERSE fn.- sort out the list in revere order(descending order)
l7=[7,62,45,69,21]
l7.sort(reverse=True)
print(l7)

#it does not sort list it just reverse the list as it is
l8=[7,62,45,69,21,1,99]
print(l8[::-1]) #it will print out the reverse list

l9=[49, 33, 23, 56, 99]
a,b,c,d,e= l9 #here we are assigning value to each elemt in the list
print(b)