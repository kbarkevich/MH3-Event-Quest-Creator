from tkinter import *
from ids import *
from equipment_ids import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import json
import math


ITEMS_SIZE = 24
GUNNER_SIZE = 8


def SaveQuestFile(data):
    ff = asksaveasfilename(title="Save Quest Json", filetypes=[("Allowed Types", "*.json",)])
    if ff:
        with open(ff, "w") as outfile:
            json.dump(DepopulateDataDict(data), outfile, indent=4)
            return True
    return False


def LoadQuestFile():
    ff = askopenfilename(title="Load Quest Json", filetypes=[("Allowed Types", "*.json",)])
    if ff:
        with open(ff, 'r') as f:
            result = json.load(f)
            return PopulateDataDict(result)
    return None


def DepopulateDataDict(data):
    def unsplit_multiline_string(strings):
        all = strings[0].get()
        pent = 1
        for string in strings[1:]:
            if len(string.get()) > 0:
                all = all + "\n"*pent + string.get()
                pent = 1
            else:
                pent += 1
        return all

    def unformat_flags(flags):
        first = [int(g.get()) for g in flags[0]]
        second = [int(g.get()) for g in flags[1]]
        third = [int(g.get()) for g in flags[2]]
        fourth = [int(g.get()) for g in flags[3]]
        return [
            first,
            second,
            third,
            fourth
        ]

    def unget_bytes(flags):
        first = flags[0][0].get()*1 + flags[0][1].get()*2 + flags[0][2].get()*4 + flags[0][3].get()*8 + flags[0][4].get()*16 + flags[0][5].get()*32 + flags[0][6].get()*64 + flags[0][7].get()*128
        second = flags[1][0].get()*1 + flags[1][1].get()*2 + flags[1][2].get()*4 + flags[1][3].get()*8 + flags[1][4].get()*16 + flags[1][5].get()*32 + flags[1][6].get()*64 + flags[1][7].get()*128
        third = flags[2][0].get()*1 + flags[2][1].get()*2 + flags[2][2].get()*4 + flags[2][3].get()*8 + flags[2][4].get()*16 + flags[2][5].get()*32 + flags[2][6].get()*64 + flags[2][7].get()*128
        try:
            fourth = flags[3][0].get()*1 + flags[3][1].get()*2 + flags[3][2].get()*4 + flags[3][3].get()*8 + flags[3][4].get()*16 + flags[3][5].get()*32 + flags[3][6].get()*64 + flags[3][7].get()*128
        except IndexError:
            fourth = 0
        return fourth * 0x1000000 + third * 0x10000 + second * 0x100 + first

    def unget_rewards(rew):
        return [
            [g[0].get(), g[1].get(), g[2].get()] for g in rew if g[0].get() != ItemsType.none
        ]

    def unfetch_items_from_slots(items):
        return [
            [x[0].get(), x[1].get()] for x in items if x[0].get() != ItemsType.none
        ]

    def unformat_arena_equipment_slot(slot):
        return [[slot[0][0].get(), slot[0][1].get()], [slot[1][0].get(), slot[1][1].get()] if slot[0][0].get() == EquipmentClasses.BowgunFrame else None, [slot[2][0].get(), slot[2][1].get()] if slot[0][0].get() == EquipmentClasses.BowgunFrame else None,
                slot[3].get(), slot[4].get(), slot[5].get(), slot[6].get(), slot[7].get(),
                unfetch_items_from_slots(slot[8]),
                unfetch_items_from_slots(slot[9])]

    out = {
        'small_monsters': [
            [
                {
                    'type': data['small_monsters'][j][k]['type'].get(),'unk1': data['small_monsters'][j][k]['unk1'].get(),'unk2': data['small_monsters'][j][k]['unk2'].get(),
                    'variant': data['small_monsters'][j][k]['variant'].get(),'room': data['small_monsters'][j][k]['room'].get(),'quantity': data['small_monsters'][j][k]['quantity'].get(),
                    'pos_x': data['small_monsters'][j][k]['pos_x'].get(),'pos_y': data['small_monsters'][j][k]['pos_y'].get(),'pos_z': data['small_monsters'][j][k]['pos_z'].get(),
                    'rot_x': data['small_monsters'][j][k]['rot_x'].get(),'rot_y': data['small_monsters'][j][k]['rot_y'].get(),'rot_z': data['small_monsters'][j][k]['rot_z'].get(),
                } for k in range(len(data['small_monsters'][j])) if data['small_monsters'][j][k]['type'].get() != 0
            ] for j in range(len(data['small_monsters']))
        ] if 'small_monsters' in data else [[] for _ in range(LOCATION_SIZE[data['quest_info']['location'].get()])],
        'quest_info': {
            'quest_id': data['quest_info']['quest_id'].get(),
            'name': data['quest_info']['name'].get(),
            'client': data['quest_info']['client'].get(),
            'description': unsplit_multiline_string(data['quest_info']['description']),
            'details': unsplit_multiline_string(data['quest_info']['details']),
            'success_message': unsplit_multiline_string(data['quest_info']['success_message']),
            'failure_message': unsplit_multiline_string(data['quest_info']['failure_message']),
            'flags': unformat_flags(data['quest_info']['flags']),
            'penalty_per_cart': data['quest_info']['penalty_per_cart'].get(),
            'quest_fee': data['quest_info']['quest_fee'].get(),
            'time_limit': data['quest_info']['time_limit'].get(),
            'main_monster_1': data['quest_info']['main_monster_1'].get(),
            'main_monster_2': data['quest_info']['main_monster_2'].get(),
            'location': data['quest_info']['location'].get(),
            'quest_rank': data['quest_info']['quest_rank'].get(),
            'hrp_restriction': data['quest_info']['hrp_restriction'].get(),
            'resources': data['quest_info']['resources'].get(),
            'supply_set_number': data['quest_info']['supply_set_number'].get(),
            'starting_position': data['quest_info']['starting_position'].get(),
            'general_enemy_level': data['quest_info']['general_enemy_level'].get(),
            'summon':  data['quest_info']['summon'][0].get() * 0x1000000 + data['quest_info']['summon'][1].get() * 0x10000 + data['quest_info']['summon'][2].get() * 0x100 + data['quest_info']['summon'][3].get(),
            'wave_1_transition_type': data['quest_info']['wave_1_transition_type'].get(),
            'wave_1_transition_target': data['quest_info']['wave_1_transition_target'].get(),
            'wave_1_transition_quantity': data['quest_info']['wave_1_transition_quantity'].get(),
            'wave_2_transition_type': data['quest_info']['wave_2_transition_type'].get(),
            'wave_2_transition_target': data['quest_info']['wave_2_transition_target'].get(),
            'wave_2_transition_quantity': data['quest_info']['wave_2_transition_quantity'].get(),
        },
        'large_monsters': {
            'monster_1': {
                'type': data['large_monsters']['monster_1']['type'].get(),
                'starting_area': data['large_monsters']['monster_1']['starting_area'].get(),
                'boss_id': data['large_monsters']['monster_1']['boss_id'].get(),
                'spawn_count': data['large_monsters']['monster_1']['spawn_count'].get(),
                'level': data['large_monsters']['monster_1']['level'].get(),
                'size': data['large_monsters']['monster_1']['size'].get(),
                'hp_spread': data['large_monsters']['monster_1']['hp_spread'].get(),
                'size_spread': data['large_monsters']['monster_1']['size_spread'].get()
            },
            'monster_2': {
                'type': data['large_monsters']['monster_2']['type'].get(),
                'starting_area': data['large_monsters']['monster_2']['starting_area'].get(),
                'boss_id': data['large_monsters']['monster_2']['boss_id'].get(),
                'spawn_count': data['large_monsters']['monster_2']['spawn_count'].get(),
                'level': data['large_monsters']['monster_2']['level'].get(),
                'size': data['large_monsters']['monster_2']['size'].get(),
                'hp_spread': data['large_monsters']['monster_2']['hp_spread'].get(),
                'size_spread': data['large_monsters']['monster_2']['size_spread'].get()
            },
            'monster_3': {
                'type': data['large_monsters']['monster_3']['type'].get(),
                'starting_area': data['large_monsters']['monster_3']['starting_area'].get(),
                'boss_id': data['large_monsters']['monster_3']['boss_id'].get(),
                'spawn_count': data['large_monsters']['monster_3']['spawn_count'].get(),
                'level': data['large_monsters']['monster_3']['level'].get(),
                'size': data['large_monsters']['monster_3']['size'].get(),
                'hp_spread': data['large_monsters']['monster_3']['hp_spread'].get(),
                'size_spread': data['large_monsters']['monster_3']['size_spread'].get()
            }
        },
        'objective_details': {
            'main_quest': {
                #'type': 0x00000001,
                'type': unget_bytes(data['objective_details']['main_quest']['type']),
                'objective_type': data['objective_details']['main_quest']['objective_type'].get(),
                'objective_num': data['objective_details']['main_quest']['objective_num'].get(),
                'zenny_reward': data['objective_details']['main_quest']['zenny_reward'].get(),
                'hrp_reward': data['objective_details']['main_quest']['hrp_reward'].get(),
                'rewards_row_1': unget_rewards(data['objective_details']['main_quest']['rewards_row_1']),
                'rewards_row_2': unget_rewards(data['objective_details']['main_quest']['rewards_row_2']),
            },
            'subquest_1': {
                'description': data['objective_details']['subquest_1']['description'].get(),
                'type': unget_bytes(data['objective_details']['subquest_1']['type']),
                'objective_type': data['objective_details']['subquest_1']['objective_type'].get(),
                'objective_num': data['objective_details']['subquest_1']['objective_num'].get(),
                'zenny_reward': data['objective_details']['subquest_1']['zenny_reward'].get(),
                'hrp_reward': data['objective_details']['subquest_1']['hrp_reward'].get(),
                'rewards_row_1': unget_rewards(data['objective_details']['subquest_1']['rewards_row_1']),
            },
            'subquest_2': {
                'description': data['objective_details']['subquest_2']['description'].get(),
                'type': unget_bytes(data['objective_details']['subquest_2']['type']),
                'objective_type': data['objective_details']['subquest_2']['objective_type'].get(),
                'objective_num': data['objective_details']['subquest_2']['objective_num'].get(),
                'zenny_reward': data['objective_details']['subquest_2']['zenny_reward'].get(),
                'hrp_reward': data['objective_details']['subquest_2']['hrp_reward'].get(),
                'rewards_row_1': unget_rewards(data['objective_details']['subquest_2']['rewards_row_1']),
            }
        },
        'unknown': {
            # (1 for hunter killer, 2 for large mon quest, 3 for small/delivery, 5 for jhen/ala)
            'unk_12': data['unknown']['unk_12'].get(),
            'unk_4': data['unknown']['unk_4'].get(),
            'unk_5': data['unknown']['unk_5'].get(),
            'unk_6': data['unknown']['unk_6'].get(),
            'unk_7': data['unknown']['unk_7'].get(),
            # NEW
            'unkInt0': data['unknown']['unkInt0'].get(),  # 0x1C2
            'unkShort0': data['unknown']['unkShort0'].get(),  # 0x1C6
            'unkByte0': data['unknown']['unkByte0'].get(),  # 0x1C8
            'unkBytes0_0': data['unknown']['unkBytes0_0'].get(),  # 0x0306
            'unkBytes0_1': data['unknown']['unkBytes0_1'].get(),
            'unkBytes0_2': data['unknown']['unkBytes0_2'].get(),
            'unkBytes1_0': data['unknown']['unkBytes1_0'].get(),  # 0x0309
            'unkBytes1_1': data['unknown']['unkBytes1_1'].get(),
            'unkBytes1_2': data['unknown']['unkBytes1_2'].get(),
            'unkBytes2_0': data['unknown']['unkBytes2_0'].get(),  # 0x030E
            'unkBytes2_1': data['unknown']['unkBytes2_1'].get(),
            'unkUintAlways15': data['unknown']['unkUintAlways15'].get(),  # 0x0360
            'unkShort1': data['unknown']['unkShort1'].get(),  # 0x0370
            'unkShort2': data['unknown']['unkShort2'].get(),  # 0x0374
            'unkByte1': data['unknown']['unkByte1'].get(),  # 0x0378
            'unkByte2': data['unknown']['unkByte2'].get(),  # 0x0379
            'unkByte3': data['unknown']['unkByte3'].get(),  # 0x037C
            'unkByte4': data['unknown']['unkByte4'].get(),  # 0x037D
            'unkByte7': data['unknown']['unkByte7'].get(),  # 0x0380
            'unkByte8': data['unknown']['unkByte8'].get(),  # 0x0381
        }
    }
    if data['quest_info']['flags'][3][4].get():
        out['arena_equipment'] = [
            unformat_arena_equipment_slot(data['arena_equipment'][0]),
            unformat_arena_equipment_slot(data['arena_equipment'][1]),
            unformat_arena_equipment_slot(data['arena_equipment'][2]),
            unformat_arena_equipment_slot(data['arena_equipment'][3])
        ]
    return out


