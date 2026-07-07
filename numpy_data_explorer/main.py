import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

print("\nFirst Element:", arr[0])

    
print("Slice:", arr[1:4])

# Mathematical Operations
print("\nAddition:", arr + 10)
print("Multiplication:", arr * 2)

# Statistics
print("\nMean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Reshape
new_arr = arr.reshape(5,1)
print("\nReshaped Array:")
print(new_arr)

# Save
np.savetxt("output/result.txt", arr)
print("\nSaved Successfully")