#!/usr/bin/env python3

input_file = "1.txt"

def verify(report):
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
    return good

def dampner(report):
    i = len(report) -1
    while i >= 0:
        _r = report[:]
        _r.pop(i)
        if verify(_r):
            return True
        i -= 1
    return False


def solve(in_file):

    num_good_reports = 0
    with open(in_file, "r") as f:
        for line in f:
            report = [int(x) for x in line.split(" ")]
            good = verify(report)
            if good:
                num_good_reports += 1
            else:
                if dampner(report):
                    num_good_reports += 1
    print(num_good_reports)

            



if __name__ == "__main__":
    solve(input_file)