def PopulateDataDict(data):
    def split_multiline_str(inp, lines):
        cur = [StringVar(value=x) for x in inp.split('\n')]
        return cur + [StringVar(value="") for g in range(lines-len(cur))]

    def format_flags(flags):
        first = [BooleanVar(value=g) for g in flags[0]]
        second = [BooleanVar(value=g) for g in flags[1]]
        third = [BooleanVar(value=g) for g in flags[2]]
        fourth = [BooleanVar(value=g) for g in flags[3]]
        return (
            tuple(first),
            tuple(second),
            tuple(third),
            tuple(fourth)
        )

    def get_bytes(num):
        fourth = int(round((num & 0xFF000000)/0x1000000))
        third = int(round((num & 0xFF0000)/0x10000))
        second = int(round((num & 0xFF00)/0x100))
        first = int(round((num & 0xFF)/0x1))
        return (
            (BooleanVar(value=first&1), BooleanVar(value=first&2), BooleanVar(value=first&4), BooleanVar(value=first&8), BooleanVar(value=first&16), BooleanVar(value=first&32), BooleanVar(value=first&64), BooleanVar(value=first&128)),
            (BooleanVar(value=second&1), BooleanVar(value=second&2), BooleanVar(value=second&4), BooleanVar(value=second&8), BooleanVar(value=second&16), BooleanVar(value=second&32), BooleanVar(value=second&64), BooleanVar(value=second&128)),
            (BooleanVar(value=third&1), BooleanVar(value=third&2), BooleanVar(value=third&4), BooleanVar(value=third&8), BooleanVar(value=third&16), BooleanVar(value=third&32), BooleanVar(value=third&64), BooleanVar(value=third&128)),
            (BooleanVar(value=fourth&1), BooleanVar(value=fourth&2), BooleanVar(value=fourth&4), BooleanVar(value=fourth&8), BooleanVar(value=fourth&16), BooleanVar(value=fourth&32), BooleanVar(value=fourth&64), BooleanVar(value=fourth&128))
        )

    def get_rewards(rew):
        ret = [
            (IntVar(value=g[0]), IntVar(value=g[1]), IntVar(value=g[2])) for g in rew
        ]
        return ret + [
            (IntVar(value=0), IntVar(value=0), IntVar(value=0)) for g in range(11-len(ret))
        ]

    def fetch_items_from_slots(items, quantity):
        return [
            (IntVar(value=x[0]), IntVar(value=x[1])) for x in items
        ] + [
            (IntVar(value=0), IntVar(value=0)) for x in range(quantity-len(items))
        ]

    def format_arena_equipment_slot(slot):
        return [(IntVar(value=slot[0][0]), IntVar(value=slot[0][1])), (IntVar(value=slot[1][0]), IntVar(value=slot[1][1])) if slot[1] is not None else (IntVar(value=EquipmentClasses.BowgunBarrel), IntVar(value=0)), (IntVar(value=slot[2][0]), IntVar(value=slot[2][1])) if slot[2] is not None else (IntVar(value=EquipmentClasses.BowgunStock), IntVar(value=0)),
                IntVar(value=slot[3]), IntVar(value=slot[4]), IntVar(value=slot[5]), IntVar(value=slot[6]), IntVar(value=slot[7]),
                fetch_items_from_slots(slot[8], ITEMS_SIZE),
                fetch_items_from_slots(slot[9], GUNNER_SIZE)]

    out = {
        'small_monsters': [
            [
                {
                    'type': IntVar(value=data['small_monsters'][j][k]['type']),'unk1': IntVar(value=data['small_monsters'][j][k]['unk1']),'unk2': IntVar(value=data['small_monsters'][j][k]['unk2']),
                    'variant': IntVar(value=data['small_monsters'][j][k]['variant']),'room': IntVar(value=data['small_monsters'][j][k]['room']),'quantity': IntVar(value=data['small_monsters'][j][k]['quantity']),
                    'pos_x': DoubleVar(value=data['small_monsters'][j][k]['pos_x']),'pos_y': DoubleVar(value=data['small_monsters'][j][k]['pos_y']),'pos_z': DoubleVar(value=data['small_monsters'][j][k]['pos_z']),
                    'rot_x': IntVar(value=data['small_monsters'][j][k]['rot_x']),'rot_y': IntVar(value=data['small_monsters'][j][k]['rot_y']),'rot_z': IntVar(value=data['small_monsters'][j][k]['rot_z']),
                } for k in range(len(data['small_monsters'][j]))
            ] for j in range(len(data['small_monsters']))
        ] if 'small_monsters' in data else [[] for _ in range(LOCATION_SIZE[data['quest_info']['location']])],
        'quest_info': {
            'quest_id': IntVar(value=data['quest_info']['quest_id']),
            'name': StringVar(value=data['quest_info']['name']),
            'client': StringVar(value=data['quest_info']['client']),
            'description': split_multiline_str(data['quest_info']['description'], lines=2),
            'details': split_multiline_str(data['quest_info']['details'], lines=7),
            'success_message': split_multiline_str(data['quest_info']['success_message'], lines=2),
            'failure_message': split_multiline_str(data['quest_info']['failure_message'] if 'failure_message' in data['quest_info'] else "Reward hits 0, or time\nexpires.", lines=2),
            'flags': format_flags(data['quest_info']['flags']),
            'penalty_per_cart': IntVar(value=data['quest_info']['penalty_per_cart']),
            'quest_fee': IntVar(value=data['quest_info']['quest_fee']),
            'time_limit': IntVar(value=data['quest_info']['time_limit']),
            'main_monster_1': IntVar(value=data['quest_info']['main_monster_1']),
            'main_monster_2': IntVar(value=data['quest_info']['main_monster_2']),
            'location': IntVar(value=data['quest_info']['location']),
            'quest_rank': IntVar(value=data['quest_info']['quest_rank']),
            'hrp_restriction': IntVar(value=data['quest_info']['hrp_restriction']),
            'resources': IntVar(value=data['quest_info']['resources']),
            'supply_set_number': IntVar(value=data['quest_info']['supply_set_number']),
            'starting_position': IntVar(value=data['quest_info']['starting_position']),
            'general_enemy_level': IntVar(value=data['quest_info']['general_enemy_level']),
            'summon': (
                IntVar(value=int(round((data['quest_info']['summon'] & 0xFF000000)/0x1000000))),
                IntVar(value=int(round((data['quest_info']['summon'] & 0xFF0000)/0x10000))),
                IntVar(value=int(round((data['quest_info']['summon'] & 0xFF00)/0x100))),
                IntVar(value=int(round((data['quest_info']['summon'] & 0xFF)/0x1)))
            ),
            'wave_1_transition_type': IntVar(value=data['quest_info']['wave_1_transition_type']),
            'wave_1_transition_target': IntVar(value=data['quest_info']['wave_1_transition_target']),
            'wave_1_transition_quantity': IntVar(value=data['quest_info']['wave_1_transition_quantity']),
            'wave_2_transition_type': IntVar(value=data['quest_info']['wave_2_transition_type']),
            'wave_2_transition_target': IntVar(value=data['quest_info']['wave_2_transition_target']),
            'wave_2_transition_quantity': IntVar(value=data['quest_info']['wave_2_transition_quantity']),
        },
        'large_monsters': {
            'monster_1': {
                'type': IntVar(value=data['large_monsters']['monster_1']['type']),
                'starting_area': IntVar(value=data['large_monsters']['monster_1']['starting_area']),
                'boss_id': IntVar(value=data['large_monsters']['monster_1']['boss_id']),
                'spawn_count': IntVar(value=data['large_monsters']['monster_1']['spawn_count']),
                'level': IntVar(value=data['large_monsters']['monster_1']['level']),
                'size': IntVar(value=data['large_monsters']['monster_1']['size']),
                'hp_spread': IntVar(value=data['large_monsters']['monster_1']['hp_spread']),
                'size_spread': IntVar(value=data['large_monsters']['monster_1']['size_spread'])
            },
            'monster_2': {
                'type': IntVar(value=data['large_monsters']['monster_2']['type']),
                'starting_area': IntVar(value=data['large_monsters']['monster_2']['starting_area']),
                'boss_id': IntVar(value=data['large_monsters']['monster_2']['boss_id']),
                'spawn_count': IntVar(value=data['large_monsters']['monster_2']['spawn_count']),
                'level': IntVar(value=data['large_monsters']['monster_2']['level']),
                'size': IntVar(value=data['large_monsters']['monster_2']['size']),
                'hp_spread': IntVar(value=data['large_monsters']['monster_2']['hp_spread']),
                'size_spread': IntVar(value=data['large_monsters']['monster_2']['size_spread'])
            },
            'monster_3': {
                'type': IntVar(value=data['large_monsters']['monster_3']['type']),
                'starting_area': IntVar(value=data['large_monsters']['monster_3']['starting_area']),
                'boss_id': IntVar(value=data['large_monsters']['monster_3']['boss_id']),
                'spawn_count': IntVar(value=data['large_monsters']['monster_3']['spawn_count']),
                'level': IntVar(value=data['large_monsters']['monster_3']['level']),
                'size': IntVar(value=data['large_monsters']['monster_3']['size']),
                'hp_spread': IntVar(value=data['large_monsters']['monster_3']['hp_spread']),
                'size_spread': IntVar(value=data['large_monsters']['monster_3']['size_spread'])
            }
        },
        'objective_details': {
            'main_quest': {
                #'type': 0x00000001,
                'type': get_bytes(data['objective_details']['main_quest']['type']),
                'objective_type': IntVar(value=data['objective_details']['main_quest']['objective_type']),
                'objective_num': IntVar(value=data['objective_details']['main_quest']['objective_num']),
                'zenny_reward': IntVar(value=data['objective_details']['main_quest']['zenny_reward']),
                'hrp_reward': IntVar(value=data['objective_details']['main_quest']['hrp_reward']),
                'rewards_row_1': get_rewards(data['objective_details']['main_quest']['rewards_row_1']),
                'rewards_row_2': get_rewards(data['objective_details']['main_quest']['rewards_row_2']),
            },
            'subquest_1': {
                'description': StringVar(value=data['objective_details']['subquest_1']['description']),
                'type': get_bytes(data['objective_details']['subquest_1']['type']),
                'objective_type': IntVar(value=data['objective_details']['subquest_1']['objective_type']),
                'objective_num': IntVar(value=data['objective_details']['subquest_1']['objective_num']),
                'zenny_reward': IntVar(value=data['objective_details']['subquest_1']['zenny_reward']),
                'hrp_reward': IntVar(value=data['objective_details']['subquest_1']['hrp_reward']),
                'rewards_row_1': get_rewards(data['objective_details']['subquest_1']['rewards_row_1']),
            },
            'subquest_2': {
                'description': StringVar(value=data['objective_details']['subquest_2']['description']),
                'type': get_bytes(data['objective_details']['subquest_2']['type']),
                'objective_type': IntVar(value=data['objective_details']['subquest_2']['objective_type']),
                'objective_num': IntVar(value=data['objective_details']['subquest_2']['objective_num']),
                'zenny_reward': IntVar(value=data['objective_details']['subquest_2']['zenny_reward']),
                'hrp_reward': IntVar(value=data['objective_details']['subquest_2']['hrp_reward']),
                'rewards_row_1': get_rewards(data['objective_details']['subquest_2']['rewards_row_1']),
            }
        },
        'unknown': {
            # (1 for hunter killer, 2 for large mon quest, 3 for small/delivery, 5 for jhen/ala)
            'unk_12': IntVar(value=data['unknown']['unk_12']),
            'unk_4': IntVar(value=data['unknown']['unk_4']),
            'unk_5': IntVar(value=data['unknown']['unk_5']),
            'unk_6': IntVar(value=data['unknown']['unk_6']),
            'unk_7': IntVar(value=data['unknown']['unk_7']),
            # NEW:
            'unkInt0': IntVar(value=data['unknown']['unkInt0'] if 'unkInt0' in data['unknown'] else 0),  # 0x1C2
            'unkShort0': IntVar(value=data['unknown']['unkShort0'] if 'unkShort0' in data['unknown'] else 0),  # 0x1C6
            'unkByte0': IntVar(value=data['unknown']['unkByte0'] if 'unkByte0' in data['unknown'] else 0),  # 0x1C8
            'unkBytes0_0': IntVar(value=data['unknown']['unkBytes0_0'] if 'unkBytes0_0' in data['unknown'] else 0),  # 0x0306
            'unkBytes0_1': IntVar(value=data['unknown']['unkBytes0_1'] if 'unkBytes0_1' in data['unknown'] else 0),
            'unkBytes0_2': IntVar(value=data['unknown']['unkBytes0_2'] if 'unkBytes0_2' in data['unknown'] else 0),
            'unkBytes1_0': IntVar(value=data['unknown']['unkBytes1_0'] if 'unkBytes1_0' in data['unknown'] else 0),  # 0x0309
            'unkBytes1_1': IntVar(value=data['unknown']['unkBytes1_1'] if 'unkBytes1_1' in data['unknown'] else 0),
            'unkBytes1_2': IntVar(value=data['unknown']['unkBytes1_2'] if 'unkBytes1_2' in data['unknown'] else 0),
            'unkBytes2_0': IntVar(value=data['unknown']['unkBytes2_0'] if 'unkBytes2_0' in data['unknown'] else 0),  # 0x030E
            'unkBytes2_1': IntVar(value=data['unknown']['unkBytes2_1'] if 'unkBytes2_1' in data['unknown'] else 0),
            'unkUintAlways15': IntVar(value=data['unknown']['unkUintAlways15'] if 'unkUintAlways15' in data['unknown'] else 15),  # 0x0360
            'unkShort1': IntVar(value=data['unknown']['unkShort1'] if 'unkShort1' in data['unknown'] else 0),  # 0x0370
            'unkShort2': IntVar(value=data['unknown']['unkShort2'] if 'unkShort2' in data['unknown'] else 0),  # 0x0374
            'unkByte1': IntVar(value=data['unknown']['unkByte1'] if 'unkByte1' in data['unknown'] else 0),  # 0x0378
            'unkByte2': IntVar(value=data['unknown']['unkByte2'] if 'unkByte2' in data['unknown'] else 0),  # 0x0379
            'unkByte3': IntVar(value=data['unknown']['unkByte3'] if 'unkByte3' in data['unknown'] else 0),  # 0x037C
            'unkByte4': IntVar(value=data['unknown']['unkByte4'] if 'unkByte4' in data['unknown'] else 0),  # 0x037D
            'unkByte7': IntVar(value=data['unknown']['unkByte7'] if 'unkByte7' in data['unknown'] else 0),  # 0x0380
            'unkByte8': IntVar(value=data['unknown']['unkByte8'] if 'unkByte8' in data['unknown'] else 0),  # 0x0381
        }
    }
    if 'arena_equipment' in data:
        out['arena_equipment'] = [\
            format_arena_equipment_slot(data['arena_equipment'][0]),
            format_arena_equipment_slot(data['arena_equipment'][1]),
            format_arena_equipment_slot(data['arena_equipment'][2]),
            format_arena_equipment_slot(data['arena_equipment'][3])
        ]
    return out


