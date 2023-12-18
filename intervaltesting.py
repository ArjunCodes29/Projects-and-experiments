# This piece of code was made to investigate the propagation of uncertainty during the standard method of calculating uncertainty in physics
# Our teacher simply told us "When multiplying to values with their own uncertainties, add the percentage uncertainties to find the resulting uncertainty"
# A quick example then, while multiplying (1,3) * (1,3) we get (1,9) but using the physics method we get (0,8)
# I was not sure why this difference existed so the following python codes sets up the neccesary interval arithmetic and then looks into the 
# difference in the two methods of multiplying uncertainty
# "            product_percent = mul_percent(interval_a,interval_b)
#           product_normal = mul_interval_fast(interval_a,interval_b) " these are the two functions in question

# Most of this code is copied from someone else- my work starts at 439

# The fruit of analysis was that - the physical method of finding uncertainty is a very good approximation for real uncertainty
# it does however break down with small numbers and high amounts of uncertainty

# this article by MIT explains this - http://web.mit.edu/fluids-modules/www/exper_techniques/2.Propagation_of_Uncertaint.pdf





def str_interval(x):
    """Return a string representation of interval x.
    
    >>> str_interval(make_interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(make_interval(-1, 2), make_interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))



"""Alyssa's program is incomplete because she has not specified the
implementation of the interval abstraction. Define the constructor and selectors
in terms of two_element tuples.
"""


# DONE

def make_interval(a, b):
    """Construct an interval from a to b."""
    return (a,b)
    
def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]
    
def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]
    
"""Alyssa implements division below, by multiplying by the reciprocal of y. Ben
Bitdiddle, an expert systems programmer, looks over Alyssa's shoulder and
comments that it is not clear what it means to divide by an interval that spans
zero. Add an assert statement to Alyssa's code to ensure that no such interval
is used as a divisor.
"""

# DONE

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-0.25 to 0.5'
    """
    # assert that interval does not contain zero
    assert 0 < lower_bound(y) or 0 > upper_bound(y), 'Zero contained in divisor interval, division undefined.'

    reciprocal_y = make_interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

"""Using reasoning analogous to Alyssa's, define a subtraction function for
intervals.  Add a doctest.
"""

# DONE

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> sub_interval(make_interval(1,2), make_interval(-5,-1))
    (2, 7)
    """
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return(make_interval(lower, upper))
    
"""In passing, Ben also cryptically comments, "By testing the signs of the
endpoints of the intervals, it is possible to break mul_interval into nine
cases, only one of which requires more than two multiplications."  Write a
fast multiplication function using Ben's suggestion.  Add a doctest.
"""

# DONE

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(make_interval(-2, 4), make_interval(1, 2)))
    '-4 to 8'

    """
    if upper_bound(y) < 0:
        if lower_bound(x) < 0:
            upper = lower_bound(x)*lower_bound(y)
        else:
            upper = lower_bound(x)*upper_bound(y)
            
        if upper_bound(x) < 0:
            lower = upper_bound(x)*upper_bound(y)
        else:
            lower = upper_bound(x)*lower_bound(y)
            
            
    elif lower_bound(y) >= 0:
        if upper_bound(x) < 0:
            upper, lower = upper_bound(x)*lower_bound(y), lower_bound(x)*upper_bound(y)
        else:
            upper, lower = upper_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y)
    
    else:
        if abs(lower_bound(y)) > abs(upper_bound(y)):
            if lower_bound(x) >= 0:   
                upper, lower = upper_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y)
            elif upper_bound(x) < 0:
                upper, lower = lower_bound(x)*lower_bound(y), lower_bound(x)*upper_bound(y)
            else:
                if abs(lower_bound(x)) <= abs(upper_bound(x)):
                    upper, lower = max(lower_bound(x)*lower_bound(y), 
                                       upper_bound(x)*upper_bound(y)), upper_bound(x)*lower_bound(y)
                else:
                    upper, lower = lower_bound(x)*lower_bound(y), min(lower_bound(x)*upper_bound(y),
                                               upper_bound(x)*lower_bound(y))
        else:
            if lower_bound(x) >= 0:
                upper, lower = upper_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y)
            elif upper_bound(x) < 0:
                upper, lower = lower_bound(x)*lower_bound(y), lower_bound(x)*upper_bound(y)
            else:
                if abs(lower_bound(x)) <= abs(upper_bound(x)):
                    upper, lower = upper_bound(x)*upper_bound(y), min(lower_bound(x)*upper_bound(y), 
                                               upper_bound(x)*lower_bound(y))
                else:
                    upper, lower = max(lower_bound(x)*lower_bound(y), 
                                       upper_bound(x)*upper_bound(y)), lower_bound(x)*upper_bound(y)
    # return the resulting interval
    return(make_interval(lower, upper))


