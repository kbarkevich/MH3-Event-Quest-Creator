from tkinter import *
from tkinter import ttk
from ids import *
import webbrowser


def CharacterLimit(P, limit):
    if len(P) > int(limit):
        return False
    return True


def Prefill(entry, text):
    entry.insert(0, text)
    return entry


class NumEntry(Entry):
    def __init__(self, master, limit=None, variable=None, decimal=True, allowNeg=False, **kwargs):
        self.decimal = decimal
        self.allowNeg = allowNeg
        if variable is not None:
            self.variable = variable
        else:
            self.variable = IntVar() if self.decimal else DoubleVar()
        super().__init__(master, validate="key", validatecommand=(master.register(self.check), '%P', limit), **kwargs)
        Prefill(self, str(self.variable.get()))

    def check(self, P, limit):
        if self.decimal:
            if self.allowNeg:
                try:
                    val = int(P)
                except:
                    return False
                if limit is None or (val <= int(limit)/2 and val > -int(limit)/2):
                    self.variable.set(val)
                    return True
                return False
            else:
                if P.isdigit() and (limit is None or int(P) <= int(limit)):
                    self.variable.set(int(P))
                    return True
                return False
        else:
            try:
                val = float(P)
            except:
                return False
            if limit is None or (((not self.allowNeg) and val >= 0.0 and val <= float(limit)) or (self.allowNeg and val <= float(limit)/2 and val > -float(limit)/2)):
                self.variable.set(val)
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
        self.optionEnum = optionEnum
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
        if optionEnum == self.optionEnum:
            return
        self.variable.set(0)
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        self.optionEnum = optionEnum
        self.set_completion_list(options, callback=self.callback)
        self['values'] = options
        self.current(self.variable.get())


class Dropdown(ttk.Combobox):
    def __init__(self, master, optionEnum, variable=None, criteria=None, onSelected=None, width=None, state='readonly', **kwargs):
        self.criteria = criteria
        if variable is not None:
            self.variable = variable
        else:
            self.variable = IntVar()
        self.optionEnum = optionEnum
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
        super().__init__(master, state=state, width=self.width, **kwargs)
        self.config(values=options)
        self.current(self.variable.get())
        self.onSelected = onSelected
        self.bind("<<ComboboxSelected>>", self.callback)

    def callback(self, *args):
        self.variable.set(self.current())
        if self.onSelected is not None:
            self.onSelected()

    def update_dropdown(self, optionEnum):
        if optionEnum == self.optionEnum:
            return
        self.variable.set(0)
        if type(optionEnum) == type(list()):
            options = [str(op) for op in optionEnum]
        elif self.criteria is None:
            options = [item for item in optionEnum.__class__.__dict__.keys() if item[:1] != "_"]
        else:
            options = self.criteria(optionEnum.__class__.__dict__.keys())
        self.optionEnum = optionEnum
        self['values'] = options
        self.current(self.variable.get())


class UrlLabel(Label):
    def __init__(self, master, url, **kwargs):
        super().__init__(master, cursor='question_arrow', **kwargs)
        self.url = url
        self.bind("<Button-1>", lambda _: self.open_url())

    def open_url(self):
        webbrowser.open_new_tab(self.url)


