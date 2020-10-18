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

    all_roles = shuffle(all_roles)

    # strengthen seer in case of mechanical wolf
    if 'mechanical wolf' in all_roles:
        for ix, role in enumerate(all_roles):
            if role == 'seer':
                all_roles[ix] = 'seer!'

    return all_roles

def dual_roles(num_players):
    if type(num_players) != int:
        raise ValueError('Number of players must be integer.')

    if num_players not in [6, 7, 8]:
        raise ValueError('Current version only supports a game of 6-8 players.')

    if num_players == 6:
        roles = ['wolf'] + ['fast wolf'] + ['villager'] * 5 + ['seer', 'witch', 'hunter', 'idiot', 'copier',]
    elif num_players == 7:
        roles = ['wolf'] * 2 + ['fast wolf'] + ['villager'] * 5 + ['seer', 'witch', 'hunter', 'idiot', 'copier', 'guard']
    elif num_players == 8:
        roles = ['wolf'] * 2 + ['fast wolf'] + ['villager'] * 6 + ['seer', 'witch', 'hunter', 'idiot', 'copier', 'guard', 'gravekeeper']

    random.shuffle(roles)

    return roles

def shuffle(roles):
    for ix in range(len(roles)):
        jx = random.randint(ix, len(roles) - 1)
        roles[ix], roles[jx] = roles[jx], roles[ix]

    return roles
