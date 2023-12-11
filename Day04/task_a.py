#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)


Cards = dict()

total_score=0

for l in file:
    print(l.strip())
    card_number = int(l.split(":")[0].split(" ")[-1])
    ticket_numbers_raw = l.split(":")[1].split("|")[0].split(" ")
    ticket_numbers = list()
    for t in ticket_numbers_raw:
        try:
            ticket_numbers.append(int(t))
        except Exception:
            pass
    winning_numbers_raw = l.split(":")[1].split("|")[1].split(" ")
    winning_numbers = list()
    for t in winning_numbers_raw:
        try:
            winning_numbers.append(int(t))
        except Exception:
            pass
    print(card_number)
    print(ticket_numbers)
    print(winning_numbers)
    score = 0
    score_found = False
    for t in ticket_numbers:
        if t in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    print(f"score: {score}")
    total_score += score
    print("--------------------")
    # break
print(f"total score: {total_score}")
