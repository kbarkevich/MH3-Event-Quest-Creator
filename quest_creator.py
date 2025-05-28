from tkinter import *
from tkinter import ttk
from ids import *
import webbrowser


def QuestInfo(tab, data):
    questNameFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questNameFrame, text="Quest Name:").pack()
    ttk.Entry(questNameFrame, width=70, validate="key", validatecommand=(tab.register(CharacterLimit), '%P', 12), textvariable=data['quest_info']['name']).pack()
    questNameFrame.pack(side='top', expand=True)

    questSuccessFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questSuccessFrame, text="Success Conditions:").pack()
    ttk.Entry(questSuccessFrame, width=60, textvariable=data['quest_info']['success_message'][0]).pack()
    ttk.Entry(questSuccessFrame, width=60, textvariable=data['quest_info']['success_message'][1]).pack()
    questSuccessFrame.pack(side='top', expand=True)

    questFailFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questFailFrame, text="Fail Conditions:").pack()
    ent1 = ttk.Entry(questFailFrame, width=60)
    ent2 = ttk.Entry(questFailFrame, width=60)
    Prefill(ent1, "Reward hits 0, or time").pack()
    Prefill(ent2, "expires.").pack()
    ent1.configure(state='readonly')
    ent2.configure(state='readonly')
    questFailFrame.pack(side='top', expand=True)

    questClientFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questClientFrame, text="Client:").pack()
    ttk.Entry(questClientFrame, width=60, textvariable=data['quest_info']['client']).pack()
    questClientFrame.pack(side='top', expand=True)

    questDescriptionFrame = ttk.Frame(tab, padding=2, width=40, height=40)
    ttk.Label(questDescriptionFrame, text="Quest Description:").pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][0]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][1]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][2]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][3]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][4]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][5]).pack()
    ttk.Entry(questDescriptionFrame, width=70, textvariable=data['quest_info']['details'][6]).pack()
    questDescriptionFrame.pack(side='bottom', expand=True)

def QuestSettings(tab, data):
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
    ttk.Checkbutton(questFlagsFrame1, text="Unknown1", variable=var11).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Multiple", variable=var12).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Single", variable=var13).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Unknown4", variable=var14).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Jhen", variable=var15).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Shakalaka", variable=var16).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Advanced", variable=var17).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame1, text="Unknown8", variable=var18).pack(side='top', anchor=N+W)

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
    ttk.Checkbutton(questFlagsFrame2, text="Unknown3", variable=var23).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown4", variable=var24).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown5", variable=var25).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown6", variable=var26).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown7", variable=var27).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame2, text="Unknown8", variable=var28).pack(side='top', anchor=N+W)

    var31 = flags[2][0]
    var32 = flags[2][1]
    var33 = flags[2][2]
    var34 = flags[2][3]
    var35 = flags[2][4]
    var36 = flags[2][5]
    var37 = flags[2][6]
    var38 = flags[2][7]
    ttk.Checkbutton(questFlagsFrame3, text="Unstable", variable=var31).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown2", variable=var32).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown3", variable=var33).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown4", variable=var34).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown5", variable=var35).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown6", variable=var36).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown7", variable=var37).pack(side='top', anchor=N+W)
    ttk.Checkbutton(questFlagsFrame3, text="Unknown8", variable=var38).pack(side='top', anchor=N+W)

    basicSettingsFrame = ttk.Frame(tab, padding=2)
    basicSettingsFrame.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
    basicSettingsFrame.columnconfigure((0,1,2), weight=1)
    ttk.Label(basicSettingsFrame, text="Map:").grid(column=0, row=0, padx=10, pady=(15,0), sticky='w')
    Dropdown(basicSettingsFrame, LocationType, variable=data['quest_info']['location'], criteria=lambda a: [x[15:] for x in a if x[:1]!="_"]).grid(column=0,row=1, padx=10, pady=(0,10))

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
    UrlLabel(basicSettingsFrame, "https://imgur.com/a/QPXdMLK/", text="Supply Set:").grid(column=1, row=4, padx=10, sticky='w')
    Dropdown(basicSettingsFrame, list(range(53)), variable=data['quest_info']['supply_set_number']).grid(column=1,row=5, padx=10, pady=(0,10))
    ttk.Label(basicSettingsFrame, text="Delivery Type:").grid(column=2, row=4, padx=10, sticky='w')
    Entry(basicSettingsFrame, state='readonly').grid(column=2, row=5, padx=10, pady=(0,10))

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
    ttk.Checkbutton(menuFlagsFrame, text="Arena", variable=var45).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Unknown2", variable=var46).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Repel", variable=var47).pack(side='top', anchor=N+W)
    ttk.Checkbutton(menuFlagsFrame, text="Unknown3", variable=var48).pack(side='top', anchor=N+W)
    menuFlagsFrame.pack(side='right', expand=True)
    
    

