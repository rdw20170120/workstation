#!/usr/bin/env python

"""
score.py will do the following tasks.

1. Calculate the total score for each exam item
   and writes into a output file.
"""

import csv
import os
import sys
import glob
import re
from certtools import args_parse
from certtools.couchbase.utils import common


class Q():
    args = args_parse(args=sys.argv)
    input_dir = args.seg1
    checks_weight_file = args.seg2
    output_file = args.seg3
    weights_dict = {}
    debug = args.debug if hasattr(args, 'debug') else 0


def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s


def alphanum_key(s):
    return [tryint(c) for c in re.split('([0-9]+)', s)]


def sort_nicely(l):
    return sorted(l, key=alphanum_key)


def parse_weight_file(file):
    ''' ROB: It seems to me that an IOError should be allowed to stop the script, rather than be
        swallowed.  Is there a reason to swallow this error?
    '''
    weights_dict = {}
    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='=', quotechar='|')
            for row in reader:
                weight_key = row[0].strip().replace(" ", "-")
                weight_value = float(row[1].strip())
                if not (weight_value >= -100 and weight_value <= 100):
                    raise common.GeneralException(
                        "{0}: score weight are outside the range of -100"
                        " and +100".format(weight_value)
                    )
                weights_dict[weight_key] = weight_value
            return weights_dict
    except IOError:
        return weights_dict


def generate_key(*args):
    return '-'.join(args)


def generate_keys(check_num, exam_item_num, task_num):
    keys = []
    keys.append(generate_key(check_num, exam_item_num, task_num))
    keys.append(generate_key(check_num, exam_item_num))
    keys.append(generate_key(check_num, task_num))
    keys.append(check_num)
    return keys


def get_weight(check_num, exam_item_num, task_num):
    for key in generate_keys(check_num, exam_item_num, task_num):
        if key in Q.weights_dict:
            return Q.weights_dict[key]
    return 1.00


def get_task_msg(input_file, outfile):
    file_path, file_name = os.path.split(input_file)
    file_name = os.path.splitext(file_name)[0].split("-")
    task_num = file_name[0]
    exam_item_num = file_name[1]
    task_score = 0
    with open(input_file) as infile:
        for line in infile:
            if 'SCORE' in line:
                tmp_check_score = line.split("=")
                check_score = int(tmp_check_score[1].split(":")[0].strip())
                check_num = tmp_check_score[1].split(":")[1].strip()
                check_weight_score = 0
                if check_score != 0:
                    weight_check = get_weight(check_num, exam_item_num,
                                              task_num)
                    check_weight_score = weight_check * check_score
                    task_score += check_weight_score
                if int(Q.debug) == 1:
                    outfile.write(
                        "DEBUG: {0} {1} {2} = {3} : {4}"
                        .format(check_num, exam_item_num, task_num,
                                check_score, check_weight_score)
                    )
                    outfile.write("\n")
    task_num = re.sub(r'([0-9]+)', r'=\1', task_num)
    exam_item_num = re.sub(r'([0-9]+)', r'=\1', exam_item_num)
    return task_score, "{0} {1} score={2}".format(task_num, exam_item_num,
                                                  task_score)


def main():
    Q.weights_dict = parse_weight_file(Q.checks_weight_file)
    # Read the input files
    input_file_list = sort_nicely(
                      glob.glob(os.path.join(Q.input_dir, '*.out'))
    )
    total_exam_score = 0
    with open(Q.output_file, "w+") as outfile:
        for input_file in input_file_list:
            task_score, msg_line = get_task_msg(input_file, outfile)
            total_exam_score += task_score
            outfile.write(msg_line)
            outfile.write("\n")
        outfile.write("\n")
        outfile.write("TOTAL score={0}".format(total_exam_score))
        outfile.write("\n")


if __name__ == '__main__':
    sys.exit(main())

