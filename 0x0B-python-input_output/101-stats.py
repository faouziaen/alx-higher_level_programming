#!/usr/bin/python3
import sys


def print_metrics(total_size, status_codes):
    """
    Prints metrics based on the provided data.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status code counts.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count:
            print("{}: {}".format(code, count))


line_count = 0
total_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}


try:
    for line in sys.stdin:
        line_count += 1
        elements = line.split()
        if len(elements) > 2:
            total_size += int(elements[-1])
            status = elements[-2]
            if status in status_codes:
                status_codes[status] += 1

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
    raise
