def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write = lengthA - 1
  read = lengthA - 1

  while(read >= 0):
    if A[read] != 0:
      A[write] = A[read]
      write -= 1

    read -= 1

  while(write >= 0):
    A[write]=0;
    write-=1
    
v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
