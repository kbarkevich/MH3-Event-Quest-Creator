import os
import sys
from sys import exit
from tkinter import *
from tkinter import ttk
from ids import *
from format import *
from utils import *
import webbrowser


def QuestInfo(tab, data):
    questNameFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questNameFrame, text="Quest Name:").pack()
    ttk.Entry(questNameFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['name']).pack()
    questNameFrame.pack(side='top', expand=True)

    questSuccessFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questSuccessFrame, text="Success Conditions:").pack()
    ttk.Entry(questSuccessFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['success_message'][0]).pack()
    ttk.Entry(questSuccessFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['success_message'][1]).pack()
    questSuccessFrame.pack(side='top', expand=True)

    questFailFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questFailFrame, text="Fail Conditions:").pack()
    ent1 = ttk.Entry(questFailFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['failure_message'][0]).pack()
    ent2 = ttk.Entry(questFailFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['failure_message'][1]).pack()
    questFailFrame.pack(side='top', expand=True)

    questClientFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questClientFrame, text="Client:").pack()
    ttk.Entry(questClientFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['client']).pack()
    questClientFrame.pack(side='top', expand=True)

    questDescriptionFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questDescriptionFrame, text="Quest Description:").pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][0]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][1]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][2]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][3]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][4]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][5]).pack()
    ttk.Entry(questDescriptionFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 33), textvariable=data['quest_info']['details'][6]).pack()
    questDescriptionFrame.pack(side='bottom', expand=True)