"""After debugging her program, Alyssa shows it to a potential user, who
complains that her program solves the wrong problem. He wants a program that can
deal with numbers represented as a center value and an additive tolerance; for
example, he wants to work with intervals such as 3.5 +/- 0.15 rather than 3.35
to 3.65. Alyssa returns to her desk and fixes this problem by supplying an
alternate constructor and alternate selectors in terms of the existing ones:
"""

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return make_interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

"""Unfortunately, most of Alyssa's users are engineers. Real engineering
situations usually involve measurements with only a small uncertainty, measured
as the ratio of the width of the interval to the midpoint of the interval.
Engineers usually specify percentage tolerances on the parameters of devices.

Define a constructor make_center_percent that takes a center and a percentage
tolerance and produces the desired interval. You must also define a selector
percent that produces the percentage tolerance for a given interval. The center
selector is the same as the one shown above.
"""

# DONE

def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.
    
    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    upper = c + abs(c)*p/100
    lower = c - abs(c)*p/100
    return make_interval(lower, upper)

# DONE

def percent(x):
    """Return the percentage tolerance of interval x.
    
    >>> percent(make_interval(1, 3))
    50.0
    """
    return width(x)/center(x)*100

"""After considerable work, Alyssa P. Hacker delivers her finished system.
Several years later, after she has forgotten all about it, she gets a frenzied
call from an irate user, Lem E. Tweakit. It seems that Lem has noticed that the
formula for parallel resistors can be written in two algebraically equivalent
ways:

    (r1 * r2) / (r1 + r2)

    and

    1 / (1/r1 + 1/r2)

He has written the following two programs, each of which computes the
parallel_resistors formula differently:
"""

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

"""Lem complains that Alyssa's program gives different answers for the two ways
of computing. This is a serious complaint.

Demonstrate that Lem is right. Investigate the behavior of the system on a
variety of arithmetic expressions. Make some intervals A and B, and use them in
computing the expressions A/A and A/B. You will get the most insight by using
intervals whose width is a small percentage of the center value.
"""

# DONE

def prove_lem_right():
    A = make_interval(1, 2)
    B = make_interval(1, 1)
    
    return str_interval(par1(A,B)), str_interval(par2(A,B))

"""Eva Lu Ator, another user, has also noticed the different intervals computed
by different but algebraically equivalent expressions. She says that the problem
is multiple references to the same interval.

The Multiple References Problem: a formula to compute with intervals using
Alyssa's system will produce tighter error bounds if it can be written in such a
form that no variable that represents an uncertain number is repeated. 

Thus, she says, par2 is a better program for parallel resistances than par1. Is
she right? Why? Write an explanation as a string below.
"""

# DONE

'''She is correct. In par1, each interval is referenced twice, which allows the
function to 'choose' different values for each instance of the interval. For
example, an interval x [-1,2] in x^2 + x can take on values from 0 to 6 when x
is fixed (as it is in normal arithmetic), but using interval multiplication 
gives us [-1,2]*[-1,2] + [-1,2] = [-2, 4] + [-1, 2] = [-3, 6].'''


"""Write a function quadratic that returns the interval of all values f(t) such
that t is in the argument interval x and 

f(t) = a * t * t + b * t + c

Make sure that your implementation returns the smallest such interval, one that
does not suffer from the multiple references problem.

Hint: the derivative f'(t) = 2 * a * t + b, and so the extreme point of the
quadratic is -b/(2*a).
"""

