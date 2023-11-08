#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(total_size, status_counts):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated read file size.
        status_counts (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    import sys

    size = 0
    statuses = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, statuses)
                count = 1
            else:
                count += 1

            elements = line.split()

            try:
                size += int(elements[-1])
            except (IndexError, ValueError):
                pass

            try:
                if elements[-2] in codes:
                    if statuses.get(elements[-2], -1) == -1:
                        statuses[elements[-2]] = 1
                    else:
                        statuses[elements[-2]] += 1
            except IndexError:
                pass

        print_stats(size, statuses)

    except KeyboardInterrupt:
        print_stats(size, statuses)
        raise