def QuestSettings(tab, data, onAreaChange=None, onArenaToggle=None):
    questFlagsFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questFlagsFrame, text="Quest Flags").grid(column=1, row=0)
    questFlagsFrame1 = ttk.Frame(questFlagsFrame, padding=2)
    questFlagsFrame1.grid(column=0, row=1)
    questFlagsFrame2 = ttk.Frame(questFlagsFrame, padding=2)
    questFlagsFrame2.grid(column=1, row=1)
    questFlagsFrame3 = ttk.Frame(questFlagsFrame, padding=2)
    questFlagsFrame3.grid(column=2, row=1)
    questFlagsFrame.pack(side='bottom', expand=True)

    flags = data['quest_info']['flags']

    var11 = flags[0][0]
    var12 = flags[0][1]
    var13 = flags[0][2]
    var14 = flags[0][3]
    var15 = flags[0][4]
    var16 = flags[0][5]
    var17 = flags[0][6]
    var18 = flags[0][7]
    ttk.Checkbutton(questFlagsFrame1, text="Tutorial", variable=var11).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Combine & Require 1st Sub", variable=var12).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Combine & Require 2 Subs", variable=var13).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Unknown4", variable=var14).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Jhen(?)", variable=var15).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Shakalaka(?)", variable=var16).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Advanced", variable=var17).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Combine Main & Subs", variable=var18).pack(side='top', anchor=N+W)

    var21 = flags[1][0]
    var22 = flags[1][1]
    var23 = flags[1][2]
    var24 = flags[1][3]
    var25 = flags[1][4]
    var26 = flags[1][5]
    var27 = flags[1][6]
    var28 = flags[1][7]
    ttk.Checkbutton(questFlagsFrame2, text="Unknown1", variable=var21).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown2", variable=var22).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Require Both Subs", variable=var23).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown4", variable=var24).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="\"Qualifying Time\"", variable=var25).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Don't Announce Subs", variable=var26).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown7", variable=var27).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="\"Dragon Left Wounded\"", variable=var28).pack(side='top', anchor=N+W)

    var31 = flags[2][0]
    var32 = flags[2][1]
    var33 = flags[2][2]
    var34 = flags[2][3]
    var35 = flags[2][4]
    var36 = flags[2][5]
    var37 = flags[2][6]
    var38 = flags[2][7]
    ttk.Checkbutton(questFlagsFrame3, text="2Mon/0Subs/ReqSub1/Unstable", variable=var31).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown2", variable=var32).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown3", variable=var33).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Banjo Music", variable=var34).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown5", variable=var35).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown6", variable=var36).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown7", variable=var37).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown8", variable=var38).pack(side='top', anchor=N+W)

    basicSettingsFrame = ttk.Frame(tab, padding=2)
    basicSettingsFrame.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
    basicSettingsFrame.columnconfigure((0,1,2), weight=1)
    ttk.Label(basicSettingsFrame, text="Map:").grid(column=0, row=0, padx=10, pady=(15,0), sticky='w')
    Dropdown(basicSettingsFrame, LocationType, onSelected=onAreaChange, variable=data['quest_info']['location'], criteria=lambda a: [x[15:] for x in a if x[:1]!="_"]).grid(column=0,row=1, padx=10, pady=(0,10))

    ttk.Label(basicSettingsFrame, text="Quest ID:").grid(column=1, row=0, padx=10, pady=(15,0), sticky='w')
    NumEntry(basicSettingsFrame, variable=data['quest_info']['quest_id'], limit=0xFFFF).grid(column=1,row=1, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Quest Rank:").grid(column=2, row=0, padx=10, pady=(15,0), sticky='w')
    Dropdown(basicSettingsFrame, QuestRankType, variable=data['quest_info']['quest_rank']).grid(column=2, row=1, padx=10, pady=(0,10))

    ttk.Label(basicSettingsFrame, text="Quest Time (mins):").grid(column=0, row=2, padx=10, sticky='w')
    NumEntry(basicSettingsFrame, variable=data['quest_info']['time_limit'], limit=0xFF).grid(column=0,row=3, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Death Reduction:").grid(column=1, row=2, padx=10, sticky='w')
    NumEntry(basicSettingsFrame, variable=data['quest_info']['penalty_per_cart'], limit=0xFFFF).grid(column=1,row=3, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Contract Fee:").grid(column=2, row=2, padx=10, sticky='w')
    NumEntry(basicSettingsFrame, variable=data['quest_info']['quest_fee'], limit=0xFFFF).grid(column=2, row=3, padx=10, pady=(0,10))

    ttk.Label(basicSettingsFrame, text="Starting Position:").grid(column=0, row=4, padx=10, sticky='w')
    Dropdown(basicSettingsFrame, StartingPositionType, variable=data['quest_info']['starting_position']).grid(column=0,row=5, padx=10, pady=(0,10))
    UrlLabel(basicSettingsFrame, "https://imgur.com/a/QPXdMLK/", hover="Click to see pictures of the online supply sets!", text="Supply Set:").grid(column=1, row=4, padx=10, sticky='w')
    Dropdown(basicSettingsFrame, list(range(255)), variable=data['quest_info']['supply_set_number']).grid(column=1,row=5, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Delivery Type:").grid(column=2, row=4, padx=10, sticky='w')
    Dropdown(basicSettingsFrame, DeliveryType, variable=data['unknown']['unkShort2'], criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"]).grid(column=2, row=5, padx=10, pady=(0,10))

    ttk.Label(basicSettingsFrame, text="Resources:").grid(column=0, row=6, padx=10, sticky='w')
    Dropdown(basicSettingsFrame, ResourcesType, data['quest_info']['resources']).grid(column=0,row=7, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Quest Requirement:").grid(column=1, row=6, columnspan=2, padx=10, sticky=W)
    Dropdown(basicSettingsFrame, QuestRestrictionType, data['quest_info']['hrp_restriction']).grid(column=1, row=7, padx=10, pady=(0,10), columnspan=2, sticky=W+E)
    basicSettingsFrame.pack(side='left', anchor='n', expand=True)
    

    menuFlagsFrame = ttk.Frame(tab, padding=2)
    ttk.Label(menuFlagsFrame, text="Menu Flags").pack(side='top', anchor=N)
    var41 = flags[3][0]
    var42 = flags[3][1]
    var43 = flags[3][2]
    var44 = flags[3][3]
    var45 = flags[3][4]
    var46 = flags[3][5]
    var47 = flags[3][6]
    var48 = flags[3][7]
    ttk.Checkbutton(menuFlagsFrame, text="Slay", variable=var41).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Gather", variable=var42).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Capture", variable=var43).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Slay Hidden", variable=var44).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Arena", variable=var45, command=lambda x=var45:onArenaToggle(x)if onArenaToggle is not None else None).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Unknown2", variable=var46).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="End@Main(?)", variable=var47).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Unknown3", variable=var48).pack(side='top', anchor=N+W)
    menuFlagsFrame.pack(side='right', expand=True)


def LargeMonsters(tab, data):
    boss1 = data['large_monsters']['monster_1']
    boss1Frame = ttk.Frame(tab, padding=2)
    ttk.Label(boss1Frame, text="Boss 1", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=(20, 0), sticky='w')
    updater1 = Dropdown(boss1Frame, Monster, boss1['type'], criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])
    updater1.grid(column=0, row=1, sticky='sw')
    ttk.Label(boss1Frame, text="Boss ID(?)").grid(column=1, row=0, sticky='sw')
    NumEntry(boss1Frame, limit=0xFF, variable=boss1['boss_id']).grid(column=1, row=1)
    ttk.Label(boss1Frame, text="Level:").grid(column=2, row=0, sticky='sw')
    updater2 = NumEntry(boss1Frame, limit=0x3c, variable=boss1['level'])
    updater2.grid(column=2, row=1)
    ttk.Label(boss1Frame, text="Spawn Location:").grid(column=3, row=0, sticky='sw')
    NumEntry(boss1Frame, limit=0xFF, variable=boss1['starting_area']).grid(column=3, row=1)
    ttk.Label(boss1Frame, text="Spawn Count:").grid(column=0, row=2, sticky='w')
    NumEntry(boss1Frame, limit=0xFF, variable=boss1['spawn_count']).grid(column=0, row=3)
    ttk.Label(boss1Frame, text="Size:").grid(column=1, row=2, sticky='w')
    NumEntry(boss1Frame, limit=0xFF, variable=boss1['size']).grid(column=1, row=3)
    ttk.Label(boss1Frame, text="HP Spread:").grid(column=2, row=2, sticky='w')
    updater3 = Dropdown(boss1Frame, ["Fixed", "+/- <=2 Levels", "+/- <=1 Level"], boss1['hp_spread'])
    updater3.grid(column=2, row=3)
    ttk.Label(boss1Frame, text="Size Spread:").grid(column=3, row=2, sticky='w')
    NumEntry(boss1Frame, limit=0xFF, variable=boss1['size_spread']).grid(column=3, row=3)
    boss1_label = ttk.Label(boss1Frame, text="------")
    boss1_label.grid(column=0, row=4, columnspan=4, sticky=E+W)
    def update_boss_info_display(boss, label):
        if boss['type'].get() == 0:
            label.config(text = "------")
        elif boss['type'].get() not in MONSTER_HP:
            label.config(text = "Invalid Monster")
        elif boss['level'].get() not in LEVELS:
            label.config(text = "Invalid Level")
        else:
            arena_mode = data['quest_info']['flags'][3][4].get()
            base_hp = MONSTER_HP[boss['type'].get()]
            level_mult = LEVELS[boss['level'].get()]
            arena_mult = 0.55 if arena_mode else 1.0
            if boss['hp_spread'].get() == 2 and boss['level'].get() - 1 in LEVELS and boss['level'].get() + 1 in LEVELS:
                info_str = "(base "+str(int(base_hp))+(" * arena 0.55"if arena_mode else "") + " * level multipliers) HP: "
                level_mult_1 = LEVELS[boss['level'].get()-1]
                level_mult_2 = LEVELS[boss['level'].get()+1]
                label.config(text = info_str + str(int(base_hp * level_mult_1 * arena_mult)) +"/"+ str(int(base_hp * level_mult * arena_mult)) +"/"+ str(int(base_hp * level_mult_2 * arena_mult)))
            elif boss['hp_spread'].get() == 1 and boss['level'].get() - 2 in LEVELS and boss['level'].get() + 2 in LEVELS:
                info_str = "(base "+str(int(base_hp))+(" * arena 0.55"if arena_mode else "") + " * level multipliers) HP: "
                level_mult_1 = LEVELS[boss['level'].get()-2]
                level_mult_2 = LEVELS[boss['level'].get()-1]
                level_mult_3 = LEVELS[boss['level'].get()+1]
                level_mult_4 = LEVELS[boss['level'].get()+2]
                label.config(text = info_str + str(int(base_hp * level_mult_1 * arena_mult)) +"/"+ str(int(base_hp * level_mult_2 * arena_mult)) +"/"+ str(int(base_hp * level_mult * arena_mult)) +"/"+ str(int(base_hp * level_mult_3 * arena_mult)) +"/"+str(int(base_hp * level_mult_4 * arena_mult)))
            else:
                info_str = "(base "+str(int(base_hp))+(" * arena 0.55"if arena_mode else "") + " * level multiplier) HP: "
                label.config(text = info_str + str(int(base_hp * level_mult * arena_mult)))
    updater1.onSelected = lambda:update_boss_info_display(boss1, boss1_label)
    updater2.bind('<KeyRelease>', lambda _:update_boss_info_display(boss1, boss1_label))
    updater3.onSelected = lambda:update_boss_info_display(boss1, boss1_label)

    boss2 = data['large_monsters']['monster_2']
    boss2Frame = ttk.Frame(tab, padding=2)
    ttk.Label(boss2Frame, text="Boss 2", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=(20, 0), sticky='w')
    updater1 = Dropdown(boss2Frame, Monster, boss2['type'], criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])
    updater1.grid(column=0, row=1, sticky='sw')
    ttk.Label(boss2Frame, text="Boss ID(?)").grid(column=1, row=0, sticky='sw')
    NumEntry(boss2Frame, limit=0xFF, variable=boss2['boss_id']).grid(column=1, row=1)
    ttk.Label(boss2Frame, text="Level:").grid(column=2, row=0, sticky='sw')
    updater2 = NumEntry(boss2Frame, limit=0x3c, variable=boss2['level'])
    updater2.grid(column=2, row=1)
    ttk.Label(boss2Frame, text="Spawn Location:").grid(column=3, row=0, sticky='sw')
    NumEntry(boss2Frame, limit=0xFF, variable=boss2['starting_area']).grid(column=3, row=1)
    ttk.Label(boss2Frame, text="Spawn Count:").grid(column=0, row=2, sticky='w')
    NumEntry(boss2Frame, limit=0xFF, variable=boss2['spawn_count']).grid(column=0, row=3)
    ttk.Label(boss2Frame, text="Size:").grid(column=1, row=2, sticky='w')
    NumEntry(boss2Frame, limit=0xFF, variable=boss2['size']).grid(column=1, row=3)
    ttk.Label(boss2Frame, text="HP Spread:").grid(column=2, row=2, sticky='w')
    updater3 = Dropdown(boss2Frame, ["Fixed", "+/- <=2 Levels", "+/- <=1 Level"], boss2['hp_spread'])
    updater3.grid(column=2, row=3)
    ttk.Label(boss2Frame, text="Size Spread:").grid(column=3, row=2, sticky='w')
    NumEntry(boss2Frame, limit=0xFF, variable=boss2['size_spread']).grid(column=3, row=3)
    boss2_label = ttk.Label(boss2Frame, text="------")
    boss2_label.grid(column=0, row=4, columnspan=4, sticky=E+W)
    updater1.onSelected = lambda:update_boss_info_display(boss2, boss2_label)
    updater2.bind('<KeyRelease>', lambda _:update_boss_info_display(boss2, boss2_label))
    updater3.onSelected = lambda:update_boss_info_display(boss2, boss2_label)

    boss3 = data['large_monsters']['monster_3']
    boss3Frame = ttk.Frame(tab, padding=2)
    ttk.Label(boss3Frame, text="Boss 3", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=(20, 0), sticky='w')
    updater1 = Dropdown(boss3Frame, Monster, boss3['type'], criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])
    updater1.grid(column=0, row=1, sticky='sw')
    ttk.Label(boss3Frame, text="Boss ID(?)").grid(column=1, row=0, sticky='sw')
    NumEntry(boss3Frame, limit=0xFF, variable=boss3['boss_id']).grid(column=1, row=1)
    ttk.Label(boss3Frame, text="Level:").grid(column=2, row=0, sticky='sw')
    updater2 = NumEntry(boss3Frame, limit=0x3c, variable=boss3['level'])
    updater2.grid(column=2, row=1)
    ttk.Label(boss3Frame, text="Spawn Location:").grid(column=3, row=0, sticky='sw')
    NumEntry(boss3Frame, limit=0xFF, variable=boss3['starting_area']).grid(column=3, row=1)
    ttk.Label(boss3Frame, text="Spawn Count:").grid(column=0, row=2, sticky='w')
    NumEntry(boss3Frame, limit=0xFF, variable=boss3['spawn_count']).grid(column=0, row=3)
    ttk.Label(boss3Frame, text="Size:").grid(column=1, row=2, sticky='w')
    NumEntry(boss3Frame, limit=0xFF, variable=boss3['size']).grid(column=1, row=3)
    ttk.Label(boss3Frame, text="HP Spread:").grid(column=2, row=2, sticky='w')
    updater3 = Dropdown(boss3Frame, ["Fixed", "+/- <=2 Levels", "+/- <=1 Level"], boss3['hp_spread'])
    updater3.grid(column=2, row=3)
    ttk.Label(boss3Frame, text="Size Spread:").grid(column=3, row=2, sticky='w')
    NumEntry(boss3Frame, limit=0xFF, variable=boss3['size_spread']).grid(column=3, row=3)
    boss3_label = ttk.Label(boss3Frame, text="------")
    boss3_label.grid(column=0, row=4, columnspan=4, sticky=E+W)
    updater1.onSelected = lambda:update_boss_info_display(boss3, boss3_label)
    updater2.bind('<KeyRelease>', lambda _:update_boss_info_display(boss3, boss3_label))
    updater3.onSelected = lambda:update_boss_info_display(boss3, boss3_label)

    summon = data['quest_info']['summon']
    bossInvaderFrame = ttk.Frame(tab, padding=2)
    ttk.Label(bossInvaderFrame, text="Invader", font=("Arial", 12, "bold")).grid(column=0, row=0, columnspan=(3), sticky='w')
    ToolTipLabel(bossInvaderFrame, hover="This value is the percentage chance for an invader to be set to enter the quest at all.\nThis is rolled once when the quest is initiated, and then never again.", text="%1:").grid(column=0, row=1, sticky='w')

    NumEntry(bossInvaderFrame, limit=0x64, width=3, variable=summon[0]).grid(column=0, row=2, pady=(0, 20))
    ToolTipLabel(bossInvaderFrame, hover="This value is the percentage chance that the determined invader (if applicable given\nthe previous value) will spawn at each 200-second interval once the quest has begun.", text="%2:").grid(column=1, row=1, sticky='sw')
    Dropdown(bossInvaderFrame, INVADER_CHANCE, summon[1], width=5).grid(column=1, row=2, pady=(0, 20))
    ToolTipLabel(bossInvaderFrame, hover="This value's exact function is unknown. However, it seems as though it should be set to\nthe first free large monster slot. If no large monsters are entered above, set this to 1.\nIf one monster is entered above, set this to 2. Etc.", text="Unk:").grid(column=2, row=1, columnspan=(2), sticky='sw')
    NumEntry(bossInvaderFrame, limit=0xFF, variable=summon[2], width=3).grid(column=2, row=2, pady=(0, 20))
    Dropdown(bossInvaderFrame, get_invader_list(), summon[3], width=69).grid(column=3, row=2, pady=(0, 20), columnspan=2, sticky=W+E)

    boss1Frame.pack(side='top', anchor='n')
    boss2Frame.pack(side='top', anchor='n')
    boss3Frame.pack(side='top', anchor='n')
    bossInvaderFrame.pack(side='bottom', anchor='n')

    def update_all_bosses(x=None):
        update_boss_info_display(boss1, boss1_label)
        update_boss_info_display(boss2, boss2_label)
        update_boss_info_display(boss3, boss3_label)
    update_all_bosses()
    return update_all_bosses


