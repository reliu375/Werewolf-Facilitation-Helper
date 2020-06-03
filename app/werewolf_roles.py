import random
import pdb

def roles(input_dict):
    all_roles = []

    for role in input_dict:
        if role != 'special_wolf':
            all_roles += [role] * int(input_dict[role])
        # special wolves
        else:
            all_roles += input_dict[role]

    random.shuffle(all_roles)

    # strengthen seer in case of mechanical wolf
    if 'mechanical wolf' in all_roles:
        for ix, role in enumerate(all_roles):
            if role == 'seer':
                all_roles[ix] = 'seer!'

    return all_roles
