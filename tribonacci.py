def tribonacci(signature,n):
    for i in range(1,n):
        signature.append(sum(signature[-3:]))
    return signature[0:n]