def Objectives(tab, data):
    # Create a notebook that holds the tabs
    objectivesNotebook = ttk.Notebook(tab)
    # Create tab frames
    mainTab = ttk.Frame(objectivesNotebook) # Quest Info
    sub1Tab = ttk.Frame(objectivesNotebook) # Quest Settings
    sub2Tab = ttk.Frame(objectivesNotebook) # Large Monsters
    # Add tabs
    objectivesNotebook.add(mainTab, text="Main Objective")
    objectivesNotebook.add(sub1Tab, text="Subquest 1")
    objectivesNotebook.add(sub2Tab, text="Subquest 2")
    objectivesNotebook.pack(expand=1, fill='both')

    # MAIN OBJECTIVE
    main = data['objective_details']['main_quest']

    mainDescriptionFrame = ttk.Frame(mainTab, padding=2)
    ttk.Label(mainDescriptionFrame, text="Objective Description:").pack(expand=True)
    ttk.Entry(mainDescriptionFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 39), textvariable=data['quest_info']['description'][0]).pack(expand=True)
    ttk.Entry(mainDescriptionFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=data['quest_info']['description'][1]).pack(expand=True)
    mainDescriptionFrame.pack(expand=True)

    mainMonetaryFrame = ttk.Frame(mainTab, padding=2)
    ttk.Label(mainMonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    NumEntry(mainMonetaryFrame, limit=0xFFFF, variable=main['zenny_reward']).grid(column=0, row=1)
    ttk.Label(mainMonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    NumEntry(mainMonetaryFrame, limit=0xFFFF, variable=main['hrp_reward']).grid(column=1, row=1)
    mainMonetaryFrame.pack(expand=True)

    mainFlagsFrame = ttk.Frame(mainTab, padding=2, width=100)
    ttk.Label(mainFlagsFrame, text="Objective Flags:").grid(column=1,row=0)

    mainFlagsFrame1 = ttk.Frame(mainFlagsFrame, padding=2)
    varMain11 = main['type'][0][0]
    varMain12 = main['type'][0][1]
    varMain13 = main['type'][0][2]
    varMain14 = main['type'][0][3]
    varMain15 = main['type'][0][4]
    varMain16 = main['type'][0][5]
    varMain17 = main['type'][0][6]
    varMain18 = main['type'][0][7]

    varMain21 = main['type'][1][0]
    varMain22 = main['type'][1][1]
    varMain23 = main['type'][1][2]
    varMain24 = main['type'][1][3]
    varMain25 = main['type'][1][4]
    varMain26 = main['type'][1][5]
    varMain27 = main['type'][1][6]
    varMain28 = main['type'][1][7]

    mainTargetFrame = ttk.Frame(mainTab, padding=2)
    targetDropdown = AutocompleteDropdown(mainTargetFrame,
        Monster if varMain11.get() or varMain13.get() or varMain25.get() \
        else ItemsType if varMain12.get() \
        else EnvironmentInteractType if varMain26.get() \
        else list(range(0x100)),
        variable=main['objective_type'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"],
        onSelected=lambda: update_target_dropdown())
    valueDropdown = AutocompleteDropdown(mainTargetFrame,
        get_monster_enum_from_id(targetDropdown.current()) if varMain22.get() and varMain13.get() \
        else BindType if varMain25.get() \
        else list(range(0xFFFF)),
        variable=main['objective_num'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])#NumEntry(mainTargetFrame, limit=0xFF, variable=main['objective_num'])

    def update_target_dropdown():
        # Update target dropdown
        if varMain11.get() or varMain13.get() or varMain25.get():
            targetDropdown.update_dropdown(Monster)
        elif varMain12.get():
            targetDropdown.update_dropdown(ItemsType)
        elif varMain26.get():
            targetDropdown.update_dropdown(EnvironmentInteractType)
        else:
            targetDropdown.update_dropdown(list(range(0x100)))
        # Update value dropdown
        if varMain22.get() and varMain13.get():
            valueDropdown.update_dropdown(get_monster_enum_from_id(targetDropdown.current()))
        elif varMain25.get():
            valueDropdown.update_dropdown(BindType)
        else:
            valueDropdown.update_dropdown(list(range(0xFFFF)))
            

    ttk.Checkbutton(mainFlagsFrame1, text="Monster", variable=varMain11, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Item", variable=varMain12, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Target", variable=varMain13, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown4", variable=varMain14).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Check On Timeout(?)", variable=varMain15).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown6", variable=varMain16).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown7", variable=varMain17).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Capture", variable=varMain18).pack(side='top', anchor=N+W)
    mainFlagsFrame1.grid(column=0, row=1, sticky='w')

    mainFlagsFrame2 = ttk.Frame(mainFlagsFrame, padding=2)
    ttk.Checkbutton(mainFlagsFrame2, text="Must Slay(?)", variable=varMain21).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Enemy Part", variable=varMain22, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Hit Points", variable=varMain23).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown4", variable=varMain24).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Bind Monster", variable=varMain25, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Environment Interaction", variable=varMain26, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown7", variable=varMain27).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown8", variable=varMain28).pack(side='top', anchor=N+W)
    mainFlagsFrame2.grid(column=1, row=1, sticky='w')

    mainFlagsFrame3 = ttk.Frame(mainFlagsFrame, padding=2)
    varMain31 = main['type'][2][0]
    varMain32 = main['type'][2][1]
    varMain33 = main['type'][2][2]
    varMain34 = main['type'][2][3]
    varMain35 = main['type'][2][4]
    varMain36 = main['type'][2][5]
    varMain37 = main['type'][2][6]
    varMain38 = main['type'][2][7]
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown1", variable=varMain31).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown2", variable=varMain32).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown3", variable=varMain33).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown4", variable=varMain34).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown5", variable=varMain35).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown6", variable=varMain36).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown7", variable=varMain37).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame3, text="Unknown8", variable=varMain38).pack(side='top', anchor=N+W)
    mainFlagsFrame3.grid(column=2, row=1, sticky='w')

    mainFlagsFrame.pack(expand=True)

    ttk.Label(mainTargetFrame, text="Target:").grid(column=0, row=0, sticky='w')
    targetDropdown.grid(column=0, row=1, pady=(0,10))
    ttk.Label(mainTargetFrame, text="Value:").grid(column=1, row=0, sticky='w')
    valueDropdown.grid(column=1, row=1, pady=(0,10))
    mainTargetFrame.pack(expand=True)

    ttk.Button(mainTab, text='Item Rewards', command=lambda:CreateRewards(data, 0)).pack(expand=True)

    # SUBQUEST 1
    sub1 = data['objective_details']['subquest_1']

    sub1DescriptionFrame = ttk.Frame(sub1Tab, padding=2)
    ttk.Label(sub1DescriptionFrame, text="Subquest 1 Description:").pack()
    ttk.Entry(sub1DescriptionFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=sub1['description']).pack()
    sub1DescriptionFrame.pack(expand=True)

    sub1MonetaryFrame = ttk.Frame(sub1Tab, padding=2)
    ttk.Label(sub1MonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    NumEntry(sub1MonetaryFrame, limit=0xFFFF, variable=sub1['zenny_reward']).grid(column=0, row=1)
    ttk.Label(sub1MonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    NumEntry(sub1MonetaryFrame, limit=0xFFFF, variable=sub1['hrp_reward']).grid(column=1, row=1)
    sub1MonetaryFrame.pack(expand=True)

    sub1FlagsFrame = ttk.Frame(sub1Tab, padding=2, width=100)
    ttk.Label(sub1FlagsFrame, text="Subquest 1 Flags:").grid(column=1,row=0)

    sub1FlagsFrame1 = ttk.Frame(sub1FlagsFrame, padding=2)
    varSub111 = sub1['type'][0][0]
    varSub112 = sub1['type'][0][1]
    varSub113 = sub1['type'][0][2]
    varSub114 = sub1['type'][0][3]
    varSub115 = sub1['type'][0][4]
    varSub116 = sub1['type'][0][5]
    varSub117 = sub1['type'][0][6]
    varSub118 = sub1['type'][0][7]

    varSub121 = sub1['type'][1][0]
    varSub122 = sub1['type'][1][1]
    varSub123 = sub1['type'][1][2]
    varSub124 = sub1['type'][1][3]
    varSub125 = sub1['type'][1][4]
    varSub126 = sub1['type'][1][5]
    varSub127 = sub1['type'][1][6]
    varSub128 = sub1['type'][1][7]

    sub1TargetFrame = ttk.Frame(sub1Tab, padding=2)
    sub1Dropdown = AutocompleteDropdown(sub1TargetFrame,
        Monster if varSub111.get() or varSub113.get() or varSub125.get() \
        else ItemsType if varSub112.get() \
        else EnvironmentInteractType if varSub126.get() \
        else list(range(0x100)),
        variable=sub1['objective_type'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"],
        onSelected=lambda: update_sub1_dropdown())
    sub1ValueDropdown = AutocompleteDropdown(sub1TargetFrame,
        get_monster_enum_from_id(sub1Dropdown.current()) if varSub122.get() and varSub113.get() \
        else BindType if varSub125.get() \
        else list(range(0xFFFF)),
        variable=sub1['objective_num'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])#NumEntry(sub1TargetFrame, limit=0xFF, variable=sub1['objective_num'])

    def update_sub1_dropdown():
        if varSub111.get() or varSub113.get() or varSub125.get():
            sub1Dropdown.update_dropdown(Monster)
        elif varSub112.get():
            sub1Dropdown.update_dropdown(ItemsType)
        elif varSub126.get():
            sub1Dropdown.update_dropdown(EnvironmentInteractType)
        else:
            sub1Dropdown.update_dropdown(list(range(0x100)))
        # Update value dropdown
        if varSub122.get() and varSub113.get():
            sub1ValueDropdown.update_dropdown(get_monster_enum_from_id(sub1Dropdown.current()))
        elif varSub125.get():
            sub1ValueDropdown.update_dropdown(BindType)
        else:
            sub1ValueDropdown.update_dropdown(list(range(0xFFFF)))

    ttk.Checkbutton(sub1FlagsFrame1, text="Monster", variable=varSub111, command=update_sub1_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Item", variable=varSub112, command=update_sub1_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Target", variable=varSub113, command=update_sub1_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown4", variable=varSub114).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Check on Timeout(?)", variable=varSub115).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown6", variable=varSub116).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown7", variable=varSub117).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Capture", variable=varSub118).pack(side='top', anchor=N+W)
    sub1FlagsFrame1.grid(column=0, row=1, sticky='w')

    sub1FlagsFrame2 = ttk.Frame(sub1FlagsFrame, padding=2)
    ttk.Checkbutton(sub1FlagsFrame2, text="Must Slay(?)", variable=varSub121).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Enemy Part", variable=varSub122).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Hit Points", variable=varSub123).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown4", variable=varSub124).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Bind Monster", variable=varSub125, command=update_sub1_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Environment Interaction", variable=varSub126, command=update_sub1_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown7", variable=varSub127).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown8", variable=varSub128).pack(side='top', anchor=N+W)
    sub1FlagsFrame2.grid(column=1, row=1, sticky='w')

    sub1FlagsFrame3 = ttk.Frame(sub1FlagsFrame, padding=2)
    varSub131 = sub1['type'][2][0]
    varSub132 = sub1['type'][2][1]
    varSub133 = sub1['type'][2][2]
    varSub134 = sub1['type'][2][3]
    varSub135 = sub1['type'][2][4]
    varSub136 = sub1['type'][2][5]
    varSub137 = sub1['type'][2][6]
    varSub138 = sub1['type'][2][7]
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown1", variable=varSub131).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown2", variable=varSub132).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown3", variable=varSub133).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown4", variable=varSub134).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown5", variable=varSub135).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown6", variable=varSub136).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown7", variable=varSub137).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame3, text="Unknown8", variable=varSub138).pack(side='top', anchor=N+W)
    sub1FlagsFrame3.grid(column=2, row=1, sticky='w')

    sub1FlagsFrame.pack(expand=True)

    ttk.Label(sub1TargetFrame, text="Target:").grid(column=0, row=0, sticky='w')
    sub1Dropdown.grid(column=0, row=1, pady=(0,10))
    ttk.Label(sub1TargetFrame, text="Value:").grid(column=1, row=0, sticky='w')
    sub1ValueDropdown.grid(column=1, row=1, pady=(0,10))
    sub1TargetFrame.pack(expand=True)

    ttk.Button(sub1Tab, text='Item Rewards', command=lambda:CreateRewards(data, 1)).pack(expand=True)

    # SUBQUEST 2
    sub2 = data['objective_details']['subquest_2']

    sub2DescriptionFrame = ttk.Frame(sub2Tab, padding=2)
    ttk.Label(sub2DescriptionFrame, text="Subquest 2 Description:").pack()
    ttk.Entry(sub2DescriptionFrame, width=60, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 40), textvariable=sub2['description']).pack()
    sub2DescriptionFrame.pack(expand=True)

    sub2MonetaryFrame = ttk.Frame(sub2Tab, padding=2)
    ttk.Label(sub2MonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    NumEntry(sub2MonetaryFrame, limit=0xFFFF, variable=sub2['zenny_reward']).grid(column=0, row=1)
    ttk.Label(sub2MonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    NumEntry(sub2MonetaryFrame, limit=0xFFFF, variable=sub2['hrp_reward']).grid(column=1, row=1)
    sub2MonetaryFrame.pack(expand=True)

    sub2FlagsFrame = ttk.Frame(sub2Tab, padding=2, width=100)
    ttk.Label(sub2FlagsFrame, text="Subquest 2 Flags:").grid(column=1,row=0)

    sub2FlagsFrame1 = ttk.Frame(sub2FlagsFrame, padding=2)
    varSub211 = sub2['type'][0][0]
    varSub212 = sub2['type'][0][1]
    varSub213 = sub2['type'][0][2]
    varSub214 = sub2['type'][0][3]
    varSub215 = sub2['type'][0][4]
    varSub216 = sub2['type'][0][5]
    varSub217 = sub2['type'][0][6]
    varSub218 = sub2['type'][0][7]

    varSub221 = sub2['type'][1][0]
    varSub222 = sub2['type'][1][1]
    varSub223 = sub2['type'][1][2]
    varSub224 = sub2['type'][1][3]
    varSub225 = sub2['type'][1][4]
    varSub226 = sub2['type'][1][5]
    varSub227 = sub2['type'][1][6]
    varSub228 = sub2['type'][1][7]

    sub2TargetFrame = ttk.Frame(sub2Tab, padding=2)
    sub2Dropdown = AutocompleteDropdown(sub2TargetFrame,
        Monster if varSub211.get() or varSub213.get() or varSub225.get() \
        else ItemsType if varSub212.get() \
        else EnvironmentInteractType if varSub226.get() \
        else list(range(0x100)),
        variable=sub2['objective_type'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"],
        onSelected=lambda: update_sub2_dropdown())
    sub2ValueDropdown = AutocompleteDropdown(sub2TargetFrame,
        get_monster_enum_from_id(sub2Dropdown.current()) if varSub222.get() and varSub213.get() \
        else BindType if varSub225.get() \
        else list(range(0xFFFF)),
        variable=sub2['objective_num'], width=30,
        criteria=lambda a: [x.replace("_"," ") for x in a if x[:1]!="_"])#NumEntry(sub2TargetFrame, limit=0xFF, variable=sub2['objective_num'])

    def update_sub2_dropdown():
        if varSub211.get() or varSub213.get() or varSub225.get():
            sub2Dropdown.update_dropdown(Monster)
        elif varSub212.get():
            sub2Dropdown.update_dropdown(ItemsType)
        elif varSub226.get():
            sub2Dropdown.update_dropdown(EnvironmentInteractType)
        else:
            sub2Dropdown.update_dropdown(list(range(0x100)))
        # Update value dropdown
        if varSub222.get() and varSub213.get():
            sub2ValueDropdown.update_dropdown(get_monster_enum_from_id(sub2Dropdown.current()))
        elif varSub225.get():
            sub2ValueDropdown.update_dropdown(BindType)
        else:
            sub2ValueDropdown.update_dropdown(list(range(0xFFFF)))

    ttk.Checkbutton(sub2FlagsFrame1, text="Monster", variable=varSub211, command=update_sub2_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Item", variable=varSub212, command=update_sub2_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Target", variable=varSub213, command=update_sub2_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown4", variable=varSub214).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Check on Timeout(?)", variable=varSub215).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown6", variable=varSub216).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown7", variable=varSub217).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Capture", variable=varSub218).pack(side='top', anchor=N+W)
    sub2FlagsFrame1.grid(column=0, row=1, sticky='w')

    sub2FlagsFrame2 = ttk.Frame(sub2FlagsFrame, padding=2)
    ttk.Checkbutton(sub2FlagsFrame2, text="Must Slay(?)", variable=varSub221).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Enemy Part", variable=varSub222).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Hit Points", variable=varSub223).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown4", variable=varSub224).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Bind Monster", variable=varSub225, command=update_sub2_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Environment Interaction", variable=varSub226, command=update_sub2_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown7", variable=varSub227).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown8", variable=varSub228).pack(side='top', anchor=N+W)
    sub2FlagsFrame2.grid(column=1, row=1, sticky='w')

    sub2FlagsFrame3 = ttk.Frame(sub2FlagsFrame, padding=2)
    varSub231 = sub2['type'][2][0]
    varSub232 = sub2['type'][2][1]
    varSub233 = sub2['type'][2][2]
    varSub234 = sub2['type'][2][3]
    varSub235 = sub2['type'][2][4]
    varSub236 = sub2['type'][2][5]
    varSub237 = sub2['type'][2][6]
    varSub238 = sub2['type'][2][7]
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown1", variable=varSub231).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown2", variable=varSub232).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown3", variable=varSub233).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown4", variable=varSub234).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown5", variable=varSub235).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown6", variable=varSub236).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown7", variable=varSub237).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame3, text="Unknown8", variable=varSub238).pack(side='top', anchor=N+W)
    sub2FlagsFrame3.grid(column=2, row=1, sticky='w')

    sub2FlagsFrame.pack(expand=True)

    ttk.Label(sub2TargetFrame, text="Target:").grid(column=0, row=0, sticky='w')
    sub2Dropdown.grid(column=0, row=1, pady=(0,10))
    ttk.Label(sub2TargetFrame, text="Value:").grid(column=1, row=0, sticky='w')
    sub2ValueDropdown.grid(column=1, row=1, pady=(0,10))
    sub2TargetFrame.pack(expand=True)

    ttk.Button(sub2Tab, text='Item Rewards', command=lambda:CreateRewards(data, 2)).pack(expand=True)


