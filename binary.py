'''Given a base- integer,10, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.'''
if __name__ == '__main__':
    n = int(input().strip())
    binary_representation = bin(n)[2:]  
    consecutive_ones = binary_representation.split('0')  
    max_consecutive_ones = max(len(group) for group in consecutive_ones)

    print(max_consecutive_ones)
