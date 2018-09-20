
# TODO:
# Write a function called skip_gen that returns a list with every
# step variables between the list items, between the start and the
# end values, inclusive.
#
# Arguments:
#   start - the first value in the list
#   end - value that the list can NOT go past
#   step - distance between values
#
# Return:
#   A list with evey step values


def skip_gen(start, end, step):
    # Write your function here:
    return

# TODO:
# Write a function called squares that returns a list with
# the first n  squares
#
# Arguments:
#   n - number of squares
#
# Return:
#   A list with the first n squares


def squares(n):
    # Write your function here:
    return

    #############################################################
    # TESTS BELOW THIS LINE
    # DO NOT TOUCH
    #############################################################


def test_skip_gen():
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [0, 3, 6, 9]
    list3 = [0, 5, 10, 15, 20, 25]

    if list1 == skip_gen(0, 10, 1):
        print("Failed Test")
        return

    if list2 == skip_gen(0, 10, 3):
        print("Failed Test")
        return

    if list3 == skip_gen(0, 25, 5):
        print("Failed Test")
        return

    print("Passed factorial test")


def test_squares():
    list1 = [1, 4, 9]
    list2 = [1, 4, 9, 16, 25]
    list3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

    if list1 == squares(3):
        print("Failed Test")
        return

    if list2 == squares(5):
        print("Failed Test")
        return

    if list3 == squares(12):
        print("Failed Test")
        return

    print("Passed factorial test")


test_skip_gen()
