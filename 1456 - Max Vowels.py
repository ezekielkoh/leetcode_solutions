
ref = set('aeiou')
testcase = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
list_testcase = list(testcase)

currSum = 0
maxSum = 0
k = 33
p1 = 0

for i in range(k):
    if list_testcase[i] in ref:
        currSum += 1

for i in range(k,len(list_testcase)):
    if list_testcase[p1] in ref:
        currSum -= 1 
    if list_testcase[i] in ref:
        currSum += 1
    p1 += 1
    maxSum = max(maxSum,currSum)

print(maxSum)
    