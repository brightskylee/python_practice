import re
import sys
from operator import itemgetter

if __name__ == "__main__":
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    if len(sys.argv) < 2:
        sys.stderr.write("argument needed")
        sys.exit(1)

    try:
        distinct_ip_list = {}
        with open(sys.argv[1]) as f:
            for line in f:
                ip_list = pattern.findall(line)
                if ip_list:
                    for ip in ip_list:
                        if not distinct_ip_list.get(ip):
                            distinct_ip_list[ip] = 1
                        else:
                            distinct_ip_list[ip] += 1

        ip_tuple_lists = distinct_ip_list.items()
        print(sorted(ip_tuple_lists, key=itemgetter(1), reverse=True))
    except IOError:
        sys.stderr.write("cannot open file")
        sys.exit(1)


