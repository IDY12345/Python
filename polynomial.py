def polynomial_multiplication(P, Q):
    m = len(P)
    n = len(Q)
    result = [0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            result[i+j] += P[i]*Q[j]
    return result
# function that print polynomial
def polynomial(poly):
    n = len(poly)
    for i in range(n): 
        print(poly[i], end = "")
        if (i != 0): 
            print("x^", i, end = "") 
        if (i != n - 1): 
            print(" + ", end = "")
# polynomial in array representation
P = [2, 3, 0, 4]
print("First polynomial is:")
polynomial(P)
print('\n')
Q = [1, 2, 4, 5]
print("Second polynomial is: ")
polynomial(Q)
print('\n')
result = (polynomial_multiplication(P, Q))
print("Product of polynomials is: ")
polynomial(result)