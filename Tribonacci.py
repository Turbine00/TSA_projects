length = 8
start_array = [1, 1, 1]


def tribonacci(signature, length):

    if length == 0:
        return []
    elif length == 1:
        return signature[0:1]
    elif length == 2:
        return signature[0:2]
    elif length == 3:
        return signature[0:3]
    else:
        i = 4
        while i <= length:
            signature.append(signature[i-4] + signature[i-3] + signature[i-2])
            i = i + 1
        return signature


print(tribonacci(start_array, length))