def SmallMonsters(tab, data):
    minionLevelFrame = ttk.Frame(tab, padding=2)
    ttk.Label(minionLevelFrame, text="Small Monster Map Settings").grid(column=0, row=0, padx=(0, 125), sticky='w')
    ttk.Label(minionLevelFrame, text="Minion Level:").grid(column=1, row=0, padx=(50, 0), sticky='e')
    NumEntry(minionLevelFrame, limit=0x3c, variable=data['quest_info']['general_enemy_level']).grid(column=2, row=0, sticky='w')
    minionLevelFrame.pack(side='top')

    # Create a notebook that holds the tabs
    wavesNotebook = ttk.Notebook(tab)
    numWaves = 1 + (1 if (data['quest_info']['wave_1_transition_type'].get() != 0) else 0) + (1 if (data['quest_info']['wave_2_transition_type'].get() != 0) else 0)
    waveTabs = []
    for i in range(numWaves):
        waveTab = ttk.Frame(wavesNotebook)
        wavesNotebook.add(waveTab, text="Wave "+str(i+1))
        waveTabs.append(waveTab)
    wavesNotebook.pack(expand=1, fill='both')

    wave = 0
    for waveTab in waveTabs:
        # Create a notebook that holds the tabs
        areasNotebook = ttk.Notebook(waveTab)
        # Create tab frames
        numAreas = LOCATION_SIZE[data['quest_info']['location'].get()]
        areaTabs = []
        for i in range(numAreas):
            areaTab = ttk.Frame(areasNotebook)
            areasNotebook.add(areaTab, text=str(i))
            areaTabs.append(areaTab)

        areasNotebook.pack(expand=1, fill='both')

        i = 0
        for areaTab in areaTabs:
            ScrolledCanvas(areaTab, data, wave, i, color='grey')
            i += 1
        wave += 1

    mainMonstersFrame = ttk.Frame(tab, padding=2)
    ttk.Label(mainMonstersFrame, text="Main Monsters:").grid(column=0, row=0, sticky='w')
    Dropdown(mainMonstersFrame, Monster, variable=data['quest_info']['main_monster_1']).grid(column=0, row=1)
    Dropdown(mainMonstersFrame, Monster, variable=data['quest_info']['main_monster_2']).grid(column=1, row=1)
    mainMonstersFrame.pack()

    wave2SelectorsHolder = []
    wave3SelectorsHolder = []
    waveConditionsFrame = ttk.Frame(tab, padding=2)
    ttk.Label(waveConditionsFrame, text="Second Wave Condition:").grid(column=0, row=0)
    ttk.Label(waveConditionsFrame, text="Target:").grid(column=1, row=0)
    ttk.Label(waveConditionsFrame, text="Number:").grid(column=2, row=0)

    wave2TargetDropdown = AutocompleteDropdown(waveConditionsFrame, Monster if data['quest_info']['wave_1_transition_type'].get() == WaveType.monster else ItemsType if data['quest_info']['wave_1_transition_type'].get() == WaveType.item else list(range(0xFF)), variable=data['quest_info']['wave_1_transition_target'])
    def update_wave2_dropdown(full):
        if data['quest_info']['wave_1_transition_type'].get() == WaveType.monster:
            wave2TargetDropdown.update_dropdown(Monster)
        elif data['quest_info']['wave_1_transition_type'].get() == WaveType.item:
            wave2TargetDropdown.update_dropdown(ItemsType)
        else:
            wave2TargetDropdown.update_dropdown(list(range(0xFF)))

        if data['quest_info']['wave_1_transition_type'].get() == WaveType.none:
            while len(data['small_monsters']) > LOCATION_SIZE[data['quest_info']['location'].get()]:
                data['small_monsters'].pop()
            if full:
                RebuildTab(tab, data, SmallMonsters)
                return
            data['quest_info']['wave_2_transition_type'].set(0)
            data['quest_info']['wave_2_transition_target'].set(0)
            data['quest_info']['wave_2_transition_quantity'].set(0)
            for a in wave3SelectorsHolder:
                a['state'] = 'disabled'
                try:
                    a.current(0)
                except:
                    pass  # can't update the NumEntrys
        else:
            while len(data['small_monsters']) < (2 * LOCATION_SIZE[data['quest_info']['location'].get()]):
                data['small_monsters'] += [[]]
            if full:
                RebuildTab(tab, data, SmallMonsters)
                return
            for a in wave3SelectorsHolder:
                if type(a) == Dropdown:
                    a['state'] = 'readonly'
                else:
                    a['state'] = 'normal'

    wave2TypeDropdown = Dropdown(waveConditionsFrame, WaveType, onSelected=lambda: update_wave2_dropdown(True), variable=data['quest_info']['wave_1_transition_type'])
    wave2TypeDropdown.grid(column=0, row=1)
    wave2TargetDropdown.grid(column=1, row=1)
    wave2QuantityDropdown = NumEntry(waveConditionsFrame, limit=0xFFFF, variable=data['quest_info']['wave_1_transition_quantity'])
    wave2QuantityDropdown.grid(column=2, row=1)

    wave2SelectorsHolder = [wave2TypeDropdown, wave2TargetDropdown, wave2QuantityDropdown]

    ttk.Label(waveConditionsFrame, text="Third Wave Condition:").grid(column=0, row=2)
    ttk.Label(waveConditionsFrame, text="Target:").grid(column=1, row=2)
    ttk.Label(waveConditionsFrame, text="Number:").grid(column=2, row=2)

    wave3TargetDropdown = AutocompleteDropdown(waveConditionsFrame, Monster if data['quest_info']['wave_2_transition_type'].get() == WaveType.monster else ItemsType if data['quest_info']['wave_2_transition_type'].get() == WaveType.item else list(range(0xFF)), variable=data['quest_info']['wave_2_transition_target'])
    def update_wave3_dropdown(full):
        if data['quest_info']['wave_2_transition_type'].get() == WaveType.monster:
            wave3TargetDropdown.update_dropdown(Monster)
        elif data['quest_info']['wave_2_transition_type'].get() == WaveType.item:
            wave3TargetDropdown.update_dropdown(ItemsType)
        else:
            wave3TargetDropdown.update_dropdown(list(range(0xFF)))

        if data['quest_info']['wave_2_transition_type'].get() == WaveType.none:
            while len(data['small_monsters']) > 2*LOCATION_SIZE[data['quest_info']['location'].get()]:
                data['small_monsters'].pop()
            if full:
                RebuildTab(tab, data, SmallMonsters)
                return
            for a in wave2SelectorsHolder:
                if type(a) == Dropdown:
                    a['state'] = 'readonly'
                else:
                    a['state'] = 'normal'
        else:
            while len(data['small_monsters']) < (3 * LOCATION_SIZE[data['quest_info']['location'].get()]):
                data['small_monsters'] += [[]]
            if full:
                RebuildTab(tab, data, SmallMonsters)
                return
            for a in wave2SelectorsHolder:
                a['state'] = 'disabled'

    wave3TypeDropdown = Dropdown(waveConditionsFrame, WaveType, onSelected=lambda: update_wave3_dropdown(True), variable=data['quest_info']['wave_2_transition_type'])
    wave3TypeDropdown.grid(column=0, row=3)
    wave3TargetDropdown.grid(column=1, row=3)
    wave3QuantityDropdown = NumEntry(waveConditionsFrame, limit=0xFFFF, variable=data['quest_info']['wave_2_transition_quantity'])
    wave3QuantityDropdown.grid(column=2, row=3)
    wave3SelectorsHolder = [wave3TypeDropdown, wave3TargetDropdown, wave3QuantityDropdown]
    waveConditionsFrame.pack()

    update_wave2_dropdown(False)
    update_wave3_dropdown(False)


