import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

# check version
print(numpy.__version__)

print(type(arr))


# 0-D array
arr = numpy.array(42)
print(arr)

#1-D array
arr = numpy.array([9,8,7,6,5,4,3,2,1,0])
print(arr)

#2_D array
arr = numpy.array([[99, 98, 97], [96, 95, 94]])
print(arr)

#3-D array
arr = numpy.array([[[99, 98, 97], [96, 95, 94]], [[93, 92, 91], [90, 89, 88]]])
print(arr)

#check number of dimensions
print(arr.ndim)


#Access Array Elements
arr = numpy.array([1, 2, 3, 4])
print(arr[0])

#Access 2-D Arrays
arr = numpy.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])


#Slicing arrays
arr = numpy.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Slice elements from index 4 to the end of the array
print(arr[4:])