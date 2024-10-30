#!/usr/bin/python3
import sys


def print_statistics(total_size, status_counts):
    """Prints the accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def process_logs():
    """Reads stdin line by line and computes metrics"""
    total_size = 0
    status_counts = {}
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()

            # Ensure the log line has the correct format
            if len(parts) < 9:
                continue

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if status_code in valid_status_codes:
                    status_counts[status_code] = (
                        status_counts.get(status_code, 0) + 1
                    )

                total_size += file_size
                line_count += 1
            except ValueError:
                continue

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise

    print_statistics(total_size, status_counts)


if __name__ == "__main__":
    process_logs()