def InitializeArenaEquipment(data):
    arena_equipment = [\
        [(EquipmentClasses.SnS, SnS.HuntersKnife), (EquipmentClasses.BowgunBarrel, BowgunBarrel.SelectBarrel), (EquipmentClasses.BowgunStock, BowgunStock.NoEquipment),
            Helmet.HuntersHelm, Chestpiece.HuntersMail, Gauntlets.HuntersVambraces, Faulds.HuntersFaulds, Leggings.HuntersGreaves,
            [(ItemsType.whetstone, 20), (ItemsType.potion, 10), (ItemsType.mega_potion, 10), (ItemsType.ration, 10), (ItemsType.lifepowder, 3),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0)],
            [(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),
                (ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0)]],
        [(EquipmentClasses.Lance, Lance.IronLance), (EquipmentClasses.BowgunBarrel, BowgunBarrel.SelectBarrel), (EquipmentClasses.BowgunStock, BowgunStock.NoEquipment),
            Helmet.HuntersHelm, Chestpiece.HuntersMail, Gauntlets.HuntersVambraces, Faulds.HuntersFaulds, Leggings.HuntersGreaves,
            [(ItemsType.whetstone, 20), (ItemsType.potion, 10), (ItemsType.mega_potion, 10), (ItemsType.ration, 10), (ItemsType.lifepowder, 3),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0)],
            [(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),
                (ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0)]],
        [(EquipmentClasses.Hammer, Hammer.IronHammer), (EquipmentClasses.BowgunBarrel, BowgunBarrel.SelectBarrel), (EquipmentClasses.BowgunStock, BowgunStock.NoEquipment),
            Helmet.HuntersHelm, Chestpiece.HuntersMail, Gauntlets.HuntersVambraces, Faulds.HuntersFaulds, Leggings.HuntersGreaves,
            [(ItemsType.whetstone, 20), (ItemsType.potion, 10), (ItemsType.mega_potion, 10), (ItemsType.ration, 10), (ItemsType.lifepowder, 3),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0)],
            [(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),
                (ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0),(ItemsType.none, 0)]],
        [(EquipmentClasses.BowgunFrame, BowgunFrame.LightBowgun), (EquipmentClasses.BowgunBarrel, BowgunBarrel.LightBowgun), (EquipmentClasses.BowgunStock, BowgunStock.NoEquipment),
            Helmet.BarrageEarring, Chestpiece.DamascusVest, Gauntlets.DamascusGuards, Faulds.DamascusCoat, Leggings.DamascusLeggings,
            [(ItemsType.potion, 10), (ItemsType.mega_potion, 10), (ItemsType.energy_drink, 5), (ItemsType.lifepowder, 3), (ItemsType.paralysis_knife, 5),
                (ItemsType.sleep_knife, 5), (ItemsType.poison_knife, 5), (ItemsType.tinged_meat, 5), (ItemsType.druged_meat, 5), (ItemsType.pitfall_trap, 1),
                (ItemsType.shock_trap, 1), (ItemsType.ez_shock_trap, 1), (ItemsType.ez_flash_bomb, 5), (ItemsType.ez_barrel_bomb_l, 2), (ItemsType.barrel_bomb_l_plus, 2),
                (ItemsType.barrel_bomb_l, 3), (ItemsType.barrel_bomb_s, 10), (ItemsType.max_potion, 2), (ItemsType.ancient_potion, 1), (ItemsType.powercharm, 1),
                (ItemsType.armorcharm, 1), (ItemsType.powertalon, 1), (ItemsType.armortalon, 1), (ItemsType.none, 1)],
            [(ItemsType.normal_s_lv2, 99), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0),
                (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0), (ItemsType.none, 0)]]
    ]

    for loadout_idx in range(len(arena_equipment)):
        arena_equipment[loadout_idx][0] = (IntVar(value=arena_equipment[loadout_idx][0][0]), IntVar(value=arena_equipment[loadout_idx][0][1]))
        arena_equipment[loadout_idx][1] = (IntVar(value=arena_equipment[loadout_idx][1][0]), IntVar(value=arena_equipment[loadout_idx][1][1]))
        arena_equipment[loadout_idx][2] = (IntVar(value=arena_equipment[loadout_idx][2][0]), IntVar(value=arena_equipment[loadout_idx][2][1]))

        arena_equipment[loadout_idx][3] = IntVar(value=arena_equipment[loadout_idx][3])
        arena_equipment[loadout_idx][4] = IntVar(value=arena_equipment[loadout_idx][4])
        arena_equipment[loadout_idx][5] = IntVar(value=arena_equipment[loadout_idx][5])
        arena_equipment[loadout_idx][6] = IntVar(value=arena_equipment[loadout_idx][6])
        arena_equipment[loadout_idx][7] = IntVar(value=arena_equipment[loadout_idx][7])

        for itempouch_idx in range(len(arena_equipment[loadout_idx][8])):
            arena_equipment[loadout_idx][8][itempouch_idx] = (IntVar(value=arena_equipment[loadout_idx][8][itempouch_idx][0]), IntVar(value=arena_equipment[loadout_idx][8][itempouch_idx][1]))

        arena_equipment[loadout_idx][8] = tuple(arena_equipment[loadout_idx][8])

        for gunnerpouch_idx in range(len(arena_equipment[loadout_idx][9])):
            arena_equipment[loadout_idx][9][gunnerpouch_idx] = (IntVar(value=arena_equipment[loadout_idx][9][gunnerpouch_idx][0]), IntVar(value=arena_equipment[loadout_idx][9][gunnerpouch_idx][1]))

        arena_equipment[loadout_idx][9] = tuple(arena_equipment[loadout_idx][9])
        arena_equipment[loadout_idx] = tuple(arena_equipment[loadout_idx])

    data['arena_equipment'] = tuple(arena_equipment)

