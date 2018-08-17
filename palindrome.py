from Deque import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    if char_deque.size() == 0 or char_deque.size() == 1:
        return True
    if char_deque.remove_front() is char_deque.remove_rear():
            return pal_checker(a_string[1:len(a_string) - 1])
    else:
        return False
    # still_equal = True
    #
    # while char_deque.size() > 1 and still_equal:
    #     first = char_deque.remove_front()
    #     last = char_deque.remove_rear()
    #     if first != last:
    #         still_equal = False
    #
    #     return still_equal

def stringToDeque(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)
    return char_deque


def pal_chekcer2(a_deque):
    if a_deque.size() < 2:
        return True
    if a_deque.remove_front() is a_deque.remove_rear():
        pal_chekcer2(a_deque)
    else:
        return False

print(pal_checker("lsdkjsfkf"))
print(pal_checker("radar"))

print(pal_chekcer2(stringToDeque("radar")))
