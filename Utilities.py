

def weightedMean(a1:list, a2:list, d:int):
    '''Returns the weighted mean of two arrays,
     a1 is value being compared.
     a2 is the weight. 
     d is an integer used to determine what decimal place to round to.
    '''
    xi = list(map(int, a1))
    wi = list(map(int, a2))
    dividend, divisor = 0.0, 0
    if len(xi) != len(wi):
        print("The lengths of the two lists are not the same.")
    else:
        size = len(xi)
        for i in range(size):
            dividend += xi[i]*wi[i]
            divisor += wi[i] 
        solution = round(dividend/divisor, d)

        return solution
#weightedMean() Test:
#print(weightedMean([10, 20, 30, 40, 50], [1, 2, 4, 3, 7], 3))

def mean(a:list, d:int):
    size = len(a)
    sum = 0
    for n in range(len(a)):
        sum += a[n]
    mean = round(sum/size, d)
    return mean
#mean() Test:
#print(mean([90,92,87], 2))

def median(a:list):
    l = sorted(a)
    if len(l)%2 == 0:
        median = float(l[len(l)//2 - 1] + l[len(l)//2])/2
    else:
        median = l[(len(l)-1)//2]
    return median
#median() Test:
#print(median([3, 15, 4, 90, 9]))

def mode(a:list):
    mode = 0
    l = sorted(a)
    count, max = 0,0
    current = 0

    for i in l:
        if (i == current):
            count += 1
        else: 
            count = 1
            current = i
        if count > max:
            max = count
            mode = i
    return mode
#mode() Test:
#print(mode([2, 4, 4, 2, 2, 5 ,6]))




def quartiles(size:int, a:list):
    l = sorted(a)
    Q1 = 0
    Q2 = 0
    Q3 = 0
    if size%2 == 0:
        Q1 = round((l[(len(l)//4)-1] + l[(len(l)//4)])/2)
        Q2 = round((l[len(l)//2 - 1] + l[len(l)//2])/2)
        Q3 = round((l[(len(l)*3//4)-1] + l[len(l)*3//4])/2)
    '''
    For some reason python rounds numbers like (14.5) towards the nearest even number: 14
    '''
    else:
        Q1 = int(l[(len(l)//4)-1] + l[(len(l)//4)])//2
        Q2 = l[(len(l)-1)//2]
        l.remove(l[(len(l)//2)])
        Q3 = int(l[(len(l)*3//4)-1] + l[len(l)*3//4])//2
    return Q1, Q2, Q3
#quartiles() Test
'''
print(quartiles(9, [3,7,8,5,12,14,21,13, 18]))
print(quartiles(12, [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]))
print(quartiles(10, [3,7,8,5,12,14,21,15,18,14]))
print(round(14.5))
'''



    

   
