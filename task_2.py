from collections import deque


def is_palindrome(string):
    deq = deque(string.lower().strip())

    while len(deq) > 1:
        left = deq.popleft()
        right = deq.pop()

        if left != right:
            print("Not a palindrome")
            return False

    print("It's a palindrome")
    return True


is_palindrome("pop pop")
is_palindrome("hello world")