def Unknowns(tab, data):
    """
    'unk_12': 0x00000002,
    'unk_4': 0x00,
    'unk_5': 0x00,
    'unk_6': 0x00,
    'unk_7': 0x0000,
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
    """
    unk_box_1 = ttk.Frame(tab)
    ttk.Label(unk_box_1, text="Unknown 4: One Byte:").grid(column=0, row=0)
    NumEntry(unk_box_1, limit=0xFF, width=25, variable=data['unknown']['unk_4']).grid(column=0, row=1)
    ttk.Label(unk_box_1, text="Tutorial:").grid(column=1, row=0)
    #NumEntry(unk_box_1, limit=0xFF, width=25, variable=data['unknown']['unk_5']).grid(column=1, row=1)
    Dropdown(unk_box_1, TutorialType, data['unknown']['unk_5']).grid(column=1, row=1)
    ttk.Label(unk_box_1, text="Unknown 6: One Byte:").grid(column=0, row=2)
    NumEntry(unk_box_1, limit=0xFF, width=25, variable=data['unknown']['unk_6']).grid(column=0, row=3)
    ttk.Label(unk_box_1, text="Unknown 7: Two Bytes:").grid(column=1, row=2)
    NumEntry(unk_box_1, limit=0xFFFF, width=25, variable=data['unknown']['unk_7']).grid(column=1, row=3)

    unk_box_2 = ttk.Frame(tab)
    ttk.Label(unk_box_2, text="Unknown 12: Four Bytes").pack()
    ttk.Label(unk_box_2, text="(1 for hunter killer, 2 for large mon quest, 3 for small/delivery, 5 for jhen/ala/ceadeus):").pack()
    NumEntry(unk_box_2, limit=0xFFFFFFFF, width=25, variable=data['unknown']['unk_12']).pack()

    unk_box_1.pack()
    unk_box_2.pack()

    unk_box_3 = ttk.Frame(tab)
    ttk.Label(unk_box_3, text="unkInt0").grid(column=0, row=0)
    NumEntry(unk_box_3, limit=0xFFFFFFFF, width=20, variable=data['unknown']['unkInt0']).grid(column=0, row=1)
    ttk.Label(unk_box_3, text="unkShort0").grid(column=1, row=0)
    NumEntry(unk_box_3, limit=0xFFFF, width=20, variable=data['unknown']['unkShort0']).grid(column=1, row=1)
    ttk.Label(unk_box_3, text="unkByte0").grid(column=2, row=0)
    NumEntry(unk_box_3, limit=0xFF, width=20, variable=data['unknown']['unkByte0']).grid(column=2, row=1)
    
    unk_box_3.pack()

    unk_box_4 = ttk.Frame(tab)
    ttk.Label(unk_box_4, text="unkBytes0_0").grid(column=0, row=0)
    NumEntry(unk_box_4, limit=0xFF, width=10, variable=data['unknown']['unkBytes0_0']).grid(column=0, row=1)
    ttk.Label(unk_box_4, text="unkBytes0_1").grid(column=1, row=0)
    NumEntry(unk_box_4, limit=0xFF, width=10, variable=data['unknown']['unkBytes0_1']).grid(column=1, row=1)
    ttk.Label(unk_box_4, text="unkBytes0_2").grid(column=2, row=0)
    NumEntry(unk_box_4, limit=0xFF, width=10, variable=data['unknown']['unkBytes0_2']).grid(column=2, row=1)

    unk_box_4.pack()

    unk_box_5 = ttk.Frame(tab)
    ttk.Label(unk_box_5, text="unkBytes1_0").grid(column=0, row=0)
    NumEntry(unk_box_5, limit=0xFF, width=10, variable=data['unknown']['unkBytes1_0']).grid(column=0, row=1)
    ttk.Label(unk_box_5, text="unkBytes1_1").grid(column=1, row=0)
    NumEntry(unk_box_5, limit=0xFF, width=10, variable=data['unknown']['unkBytes1_1']).grid(column=1, row=1)
    ttk.Label(unk_box_5, text="unkBytes1_2").grid(column=2, row=0)
    NumEntry(unk_box_5, limit=0xFF, width=10, variable=data['unknown']['unkBytes1_2']).grid(column=2, row=1)

    unk_box_5.pack()

    unk_box_6 = ttk.Frame(tab)
    ttk.Label(unk_box_6, text="unkBytes2_0").grid(column=0, row=0)
    NumEntry(unk_box_6, limit=0xFF, width=10, variable=data['unknown']['unkBytes2_0']).grid(column=0, row=1)
    ttk.Label(unk_box_6, text="unkBytes2_1").grid(column=1, row=0)
    NumEntry(unk_box_6, limit=0xFF, width=10, variable=data['unknown']['unkBytes2_1']).grid(column=1, row=1)

    unk_box_6.pack()

    unk_box_7 = ttk.Frame(tab)
    ttk.Label(unk_box_7, text="unkUint (Always 15...)").grid(column=0, row=0)
    NumEntry(unk_box_7, limit=0xFFFFFFFF, width=25, variable=data['unknown']['unkUintAlways15']).grid(column=0, row=1)

    unk_box_7.pack()

    unk_box_8 = ttk.Frame(tab)
    ttk.Label(unk_box_8, text="unkShort1").grid(column=0, row=0)
    NumEntry(unk_box_8, limit=0xFFFF, width=10, variable=data['unknown']['unkShort1']).grid(column=0, row=1)
    #ttk.Label(unk_box_8, text="unkShort2").grid(column=1, row=0)
    #NumEntry(unk_box_8, limit=0xFFFF, width=10, variable=data['unknown']['unkShort2']).grid(column=1, row=1)

    unk_box_8.pack()

    unk_box_9 = ttk.Frame(tab)
    ttk.Label(unk_box_9, text="unkByte1").grid(column=0, row=0)
    NumEntry(unk_box_9, limit=0xFF, width=10, variable=data['unknown']['unkByte1']).grid(column=0, row=1)
    ttk.Label(unk_box_9, text="unkByte2").grid(column=1, row=0)
    NumEntry(unk_box_9, limit=0xFF, width=10, variable=data['unknown']['unkByte2']).grid(column=1, row=1)
    ttk.Label(unk_box_9, text="unkByte3").grid(column=2, row=0)
    NumEntry(unk_box_9, limit=0xFF, width=10, variable=data['unknown']['unkByte3']).grid(column=2, row=1)

    unk_box_9.pack()

    unk_box_10 = ttk.Frame(tab)
    ttk.Label(unk_box_10, text="unkByte4").grid(column=0, row=0)
    NumEntry(unk_box_10, limit=0xFF, width=10, variable=data['unknown']['unkByte4']).grid(column=0, row=1)
    ttk.Label(unk_box_10, text="unkByte7").grid(column=1, row=0)
    NumEntry(unk_box_10, limit=0xFF, width=10, variable=data['unknown']['unkByte7']).grid(column=1, row=1)
    ttk.Label(unk_box_10, text="unkByte8").grid(column=2, row=0)
    NumEntry(unk_box_10, limit=0xFF, width=10, variable=data['unknown']['unkByte8']).grid(column=2, row=1)

    unk_box_10.pack()


