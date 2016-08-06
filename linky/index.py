#!/usr/bin/env python3

from linky import Link
from linky import helping
import sys


def main():
    arg = str(sys.argv[1:][0])

    l = Link()

    if arg:

        # unlinks
        if arg == "unlink" or arg == "-u":
            l.tear_down()

        # links
        elif arg == "link" or arg == "-l":
            l.create_command()
            l.create_package()
            l.save_options()

        # help
        else:
            helping()


if __name__ == "__main__":
    main()