def LargeMonsters(tab, data):

    """
        'type': IntVar(value=Monster.great_jaggi),
        'starting_area': IntVar(value=0x00),
        'boss_id': IntVar(value=0xFF),
        'spawn_count': IntVar(value=0x04),
        'level': IntVar(value=0x17),  # 0x01 through 0x3c
        'size': IntVar(value=0x64),
        'hp_spread': IntVar(value=0x01),  # 0: fixed, 1: spread of 5, 2: spread of 3
        'size_spread': IntVar(value=0x01)
    """

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
    def update_boss1_info_display(e):
        if boss1['type'].get() == 0:
            boss1_label.config(text = "------")
        elif boss1['type'].get() not in MONSTER_HP:
            boss1_label.config(text = "Invalid Monster")
        elif boss1['level'].get() not in LEVELS:
            boss1_label.config(text = "Invalid Level")
        else:
            if boss1['hp_spread'].get() == 2 and boss1['level'].get() - 1 in LEVELS and boss1['level'].get() + 1 in LEVELS:
                boss1_label.config(text = "HP: " + str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()])) +"/"+ str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()+1])))
            elif boss1['hp_spread'].get() == 1 and boss1['level'].get() - 2 in LEVELS and boss1['level'].get() + 2 in LEVELS:
                boss1_label.config(text = "HP: " + str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()-2])) +"/"+ str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()])) +"/"+ str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()+1])) +"/"+str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()+2])))
            else:
                boss1_label.config(text = "HP: " + str(int(MONSTER_HP[boss1['type'].get()] * LEVELS[boss1['level'].get()])))
    update_boss1_info_display(None)
    updater1.onSelected = lambda:update_boss1_info_display(None)
    updater2.bind('<KeyRelease>', update_boss1_info_display)
    updater3.onSelected = lambda:update_boss1_info_display(None)

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
    def update_boss2_info_display(e):
        if boss2['type'].get() == 0:
            boss2_label.config(text = "------")
        elif boss2['type'].get() not in MONSTER_HP:
            boss2_label.config(text = "Invalid Monster")
        elif boss2['level'].get() not in LEVELS:
            boss2_label.config(text = "Invalid Level")
        else:
            if boss2['hp_spread'].get() == 2 and boss2['level'].get() - 1 in LEVELS and boss2['level'].get() + 1 in LEVELS:
                boss2_label.config(text = "HP: " + str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()])) +"/"+ str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()+1])))
            elif boss2['hp_spread'].get() == 1 and boss2['level'].get() - 2 in LEVELS and boss2['level'].get() + 2 in LEVELS:
                boss2_label.config(text = "HP: " + str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()-2])) +"/"+ str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()])) +"/"+ str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()+1])) +"/"+str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()+2])))
            else:
                boss2_label.config(text = "HP: " + str(int(MONSTER_HP[boss2['type'].get()] * LEVELS[boss2['level'].get()])))
    update_boss2_info_display(None)
    updater1.onSelected = lambda:update_boss2_info_display(None)
    updater2.bind('<KeyRelease>', update_boss2_info_display)
    updater3.onSelected = lambda:update_boss2_info_display(None)

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
    def update_boss3_info_display(e):
        if boss3['type'].get() == 0:
            boss3_label.config(text = "------")
        elif boss3['type'].get() not in MONSTER_HP:
            boss3_label.config(text = "Invalid Monster")
        elif boss3['level'].get() not in LEVELS:
            boss3_label.config(text = "Invalid Level")
        else:
            if boss3['hp_spread'].get() == 2 and boss3['level'].get() - 1 in LEVELS and boss3['level'].get() + 1 in LEVELS:
                boss3_label.config(text = "HP: " + str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()])) +"/"+ str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()+1])))
            elif boss3['hp_spread'].get() == 1 and boss3['level'].get() - 2 in LEVELS and boss3['level'].get() + 2 in LEVELS:
                boss3_label.config(text = "HP: " + str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()-2])) +"/"+ str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()-1])) +"/"+ str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()])) +"/"+ str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()+1])) +"/"+str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()+2])))
            else:
                boss3_label.config(text = "HP: " + str(int(MONSTER_HP[boss3['type'].get()] * LEVELS[boss3['level'].get()])))
    update_boss3_info_display(None)
    updater1.onSelected = lambda:update_boss3_info_display(None)
    updater2.bind('<KeyRelease>', update_boss3_info_display)
    updater3.onSelected = lambda:update_boss3_info_display(None)

    summon = data['quest_info']['summon']
    bossInvaderFrame = ttk.Frame(tab, padding=2)
    ttk.Label(bossInvaderFrame, text="Invader", font=("Arial", 12, "bold")).grid(column=0, row=0, sticky='w')
    ttk.Label(bossInvaderFrame, text="%:").grid(column=0, row=1, sticky='w')
    NumEntry(bossInvaderFrame, limit=0x64, variable=summon[0]).grid(column=0, row=2, pady=(0, 20))
    ttk.Label(bossInvaderFrame, text="Unk 1:").grid(column=1, row=1, sticky='sw')
    NumEntry(bossInvaderFrame, limit=0xFF, variable=summon[1]).grid(column=1, row=2, pady=(0, 20))
    ttk.Label(bossInvaderFrame, text="Unk 2:").grid(column=2, row=1, sticky='sw')
    NumEntry(bossInvaderFrame, limit=0xFF, variable=summon[2]).grid(column=2, row=2, pady=(0, 20))
    Dropdown(bossInvaderFrame, InvaderType, summon[3], criteria=lambda a: [x[:-3].replace("_"," ") for x in a if x[:1]!="_"]).grid(column=3, row=2, pady=(0, 20), columnspan=2, sticky=W+E)

    boss1Frame.pack(side='top', anchor='n')
    boss2Frame.pack(side='top', anchor='n')
    boss3Frame.pack(side='top', anchor='n')
    bossInvaderFrame.pack(side='bottom', anchor='n')

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
    ttk.Entry(mainDescriptionFrame, width=60, textvariable=data['quest_info']['description'][0]).pack(expand=True)
    ttk.Entry(mainDescriptionFrame, width=60, textvariable=data['quest_info']['description'][1]).pack(expand=True)
    mainDescriptionFrame.pack(expand=True)

    mainMonetaryFrame = ttk.Frame(mainTab, padding=2)
    ttk.Label(mainMonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    NumEntry(mainMonetaryFrame, limit=0xFFFF, variable=main['zenny_reward']).grid(column=0, row=1)
    ttk.Label(mainMonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    NumEntry(mainMonetaryFrame, limit=0xFFFF, variable=main['hrp_reward']).grid(column=1, row=1)
    mainMonetaryFrame.pack(expand=True)

    mainFlagsFrame = ttk.Frame(mainTab, padding=2, width=100)
    ttk.Label(mainFlagsFrame, text="Objective Flags:").grid(column=1,row=0)

    mainTargetFrame = ttk.Frame(mainTab, padding=2)
    targetDropdown = AutocompleteDropdown(mainTargetFrame, Monster, variable=main['objective_type'])

    mainFlagsFrame1 = ttk.Frame(mainFlagsFrame, padding=2)
    varMain11 = main['type'][0][0]
    varMain12 = main['type'][0][1]
    varMain13 = main['type'][0][2]
    varMain14 = main['type'][0][3]
    varMain15 = main['type'][0][4]
    varMain16 = main['type'][0][5]
    varMain17 = main['type'][0][6]
    varMain18 = main['type'][0][7]

    def update_target_dropdown():
        if varMain11.get() or varMain13.get():
            targetDropdown.update_dropdown(Monster)
        elif varMain12.get():
            targetDropdown.update_dropdown(ItemsType)
        else:
            targetDropdown.update_dropdown(list(range(0x100)))

    ttk.Checkbutton(mainFlagsFrame1, text="Monster", variable=varMain11, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Item", variable=varMain12, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Target", variable=varMain13, command=update_target_dropdown).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown4", variable=varMain14).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown5", variable=varMain15).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown6", variable=varMain16).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Unknown7", variable=varMain17).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame1, text="Capture", variable=varMain18).pack(side='top', anchor=N+W)
    mainFlagsFrame1.grid(column=0, row=1, sticky='w')

    mainFlagsFrame2 = ttk.Frame(mainFlagsFrame, padding=2)
    varMain21 = main['type'][1][0]
    varMain22 = main['type'][1][1]
    varMain23 = main['type'][1][2]
    varMain24 = main['type'][1][3]
    varMain25 = main['type'][1][4]
    varMain26 = main['type'][1][5]
    varMain27 = main['type'][1][6]
    varMain28 = main['type'][1][7]
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown1", variable=varMain21).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Enemy Part", variable=varMain22).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Hit Points", variable=varMain23).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown4", variable=varMain24).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown5", variable=varMain25).pack(side='top', anchor=N+W)
    ttk.Checkbutton(mainFlagsFrame2, text="Unknown6", variable=varMain26).pack(side='top', anchor=N+W)
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
    NumEntry(mainTargetFrame, limit=0xFF, variable=main['objective_num']).grid(column=1, row=1, pady=(0,10))
    mainTargetFrame.pack(expand=True)

    ttk.Button(mainTab, text='Item Rewards', command=CreateMainRewards).pack(expand=True)

    # SUBQUEST 1

    sub1DescriptionFrame = ttk.Frame(sub1Tab, padding=2)
    ttk.Label(sub1DescriptionFrame, text="Subquest 1 Description:").pack()
    ttk.Entry(sub1DescriptionFrame, width=60).pack()
    sub1DescriptionFrame.pack(expand=True)

    sub1MonetaryFrame = ttk.Frame(sub1Tab, padding=2)
    ttk.Label(sub1MonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    Entry(sub1MonetaryFrame).grid(column=0, row=1)
    ttk.Label(sub1MonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    Entry(sub1MonetaryFrame).grid(column=1, row=1)
    sub1MonetaryFrame.pack(expand=True)

    sub1FlagsFrame = ttk.Frame(sub1Tab, padding=2, width=100)
    ttk.Label(sub1FlagsFrame, text="Subquest 1 Flags:").grid(column=1,row=0)

    sub1FlagsFrame1 = ttk.Frame(sub1FlagsFrame, padding=2)
    varSub111 = BooleanVar()
    varSub112 = BooleanVar()
    varSub113 = BooleanVar()
    varSub114 = BooleanVar()
    varSub115 = BooleanVar()
    varSub116 = BooleanVar()
    varSub117 = BooleanVar()
    varSub118 = BooleanVar()
    ttk.Checkbutton(sub1FlagsFrame1, text="Monster", variable=varSub111).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Item", variable=varSub112).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Target", variable=varSub113).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown4", variable=varSub114).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown5", variable=varSub115).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown6", variable=varSub116).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Unknown7", variable=varSub117).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame1, text="Capture", variable=varSub118).pack(side='top', anchor=N+W)
    sub1FlagsFrame1.grid(column=0, row=1, sticky='w')

    sub1FlagsFrame2 = ttk.Frame(sub1FlagsFrame, padding=2)
    varSub121 = BooleanVar()
    varSub122 = BooleanVar()
    varSub123 = BooleanVar()
    varSub124 = BooleanVar()
    varSub125 = BooleanVar()
    varSub126 = BooleanVar()
    varSub127 = BooleanVar()
    varSub128 = BooleanVar()
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown1", variable=varSub121).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Enemy Part", variable=varSub122).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Hit Points", variable=varSub123).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown4", variable=varSub124).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown5", variable=varSub125).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown6", variable=varSub126).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown7", variable=varSub127).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub1FlagsFrame2, text="Unknown8", variable=varSub128).pack(side='top', anchor=N+W)
    sub1FlagsFrame2.grid(column=1, row=1, sticky='w')

    sub1FlagsFrame3 = ttk.Frame(sub1FlagsFrame, padding=2)
    varSub131 = BooleanVar()
    varSub132 = BooleanVar()
    varSub133 = BooleanVar()
    varSub134 = BooleanVar()
    varSub135 = BooleanVar()
    varSub136 = BooleanVar()
    varSub137 = BooleanVar()
    varSub138 = BooleanVar()
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

    sub1TargetFrame = ttk.Frame(sub1Tab, padding=2)
    ttk.Label(sub1TargetFrame, text="Target:").grid(column=0, row=0, sticky='w')
    Entry(sub1TargetFrame).grid(column=0, row=1, pady=(0,10))
    ttk.Label(sub1TargetFrame, text="Value:").grid(column=1, row=0, sticky='w')
    Entry(sub1TargetFrame).grid(column=1, row=1, pady=(0,10))
    sub1TargetFrame.pack(expand=True)

    ttk.Button(sub1Tab, text='Item Rewards').pack(expand=True)

    # SUBQUEST 2

    sub2DescriptionFrame = ttk.Frame(sub2Tab, padding=2)
    ttk.Label(sub2DescriptionFrame, text="Subquest 2 Description:").pack()
    ttk.Entry(sub2DescriptionFrame, width=60).pack()
    sub2DescriptionFrame.pack(expand=True)

    sub2MonetaryFrame = ttk.Frame(sub2Tab, padding=2)
    ttk.Label(sub2MonetaryFrame, text="Zenny Reward:").grid(column=0, row=0, sticky='w')
    Entry(sub2MonetaryFrame).grid(column=0, row=1)
    ttk.Label(sub2MonetaryFrame, text="Hunter Rank Points:").grid(column=1, row=0, sticky='w')
    Entry(sub2MonetaryFrame).grid(column=1, row=1)
    sub2MonetaryFrame.pack(expand=True)

    sub2FlagsFrame = ttk.Frame(sub2Tab, padding=2, width=100)
    ttk.Label(sub2FlagsFrame, text="Subquest 2 Flags:").grid(column=1,row=0)

    sub2FlagsFrame1 = ttk.Frame(sub2FlagsFrame, padding=2)
    varSub211 = BooleanVar()
    varSub212 = BooleanVar()
    varSub213 = BooleanVar()
    varSub214 = BooleanVar()
    varSub215 = BooleanVar()
    varSub216 = BooleanVar()
    varSub217 = BooleanVar()
    varSub218 = BooleanVar()
    ttk.Checkbutton(sub2FlagsFrame1, text="Monster", variable=varSub211).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Item", variable=varSub212).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Target", variable=varSub213).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown4", variable=varSub214).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown5", variable=varSub215).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown6", variable=varSub216).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Unknown7", variable=varSub217).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame1, text="Capture", variable=varSub218).pack(side='top', anchor=N+W)
    sub2FlagsFrame1.grid(column=0, row=1, sticky='w')

    sub2FlagsFrame2 = ttk.Frame(sub2FlagsFrame, padding=2)
    varSub221 = BooleanVar()
    varSub222 = BooleanVar()
    varSub223 = BooleanVar()
    varSub224 = BooleanVar()
    varSub225 = BooleanVar()
    varSub226 = BooleanVar()
    varSub227 = BooleanVar()
    varSub228 = BooleanVar()
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown1", variable=varSub221).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Enemy Part", variable=varSub222).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Hit Points", variable=varSub223).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown4", variable=varSub224).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown5", variable=varSub225).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown6", variable=varSub226).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown7", variable=varSub227).pack(side='top', anchor=N+W)
    ttk.Checkbutton(sub2FlagsFrame2, text="Unknown8", variable=varSub228).pack(side='top', anchor=N+W)
    sub2FlagsFrame2.grid(column=1, row=1, sticky='w')

    sub2FlagsFrame3 = ttk.Frame(sub2FlagsFrame, padding=2)
    varSub231 = BooleanVar()
    varSub232 = BooleanVar()
    varSub233 = BooleanVar()
    varSub234 = BooleanVar()
    varSub235 = BooleanVar()
    varSub236 = BooleanVar()
    varSub237 = BooleanVar()
    varSub238 = BooleanVar()
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

    sub2TargetFrame = ttk.Frame(sub2Tab, padding=2)
    ttk.Label(sub2TargetFrame, text="Target:").grid(column=0, row=0, sticky='w')
    Entry(sub2TargetFrame).grid(column=0, row=1, pady=(0,10))
    ttk.Label(sub2TargetFrame, text="Value:").grid(column=1, row=0, sticky='w')
    Entry(sub2TargetFrame).grid(column=1, row=1, pady=(0,10))
    sub2TargetFrame.pack(expand=True)

    ttk.Button(sub2Tab, text='Item Rewards').pack(expand=True)

