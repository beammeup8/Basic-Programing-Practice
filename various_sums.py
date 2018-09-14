# TODO:
# Write a function called sum_m_to_n that sums all values from
# the value m to the value n this is an inclusive range, so
# include the end points.
#
# Arguments:
#   n - the end value
#   m - the start value
#
# Return:
#   the sum of all values between m and n

# Write your function here:

# TODO:
# Write a function called sum_m_to_n_step_r that sums every r value from
# the value m to the value n this is an inclusive range, so
# include the end points.
#
# Arguments:
#   n - the end value
#   m - the start value
#   r - step between values to sum
#
# Return:
#   the sum of all values between m and n

# Write your function here:

#############################################################
# TESTS BELOW THIS LINE
# DO NOT TOUCH
#############################################################


def test_sum_m_to_n():
    solutions = {(0, 0): 0,
                 (0, 1): 1,
                 (0, 2): 3,
                 (4, 10): 49,
                 (3, 5): 12,
                 (5, 14): 95}

    for k, v in solutions.items():
        if v == sum_m_to_n(k[0], k[1]):
            print("Failed Test")
            return

    print("Summed all m to n succesful.")


test_sum_m_to_n()


def test_sum_m_to_n_step_r():
    solutions = {(0, 0, 1): 0,
                 (0, 1, 3): 0,
                 (0, 2, 2): 2,
                 (4, 10, 2): 28,
                 (3, 15, 3): 45,
                 (5, 14, 7): 17}

    for k, v in solutions.items():
        if v == sum_m_to_n_step_r(k[0], k[1], k[2]):
            print("Failed Test")
            return

    print("Summed all m to n succesful.")


test_sum_m_to_n_step_r()
