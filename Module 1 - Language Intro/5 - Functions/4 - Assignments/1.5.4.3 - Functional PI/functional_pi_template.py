import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

    a = 1
    b = 1/math.sqrt(2)
    t = 1/4
    p = 1

    for i in range(1, 11):
        """
        Step 2: Update each variable based upon the algorithm. Take care to ensure
        the order of operations and dependencies among calculations is respected. You
        may wish to create new "temporary" variables to hold intermediate results
        """
     ### YOUR CODE HERE ###
        a2 = (a + b)/2
        b2 = math.sqrt(a * b)
        t2 = t - p * (a - a2) ** 2
        p2 = (2 * p)

    #updated variables
        a = a2
        b = b2
        t = t2
        p = p2
    # change this so an actual value is returned
    pi_estimate = ((a+b) ** 2) / (4*t)
    return pi_estimate



desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
