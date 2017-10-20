## KEYMAP ##


from bge import logic, events

import PYTHON.Input as input


# Change Exit Key
logic.setExitKey(events.PAUSEKEY)

print("Exit Key Changed: [events.PAUSEKEY]")


## LOAD KEYBINDS ##

KEY = {

## Global ##
"ACTIVATE":          input.KEYBASE("000.A",  "Activate",           events.MIDDLEMOUSE,    "Mouse", JOYBUTTON=10),
"ENTERVEH":          input.KEYBASE("001.A",  "Enter/Exit Vehicle", events.ENTERKEY,       "Keyboard", JOYBUTTON=13),
"TOGGLEMODE":        input.KEYBASE("002.A",  "Mode Switch",        events.FKEY,           "Keyboard", JOYBUTTON=12),
"TOGGLECAM":         input.KEYBASE("003.A",  "Camera Switch",      events.VKEY,           "Keyboard", JOYBUTTON=7),
"TOGGLEHUD":         input.KEYBASE("004.A",  "HUD Display Switch", events.HKEY,           "Keyboard", JOYBUTTON=5),
"ZOOM_IN":           input.KEYBASE("005.A",  "Camera In",          events.WHEELUPMOUSE,   "Mouse", SHIFT=True, JOYBUTTON=0),
"ZOOM_OUT":          input.KEYBASE("006.A",  "Camera Out",         events.WHEELDOWNMOUSE, "Mouse", SHIFT=True, JOYBUTTON=1),

## Player Movement ##
"PLR_FORWARD":       input.KEYBASE("100.P",  "Move Forward",  events.WKEY,          "Keyboard", JOYAXIS=1, JOYAXISTYPE=("NEG", "B")),
"PLR_BACKWARD":      input.KEYBASE("101.P",  "Move Backward", events.SKEY,          "Keyboard", JOYAXIS=1, JOYAXISTYPE=("POS", "B")),
"PLR_STRAFELEFT":    input.KEYBASE("102.P",  "Strafe Left",   events.AKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("NEG", "A")),
"PLR_STRAFERIGHT":   input.KEYBASE("103.P",  "Strafe Right",  events.DKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("POS", "A")),
"PLR_LOOKUP":        input.KEYBASE("104.P",  "Look Up",       events.UPARROWKEY,    "Keyboard", JOYAXIS=3, JOYAXISTYPE=("NEG", "A")),
"PLR_LOOKDOWN":      input.KEYBASE("105.P",  "Look Down",     events.DOWNARROWKEY,  "Keyboard", JOYAXIS=3, JOYAXISTYPE=("POS", "A")),
"PLR_TURNLEFT":      input.KEYBASE("106.P",  "Turn Left",     events.LEFTARROWKEY,  "Keyboard", JOYAXIS=2, JOYAXISTYPE=("NEG", "A")),
"PLR_TURNRIGHT":     input.KEYBASE("107.P",  "Turn Right",    events.RIGHTARROWKEY, "Keyboard", JOYAXIS=2, JOYAXISTYPE=("POS", "A")),
"PLR_JUMP":          input.KEYBASE("108.P",  "Jump",          events.SPACEKEY,      "Keyboard", JOYBUTTON=9),
"PLR_DUCK":          input.KEYBASE("109.P",  "Duck",          events.CKEY,          "Keyboard", JOYBUTTON=8),
"PLR_RUN":           input.KEYBASE("110.P",  "Toggle Run",    events.RKEY,          "Keyboard", JOYBUTTON=6),
"PLR_EDIT":          input.KEYBASE("111.P",  "Toggle Edit",   events.BACKSLASHKEY,  "Keyboard"),

## Vehicle Movement ##
"VEH_THROTTLEUP":    input.KEYBASE("200.V",  "Vehicle Throttle Up",   events.WKEY,          "Keyboard", JOYAXIS=5, JOYAXISTYPE=("SLIDER", "B")),
"VEH_THROTTLEDOWN":  input.KEYBASE("201.V",  "Vehicle Throttle Down", events.SKEY,          "Keyboard", JOYAXIS=4, JOYAXISTYPE=("SLIDER", "B")),
"VEH_YAWLEFT":       input.KEYBASE("202.V",  "Vehicle Yaw Left",      events.AKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("NEG", "A")),
"VEH_YAWRIGHT":      input.KEYBASE("203.V",  "Vehicle Yaw Right",     events.DKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("POS", "A")),
"VEH_PITCHUP":       input.KEYBASE("204.V",  "Vehicle Pitch Up",      events.DOWNARROWKEY,  "Keyboard", JOYAXIS=3, JOYAXISTYPE=("POS", "A")),
"VEH_PITCHDOWN":     input.KEYBASE("205.V",  "Vehicle Pitch Down",    events.UPARROWKEY,    "Keyboard", JOYAXIS=3, JOYAXISTYPE=("NEG", "A")),
"VEH_BANKLEFT":      input.KEYBASE("206.V",  "Vehicle Bank Left",     events.LEFTARROWKEY,  "Keyboard", SHIFT=False, JOYAXIS=2, JOYAXISTYPE=("NEG", "A")),
"VEH_BANKRIGHT":     input.KEYBASE("207.V",  "Vehicle Bank Right",    events.RIGHTARROWKEY, "Keyboard", SHIFT=False, JOYAXIS=2, JOYAXISTYPE=("POS", "A")),
"VEH_ASCEND":        input.KEYBASE("208.V",  "Vehicle Ascend",        events.SPACEKEY,      "Keyboard", JOYBUTTON=9),
"VEH_DESCEND":       input.KEYBASE("209.V",  "Vehicle Descend",       events.CKEY,          "Keyboard", JOYBUTTON=8),
"VEH_STRAFELEFT":    input.KEYBASE("210.V",  "Vehicle Strafe Left",   events.LEFTARROWKEY,  "Keyboard", SHIFT=True),
"VEH_STRAFERIGHT":   input.KEYBASE("211.V",  "Vehicle Strafe Right",  events.RIGHTARROWKEY, "Keyboard", SHIFT=True),
"VEH_FIRE":          input.KEYBASE("212.V",  "Vehicle Weapon Fire",   events.FKEY,          "Keyboard", JOYBUTTON=12),
"VEH_ACTION":        input.KEYBASE("213.V",  "Vehicle Action Key",    events.BACKSPACEKEY,  "Keyboard", JOYBUTTON=11),
"CAM_ORBIT":         input.KEYBASE("299.V",  "Rotate Camera",         events.RKEY,          "Keyboard"),

## Weapons ##
"WP_UP":             input.KEYBASE("300.W",  "Weapon Up",        events.WHEELUPMOUSE,   "Mouse", SHIFT=False),
"WP_DOWN":           input.KEYBASE("301.W",  "Weapon Down",      events.WHEELDOWNMOUSE, "Mouse", SHIFT=False),
"WP_MODE":           input.KEYBASE("302.W",  "Weapon Mode",      events.QKEY,           "Keyboard", JOYBUTTON=11),
"ATTACK_ONE":        input.KEYBASE("303.W",  "Primary Attack",   events.LEFTMOUSE,      "Mouse"),
"ATTACK_TWO":        input.KEYBASE("304.W",  "Secondary Attack", events.RIGHTMOUSE,     "Mouse"),
"SHEALTH":           input.KEYBASE("305.W",  "Shealth Weapon",   events.XKEY,           "Keyboard"),

## Slot Keys ##
"SLOT_ZERO":         input.KEYBASE("900.S",  "Slot 0", events.ZEROKEY,  "Keyboard"),
"SLOT_ONE":          input.KEYBASE("901.S",  "Slot 1", events.ONEKEY,   "Keyboard"),
"SLOT_TWO":          input.KEYBASE("902.S",  "Slot 2", events.TWOKEY,   "Keyboard"),
"SLOT_THREE":        input.KEYBASE("903.S",  "Slot 3", events.THREEKEY, "Keyboard"),
"SLOT_FOUR":         input.KEYBASE("904.S",  "Slot 4", events.FOURKEY,  "Keyboard"),
"SLOT_FIVE":         input.KEYBASE("905.S",  "Slot 5", events.FIVEKEY,  "Keyboard"),
"SLOT_SIX":          input.KEYBASE("906.S",  "Slot 6", events.SIXKEY,   "Keyboard"),
"SLOT_SEVEN":        input.KEYBASE("907.S",  "Slot 7", events.SEVENKEY, "Keyboard"),
"SLOT_EIGHT":        input.KEYBASE("908.S",  "Slot 8", events.EIGHTKEY, "Keyboard"),
"SLOT_NINE":         input.KEYBASE("909.S",  "Slot 9", events.NINEKEY,  "Keyboard"),

## Mouse ##
"MOUSELOOK":         input.MOUSELOOK("999.X", "Mouse Speed", 5, "Mouse"),

## System/Extras ##
"KILL":              input.KEYBASE("999.Z",  "Terminate/Kill",     events.TKEY,           "Keyboard"),
"SHUFFLE":           input.KEYBASE("999.Z",  "Arrange Slots",      events.ACCENTGRAVEKEY, "Keyboard", ALT=False),
"SUPER_DROP":        input.KEYBASE("999.Z",  "Drop All",           events.ACCENTGRAVEKEY, "Keyboard", ALT=True),
"SPECIAL":           input.KEYBASE("999.Z",  "Alternative",        None,                  "Keyboard", ALT=True),
"ESCAPE":            input.KEYBASE("999.Z",  "Escape Key",         events.ESCKEY,         "Keyboard", JOYBUTTON=4)

}

print("Keymap.py Imported")