class ScrolledCanvas():
    def __init__(self, root, color='brown'):
        canv = Canvas(root, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)                

        ##---------- scrollregion has to be larger than canvas size
        ##           otherwise it just stays in the visible canvas
        canv.config(scrollregion=(0,0,300, 1000))         
        canv.config(highlightthickness=0)                 

        ybar = Scrollbar(root)
        ybar.config(command=canv.yview)                   
        ## connect the two widgets together
        canv.config(yscrollcommand=ybar.set)              
        ybar.pack(side=RIGHT, fill=Y)                     
        canv.pack(side=LEFT, expand=YES, fill=BOTH)       

        bg_color=True
        for ctr in range(10):
            clr="lightgrey"
            if bg_color:
                clr="white"
            bg_color= not bg_color
            frm = ttk.Frame(root, padding=2)#,width=960, height=100,
                        #bd=2, relief=SUNKEN)
            #Label(frm, text="Frame #"+str(ctr+1),
            #      bg=clr).grid()
            Label(frm, text="", bg=clr).grid(column=0, row=0, columnspan=2, sticky='ew')
            Label(frm, text="Var:", bg=clr).grid(column=2, row=0, sticky='ew')
            Label(frm, text="Room:", bg=clr).grid(column=3, row=0, sticky='ew')
            Label(frm, text="Quantity:", bg=clr).grid(column=4, row=0, sticky='ew')
            Label(frm, text="Unk 1:", bg=clr).grid(column=5, row=0, sticky='ew')
            ttk.Entry(frm, width=26).grid(column=0, row=1, columnspan=2, sticky=W+E)
            ttk.Entry(frm, width=13).grid(column=2, row=1)
            ttk.Entry(frm, width=13).grid(column=3, row=1)
            ttk.Entry(frm, width=13).grid(column=4, row=1)
            ttk.Entry(frm, width=13).grid(column=5, row=1)
            Label(frm, text="Pos X:", bg=clr).grid(column=0, row=2, sticky='ew')
            Label(frm, text="Pos Y:", bg=clr).grid(column=1, row=2, sticky='ew')
            Label(frm, text="Pos Z:", bg=clr).grid(column=2, row=2, sticky='ew')
            Label(frm, text="Rot X:", bg=clr).grid(column=3, row=2, sticky='ew')
            Label(frm, text="Rot Y:", bg=clr).grid(column=4, row=2, sticky='ew')
            Label(frm, text="Rot Z:", bg=clr).grid(column=5, row=2, sticky='ew')
            ttk.Entry(frm, width=13).grid(column=0, row=3)
            ttk.Entry(frm, width=13).grid(column=1, row=3)
            ttk.Entry(frm, width=13).grid(column=2, row=3)
            ttk.Entry(frm, width=13).grid(column=3, row=3)
            ttk.Entry(frm, width=13).grid(column=4, row=3)
            ttk.Entry(frm, width=13).grid(column=5, row=3)
            canv.create_window(3,3+(95*ctr),anchor=NW, window=frm)

