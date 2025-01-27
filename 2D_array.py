'''Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.'''
arr = []
for _ in range(6):
    row = list(map(int, input().strip().split()))
    if len(row) != 6:  
        raise ValueError("Each row must contain exactly 6 integers.")
    arr.append(row)


if len(arr) != 6:  
    raise ValueError("The input must contain exactly 6 rows.")


max_sum = -float('inf')


for i in range(4):  
    for j in range(4):  

        hourglass_sum = (
            arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
            arr[i+1][j+1] +                          # Middle element
            arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
        )

        max_sum = max(max_sum, hourglass_sum)


print(max_sum)