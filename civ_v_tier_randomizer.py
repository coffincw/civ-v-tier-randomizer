import sys
from random import randint

# based on https://gaminggorilla.com/civ-5-tier-list/ w/ Iroquois moved to F tier
tier_map = {
    'S': {'Korea', 'Poland'},
    'A': {'Babylon', 'Maya', 'Inca', 'Persia', 'England', 'Arabia', 'Egypt', 'Huns'},
    'B': {'China', 'Ethiopia','Shoshone', 'Aztecs', 'Spain', 'Zulus', 'Russia', 'Celts', 'Siam'},
    'C': {'Greece', 'Austria', 'Germany', 'Mongolia', 'Songhai', 'Brazil', 'America', 'Rome', 'Morroco', 'Sweden', 'India'},
    'D': {'Indonesia', 'Denmark', 'Netherlands', 'Portugal', 'Byzantium', 'Ottomans', 'Assyria', 'Carthage', 'Japan', 'Polynesia'},
    'F': {'France', 'Venice', 'Iroquois'}
}

table_format = "{:<12} {:<12} {:<12}"
picked_civs = set() # keeps track of picked civs so no one gets the same civ as anyone else

# pick civ
def randomly_select_new_civ(possible_civs):
    # check if we have any option left
    if len(possible_civs) == 0:
        print('[ERROR] Invalid configuration - not enough civs in the selected tiers')
        exit(1)

    # roll for civ, then remove pick from available civs
    civ_pick = list(possible_civs)[randint(0, len(possible_civs)-1)]
    possible_civs.remove(civ_pick)
    picked_civs.add(civ_pick)

    return civ_pick


# example `python .\civ_v_tier_randomizer.py "Caleb:B,C|Miko:D,F|Greg:B|Chris:S,A|Jack:S,A|Zach:S,A|Roger:A,B"`
if len(sys.argv) != 2:
    print('[ERROR] Expecting one argument w/ requested tiers as input')
    exit(1)

player_groups = sys.argv[1].split('|')

# output header
print(table_format.format("Player", "Primary", "Backup"))
print("--------------------------------------")

for pg in player_groups:
    player_components = pg.split(':')

    # validate player component (should include name and list of tiers)
    if len(player_components) < 2:
        print('[ERROR] Invalid player component -> [{}]'.format(pg))
        exit(1)
    
    player_name = player_components[0]
    player_tiers = player_components[1].split(',')

    # validate at least one tier provided
    if len(player_tiers[0]) == 0:
        print('[ERROR] Invalid tier list for player component -> [{}]'.format(pg))
        exit(1)

    # Add all applicable civs to our possible civ options
    civs_to_consider = set()
    for tier in player_tiers:
        civs_to_consider.update(tier_map[tier.upper()])

    # remove already selected civs
    civs_to_consider.difference_update(picked_civs)

    first_pick = randomly_select_new_civ(civs_to_consider)
    second_pick = randomly_select_new_civ(civs_to_consider)

    print(table_format.format(player_name, first_pick, second_pick))