def Arena(tab, data):
    if 'arena_equipment' not in data:
        InitializeArenaEquipment(data)

    loadouts = data['arena_equipment']

    #frameHolder = ttk.Frame(tab, padding=2).grid(sticky='nsew')
    tab.grid_columnconfigure((0,1), weight=1)
    tab.grid_rowconfigure((0,1), weight=1)
    frame1 = ttk.Frame(tab, padding=2)
    frame2 = ttk.Frame(tab, padding=2)
    frame3 = ttk.Frame(tab, padding=2)
    frame4 = ttk.Frame(tab, padding=2)

    def valid_bowgun_start(wepType):
        return wepType.get() == EquipmentClasses.BowgunFrame

    def determine_weapon_enum(wepType, allowBarrelStock=False):
        if wepType.get() == EquipmentClasses.Greatsword:
            return True, Greatsword
        elif wepType.get() == EquipmentClasses.SnS:
            return True, SnS
        elif wepType.get() == EquipmentClasses.Hammer:
            return True, Hammer
        elif wepType.get() == EquipmentClasses.Lance:
            return True, Lance
        elif wepType.get() == EquipmentClasses.BowgunFrame and not allowBarrelStock:
            return True, BowgunFrame
        elif wepType.get() == EquipmentClasses.BowgunBarrel and allowBarrelStock:
            return True, BowgunBarrel
        elif wepType.get() == EquipmentClasses.BowgunStock and allowBarrelStock:
            return True, BowgunStock
        elif wepType.get() == EquipmentClasses.Longsword:
            return True, Longsword
        elif wepType.get() == EquipmentClasses.Switchaxe:
            return True, Switchaxe
        else:
            return False, SnS

    def on_switch_weapon_type(dropdown, wepType, bowgunOnlyDropdowns=[]):
        status, enum = determine_weapon_enum(wepType, allowBarrelStock=len(bowgunOnlyDropdowns)==0)
        dropdown.update_dropdown(enum)
        dropdown['state'] = "readonly" if status else "disabled"
        for dd in bowgunOnlyDropdowns:
            _ = dd.grid() if valid_bowgun_start(wepType) else dd.grid_remove()

    def construct_loadout_slot(loadout, frame, number):
        ttk.Label(frame, text="Loadout "+str(number)).pack(side='top', expand=True)
        weapon12Frame = ttk.Frame(frame, padding=2)
        weapon12TypeDropdown = Dropdown(weapon12Frame, determine_weapon_enum(loadout[1][0], allowBarrelStock=True)[1], variable=loadout[1][1])
        weapon12CategoryDropdown = Dropdown(weapon12Frame, EquipmentClasses,  state='disabled', onSelected=lambda:on_switch_weapon_type(weapon12TypeDropdown, loadout[1][0]), width=13, variable=loadout[1][0])
        weapon13Frame = ttk.Frame(frame, padding=2)
        weapon13TypeDropdown = Dropdown(weapon13Frame, determine_weapon_enum(loadout[2][0], allowBarrelStock=True)[1], variable=loadout[2][1])
        weapon13CategoryDropdown = Dropdown(weapon13Frame, EquipmentClasses,  state='disabled', onSelected=lambda:on_switch_weapon_type(weapon13TypeDropdown, loadout[2][0]), width=13, variable=loadout[2][0])
        
        weapon11Frame = ttk.Frame(frame, padding=2)
        weapon11TypeDropdown = Dropdown(weapon11Frame, determine_weapon_enum(loadout[0][0])[1], variable=loadout[0][1])
        Dropdown(weapon11Frame, EquipmentClasses, onSelected=lambda:on_switch_weapon_type(weapon11TypeDropdown, loadout[0][0], [weapon12CategoryDropdown, weapon13CategoryDropdown, weapon12TypeDropdown, weapon13TypeDropdown]), width=13, variable=loadout[0][0]).grid(column=0,row=0)#.pack(side='left')
        weapon11TypeDropdown.grid(column=1,row=0)#.pack(side='right')
        weapon11Frame.pack()

        weapon12CategoryDropdown.grid(column=0,row=0)#.pack(side='left')
        weapon12TypeDropdown.grid(column=1,row=0)#.pack(side='right')
        weapon12Frame.pack()

        weapon13CategoryDropdown.grid(column=0,row=0)#.pack(side='left')
        weapon13TypeDropdown.grid(column=1,row=0)#.pack(side='right')
        weapon13Frame.pack()

        _ = weapon12CategoryDropdown.grid() if valid_bowgun_start(loadout[0][0]) else weapon12CategoryDropdown.grid_remove()
        _ = weapon12TypeDropdown.grid() if valid_bowgun_start(loadout[0][0]) else weapon12TypeDropdown.grid_remove()
        _ = weapon13CategoryDropdown.grid() if valid_bowgun_start(loadout[0][0]) else weapon13CategoryDropdown.grid_remove()
        _ = weapon13TypeDropdown.grid() if valid_bowgun_start(loadout[0][0]) else weapon13TypeDropdown.grid_remove()

        armor11Frame = ttk.Frame(frame, padding=2)
        armor12Frame = ttk.Frame(frame, padding=2)
        armor13Frame = ttk.Frame(frame, padding=2)

        Dropdown(armor11Frame, Helmet, variable=loadout[3]).pack(side='left')
        Dropdown(armor11Frame, Chestpiece, variable=loadout[4]).pack(side='right')
        Dropdown(armor12Frame, Gauntlets, variable=loadout[5]).pack(side='left')
        Dropdown(armor12Frame, Faulds, variable=loadout[6]).pack(side='right')
        Dropdown(armor13Frame, Leggings, variable=loadout[7]).pack()

        armor11Frame.pack()
        armor12Frame.pack()
        armor13Frame.pack()

        Button(frame, text="Item Pouch", command=lambda:CreateItemPouch(loadout[8], False)).pack()
        Button(frame, text="Gunner's Pouch", command=lambda:CreateItemPouch(loadout[9], True)).pack()

    construct_loadout_slot(loadouts[0], frame1, 1)
    construct_loadout_slot(loadouts[1], frame2, 2)
    construct_loadout_slot(loadouts[2], frame3, 3)
    construct_loadout_slot(loadouts[3], frame4, 4)

    frame1.grid(column=0, row=0, sticky='nsew')
    frame2.grid(column=1, row=0, sticky='nsew')
    frame3.grid(column=0, row=1, sticky='nsew')
    frame4.grid(column=1, row=1, sticky='nsew')


