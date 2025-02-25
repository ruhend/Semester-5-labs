
def calcRedundantBits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation
    for i in range(m):
        if(2**i >= m + i + 1):
            return i
1
def calcParityBits(arr, r):
    n = len(arr)
    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j is given since array is reversed
        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr


def detectError(arr, nr):
    n   = len(arr)
    res = 0
    # Calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        # Create a binary no by appending
        # parity bits together.
        res = res + val*(10**i)
    # Convert binary to decimal
    return int(str(res), 2)


def main():
    arr = '10101000100'
    m   = 7
    r   = calcRedundantBits(m)
    arr = calcParityBits(arr, r)
    print("Received data is : " + arr)
    correction = detectError(arr, r)
    if correction:
        print("The position of error is " + str(correction))
    else:
        print("The data received is uncorrupted!")


if __name__ == '__main__':
    main()
