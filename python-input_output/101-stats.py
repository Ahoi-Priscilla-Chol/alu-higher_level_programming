#!/usr/bin/python3
"""Reads stdin line by line and computes log metrics."""
import sys


def print_stats(total_size, status_codes):
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue

            file_size = parts[-1]
            status_code = parts[-2]

            try:
                total_size += int(file_size)
            except ValueError:
                continue

            if status_code in valid_codes:
                status_codes[status_code] = (
                    status_codes.get(status_code, 0) + 1
                )

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    else:
        print_stats(total_size, status_codes)