def CreateItemPouch(items, gunner=False):
    t = Toplevel(win)
    if gunner:
        t.wm_title("Ammo Pouch")
        t.geometry('260x198')
    else:
        t.wm_title("Item Pouch")
        t.geometry('520x198')

    t.resizable(False, False)
    tstyle = ttk.Style(t)
    tstyle.theme_use('clam')

    item_width=21
    other_width=4
    page_padding = 10

    pouchFrame = ttk.Frame(t)

    page1Frame = ttk.Frame(pouchFrame, padding=2)
    ttk.Label(page1Frame, text="Ammo" if gunner else "Page 1 Items").grid(column=0, row=0, sticky=W)
    ttk.Label(page1Frame, text="#").grid(column=1, row=0)

    def add_item_row(frame, items, idx):
        AutocompleteDropdown(frame, ItemsType, variable=items[idx][0], width=item_width).grid(column=0, row=1+idx)
        NumEntry(frame, limit=0xFF, variable=items[idx][1], width=other_width).grid(column=1, row=1+idx)

    add_item_row(page1Frame, items, 0)
    add_item_row(page1Frame, items, 1)
    add_item_row(page1Frame, items, 2)
    add_item_row(page1Frame, items, 3)
    add_item_row(page1Frame, items, 4)
    add_item_row(page1Frame, items, 5)
    add_item_row(page1Frame, items, 6)
    add_item_row(page1Frame, items, 7)

    page1Frame.grid(column=0, row=0, padx=(0,page_padding))

    if not gunner:
        page2Frame = ttk.Frame(pouchFrame, padding=2)
        ttk.Label(page2Frame, text="Page 2 Items").grid(column=0, row=0, sticky=W)
        ttk.Label(page2Frame, text="#").grid(column=1, row=0)

        add_item_row(page2Frame, items, 8)
        add_item_row(page2Frame, items, 9)
        add_item_row(page2Frame, items, 10)
        add_item_row(page2Frame, items, 11)
        add_item_row(page2Frame, items, 12)
        add_item_row(page2Frame, items, 13)
        add_item_row(page2Frame, items, 14)
        add_item_row(page2Frame, items, 15)

        page2Frame.grid(column=1, row=0, padx=(0,page_padding))

        page3Frame = ttk.Frame(pouchFrame, padding=2)
        ttk.Label(page3Frame, text="Page 3 Items").grid(column=0, row=0, sticky=W)
        ttk.Label(page3Frame, text="#").grid(column=1, row=0)

        add_item_row(page3Frame, items, 16)
        add_item_row(page3Frame, items, 17)
        add_item_row(page3Frame, items, 18)
        add_item_row(page3Frame, items, 19)
        add_item_row(page3Frame, items, 20)
        add_item_row(page3Frame, items, 21)
        add_item_row(page3Frame, items, 22)
        add_item_row(page3Frame, items, 23)

        page3Frame.grid(column=2, row=0, padx=(0,page_padding))

    pouchFrame.pack()

    t.wait_visibility()
    x = win.winfo_x() + win.winfo_width()//2 - t.winfo_width()//2
    y = win.winfo_y() + win.winfo_height()//2 - t.winfo_height()//2
    t.geometry(f"+{x}+{y}")


