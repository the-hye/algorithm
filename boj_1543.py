n = input()
test = input()
result = 0
i = 0

while i<=len(n):
    
    if test == n[i:i+len(test)]:
        result += 1
        i = i + len(test)
        
    else :
        i = i + 1
        
print(result)