def SmallMonsters(tab, data):
    minionLevelFrame = ttk.Frame(tab, padding=2)
    ttk.Label(minionLevelFrame, text="Small Monster Map Settings").grid(column=0, row=0, padx=(0, 125), sticky='w')
    ttk.Label(minionLevelFrame, text="Minion Level:").grid(column=1, row=0, padx=(50, 0), sticky='e')
    Entry(minionLevelFrame).grid(column=2, row=0, sticky='w')
    minionLevelFrame.pack(side='top')

    # Create a notebook that holds the tabs
    objectivesNotebook = ttk.Notebook(tab)
    # Create tab frames
    wave1Tab = ttk.Frame(objectivesNotebook) # Quest Info
    wave2Tab = ttk.Frame(objectivesNotebook) # Quest Settings
    wave3Tab = ttk.Frame(objectivesNotebook) # Large Monsters
    # Add tabs
    objectivesNotebook.add(wave1Tab, text="Wave 1")
    objectivesNotebook.add(wave2Tab, text="Wave 2")
    objectivesNotebook.add(wave3Tab, text="Wave 3")
    objectivesNotebook.pack(expand=1, fill='both')
    
    ScrolledCanvas(wave1Tab, color='grey')
    ScrolledCanvas(wave2Tab, color='grey')
    ScrolledCanvas(wave3Tab, color='grey')
    """
    h = Scrollbar(wave1Tab)
    h.pack(side='right', fill=Y)
    for i in range(30):
        myFrame = ttk.Frame(wave1Tab)
        Entry(myFrame).pack(side='left')
        Entry(myFrame).pack(side='left')
        Entry(myFrame).pack(side='left')
        myFrame.pack(side='top')
    """

    mainMonstersFrame = ttk.Frame(tab, padding=2)
    ttk.Label(mainMonstersFrame, text="Main Monsters:").grid(column=0, row=0, sticky='w')
    Entry(mainMonstersFrame).grid(column=0, row=1)
    Entry(mainMonstersFrame).grid(column=1, row=1)
    mainMonstersFrame.pack()

    waveConditionsFrame = ttk.Frame(tab, padding=2)
    ttk.Label(waveConditionsFrame, text="Second Wave Condition:").grid(column=0, row=0)
    ttk.Label(waveConditionsFrame, text="Number:").grid(column=1, row=0)
    Entry(waveConditionsFrame).grid(column=0, row=1)
    Entry(waveConditionsFrame).grid(column=1, row=1)
    ttk.Label(waveConditionsFrame, text="Third Wave Condition:").grid(column=0, row=2)
    ttk.Label(waveConditionsFrame, text="Number:").grid(column=1, row=2)
    Entry(waveConditionsFrame).grid(column=0, row=3)
    Entry(waveConditionsFrame).grid(column=1, row=3)
    waveConditionsFrame.pack()