class ScrolledCanvas():
    def __init__(self, root, data, waveIdx, areaIdx, color='brown'):
        self.root = root
        self.areaIdx = areaIdx
        self.monsters = data['small_monsters'][LOCATION_SIZE[data['quest_info']['location'].get()]*waveIdx + self.areaIdx]

        self.canv = Canvas(self.root, bg=color, relief=SUNKEN)
        self.canv.config(width=300, height=200)
        self.canv.config(highlightthickness=0)

        ybar = Scrollbar(self.root)
        ybar.config(command=self.canv.yview)
        ## connect the two widgets together
        self.canv.config(yscrollcommand=ybar.set)
        ybar.pack(side=RIGHT, fill=Y)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)
        self.draw()

    def draw(self):
        self.canv.delete('all')
        bg_color=True
        ctr=0
        self.canv.config(scrollregion=(0,0,300, 95*len(self.monsters) + 45))
        for monster in self.monsters:
            clr="lightgrey"
            if bg_color:
                clr="white"
            bg_color= not bg_color
            frm = ttk.Frame(self.root, padding=2)#,width=960, height=100,
                        #bd=2, relief=SUNKEN)

            #Label(frm, text="", bg=clr).grid(column=0, row=0, sticky='ew')
            Button(frm, text='Delete', bg=clr, command=lambda x=ctr:self.delete_entry(x)).grid(column=0, row=0, sticky='ew')
            Label(frm, text="Unk. 1", bg=clr).grid(column=1, row=0, sticky='ew')
            Label(frm, text="Unk. 2:", bg=clr).grid(column=2, row=0, sticky='ew')
            Label(frm, text="Variant:", bg=clr).grid(column=3, row=0, sticky='ew')
            Label(frm, text="Room:", bg=clr).grid(column=4, row=0, sticky='ew')
            Label(frm, text="Quantity:", bg=clr).grid(column=5, row=0, sticky='ew')
            Dropdown(frm, Monster, width=13, variable=monster['type']).grid(column=0, row=1)
            NumEntry(frm, limit=0xFF, width=13, variable=monster['unk1']).grid(column=1, row=1)
            NumEntry(frm, limit=0xFF, width=13, variable=monster['unk2']).grid(column=2, row=1)
            NumEntry(frm, limit=0xFF, width=13, variable=monster['variant']).grid(column=3, row=1)
            NumEntry(frm, limit=0xFF, width=13, variable=monster['room']).grid(column=4, row=1)
            NumEntry(frm, limit=0xFF, width=13, allowNeg=True, variable=monster['quantity']).grid(column=5, row=1)
            Label(frm, text="Pos X:", bg=clr).grid(column=0, row=2, sticky='ew')
            Label(frm, text="Pos Y:", bg=clr).grid(column=1, row=2, sticky='ew')
            Label(frm, text="Pos Z:", bg=clr).grid(column=2, row=2, sticky='ew')
            Label(frm, text="Rot X:", bg=clr).grid(column=3, row=2, sticky='ew')
            Label(frm, text="Rot Y:", bg=clr).grid(column=4, row=2, sticky='ew')
            Label(frm, text="Rot Z:", bg=clr).grid(column=5, row=2, sticky='ew')
            NumEntry(frm, limit=0xFFFF, width=13, allowNeg=True, decimal=False, variable=monster['pos_x']).grid(column=0, row=3)
            NumEntry(frm, limit=0xFFFF, width=13, allowNeg=True, decimal=False, variable=monster['pos_y']).grid(column=1, row=3)
            NumEntry(frm, limit=0xFFFF, width=13, allowNeg=True, decimal=False, variable=monster['pos_z']).grid(column=2, row=3)
            NumEntry(frm, limit=0xFFFFFFFF, width=13, allowNeg=True, variable=monster['rot_x']).grid(column=3, row=3)
            NumEntry(frm, limit=0xFFFFFFFF, width=13, allowNeg=True, variable=monster['rot_y']).grid(column=4, row=3)
            NumEntry(frm, limit=0xFFFFFFFF, width=13, allowNeg=True, variable=monster['rot_z']).grid(column=5, row=3)
            self.canv.create_window(8,3+(95*ctr),anchor=NW, window=frm)
            ctr += 1

        frm = ttk.Frame(self.root, padding=2)
        Button(frm, text='ADD MONSTER', bg="white"if bg_color else"lightgrey", width=13+13+13+13+13+4, command=self.add_entry).grid(column=0, row=0, sticky='ew')
        self.canv.create_window(8,3+(95*ctr),anchor=NW, window=frm)
        
    def add_entry(self):
        self.monsters.append({
            'type': IntVar(value=Monster.none),'unk1': IntVar(value=1),'unk2': IntVar(value=0xFF),
            'variant': IntVar(value=0),'room': IntVar(value=self.areaIdx),'quantity': IntVar(value=1),
            'pos_x': DoubleVar(value=0.0),'pos_y': DoubleVar(value=0.0),'pos_z': DoubleVar(value=0.0),
            'rot_x': IntVar(value=0),'rot_y': IntVar(value=0),'rot_z': IntVar(value=0),
        })
        self.draw()

    def delete_entry(self, monsterIdx):
        del self.monsters[monsterIdx]
        self.draw()
