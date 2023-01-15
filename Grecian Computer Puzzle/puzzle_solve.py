import itertools

numbers = [
    [[0,0,0,15],[0,0,0,0],[0,0,0,8],[0,0,0,0],[0,0,0,3],[0,0,0,0],[0,0,0,6],[0,0,0,0],[0,0,0,10],[0,0,0,0],[0,0,0,7],[0,0,0,0]],
    [[0,0,0,3],[0,0,7,0],[0,0,15,6],[0,0,0,0],[0,0,0,11],[0,0,14,11],[0,0,0,6],[0,0,9,11],[0,0,0,0],[0,0,12,6],[0,0,0,17],[0,0,4,7]],
    [[0,16,14,5],[0,0,1,0],[0,9,12,7],[0,0,0,8],[0,5,21,9],[0,0,6,13],[0,10,15,9],[0,0,4,7],[0,8,9,13],[0,0,18,21],[0,22,11,17],[0,0,26,4]],
    [[12,2,6,7],[0,13,0,14],[6,9,14,11],[0,0,12,0],[10,17,3,8],[0,19,8,0],[10,3,9,16],[0,12,0,2],[1,3,9,7],[0,26,20,0],[9,6,12,9],[0,0,3,0]],
    [[7,14,11,14],[16,21,12,11],[8,21,13,14],[7,9,14,11],[8,9,15,14],[8,4,4,11],[3,4,5,11],[4,6,6,14],[12,6,7,11],[2,3,8,14],[5,3,9,11],[10,14,10,14]]
    ]

options = [0,1,2,3,4,5,6,7,8,9,10,11]

master = [options,options,options,options,options]
combination = [p for p in itertools.product(*master)]

def rotate(l, n):
    return l[n:] + l[:n]

results = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for chosen in combination:
    count = 0
        
    for r in range(0,5):
        numbers[r] = rotate(numbers[r],chosen[r])

    for column in range(0,12):
        temp = [0,0,0,0]
        
        for num in [3,2,1,0]:
            for wheel in range(0,5):
                
                if numbers[wheel][column][num] == 0:
                    continue
                else:
                    temp[num] = numbers[wheel][column][num]
                    break

        if sum(temp) == 42:   
            count += 1
            continue

    results[count] += 1

print(results)
