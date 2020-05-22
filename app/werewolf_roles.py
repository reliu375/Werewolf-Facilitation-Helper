import random

def roles(input_dict):
    all_roles = []
    # add all roles that are not werewolves

    if 'special_wolf' in input_dict:
        input_dict['wolf'] -= len(input_dict['special_wolf'])

    for role in input_dict:
        if role != 'special_wolf':
            all_roles += [role] * int(input_dict[role])
        # special wolves
        else:
            all_roles += input_dict[role]

    random.shuffle(all_roles)

    return all_roles
