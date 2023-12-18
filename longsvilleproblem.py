# This was some code i made to help me solve a problem from Atlas's application
## In Linesville, every resident lives on Main St., a long, straight road. The Linesville City Council decides to build a garden,
#  and wants to build it in the place that minimizes the sum of the squares of the distances to the residents of Linesville.
## Where should the garden be built?
## This program takes in a list of 10 numbers (the number of people livingin each house) and returns a list of 10 numbers ( the total sum of squares at if the garden was built at each location)

#This experiment gave me the confidence that most configurations will be u-shaped so as long as i am going down the curve
# I am reaching the optimal garden building point.
import random
import math



def calculator(list,position):
    copy = position
    sum = 0
    while(position<(len(list) -1)):
        position= position + 1
        sum = sum + list[position] * ((position - copy) * (position - copy))
    copy2 = copy
    while(copy > -1):
        copy =copy-1
        sum= sum + list[copy] * ((copy2 -copy) * (copy2 -copy))
    return sum


def get_minvalue(inputlist):
 
    #get the minimum value in the list
    min_value = min(inputlist)
 
    #return the index of minimum value 
    min_index=inputlist.index(min_value)
    return min_index

def checkUshaped(list):
    min = get_minvalue(list)
    position_min = min[0]
    i=position_min
    while(i<(len(list)-1)):
        if(list[i]>list[i+1]):
            print("false here")
            return False
        i += 1
    ii = position_min
    while(ii>0):
        if(list[ii]>list[ii - 1]):
            print("false there")
            return False
        ii = ii - 1
    
    return True


def optimalSolution(randomlist):
    n = random.randint(0,14)
    copy = n
    total = 0
    while(copy<(len(randomlist) -1)):
        copy += 1
        total += randomlist[copy]* (copy - n)
    copy2 = n
    while(copy2 > -1):
        copy2 -= 1
        total -= randomlist[copy2]* (n - copy2)
    movementRequired= total/sum(randomlist)
    return n+movementRequired

##for i in range(50):
   ## randomlist = random.sample(range(0, 15), 15)
    ##answer = randomlist[:]
    ##for count,value  in enumerate(randomlist):
        ##answer[count]= calculator(randomlist,count)
    ##print(get_minvalue(answer))
    ##print(optimalSolution(randomlist))
    ##print("--")

def leftr(n):
    randomlist = random.sample(range(0, 15), 15)
    answer = randomlist[:]
    for count,value  in enumerate(randomlist):
        answer[count]= calculator(randomlist,count)
    copy = n
    totalRight = 0
    totalLeft =0
    while(copy<(len(randomlist) -1)):
        copy += 1
        totalRight += randomlist[copy]* (copy - n)
    copy2 = n
    while(copy2 > -1):
        copy2 -= 1
        totalLeft += randomlist[copy2]* (n - copy2)
    return [totalLeft,totalRight, optimalSolution(randomlist)]

def StansTrickery(randomlist):
    n = random.randint(0,15)
    listlist = leftr(n)
    difference = listlist[1]-listlist[0]
    if(difference>0):
        reportedLocation = n + math.sqrt(abs(difference))
    else:
        reportedLocation = n - math.sqrt(abs(difference))
    return (reportedLocation,n)

randomlist = random.sample(range(0, 15), 15)
print(randomlist)
print(StansTrickery(randomlist))
stansFakelist = [12, 11, 4, 10, 14, 7, 1, 2, 5, 0, 8, 13, 9, 6, 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
print(optimalSolution(stansFakelist))