#Constant Complexity: O(1)
def ConstantComplexity():
    print ("Hello")
    return ""

#Linear Complexity: O(n)
def LinearComplexity(array1):
    for i in array1:
        print(i)
    return ""

#Quadratic Complexity: O(N²)
def QuadraticComplexity(array2):
    for i in array2:
        for j in i:
            print(j)
    return ""

#Exponential: O(2^N)
def Exponential(fibbonaci):

    if fibbonaci <= 1:
        return fibbonaci
    
    else:
        return Exponential(fibbonaci - 2) + Exponential(fibbonaci - 1)

#Logarithmic Complexity: O(log n)
def LogarithmicComplexity(array1, number):
    
    #Binary Search
    low = 0
    high = len(array1) - 1
    answer = 0
    
    while low <= high:

        mid = low + high // 2

        if array1[mid] < number:
            low = mid - 1

        elif array1[mid] > number:
            high = mid - 1
            
        else:
            return mid
           
    


array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
number = 8
fibbonaci = 8

print("Constant Complexity:")
print(ConstantComplexity())
print("Linear Complexity:")
print(LinearComplexity(array1))
print("QuadraticComplexity:")
print(QuadraticComplexity(array2))
print("Exponential:")
print(Exponential(fibbonaci))
print("Logarithmic Complexity:")
print(LogarithmicComplexity(array1, number))





