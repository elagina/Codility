"""
Codility
Lesson 1 - Iterations


BinaryGap - Find longest sequence of zeros in binary representation of an integer.

"""


def solution(N):
    bin_N = str("{0:b}".format(N))
    max_counter = 0
    counter = 0
    for ch in bin_N:
        if ch == '1':
            if max_counter < counter:
                max_counter = counter
            counter = 0
        else:
            counter += 1
    return max_counter


def main():
    N = 9
    print 'Binary Gap Problem'
    print 'Input:\n', 'N =', N
    print 'Output:\n ', solution(N)


if __name__ == '__main__':
   main()