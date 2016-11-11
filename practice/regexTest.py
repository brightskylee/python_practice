import re
import sys

if __name__ == "__main__":
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    if len(sys.argv) < 2:
        sys.stderr.write("argument needed")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            for line in f:
                ip_list = pattern.findall(line)
                if ip_list:
                    print(ip_list)
    except IOError:
        sys.stderr.write("cannot open file")
        sys.exit(1)


