# TODO:
# Write a function logic1 that takes 2 boolean values and returns
# True or False based on the value of the booleans fed in.
#
# Use the following sentance to determine the function's logic:
# This value can only be true if n1 and n2 are true
#
# Arguments:
#   n1 - first boolean
#   n2 - second boolean
#
# Return:
#   The logical evaluation of the expression

# Write your function here:


# TODO:
# Write a function logic2 that takes 3 boolean values and returns
# True or False based on the value of the booleans fed in.
#
# Use the following sentance to determine the function's logic:
#   This value can only be true if n1 is true, and either n2 is true
#   and n3 is false or n3 is true and n2 is false.
#
# Arguments:
#   n1 - first boolean
#   n2 - second boolean
#   n3 - third boolean
#
# Return:
#   The logical evaluation of the expression

# Write your function here:

#############################################################
# TESTS BELOW THIS LINE
# DO NOT TOUCH
#############################################################

def test_logic1():
    if not logic1(True, True):
        print("Failed Test")
        return

    if logic1(True, False):
        print("Failed Test")
        return

    if logic1(False, True):
        print("Failed Test")
        return

    if logic1(False, False):
        print("Failed Test")
        return

    print("Passed logic 1 test")


def test_logic2():
    if not logic2(True, True, False):
        print("Failed Test")
        return

    if not logic2(True, False, True):
        print("Failed Test")
        return

    if logic2(False, True, True):
        print("Failed Test")
        return

    if logic2(False, False, False):
        print("Failed Test")
        return

    print("Passed logic 1 test")


test_logic1()
test_logic2()
