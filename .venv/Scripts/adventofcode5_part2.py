from typing import List
import math

rules = []
updates = [] # Nested list

def satisfies_rule(update: List[str], rule: str) -> bool:
    rule_list = rule.split('|') # rule_list[0] comes before rule_list[1]
    if not rule_list[0] in update or not rule_list[1] in update:
        # By default, let this update be deemed as satisfying rule
        return True

    return update.index(rule_list[0]) < update.index(rule_list[1])


def is_correctly_ordered(update: List[str]) -> bool:
    for rule in rules:
        if not satisfies_rule(update, rule):
            return False
    return True

def get_rule_list(rule: str):
    return rule.split('|') # rule_list[0] comes before rule_list[1]

def correctly_order(update: List[str], rule: str) -> List[str]:
    corrected = update.copy()

    if satisfies_rule(update, rule):
        return corrected

    corrected[update.index(get_rule_list(rule)[0])] = get_rule_list(rule)[1]
    corrected[update.index(get_rule_list(rule)[1])] = get_rule_list(rule)[0]

    return corrected

with open('adventofcode_input.txt', 'r') as file:
    is_section_1 = True
    for line in file:
        if line == '\n':
            is_section_1 = False
            continue
        if is_section_1:
            rules.append(line.strip())
        else:
            updates.append(line.strip().split(','))

    sum_of_middle_page_nums = 0



    for update in updates:
        while not is_correctly_ordered(update):
            for rule in rules:
                update = correctly_order(update, rule)
            if is_correctly_ordered(update):
                sum_of_middle_page_nums += int(update[math.floor(len(update) / 2)].strip())


    print(sum_of_middle_page_nums)