#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    plural = "s" if num_args != 1 else ""

    print("{} argument{}:".format(num_args, plural))

    for i in range(1, len(argv)):
        print("{0}: {1}".format(i, argv[i]))
