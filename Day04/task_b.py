#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)


Cards = dict()

total_score = 0

card_multiplier = dict()

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
    # score = 0
    score_found = False
    number_of_matches = 0
    for t in ticket_numbers:
        if t in winning_numbers:
            score_found = True
            number_of_matches += 1
    print(f"number of matches: {number_of_matches}")
    if card_number not in card_multiplier:
        card_multiplier[card_number] = 1
    for i in range(card_number + 1, card_number + 1 + number_of_matches):
        if i not in card_multiplier:
            card_multiplier[i] = 1
        card_multiplier[i] += card_multiplier[card_number]
        print(i)
    # total_score += score
    print("--------------------")
    # break
print(card_multiplier)
# print(f"total score: {total_score}")
total = 0
for k in card_multiplier.keys():
    total += card_multiplier[k]
print(f"total: {total}")