def CreateRewards(data, objective=0):
    t = Toplevel(win)
    if objective == 0:
        rewards1 = data['objective_details']['main_quest']['rewards_row_1']
        rewards2 = data['objective_details']['main_quest']['rewards_row_2']
        t.wm_title("Main Quest Rewards")
        t.geometry('580x300')
    elif objective == 1:
        rewards1 = data['objective_details']['subquest_1']['rewards_row_1']
        rewards2 = None
        t.wm_title("Subquest 1 Rewards")
        t.geometry('290x300')
    else:
        rewards1 = data['objective_details']['subquest_2']['rewards_row_1']
        rewards2 = None
        t.wm_title("Subquest 2 Rewards")
        t.geometry('290x300')

    t.resizable(False, False)
    tstyle = ttk.Style(t)
    tstyle.theme_use('clam')

    item_width=25
    other_width=4

    rewardsFrame = ttk.Frame(t)

    mainRewardsFrame = ttk.Frame(rewardsFrame, padding=2)
    Label(mainRewardsFrame, text="Primary Rewards").grid(column=0,row=0,columnspan=2, sticky=W)
    ttk.Label(mainRewardsFrame, text="Item:").grid(column=0,row=1, sticky=W)
    ttk.Label(mainRewardsFrame, text="Amount:").grid(column=1,row=1, sticky=W)
    ttk.Label(mainRewardsFrame, text="Percent:").grid(column=2,row=1, sticky=W)
    
    def add_reward_row(frame, rewards, idx, totalBox):
        AutocompleteDropdown(frame,ItemsType,variable=rewards[idx][0],width=item_width).grid(column=0,row=2+idx)
        NumEntry(frame,limit=0xFF,variable=rewards[idx][1],width=other_width).grid(column=1,row=2+idx)
        percent = NumEntry(frame,limit=100,variable=rewards[idx][2],width=other_width)
        percent.grid(column=2,row=2+idx)
        percent.bind('<KeyRelease>', lambda x:totalBox.config(text=str(sum([rewards[i][2].get() for i in range(11)]))))

    totalPercent1 = ttk.Label(mainRewardsFrame, text=str(sum([rewards1[i][2].get() for i in range(11)])))
    add_reward_row(mainRewardsFrame, rewards1, 0, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 1, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 2, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 3, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 4, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 5, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 6, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 7, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 8, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 9, totalPercent1)
    add_reward_row(mainRewardsFrame, rewards1, 10, totalPercent1)

    ttk.Label(mainRewardsFrame, text="Total Percent:").grid(column=0, row=13, columnspan=2, sticky=E)
    totalPercent1.grid(column=2, row=13, sticky=W)
    mainRewardsFrame.grid(column=0, row=0, padx=(0,20))

    if rewards2 is not None:
        additionalRewardsFrame = ttk.Frame(rewardsFrame, padding=2)
        Label(additionalRewardsFrame, text="Additional Rewards").grid(column=0,row=0,columnspan=2, sticky=W)
        ttk.Label(additionalRewardsFrame, text="Item:").grid(column=0,row=1, sticky=W)
        ttk.Label(additionalRewardsFrame, text="Amount:").grid(column=1,row=1, sticky=W)
        ttk.Label(additionalRewardsFrame, text="Percent:").grid(column=2,row=1, sticky=W)

        totalPercent2 = ttk.Label(additionalRewardsFrame, text=str(sum([rewards2[i][2].get() for i in range(11)])))
        add_reward_row(additionalRewardsFrame, rewards2, 0, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 1, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 2, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 3, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 4, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 5, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 6, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 7, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 8, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 9, totalPercent2)
        add_reward_row(additionalRewardsFrame, rewards2, 10, totalPercent2)

        ttk.Label(additionalRewardsFrame, text="Total Percent:").grid(column=0, row=13, columnspan=2, sticky=E)
        totalPercent2.grid(column=2, row=13, sticky=W)
        additionalRewardsFrame.grid(column=1,row=0, padx=(20,0))
    rewardsFrame.pack()

    t.wait_visibility()
    x = win.winfo_x() + win.winfo_width()//2 - t.winfo_width()//2
    y = win.winfo_y() + win.winfo_height()//2 - t.winfo_height()//2
    t.geometry(f"+{x}+{y}")


def RebuildTab(tab, data, Builder):
    for widget in tab.winfo_children():
        widget.destroy()
    return Builder(tab, data)

def RebuildTabs(data, notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7):
    RebuildTab(tab1, data, QuestInfo)
    for widget in tab2.winfo_children():
        widget.destroy()
    QuestSettings(tab2, data, onAreaChange=on_area_change, onArenaToggle=on_arena_toggle)
    callback2 = RebuildTab(tab3, data, LargeMonsters)
    RebuildTab(tab4, data, Objectives)
    RebuildTab(tab5, data, SmallMonsters)
    RebuildTab(tab6, data, Unknowns)
    RebuildTab(tab7, data, Arena)
    notebook.tab(6, state="normal" if data['quest_info']['flags'][3][4].get() else "hidden")
    return [lambda checkbox:notebook.tab(6, state="normal" if checkbox.get() else "hidden"), callback2]

def LoadBin(win, notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7):
    questdata = LoadFromQuestBinary(win)
    if questdata is not None:
        data = questdata
        arenaCallbacks = RebuildTabs(data, notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7)
        return data, arenaCallbacks
    return None, None

def SaveBin(win, data):
    SaveBinFile(win, data)

def LoadQuest(notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7):
    questdata = LoadQuestFile()
    if questdata is not None:
        data = questdata
        arenaCallbacks = RebuildTabs(data, notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7)
        return data, arenaCallbacks
    return None, None

def SaveQuest(data):
    SaveQuestFile(data)

def resource(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    else:
        return "resources/"+path


VERSION = "0.9.1"

if __name__ == '__main__':
    win = Tk(screenName="MH3 Event Quest Creator")
    win.iconphoto(False, PhotoImage(file=resource('Lagiacrus.png')))
    win.title("SpyRo's Monster Hunter Tri [NA/EU] Event Quest Creator <Beta "+str(VERSION)+">")
    win.geometry('540x540')
    win.resizable(False, False)
    style = ttk.Style(win)
    style.theme_use('clam')

    dataholder = []
    dataholder.append(InitializeDataDict())

    # Create a notebook that holds the tabs
    notebook = ttk.Notebook(win)

    # Create tab frames
    tab1 = ttk.Frame(notebook) # Quest Info
    tab2 = ttk.Frame(notebook) # Quest Settings
    tab3 = ttk.Frame(notebook) # Large Monsters
    tab4 = ttk.Frame(notebook) # Objectives
    tab5 = ttk.Frame(notebook) # Small Monsters
    tab6 = ttk.Frame(notebook) # Unknowns
    tab7 = ttk.Frame(notebook) # Arena

    # Add the tab frames to the notebook
    notebook.add(tab1, text="Quest Info")
    notebook.add(tab2, text="Quest Settings")
    notebook.add(tab3, text="Large Monsters")
    notebook.add(tab4, text="Objectives")
    notebook.add(tab5, text="Minions")
    notebook.add(tab6, text="Unknowns")
    notebook.add(tab7, text="Arena", state="normal" if dataholder[0]['quest_info']['flags'][3][4].get() else "hidden")

    notebook.pack(expand=1, fill='both')

    arenaCallbacks = [
        lambda checkbox:notebook.tab(6, state="normal" if checkbox.get() else "hidden")
    ]
    def on_arena_toggle(checkbox):
        for cb in arenaCallbacks:
            cb(checkbox)
    def on_area_change():
        ClearSmallMonsters(dataholder[0])
        RebuildTab(tab5, dataholder[0], SmallMonsters)
        #RebuildTabs(dataholder[0], notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7)
        #for cb in areachangeCallbacks:
        #    cb()

    QuestInfo(tab1, dataholder[0])
    QuestSettings(tab2, dataholder[0], onAreaChange=on_area_change, onArenaToggle=on_arena_toggle)
    arenacallback2 = LargeMonsters(tab3, dataholder[0])
    Objectives(tab4, dataholder[0])
    SmallMonsters(tab5, dataholder[0])
    Unknowns(tab6, dataholder[0])
    Arena(tab7, dataholder[0])

    arenaCallbacks.append(arenacallback2)

    def BinLoader():
        newData, newArenaCallbacks = LoadBin(win, notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7)
        if newData is not None:
            dataholder[0] = newData
            arenaCallbacks.clear()
            for cb in newArenaCallbacks:
                arenaCallbacks.append(cb)
    def BinSaver():
        SaveBin(win, dataholder[0])
    def Loader():
        newData, newArenaCallbacks = LoadQuest(notebook, on_area_change, on_arena_toggle, tab1, tab2, tab3, tab4, tab5, tab6, tab7)
        if newData is not None:
            dataholder[0] = newData
            arenaCallbacks.clear()
            for cb in newArenaCallbacks:
                arenaCallbacks.append(cb)
    def Saver():
        SaveQuest(dataholder[0])

    frm = Frame(win, width=100)
    frm.pack()
    ttk.Button(frm, text='Load Json', command=Loader).pack(side='left')
    ttk.Button(frm, text='Save', command=Saver).pack(side='left')
    ttk.Button(frm, text='Load Game Binary', command=BinLoader).pack(side='left')
    ttk.Button(frm, text='Overwrite Game Binary (danger)', command=BinSaver).pack(side='left')
    ttk.Button(frm, text='Close', command=exit).pack(side='right')

    win.mainloop()
