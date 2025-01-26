''' Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers. '''

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    i = len(arr) - 1
    while i >= 0:
        print(arr[i], end= ' ')
        i -= 1