names=["Dan",1,"tim",True,False,10.2]

print(names[2])
#checking length of
print(len(names))

print(names[5])
print(names[3])
print(names[4])
#accessing an element in a list within a list also known as list nesting
matrix=[[1,2,3],[4,5,6,["a","b","c","d",[11,12,13]]],[7,8,9]]

print(matrix[1][2])

print(matrix[1][3][-1])

print(matrix[-1])

print(matrix[1][3][4][1])

mat=[[1,2,3],[4,5,6,["a,b,c,d"]],[7,8,9]]
d=mat[1][3][0]
print(d)
print(d[-1])




