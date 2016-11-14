import re
import sys
import os
from operator import itemgetter
from datetime import datetime
from collections import OrderedDict


class LogAnalyzer():

    def __init__(self, file):
        self.summary = OrderedDict()
        if os.path.isfile(file):
            self.file = file
        else:
            print(file + " is not file")
            sys.exit(1)

    def parse_file(self):
        with open(self.file, "r") as file:
            for line in file:
                line_array = line.split(" ")
                ip = line_array[0]
                timestamp = line_array[3].strip("[]")
                timestamp = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d")

                request = line_array[5].strip("\"")
                user_agent = line_array[11].strip("\"")

                if timestamp in self.summary:
                    if ip in self.summary[timestamp]:
                        self.summary[timestamp][ip][request] = self.summary[timestamp][ip].get(request, 0) + 1
                    else:
                        self.summary[timestamp][ip] = OrderedDict()
                        self.summary[timestamp][ip][request] = 1
                else:
                    self.summary[timestamp] = OrderedDict()
                    self.summary[timestamp][ip] = OrderedDict()
                    self.summary[timestamp][ip][request] = 1

    def print_summary(self):
        for timestamp, timestamp_dict in self.summary.items():
            print(timestamp + ":")
            for ip, ip_dict in timestamp_dict.items():
                print(" \_" + ip + ":")
                for request_method, number in ip_dict.items():
                    print("   \_" + request_method + ": " + str(number))

if __name__ == "__main__":
    log_analyzer = LogAnalyzer("access_log.1")
    log_analyzer.parse_file()
    log_analyzer.print_summary()
