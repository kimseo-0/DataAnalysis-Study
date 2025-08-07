def split_number(n, s, c, answer, path=[]):
    if n == 1:
        answer.append(path + [s])
        return
    
    for i in range(1, int(s / 2) + 1):
        split_number(n - 1, s - i, c, answer, path + [i])

# 예시
answer = []
split_number(4, 5, 4, answer)
print(answer)

def split_number1(n, s, c):
    if n == 1:
        if s >= 1:
            return [[s]]
        else:
            return []

    results = []
    for i in range(1, int(s / 2) + 1):
        for rest in split_number(n - 1, s - i, c):
            results.append([i] + rest)

    return results

answer = []

def split_number2(n, s, c):
    result = []
    
    if n == 1:
        return [s]
    
    for i in range(1, int(s / 2) + 1):
        result = [i]
        result.extend(split_number(n - 1, s - i, c))

        if n == c:
            answer.append(result)
        
    return result