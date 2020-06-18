from textwrap import dedent
# TODO: get parameters from external file. *dict can be used.
        # Look up conversion from csv to dict
# TODO: import this data from JSON or csv in assets dict

assets = dict(

template=dict(
    cls="Actor", # class name, default Actor
    # accepted names
    name=[],
    location="", # setting to self makes obj a room
    description="", # decapitalized and include article
    visible=False,
    # examine
    examined=False,
    examined_false_text=[],
    examined_true_text=[],
    examine_makes_visible=[],
    examine_to_activate=False,
    # use
    used=False,
    reusable=False,
    active=False, # can be used
    active_false_text=[], # display if obj is not active
    used_false_text=[], # display first time used
    used_true_text=[], # display if used again
    # use with
    usable=False, # obj can only be used if obj makes_usable
    makes_usable=[], # can use usable=False obj and makes usable
    usable_false_text=[], # display if target obj not usable
    usable_with=[],
    usable_with_true_text=[], # display if no target object given
    # action
    use_activates=[],
    makes_takeable=[],
    use_makes_visible=[],
    del_after_use=False,
    has_special=False,
    # take
    takeable=False,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=[], # north, east, south, west
    leads_to="", # room that will be entered on use
    in_room_inventory=True, # displayed in room inventory
    #room parameters
    entering_text=[],
    # accepted commands
    use_words=[],
    examine_words=[],
    take_words=[],
    talk_words=[]
    ),

player=dict(
    cls="Player", # Actor if empty
    # accepted names
    name=["Player", "me", "slef", "myself"],
    location="", # setting to self makes obj a room
    description="Just old regular me.", # decapitalized and include article
    visible=True,
    # examine
    examined=False,
    examined_false_text=[],
    examined_true_text=[],
    examine_makes_visible=[],
    examine_to_activate=False,
    # use
    used=False,
    reusable=False,
    active=False, # can be used
    active_false_text=[], # display if obj is not active
    used_false_text=[], # display first time used
    used_true_text=[], # display if used again
    # use with
    usable=False, # obj can only be used if obj makes_usable
    makes_usable=[], # can use usable=False obj and makes usable
    usable_false_text=[], # display if target obj not usable
    usable_with=[],
    usable_with_true_text=[], # display if no target object given
    # action
    use_activates=[],
    makes_takeable=[],
    use_makes_visible=[],
    del_after_use=False,
    has_special=False,
    # take
    takeable=False,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=[], # north, east, south, west
    leads_to="", # room that will be entered on use
    in_room_inventory=True, # displayed in room inventory
    #room parameters
    entering_text=[],
    # accepted commands
    use_words=[],
    examine_words=[],
    take_words=[],
    talk_words=[]
    ),
    device=dict(
        cls="Device",
        # accepted names
        name=["Device"],
        location="player", # setting to self makes obj a room
        description="a strange device", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=["A strange device without a real shape.\nA small little bump on the surface looks like i could be pushed."],
        examined_true_text=["Maybe I should try to push the bump."],
        examine_makes_visible=[],
        examine_to_activate=True,
        # use
        used=False,
        reusable=True,
        active=False, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=True,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="menu", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["push"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),

menu=dict(
    cls="Menu",
    # accepted names
    name=["Menu","Room", "surroundings"],
    location=None, # setting to self makes obj a room
    description=None, # decapitalized and include article
    visible=True,
    # examine
    examined=False,
    examined_false_text=[dedent(
        """\
        Nothing but darkness. Any sense of time is absent here.
        """)],
    examined_true_text=None,
    examine_makes_visible=(),
    examine_to_activate=False,
    # use
    used=False,
    reusable=False,
    active=False, # can be used
    active_false_text=None, # display if obj is not active
    used_false_text=None, # display first time used
    used_true_text=None, # display if used again
    # use with
    usable=False, # obj can only be used if obj makes_usable
    makes_usable=(), # can use usable=False obj and makes usable
    usable_false_text=None, # display if target obj not usable
    usable_with=(),
    usable_with_true_text=None, # display if no target object given
    # action
    use_activates=(),
    makes_takeable=(),
    use_makes_visible=(),
    del_after_use=False,
    has_special=False,
    # take
    takeable=False,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=[],
    leads_to="",
    in_room_inventory=True,
    #room parameters
    entering_text=[dedent("""\
        Back in the black void.
        Only things here are:
        START, LOAD, SAVE, LEAVE.
        """)],
    # accepted commands
    use_words=[],
    examine_words=[],
    take_words=[],
    talk_words=[]
    ),
    start=dict(
        cls="Start",
        # accepted names
        name=["start"],
        location="menu", # setting to self makes obj a room
        description="", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=True, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[""], # display first time used
        used_true_text=["It's power seems to be gone."], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=True,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="bedroom", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["use", "interact", "touch", "push"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    load=dict(
        cls="Load",
        # accepted names
        name=["load"],
        location="menu", # setting to self makes obj a room
        description="", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=True,
        active=True, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=True,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["use", "interact", "touch", "push"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    save=dict(
        cls="Save",
        # accepted names
        name=["save"],
        location="menu", # setting to self makes obj a room
        description="", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=True,
        active=True, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=True,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["use", "interact", "touch", "push"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    leave=dict(
        cls="Leave",
        # accepted names
        name=("Leave",),
        location="leave", # setting to self makes obj a room
        description="", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=True,
        active=False, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["use", "interact", "touch", "push"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),

bedroom=dict(
    cls="Actor",
    # accepted names
    name=["Bedroom","Room", "Sourroundings", "Area"],
    location="", # setting to self makes obj a room
    description="You are in your smelly bedroom", # decapitalized and include article
    visible=True,
    # examine
    examined=False,
    examined_false_text=[],
    examined_true_text=[],
    examine_makes_visible=[],
    examine_to_activate=False,
    # use
    used=False,
    reusable=False,
    active=False, # can be used
    active_false_text=[], # display if obj is not active
    used_false_text=[], # display first time used
    used_true_text=[], # display if used again
    # use with
    usable=False, # obj can only be used if obj makes_usable
    makes_usable=[], # can use usable=False obj and makes usable
    usable_false_text=[], # display if target obj not usable
    usable_with=[],
    usable_with_true_text=[], # display if no target object given
    # action
    use_activates=[],
    makes_takeable=[],
    use_makes_visible=[],
    del_after_use=False,
    has_special=False,
    # take
    takeable=False,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=[], # north, east, south, west
    leads_to="", # room that will be entered on use
    in_room_inventory=True, # displayed in room inventory
    #room parameters
    entering_text=["You open your eyes and you recognize your own bedroom."],
    # accepted commands
    use_words=[],
    examine_words=[],
    take_words=[],
    talk_words=[]
    ),
    bedroom_north=dict(
        cls="Actor",
        # accepted names
        name=["Door"],
        location="bedroom", # setting to self makes obj a room
        description="a door", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=False, # can be used
        active_false_text=["It's locked"], # display if obj is not active
        used_false_text=["The door opens."], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=("north",), # north, east, south, west
        leads_to="victory", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=["open", "go", "explore"],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    bedroom_else=dict(
        cls="Actor",
        # accepted names
        name=[],
        location="bedroom", # setting to self makes obj a room
        description="", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=[],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=False, # can be used
        active_false_text=["BONK! You walked against the wall!"], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=("east","south", "west"), # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=False, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=[],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),

    lock=dict(
        cls="Actor",
        # accepted names
        name=["Lock"],
        location="bedroom", # setting to self makes obj a room
        description="an old lock", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=["Looks like this old lock is a little rusty."],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=False, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=[], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=[],
        usable_with_true_text=[], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=[],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    oil=dict(
        cls="Actor",
        # accepted names
        name=["Oil"],
        location="bedroom", # setting to self makes obj a room
        description="a can of oil", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=["Looks like this old lock is a little rusty."],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=False,
        active=True, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=["*pfffft* This should be enough"], # display first time used
        used_true_text=["I think thats enough oil",
                        "We really don't need more",
                        "Whatever... *pffffft pffffft *\n*pffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff*\n...happy now?"], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=("lock",), # can use usable=False obj and makes usable
        usable_false_text=[], # display if target obj not usable
        usable_with=("lock",),
        usable_with_true_text=["I can try using this on something stuck."], # display if no target object given
        # action
        use_activates=[],
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=False,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[], # north, east, south, west
        leads_to="", # room that will be entered on use
        in_room_inventory=True, # displayed in room inventory
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=[],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),
    key=dict(
        cls="Actor",
        name=["Key"],
        location="bedroom", # setting to self makes obj a room
        description="an old brass key", # decapitalized and include article
        visible=True,
        # examine
        examined=False,
        examined_false_text=["This key looks quite old. I wonder what it will open."],
        examined_true_text=[],
        examine_makes_visible=[],
        examine_to_activate=False,
        # use
        used=False,
        reusable=True,
        active=True, # can be used
        active_false_text=[], # display if obj is not active
        used_false_text=["You hear a satisfying CLICK as the bolt moves into place"], # display first time used
        used_true_text=[], # display if used again
        # use with
        usable=False, # obj can only be used if obj makes_usable
        makes_usable=[], # can use usable=False obj and makes usable
        usable_false_text=["The key fits, but I can't turn the look."], # display if target obj not usable
        usable_with=("lock",),
        usable_with_true_text=["I guess I need to find a lock."], # display if no target object given
        # action
        use_activates=("bedroom_north",),
        makes_takeable=[],
        use_makes_visible=[],
        del_after_use=False,
        has_special=False,
        # take
        takeable=True,
        takeable_false_text=[],
        takeable_true_text=[],
        # door parameters
        direction=[],
        leads_to="",
        in_room_inventory=True,
        #room parameters
        entering_text=[],
        # accepted commands
        use_words=[],
        examine_words=[],
        take_words=[],
        talk_words=[]
        ),

victory=dict(
    cls="Actor",
    # accepted names
    name=["Victory"],
    location="", # setting to self makes obj a room
    description="", # decapitalized and include article
    visible=True,
    # examine
    examined=False,
    examined_false_text=[],
    examined_true_text=[],
    examine_makes_visible=[],
    examine_to_activate=False,
    # use
    used=False,
    reusable=False,
    active=False, # can be used
    active_false_text=[], # display if obj is not active
    used_false_text=[], # display first time used
    used_true_text=[], # display if used again
    # use with
    usable=False, # obj can only be used if obj makes_usable
    makes_usable=[], # can use usable=False obj and makes usable
    usable_false_text=[], # display if target obj not usable
    usable_with=[],
    usable_with_true_text=[], # display if no target object given
    # action
    use_activates=[],
    makes_takeable=[],
    use_makes_visible=[],
    del_after_use=False,
    has_special=False,
    # take
    takeable=False,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=[], # north, east, south, west
    leads_to="", # room that will be entered on use
    in_room_inventory=True, # displayed in room inventory
    #room parameters
    entering_text=["Yay, you made it, you are so cool...NOT!"],
    # accepted commands
    use_words=[],
    examine_words=[],
    take_words=[],
    talk_words=[]
    ),

)
