# hey essentially i wanted to find how much free time i would have in school because i had free periods surrounding a lunch break
# there were 4 continous free period blocks starting at 11 45 and ending at 2 35
# i was too lazy to do  the mental math to find the amt of free time i would have
# there was a website https://www.easysurf.cc/tspan-s.htm which tried to solve this issue but i didnt like the way it did it
# so i made my own python code to do this
# essentially it asks you to input two numbers in 24 hr format (without the colons just a 4 digit number) and it doesnt matter in what order you put the time it tells you the difference in hrs and mins between the two 
#events
# this works for any 2 times in a day .
#caveat is you must enter time in a specif way ie 2:35 pm because 1435

def split(a): # a helper function
    ''' 
    Given a 4 digit number, returns the first two and last two numbers seperately

    >>> split(1210)
    (12, 10)
    '''
    min = a % 10 + 10 * ((a//10)%10)
    hr = ((a//100)%10) + 10 * ((a//1000)%10)
    return hr,min
def diff(a,b): #finds the difference in hours and minutes between two tiimes (24 hour format)
    '''
    Given 2 formatted 24 hour times in the same day, returns the difference in time between them

    >>> diff(1200,1430)
    2 30
    '''
    a_hr, a_min = split(a)
    b_hr, b_min = split(b)
    if b_hr== a_hr:
        print (abs(a_min- b_min))
    if b_hr>a_hr:
        diff_min = b_min - a_min
        if diff_min < 0:
            diff_min = 60 + diff_min
            diff_hr = b_hr -1 - a_hr
            print(diff_hr,diff_min)
        else:
            diff_hr = b_hr-a_hr
            print(diff_hr,diff_min)
    else:
        diff_min = a_min - b_min
        if diff_min < 0:
            diff_min = 60 + diff_min
            diff_hr = a_hr -1 - b_hr
            print(diff_hr,diff_min)
        else:
            diff_hr = a_hr-b_hr
            print(diff_hr,diff_min)
