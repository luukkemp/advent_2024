#!/usr/bin/env python3

input_file = "1.txt"

def solve(in_file):

    num_good_reports = 0
    with open(in_file, "r") as f:
        for line in f:
            report = [int(x) for x in line.split(" ")]
            up = False
            if report[0] < report[1]:
                up = True
            i = 0
            good = True
            print(report)
            if up:
                while i < len(report)-1:
                    if report[i+1] > report[i] + 3 or report[i+1] < report[i] or report[i]==report[i+1]:
                        good = False
                        break
                    i += 1
            else:
                while i < len(report)-1:
                    if report[i+1] < report[i] - 3 or report[i+1] > report[i] or report[i]==report[i+1]:
                        good = False
                        break
                    i += 1
            if good:
                print(good)
                num_good_reports += 1
    print(num_good_reports)

            



if __name__ == "__main__":
    solve(input_file)
