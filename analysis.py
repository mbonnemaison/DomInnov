#!/usr/bin/python3

import datetime
import dateutil.parser as p
import csv


def read_data(path):
    rows = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        print("ignoring header: {}".format(header))
        for row in reader:
            rows.append((p.parse(row[0], fuzzy=True), row[1] == '1'))
    return rows


def analyze_data(rows):
    prev, is_on = rows[0]
    on_total = datetime.timedelta(0)
    off_total = datetime.timedelta(0)
    for row in rows[1:]:
        curr = row[0]
        duration = curr - prev
        if is_on:
            on_total += duration
        else:
            off_total += duration
        state = "on" if is_on else "OFF"
        print("{} for {} ({}, {})".format(state, duration, prev, curr))
        prev = curr
        is_on = row[1]
    print("total on time: {}".format(on_total))
    print("total off time: {}".format(off_total))


rows = read_data('data_dec_6_2020.csv')
analyze_data(rows)
