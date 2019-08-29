def mergesort(A):
	if len(A) > 1: # if the length of the array is > than 1 
		middle  = len(A)//2 # devide the array in 2
		L = A[:middle] # everything before the middle of the array L = Left
		R = A[middle:] # everything after the middle array R  = Right

		mergesort(L) # recursion section. sorts the left side first
		mergesort(R)

		i = j = k = 0 # set all the variables that will deal with indices to 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				i += 1

			else:
				A[k] = R[j]
				j += 1

			k +=1

		while i < len(L):	
			A[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			A[k] = R[j]
			j += 1
			k += 1


######################################################################################################
def printL(arr):

	for i in range(len(arr)):
		print(arr[i],end=" ")
	print()

if __name__ == '__main__':
	arr = [32,37,39,36,31,35,38,40,43,16,56,45]
	print ("Given array: ", end="\n")
	printL(arr)
	mergesort(arr)
	print("Sorted Array: ", end="\n")
	printL(arr)
#####################################################################################################	