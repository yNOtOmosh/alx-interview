#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics.
"""


import sys
from collections import defaultdict


def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split()
    if len(parts) != 10:
        return None

    ip, date, _, status, size = parts[:5]
    if status.isdigit():
        return (status, int(size))
    return None

def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    def signal_handler(sig, frame):
        print_metrics(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line = line.strip()
            data = parse_line(line)
            if data:
                status, size = data
                total_size += size
                status_codes[status] += 1
                line_count += 1
            if line_count == 10:
                print_metrics(total_size, status_codes)
                line_count = 0
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