def ClearSmallMonsters(data):
    data['small_monsters'] = [[] for _ in range(LOCATION_SIZE[data['quest_info']['location'].get()] * (
        1 + (1 if (data['quest_info']['wave_1_transition_type'].get() != 0) else 0) + (1 if (data['quest_info']['wave_2_transition_type'].get() != 0) else 0)
    ))]

def InitializeDataDict():
    data = {
        'small_monsters': [
            [
                # Area 0
            ],
            [
                # Area 1
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 1,'quantity': 1,
                    'pos_x': 2039.26,'pos_y': 12.70,'pos_z': 210.05,
                    'rot_x': 0,'rot_y': 17,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 1,'quantity': 1,
                    'pos_x': 857.89,'pos_y': -41.97,'pos_z': 814.06,
                    'rot_x': 0,'rot_y': 170,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 1,'quantity': 1,
                    'pos_x': 97.58,'pos_y': -75.54,'pos_z': 135.22,
                    'rot_x': 0,'rot_y': -45,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 1,'quantity': 1,
                    'pos_x': -393.52,'pos_y': -163.94,'pos_z': -667.01,
                    'rot_x': 0,'rot_y': -199,'rot_z': 0,
                },
            ],
            [
                # Area 2
                {
                    'type': Monster.kelbi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 2,'quantity': 1,
                    'pos_x': -853.86,'pos_y': 19.45,'pos_z': 1381.66,
                    'rot_x': 0,'rot_y': -113,'rot_z': 0,
                },
                {
                    'type': Monster.kelbi,'unk1': 1,'unk2': 0xFF,
                    'variant': 1,'room': 2,'quantity': 2,
                    'pos_x': -553.59,'pos_y': -2.57,'pos_z': -369.71,
                    'rot_x': 0,'rot_y': 193,'rot_z': 0,
                },
                {
                    'type': Monster.kelbi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 2,'quantity': 3,
                    'pos_x': -1698.75,'pos_y': 5.74,'pos_z': -530.30,
                    'rot_x': 0,'rot_y': 398,'rot_z': 0,
                },
            ],
            [
                # Area 3
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 3,'quantity': -1,
                    'pos_x': 873.28,'pos_y': 85.07,'pos_z': -610.86,
                    'rot_x': 0,'rot_y': -153,'rot_z': 0,
                },
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 3,'quantity': -1,
                    'pos_x': 1247.84,'pos_y': 106.65,'pos_z': 25.11,
                    'rot_x': 0,'rot_y': -358,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 2,'room': 3,'quantity': 2,
                    'pos_x': 177.92,'pos_y': 450.70,'pos_z': -32.21,
                    'rot_x': 0,'rot_y': -238,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 3,'quantity': 2,
                    'pos_x': -78.66,'pos_y': 330.70,'pos_z': 362.86,
                    'rot_x': 0,'rot_y': -79,'rot_z': 0,
                },
            ],
            [
                # Area 4
                {
                    'type': Monster.jaggia,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 4,'quantity': 3,
                    'pos_x': 606.18,'pos_y': -12.89,'pos_z': 4145.11,
                    'rot_x': 0,'rot_y': 324,'rot_z': 0,
                },
                {
                    'type': Monster.jaggia,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 4,'quantity': 1,
                    'pos_x': 524.37,'pos_y': -18.65,'pos_z': 2292.05,
                    'rot_x': 0,'rot_y': 199,'rot_z': 0,
                },
                {
                    'type': Monster.rhenoplos,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 4,'quantity': -1,
                    'pos_x': -460.08,'pos_y': -71.51,'pos_z': 3044.50,
                    'rot_x': 0,'rot_y': -460,'rot_z': 0,
                },
            ],
            [
                # Area 5
                {
                    'type': Monster.jaggi,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': 1,
                    'pos_x': 300.40,'pos_y': 4.00,'pos_z': -211.14,
                    'rot_x': 0,'rot_y': 0,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': -1,
                    'pos_x': 458.16,'pos_y': 1.49,'pos_z': -918.94,
                    'rot_x': 0,'rot_y': 51,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': 4,
                    'pos_x': 1813.83,'pos_y': 3.06,'pos_z': 925.68,
                    'rot_x': 0,'rot_y': 494,'rot_z': 0,
                },
                {
                    'type': Monster.jaggia,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': -1,
                    'pos_x': -504.37,'pos_y': 3.05,'pos_z': -757.30,
                    'rot_x': 0,'rot_y': 676,'rot_z': 0,
                },
                {
                    'type': Monster.jaggia,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': 2,
                    'pos_x': 1118.48,'pos_y': 4.00,'pos_z': -420.89,
                    'rot_x': 0,'rot_y': 364,'rot_z': 0,
                },
                {
                    'type': Monster.jaggia,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 5,'quantity': -1,
                    'pos_x': 2658.84,'pos_y': 3.24,'pos_z': 222.99,
                    'rot_x': 0,'rot_y': 756,'rot_z': 0,
                },
            ],
            [
                # Area 6 (Area 8 in Sandy Plains)
                {
                    'type': Monster.rhenoplos,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': -1,
                    'pos_x': 1612.71,'pos_y': -30.27,'pos_z': 695.30,
                    'rot_x': 0,'rot_y': 517,'rot_z': 0,
                },
                {
                    'type': Monster.rhenoplos,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': -1,
                    'pos_x': -2050.04,'pos_y': -31.90,'pos_z': -266.33,
                    'rot_x': 0,'rot_y': 28,'rot_z': 0,
                },
                {
                    'type': Monster.altaroth,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': 5,
                    'pos_x': -344.14,'pos_y': -13.00,'pos_z': -26.14,
                    'rot_x': 0,'rot_y': 443,'rot_z': 0,
                },
                {
                    'type': Monster.altaroth,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': 4,
                    'pos_x': -161.74,'pos_y': 4.80,'pos_z': -416.52,
                    'rot_x': 0,'rot_y': 472,'rot_z': 0,
                },
                {
                    'type': Monster.altaroth,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': 2,
                    'pos_x': -481.05,'pos_y': 15.34,'pos_z': -643.19,
                    'rot_x': 0,'rot_y': 568,'rot_z': 0,
                },
                {
                    'type': Monster.altaroth,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': -1,
                    'pos_x': -692.26,'pos_y': -11.02,'pos_z': -235.13,
                    'rot_x': 0,'rot_y': 608,'rot_z': 0,
                },
                {
                    'type': Monster.altaroth,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 6,'quantity': 3,
                    'pos_x': -417.82,'pos_y': -1.44,'pos_z': -343.46,
                    'rot_x': 0,'rot_y': 147,'rot_z': 0,
                },
            ],
            [
                # Area 7 (Area 9 in Sandy Plains)
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 7,'quantity': 3,
                    'pos_x': 4294.59,'pos_y': -75.65,'pos_z': -2925.29,
                    'rot_x': 0,'rot_y': -130,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 7,'quantity': 2,
                    'pos_x': 3995.30,'pos_y': -45.09,'pos_z': -2049.22,
                    'rot_x': 0,'rot_y': -85,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 7,'quantity': 2,
                    'pos_x': 4187.00,'pos_y': -17.07,'pos_z': -1574.97,
                    'rot_x': 0,'rot_y': -17,'rot_z': 0,
                },
                {
                    'type': Monster.jaggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 7,'quantity': 1,
                    'pos_x': 3781.64,'pos_y': -66.86,'pos_z': -2570.78,
                    'rot_x': 0,'rot_y': -130,'rot_z': 0,
                },
            ],
            [
                # Area 8 (Area 10 in Sandy Plains)
                {
                    'type': Monster.delex,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': 7,
                    'pos_x': 293.99,'pos_y': -170.31,'pos_z': 4049.95,
                    'rot_x': 0,'rot_y': 819,'rot_z': 0,
                },
                {
                    'type': Monster.delex,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': 5,
                    'pos_x': 124.95,'pos_y': -186.54,'pos_z': 3440.16,
                    'rot_x': 0,'rot_y': 819,'rot_z': 0,
                },
                {
                    'type': Monster.delex,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': 3,
                    'pos_x': -425.01,'pos_y': -179.30,'pos_z': 4509.84,
                    'rot_x': 0,'rot_y': 819,'rot_z': 0,
                },
                {
                    'type': Monster.delex,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': 2,
                    'pos_x': -714.48,'pos_y': -183.78,'pos_z': 4108.50,
                    'rot_x': 0,'rot_y': 819,'rot_z': 0,
                },
                {
                    'type': Monster.delex,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': 1,
                    'pos_x': -1021.27,'pos_y': -215.48,'pos_z': 3726.09,
                    'rot_x': 0,'rot_y': 819,'rot_z': 0,
                },
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': -1,
                    'pos_x': -1974.57,'pos_y': -209.48,'pos_z': -316.05,
                    'rot_x': 0,'rot_y': -56,'rot_z': 0,
                },
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 8,'quantity': -1,
                    'pos_x': -1825.11,'pos_y': -210.91,'pos_z': -382.90,
                    'rot_x': 0,'rot_y': 130,'rot_z': 0,
                    
                },
            ],
            [
                # Area 9 (Area 7 in Sandy Plains)
                {
                    'type': Monster.felyne,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 9,'quantity': 2,
                    'pos_x': 3383.92,'pos_y': 2.65,'pos_z': 592.49,
                    'rot_x': 0,'rot_y': -193,'rot_z': 0,
                },
                {
                    'type': Monster.felyne,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 9,'quantity': 1,
                    'pos_x': 2653.55,'pos_y': -22.59,'pos_z': 987.24,
                    'rot_x': 0,'rot_y': -73,'rot_z': 0,
                },
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 9,'quantity': -1,
                    'pos_x': 2838.69,'pos_y': -28.00,'pos_z': 445.91,
                    'rot_x': 0,'rot_y': -142,'rot_z': 0,
                },
                {
                    'type': Monster.melynx,'unk1': 3,'unk2': 0xFF,
                    'variant': 0,'room': 9,'quantity': -1,
                    'pos_x': 2109.53,'pos_y': -26.57,'pos_z': 575.43,
                    'rot_x': 0,'rot_y': -460,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 1,'room': 9,'quantity': -1,
                    'pos_x': -1713.72,'pos_y': 1262.50,'pos_z': 2199.24,
                    'rot_x': 273,'rot_y': -45,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 1,'room': 9,'quantity': 6,
                    'pos_x': -1174.44,'pos_y': 1319.50,'pos_z': 1682.19,
                    'rot_x': 0,'rot_y': -39,'rot_z': 0,
                },
            ],
            [
                # Area 10
            ],
            [
                # Area 11 (Area 6 in Sandy Plains)
                {
                    'type': Monster.giggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 11,'quantity': 2,
                    'pos_x': 2195.89,'pos_y': 73.70,'pos_z': -720.92,
                    'rot_x': 0,'rot_y': 39,'rot_z': 0,
                    
                },
                {
                    'type': Monster.giggi,'unk1': 1,'unk2': 0xFF,
                    'variant': 6,'room': 11,'quantity': 1,
                    'pos_x': -535.73,'pos_y': 1212.59,'pos_z': 896.44,
                    'rot_x': 0,'rot_y': 169,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 11,'quantity': 2,
                    'pos_x': -434.00,'pos_y': 198.96,'pos_z': 289.52,
                    'rot_x': 0,'rot_y': -267,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 11,'quantity': 2,
                    'pos_x': -802.69,'pos_y': 198.96,'pos_z': 66.62,
                    'rot_x': 0,'rot_y': -216,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 11,'quantity': 2,
                    'pos_x': -645.14,'pos_y': 288.96,'pos_z': -371.21,
                    'rot_x': 0,'rot_y': -227,'rot_z': 0,
                },
                {
                    'type': Monster.bnahabra_orange,'unk1': 1,'unk2': 0xFF,
                    'variant': 0,'room': 11,'quantity': 1,
                    'pos_x': -473.33,'pos_y': 168.96,'pos_z': -166.43,
                    'rot_x': 0,'rot_y': -210,'rot_z': 0,
                },
            ],
        ],
        'quest_info': {
            'quest_id': IntVar(value=61001),
            'name': StringVar(value="Jump Four Jaggi"),
            'client': StringVar(value="Guild Subcontractor"),
            'description': (
                StringVar(value="Hunt 4 Great Jaggi"),
                StringVar(value="")
            ),
            'details': (
                StringVar(value="I'm gonna get so fired for"),
                StringVar(value="this... The Great Jaggi some"),
                StringVar(value="hunter brought in just"),
                StringVar(value="escaped. Mind going after"),
                StringVar(value="them? You better hurry,"),
                StringVar(value="though. Bet they've got some"),
                StringVar(value="incredible materials, too.")),
            'success_message': (
                StringVar(value="Complete the Main Quest."),
                StringVar()
            ),
            'failure_message': (
                StringVar(value="Reward hits 0, or time"),
                StringVar(value="expires.")
            ),
            'flags': (
                (BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0)),
                (BooleanVar(value=1), BooleanVar(value=1), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0)),
                (BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0)),
                (BooleanVar(value=1), BooleanVar(value=0), BooleanVar(value=1), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=0), BooleanVar(value=1), BooleanVar(value=1))
            ),
            'penalty_per_cart': IntVar(value=1400),
            'quest_fee': IntVar(value=400),
            'time_limit': IntVar(value=50),
            'main_monster_1': IntVar(value=Monster.bnahabra_blue),
            'main_monster_2': IntVar(value=Monster.melynx),
            'location': IntVar(value=LocationType.QUEST_LOCATION_SANDY_PLAINS),
            'quest_rank': IntVar(value=QuestRankType.star_1),
            'hrp_restriction': IntVar(value=QuestRestrictionType.RESTRICTION_NONE),
            'resources': IntVar(value=ResourcesType.low_rank),
            'supply_set_number': IntVar(value=19),
            'starting_position': IntVar(value=StartingPositionType.camp),
            'general_enemy_level': IntVar(value=0x0017),
            'summon': (
                IntVar(value=0x64),
                IntVar(value=0x05),
                IntVar(value=0x02),
                IntVar(value=0x19)
            ),#(0x64050219),
            'wave_1_transition_type': IntVar(value=WaveType.none),
            'wave_1_transition_target': IntVar(value=0x0000),
            'wave_1_transition_quantity': IntVar(value=0x0000),
            'wave_2_transition_type': IntVar(value=WaveType.none),
            'wave_2_transition_target': IntVar(value=0x0000),
            'wave_2_transition_quantity': IntVar(value=0x0000),
        },
        'large_monsters': {
            'monster_1': {
                'type': IntVar(value=Monster.great_jaggi),
                'starting_area': IntVar(value=0x00),
                'boss_id': IntVar(value=0xFF),
                'spawn_count': IntVar(value=0x04),
                'level': IntVar(value=0x17),  # 0x01 through 0x3c
                'size': IntVar(value=0x64),
                'hp_spread': IntVar(value=0x01),  # 0: fixed, 1: spread of 5, 2: spread of 3
                'size_spread': IntVar(value=0x01)
            },
            'monster_2': {
                'type': IntVar(value=Monster.none),
                'starting_area': IntVar(value=0x00),
                'boss_id': IntVar(value=0x00),
                'spawn_count': IntVar(value=0x00),
                'level': IntVar(value=0x00),  # 0x01 through 0x3c
                'size': IntVar(value=0x00),
                'hp_spread': IntVar(value=0x00),  # 0: fixed, 1: spread of 5, 2: spread of 3
                'size_spread': IntVar(value=0x00)
            },
            'monster_3': {
                'type': IntVar(value=Monster.none),
                'starting_area': IntVar(value=0x00),
                'boss_id': IntVar(value=0x00),
                'spawn_count': IntVar(value=0x00),
                'level': IntVar(value=0x00),  # 0x01 through 0x3c
                'size': IntVar(value=0x00),
                'hp_spread': IntVar(value=0x00),  # 0: fixed, 1: spread of 5, 2: spread of 3
                'size_spread': IntVar(value=0x00)
            }
        },
        'objective_details': {
            'main_quest': {
                #'type': 0x00000001,
                'type': (
                    (BooleanVar(value=1),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0))
                ),
                'objective_type': IntVar(value=Monster.great_jaggi),
                'objective_num': IntVar(value=0x04),
                'zenny_reward': IntVar(value=4000),
                'hrp_reward': IntVar(value=440),
                'rewards_row_1': [
                    (IntVar(value=ItemsType.great_jagi_claw), IntVar(value=1), IntVar(value=3)),
                    (IntVar(value=ItemsType.great_jagi_hide), IntVar(value=1), IntVar(value=12)),
                    (IntVar(value=ItemsType.jagi_scale), IntVar(value=1), IntVar(value=10)),
                    (IntVar(value=ItemsType.screamer), IntVar(value=1), IntVar(value=20)),
                    (IntVar(value=ItemsType.kings_frill), IntVar(value=1), IntVar(value=12)),
                    (IntVar(value=ItemsType.bone_husk_s), IntVar(value=8), IntVar(value=18)),
                    (IntVar(value=ItemsType.great_jagi_head), IntVar(value=1), IntVar(value=25)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0))
                ],
                'rewards_row_2': [
                    (IntVar(value=ItemsType.mystery_charm), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.aquaglow_jewel), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.shining_charm), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.armor_sphere), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.armor_sphere_plus), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0))
                ],
            },
            'subquest_1': {
                'description': StringVar(value="Hunt 2 Great Jaggi"),
                'type': (
                    (BooleanVar(value=1),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0))
                ),
                'objective_type': IntVar(value=Monster.great_jaggi),
                'objective_num': IntVar(value=0x02),
                'zenny_reward': IntVar(value=4000),
                'hrp_reward': IntVar(value=440),
                'rewards_row_1': [
                    (IntVar(value=ItemsType.great_jagi_claw), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.great_jagi_hide), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.jagi_scale), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.screamer), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.kings_frill), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.bone_husk_s), IntVar(value=8), IntVar(value=1)),
                    (IntVar(value=ItemsType.great_jagi_head), IntVar(value=1), IntVar(value=1)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0))
                ],
            },
            'subquest_2': {
                'description': StringVar(value="None"),
                'type': (
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0)),
                    (BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0),BooleanVar(value=0))
                ),
                'objective_type': IntVar(value=Monster.none),
                'objective_num': IntVar(value=0),
                'zenny_reward': IntVar(value=0),
                'hrp_reward': IntVar(value=0),
                'rewards_row_1': [
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0)),
                    (IntVar(value=ItemsType.none), IntVar(value=0), IntVar(value=0))
                ],
            }
        },
        'unknown': {
            # (1 for hunter killer, 2 for large mon quest, 3 for small/delivery, 5 for jhen/ala)
            'unk_12': IntVar(value=0x00000002),  # 0x390
            'unk_4': IntVar(value=0x00),  # 0x036C
            'unk_5': IntVar(value=0x00),  # 0x036E
            'unk_6': IntVar(value=0x00),  # 0x036F
            'unk_7': IntVar(value=0x0000),  # 0x0376
            # NEW:
            'unkInt0': IntVar(value=0x0000),  # 0x1C2
            'unkShort0': IntVar(value=0x0000),  # 0x1C6
            'unkByte0': IntVar(value=0x0000),  # 0x1C8
            'unkBytes0_0': IntVar(value=0x00),  # 0x0306
            'unkBytes0_1': IntVar(value=0x00),
            'unkBytes0_2': IntVar(value=0x00),
            'unkBytes1_0': IntVar(value=0x00),  # 0x0309
            'unkBytes1_1': IntVar(value=0x00),
            'unkBytes1_2': IntVar(value=0x00),
            'unkBytes2_0': IntVar(value=0x00),  # 0x030E
            'unkBytes2_1': IntVar(value=0x00),
            'unkUintAlways15': IntVar(value=0x0000000f),  # 0x0360
            'unkShort1': IntVar(value=0x0000),  # 0x0370
            'unkShort2': IntVar(value=0x0000),  # 0x0374
            'unkByte1': IntVar(value=0x00),  # 0x0378
            'unkByte2': IntVar(value=0x00),  # 0x0379
            'unkByte3': IntVar(value=0x00),  # 0x037C
            'unkByte4': IntVar(value=0x00),  # 0x037D
            'unkByte7': IntVar(value=0x00),  # 0x0380
            'unkByte8': IntVar(value=0x00),  # 0x0381
        }
    }

    for area in data['small_monsters']:
        for monster in area:
            if type(monster['type']) != IntVar:
                monster['type'] = IntVar(value=monster['type'])
            if type(monster['unk1']) != IntVar:
                monster['unk1'] = IntVar(value=monster['unk1'])
            if type(monster['unk2']) != IntVar:
                monster['unk2'] = IntVar(value=monster['unk2'])
            if type(monster['variant']) != IntVar:
                monster['variant'] = IntVar(value=monster['variant'])
            if type(monster['room']) != IntVar:
                monster['room'] = IntVar(value=monster['room'])
            if type(monster['quantity']) != IntVar:
                monster['quantity'] = IntVar(value=monster['quantity'])
            if type(monster['pos_x']) != DoubleVar:
                monster['pos_x'] = DoubleVar(value=monster['pos_x'])
            if type(monster['pos_y']) != DoubleVar:
                monster['pos_y'] = DoubleVar(value=monster['pos_y'])
            if type(monster['pos_z']) != DoubleVar:
                monster['pos_z'] = DoubleVar(value=monster['pos_z'])
            if type(monster['rot_x']) != IntVar:
                monster['rot_x'] = IntVar(value=monster['rot_x'])
            if type(monster['rot_y']) != IntVar:
                monster['rot_y'] = IntVar(value=monster['rot_y'])
            if type(monster['rot_z']) != IntVar:
                monster['rot_z'] = IntVar(value=monster['rot_z'])

    return data
