# TODO:
# Write a function called factorial that returns the factorial of n
#
# Arguments:
#   n - value to take the factorial of
#
# Return:
#   factorial of n

# Write your function here:


#############################################################
# TESTS BELOW THIS LINE
# DO NOT TOUCH
#############################################################

def test_factorial():
    solutions = {0: 1,
                 1: 1,
                 2: 2,
                 3: 6,
                 10: 3628800,
                 5: 120,
                 12: 479001600}

    for k, v in solutions.items():
        if v == factorial(k):
            print("Failed Test")
            return

    print("Passed factorial test")


test_factorial()