# DONE

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b, and
    c, for domain interval x.

    >>> str_interval(quadratic(make_interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(make_interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def extreme_point(a, b, c):
        return -b/(2*a)
    
    if a > 0: # extreme point will be a minima
        if extreme_point(a, b, c) >= lower_bound(x) and extreme_point(a, b, c) <= upper_bound(x): 
            
            lower = a * extreme_point(a, b, c) ** 2 + b * extreme_point(a, b, c) + c
            
            upper = max(a * upper_bound(x) ** 2 + b * upper_bound(x)  + c,
                        a * lower_bound(x) ** 2 + b * lower_bound(x)  + c)
                                     
        elif extreme_point(a, b, c) < lower_bound(x):
             
             lower = a * lower_bound(x) ** 2 + b * lower_bound(x) + c
             upper = a * upper_bound(x) ** 2 + b * upper_bound(x) + c
                                    
        else: # extreme_point(a, b, c) > upper_bound(x)
             upper = a * lower_bound(x) ** 2 + b * lower_bound(x) + c
             lower = a * upper_bound(x) ** 2 + b * upper_bound(x) + c    
         
    elif a < 0: # extreme point will be a maxima 

        if extreme_point(a, b, c) >= lower_bound(x) and extreme_point(a, b, c) <= upper_bound(x): 

            upper = a * extreme_point(a, b, c) ** 2 + b * extreme_point(a, b, c) + c
            
            lower = min(a * upper_bound(x) ** 2 + b * upper_bound(x)  + c,
                        a * lower_bound(x) ** 2 + b * lower_bound(x)  + c)
        
        elif extreme_point(a, b, c) < lower_bound(x):
             
             lower = a * upper_bound(x) ** 2 + b * upper_bound(x) + c
             upper = a * lower_bound(x) ** 2 + b * lower_bound(x) + c
                                    
        else: # extreme_point(a, b, c) > upper_bound(x)
             upper = a * upper_bound(x) ** 2 + b * upper_bound(x) + c
             lower = a * lower_bound(x) ** 2 + b * lower_bound(x) + c       
            
    else: # function is linear, min and max of intervals will be the endpoints
        
        upper = max(b * upper_bound(x) + c, b * lower_bound(x) + c)
        lower = min(b * upper_bound(x) + c, b * lower_bound(x) + c)
        
    return make_interval(lower, upper)
        
"""Write three similar functions, each of which takes as an argument a sequence
of intervals and returns the sum of the square of each interval that does not
contain 0.

    1. Using a for statement containing an if statement.
    2. Using map and filter and reduce.
    3. Using generator expression and reduce.

Hint: Square is a special case of quadratic, but you can also use the simpler
square_interval function below for intervals that do not contain 0.
"""

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

# DONE

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    ans = make_interval(0, 0) # initialize answer
    
    for interval in seq: # loop over all intervals
        
        if non_zero(interval) is True: # if the interval does not contain zero
            ans = add_interval(ans, square_interval(interval)) # add the square
    
    return ans
                
# DONE

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
    
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    
    return reduce(sum, map(square_interval, filter(non_zero, seq)))
    
# DONE

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.
    
    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """

    return reduce(sum, (square_interval(interval) for interval in seq if non_zero(interval)))












#arjuns work

def mul_percent(a,b):
    c = center(a)*center(b)
    p = percent(a)+percent(b)
    return make_center_percent(c,p)

def comparer(a,b):
    if lower_bound(a)==lower_bound(b) and upper_bound(a)==upper_bound(b):
        print('True ' + str_interval(a) + ' and ' + str_interval(b))
        return True
    else:
        print('False ' + str_interval(a) + ' : ' + str_interval(b))
        return False

def comparerpercent(a,b):
    if percent(a)==percent(b):
        print('True ' + percent(a) + ' and ' + percent(b))
        return True
    else:
        print('False '  + str(percent(a)) + ' and ' + str(percent(b)))
        return False

def mullertester(x,y):
    for a in range(9999999,x):
        for b in range(99999999,y):
            interval_a = make_center_percent(a,1)
            interval_b = make_center_percent(b,1)
            # print(interval_a,interval_b)
            # print(str_interval(mul_interval_fast(interval_a,interval_b)))
            # print('--')
            print(str_interval(interval_a) + " times " + str_interval(interval_b))
            product_percent = mul_percent(interval_a,interval_b)
            product_normal = mul_interval_fast(interval_a,interval_b)
            comparer(product_normal,product_percent)
            comparerpercent(product_normal,product_percent)
            print('--')

mullertester(99999991,999999991)
