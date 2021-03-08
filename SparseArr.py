#sparse array
rows=cols=11
chess_arr1 = [[0 for i in range(cols)] for j in range(rows)]
#for i in range(rows):
 #   print(chess_arr1[i][:])
chess_arr1[1][2] = 1
chess_arr1[2][3] = 2
chess_arr1[4][5] = 2
print("the orinigal array is like:","\n")
for i in range(rows):
   print(chess_arr1[i][:])

#2-dim arrary to sparse:
num = 0 #how many non zero nums ?
for i in range (rows):
    for j in range(cols):
        if chess_arr1[i][j] !=0:
            num +=1
print(num)

sparse_arr = [[0 for i in range(3)] for j in range(num+1)]

#values:
sparse_arr[0][0] = len(chess_arr1)
sparse_arr[0][1] = len(chess_arr1[0])
sparse_arr[0][2]=num

count = 0
for i in range(len(chess_arr1)):
    for j in range(len(chess_arr1[0])):
        if (chess_arr1[i][j] !=0):
            count +=1
            sparse_arr[count][0] = i
            sparse_arr[count][1] = j
            sparse_arr[count][2] = chess_arr1[i][j]
print("now we got the spare array of chess_arr1")           
for i in range(len(sparse_arr)):
    print(sparse_arr[i][:])

#back to original array:
rows2 = sparse_arr[0][0]
cols2 = sparse_arr[0][1]
chess_arr2 = [[0 for i in range(cols2)] for j in range(rows2)]

for i in range(1, len(sparse_arr)):
    chess_arr2[sparse_arr[i][0]][sparse_arr[i][1]] = sparse_arr[i][2]
for i in range(len(chess_arr2)):
    print(chess_arr2[i][:])
