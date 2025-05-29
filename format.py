from tkinter import *
from ids import *
from tkinter.filedialog import askopenfilename
import json
import math


def LoadQuestFile():
    ff = askopenfilename(title="Load Quest Json", filetypes=[("Allowed Types", "*.json",)])
    if ff:
        with open(ff, 'r') as f:
            result = json.load(f)
            return PopulateDataDict(result)
    return None


def PopulateDataDict(data):
    def split_multiline_str(inp, lines):
        cur = [StringVar(value=x) for x in inp.split('\n')]
        return cur + ["" for g in range(lines-len(cur))]

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

    return {
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
        }
    }


def InitializeDataDict():
    data = {
        'small_monsters': [
            [
                # Area 0
            ],
            [
                # Area 1
                {
                    'type': IntVar(value=Monster.jaggi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=1),'quantity': IntVar(value=1),
                    'pos_x': DoubleVar(value=2039.26),'pos_y': DoubleVar(value=12.70),'pos_z': DoubleVar(value=210.05),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=17),'rot_z': IntVar(value=0),
                    
                },
                {
                    'type': IntVar(value=Monster.jaggi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=1),'quantity': IntVar(value=1),
                    'pos_x': DoubleVar(value=857.89),'pos_y': DoubleVar(value=-41.97),'pos_z': DoubleVar(value=814.06),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=170),'rot_z': IntVar(value=0),
                },
                {
                    'type': IntVar(value=Monster.jaggi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=1),'quantity': IntVar(value=1),
                    'pos_x': DoubleVar(value=97.58),'pos_y': DoubleVar(value=-75.54),'pos_z': DoubleVar(value=135.22),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=-45),'rot_z': IntVar(value=0),
                },
                {
                    'type': IntVar(value=Monster.jaggi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=1),'quantity': IntVar(value=1),
                    'pos_x': DoubleVar(value=-393.52),'pos_y': DoubleVar(value=-163.94),'pos_z': DoubleVar(value=-667.01),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=-199),'rot_z': IntVar(value=0),
                },
            ],
            [
                # Area 2
                {
                    'type': IntVar(value=Monster.kelbi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=2),'quantity': IntVar(value=1),
                    'pos_x': DoubleVar(value=-853.86),'pos_y': DoubleVar(value=19.45),'pos_z': DoubleVar(value=1381.66),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=-113),'rot_z': IntVar(value=0),
                },
                {
                    'type': IntVar(value=Monster.kelbi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=1),'room': IntVar(value=2),'quantity': IntVar(value=2),
                    'pos_x': DoubleVar(value=-553.59),'pos_y': DoubleVar(value=-2.57),'pos_z': DoubleVar(value=-369.71),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=193),'rot_z': IntVar(value=0),
                },
                {
                    'type': IntVar(value=Monster.kelbi),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
                    'variant': IntVar(value=0),'room': IntVar(value=2),'quantity': IntVar(value=3),
                    'pos_x': DoubleVar(value=-1698.75),'pos_y': DoubleVar(value=5.74),'pos_z': DoubleVar(value=-530.30),
                    'rot_x': IntVar(value=0),'rot_y': IntVar(value=398),'rot_z': IntVar(value=0),
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
            'unk_12': IntVar(value=0x00000002),
            'unk_4': IntVar(value=0x00),
            'unk_5': IntVar(value=0x00),
            'unk_6': IntVar(value=0x00),
            'unk_7': IntVar(value=0x00000000),
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