def Unknowns(tab, data):
    ttk.Label(tab, text="Type something:").pack()
    Entry(tab, width=100).pack()


def CreateMainRewards():
    t = Toplevel(win)
    t.wm_title("Main Quest Rewards")
    t.geometry('580x340')
    t.resizable(False, False)
    tstyle = ttk.Style(t)
    tstyle.theme_use('clam')

    item_width=25
    other_width=4

    rewardsFrame = ttk.Frame(t)

    mainRewardsFrame = ttk.Frame(rewardsFrame, padding=2)
    #mainRewardsFrame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
    #mainRewardsFrame.grid_columnconfigure(0, weight=5)
    #mainRewardsFrame.grid_columnconfigure(1, weight=1)
    #mainRewardsFrame.grid_columnconfigure(2, weight=1)
    Label(mainRewardsFrame, text="Main Rewards").grid(column=0,row=0,columnspan=2, sticky=W)
    Label(mainRewardsFrame, text="Item:").grid(column=0,row=1, sticky=W)
    Label(mainRewardsFrame, text="Amount:").grid(column=1,row=1, sticky=W)
    Label(mainRewardsFrame, text="Percent:").grid(column=2,row=1, sticky=W)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=2)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=2)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=2)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=3)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=3)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=3)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=4)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=4)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=4)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=5)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=5)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=5)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=6)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=6)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=6)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=7)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=7)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=7)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=8)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=8)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=8)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=9)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=9)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=9)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=10)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=10)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=10)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=11)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=11)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=11)
    Entry(mainRewardsFrame,width=item_width).grid(column=0,row=12)
    Entry(mainRewardsFrame,width=other_width).grid(column=1,row=12)
    Entry(mainRewardsFrame,width=other_width).grid(column=2,row=12)
    Label(mainRewardsFrame, text="Total Percent:").grid(column=0, row=13, columnspan=2, sticky=E)
    Label(mainRewardsFrame, text="").grid(column=2, row=13, sticky=W)
    mainRewardsFrame.grid(column=0, row=0, padx=(0,20))

    additionalRewardsFrame = ttk.Frame(rewardsFrame, padding=2)
    Label(additionalRewardsFrame, text="Additional Rewards").grid(column=0,row=0,columnspan=2, sticky=W)
    Label(additionalRewardsFrame, text="Item:").grid(column=0,row=1, sticky=W)
    Label(additionalRewardsFrame, text="Amount:").grid(column=1,row=1, sticky=W)
    Label(additionalRewardsFrame, text="Percent:").grid(column=2,row=1, sticky=W)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=2)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=2)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=2)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=3)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=3)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=3)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=4)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=4)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=4)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=5)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=5)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=5)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=6)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=6)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=6)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=7)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=7)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=7)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=8)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=8)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=8)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=9)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=9)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=9)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=10)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=10)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=10)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=11)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=11)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=11)
    Entry(additionalRewardsFrame,width=item_width).grid(column=0,row=12)
    Entry(additionalRewardsFrame,width=other_width).grid(column=1,row=12)
    Entry(additionalRewardsFrame,width=other_width).grid(column=2,row=12)
    Label(additionalRewardsFrame, text="Total Percent:").grid(column=0, row=13, columnspan=2, sticky=E)
    Label(additionalRewardsFrame, text="").grid(column=2, row=13, sticky=W)
    additionalRewardsFrame.grid(column=1,row=0, padx=(20,0))
    rewardsFrame.pack()


