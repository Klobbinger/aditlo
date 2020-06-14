assets = {
"key": dict(
    cls=Actor,
    id="key",
    name=["Key"],
    location="bedroom", # setting to self makes obj a room
    description="an old brass key", # decapitalized and include article
    visible=True,
    # examine
    examined=False,
    examined_false_text=["This key looks quite old. I wonder what it will open."],
    examined_true_text=[],
    examine_makes_visible=(),
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
    makes_usable=(), # can use usable=False obj and makes usable
    usable_false_text=["The key fits, but I can't turn the look."], # display if target obj not usable
    usable_with=("lock",),
    usable_with_true_text=["I guess I need to find a lock."], # display if no target object given
    # action
    use_activates=("door",),
    makes_takeable=(),
    use_makes_visible=(),
    del_after_use=False,
    has_special=False,
    # take
    takeable=True,
    takeable_false_text=[],
    takeable_true_text=[],
    # door parameters
    direction=(),
    leads_to=(),
    in_room_inventory=True,
    #room parameters
    entering_text=[],
    # accepted commands
    use_words=(),
    examine_words=(),
    take_words=(),
    talk_words=()
    ),

}
