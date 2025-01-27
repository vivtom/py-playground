'''Function Description
factorial has the following paramter:
int n: an integer
Returns
int: the factorial of n'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()