def CharacterLimit(P, limit):
    if len(P) > int(limit):
        return False
    return True


def Prefill(entry, text):
    entry.insert(0, text)
    return entry


class NumEntry(Entry):
    def __init__(self, master, limit=None, variable=None, **kwargs):
        if variable is not None:
            self.variable = variable
        else:
            self.variable = IntVar()
        super().__init__(master, validate="key", validatecommand=(master.register(self.check), '%P', limit), **kwargs)
        Prefill(self, str(self.variable.get()))

    def check(self, P, limit):
        if P.isdigit() and (limit is None or int(P) <= int(limit)):
            self.variable.set(int(P))
            return True
        return False


class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list, callback=None):
        """Use our completion list as our drop down selection menu, arrows move through menu."""
        try:
            self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
        except:
            self._completion_list = sorted(completion_list) # Work with a sorted list
        self.autocompleteCallback = callback
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list  # Setup our popup menu

    def autocomplete(self, delta=0):
        """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
        if delta: # need to delete selection otherwise we would fix the current position
            self.delete(self.position, END)
        else: # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()): # Match case insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits=_hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0,END)
            self.insert(0,self._hits[self._hit_index])
            self.select_range(self.position,END)
            self.autocompleteCallback()

    def handle_keyrelease(self, event):
        """event handler for the keyrelease event on this widget"""
        if event.keysym == "BackSpace":
            self.delete(self.index(INSERT), END)
            self.position = self.index(END)
        if event.keysym == "Left":
            if self.position < self.index(END): # delete the selection
                self.delete(self.position, END)
            else:
                self.position = self.position-1 # delete one character
                self.delete(self.position, END)
        if event.keysym == "Right":
            self.position = self.index(END) # go to end (no selection)
        if len(event.keysym) == 1:
            self.autocomplete()
        # No need for up/down, we'll jump to the popup
        # list at the position of the autocompletion


class AutocompleteDropdown(AutocompleteCombobox):
    def __init__(self, master, optionEnum, variable=None, criteria=None, onSelected=None, width=None, **kwargs):
        self.criteria = criteria
        if variable is not None:
            self.variable = variable
        else:
            self.variable = IntVar()
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        if width is None:
            self.width = 20 - 3
        else:
            self.width = width - 3
        super().__init__(master, width=self.width, **kwargs)
        self.set_completion_list(options, callback=self.callback)
        self.config(values=options)
        self.current(self.variable.get())
        self.onSelected = onSelected
        self.bind("<<ComboboxSelected>>", self.callback)

    def callback(self, *args):
        self.variable.set(self.current())
        if self.onSelected is not None:
            self.onSelected()

    def update_dropdown(self, optionEnum):
        self.variable.set(0)
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        self.set_completion_list(options, callback=self.callback)
        self['values'] = options
        self.current(self.variable.get())


class Dropdown(ttk.Combobox):
    def __init__(self, master, optionEnum, variable=None, criteria=None, onSelected=None, width=None, **kwargs):
        self.criteria = criteria
        if variable is not None:
            self.variable = variable
        else:
            self.variable = IntVar()
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        if width is None:
            self.width = 20 - 3
        else:
            self.width = width - 3
        super().__init__(master, state='readonly', width=self.width, **kwargs)
        self.config(values=options)
        self.current(self.variable.get())
        self.onSelected = onSelected
        self.bind("<<ComboboxSelected>>", self.callback)

    def callback(self, *args):
        self.variable.set(self.current())
        if self.onSelected is not None:
            self.onSelected()

    def update_dropdown(self, optionEnum):
        self.variable.set(0)
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        self['values'] = options
        self.current(self.variable.get())

class UrlLabel(Label):
    def __init__(self, master, url, **kwargs):
        super().__init__(master, cursor='question_arrow', **kwargs)
        self.url = url
        self.bind("<Button-1>", lambda _: self.open_url())

    def open_url(self):
        webbrowser.open_new_tab(self.url)


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
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
                'variant': 2,'room': 3,'quantity': 2,
                'pos_x': 177.92,'pos_y': 450.70,'pos_z': -32.21,
                'rot_x': 0,'rot_y': -238,'rot_z': 0,
            },
            {
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
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
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
                'variant': 1,'room': 9,'quantity': -1,
                'pos_x': -1713.72,'pos_y': 1262.50,'pos_z': 2199.24,
                'rot_x': 273,'rot_y': -45,'rot_z': 0,
            },
            {
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
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
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
                'variant': 0,'room': 11,'quantity': 2,
                'pos_x': -434.00,'pos_y': 198.96,'pos_z': 289.52,
                'rot_x': 0,'rot_y': -267,'rot_z': 0,
            },
            {
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
                'variant': 0,'room': 11,'quantity': 2,
                'pos_x': -802.69,'pos_y': 198.96,'pos_z': 66.62,
                'rot_x': 0,'rot_y': -216,'rot_z': 0,
            },
            {
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
                'variant': 0,'room': 11,'quantity': 2,
                'pos_x': -645.14,'pos_y': 288.96,'pos_z': -371.21,
                'rot_x': 0,'rot_y': -227,'rot_z': 0,
            },
            {
                'type': Monster.bnahabra3,'unk1': 1,'unk2': 0xFF,
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
        'main_monster_1': Monster.bnahabra2,
        'main_monster_2': Monster.melynx,
        'location': IntVar(value=LocationType.QUEST_LOCATION_SANDY_PLAINS),
        'quest_rank': IntVar(value=QuestRankType.star_1),
        'hrp_restriction': IntVar(value=QuestRestrictionType.RESTRICTION_NONE),
        'resources': IntVar(value=ResourcesType.low_rank),
        'supply_set_number': IntVar(value=19),
        'starting_position': IntVar(value=StartingPositionType.camp),
        'general_enemy_level': 0x0017,
        'summon': (
            IntVar(value=0x64),
            IntVar(value=0x05),
            IntVar(value=0x02),
            IntVar(value=0x19)
        ),#(0x64050219),
        'wave_1_transition_type': WaveType.none,
        'wave_1_transition_target': 0x0000,
        'wave_1_transition_quantity': 0x0000,
        'wave_2_transition_type': WaveType.none,
        'wave_2_transition_target': 0x0000,
        'wave_2_transition_quantity': 0x0000,
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
                (IntVar(value=ItemsType.great_jagi_head), IntVar(value=1), IntVar(value=25))
            ],
            'rewards_row_2': [
                (IntVar(value=ItemsType.mystery_charm), IntVar(value=1), IntVar(value=1)),
                (IntVar(value=ItemsType.aquaglow_jewel), IntVar(value=1), IntVar(value=1)),
                (IntVar(value=ItemsType.shining_charm), IntVar(value=1), IntVar(value=1)),
                (IntVar(value=ItemsType.armor_sphere), IntVar(value=1), IntVar(value=1)),
                (IntVar(value=ItemsType.armor_sphere_plus), IntVar(value=1), IntVar(value=1))
            ],
        },
        'subquest_1': {
            'description': "Hunt 2 Great Jaggi",
            'type': 0x00000001,
            'objective_type': Monster.great_jaggi,
            'objective_num': 0x02,
            'zenny_reward': 4000,
            'hrp_reward': 440,
            'rewards_row_1': [
                (ItemsType.great_jagi_claw, 1, 1),
                (ItemsType.great_jagi_hide, 1, 1),
                (ItemsType.jagi_scale, 1, 1),
                (ItemsType.screamer, 1, 1),
                (ItemsType.kings_frill, 1, 1),
                (ItemsType.bone_husk_s, 8, 1),
                (ItemsType.great_jagi_head, 1, 1)
            ],
        },
        'subquest_2': {
            'description': "None",
            'type': 0,
            'objective_type': Monster.none,
            'objective_num': 0,
            'zenny_reward': 0,
            'hrp_reward': 0,
            'rewards_row_1': [],
        }
    },
    'unknown': {
        # (2 for large mon quest, 3 for small/delivery, 5 for jhen/ala)
        'unk_12': 0x00000002,
        'unk_4': 0x00,
        'unk_5': 0x00,
        'unk_6': 0x00,
        'unk_7': 0x00000000,
    }
}
    return data


win = Tk(screenName="MH3 Event Quest Creator")
win.title("SpyRo's Monster Hunter Tri [NA/EU] Event Quest Creator <Alpha 0.0.1>")
win.geometry('540x540')
win.resizable(False, False)
style = ttk.Style(win)
style.theme_use('clam')

data = InitializeDataDict()

# Create a notebook that holds the tabs
notebook = ttk.Notebook(win)

# Create tab frames
tab1 = ttk.Frame(notebook) # Quest Info
tab2 = ttk.Frame(notebook) # Quest Settings
tab3 = ttk.Frame(notebook) # Large Monsters
tab4 = ttk.Frame(notebook) # Objectives
tab5 = ttk.Frame(notebook) # Small Monsters
tab6 = ttk.Frame(notebook) # Unknowns

# Add the tab frames to the notebook
notebook.add(tab1, text="Quest Info")
notebook.add(tab2, text="Quest Settings")
notebook.add(tab3, text="Large Monsters")
notebook.add(tab4, text="Objectives")
notebook.add(tab5, text="Small Monsters")
notebook.add(tab6, text="Unknowns")

notebook.pack(expand=1, fill='both')

QuestInfo(tab1, data)
QuestSettings(tab2, data)
LargeMonsters(tab3, data)
Objectives(tab4, data)
SmallMonsters(tab5, data)
Unknowns(tab6, data)

#frm = ttk.Frame(win, padding=10)
#frm.grid()
frm = Frame(win, width=100)
frm.pack()
ttk.Button(frm, text='Load').pack(side='left')
ttk.Button(frm, text='Save', command=lambda: print(data['objective_details']['main_quest']['objective_type'].get())).pack(side='left')#.grid(column=0, row=0)
ttk.Button(frm, text='Close').pack(side='right')#.grid(column=1,row=0)

win.mainloop()
