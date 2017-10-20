####
# bge_keymapper_class: a class based keymapper with joystick support
# Copyright (C) 2017  DaedalusMDW
#
# This file is part of bge_keymapper_class.
#
#    bge_keymapper_class is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    bge_keymapper_class is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with bge_keymapper_class.  If not, see <http://www.gnu.org/licenses/>.
#
####

## KEYMAP ##


from bge import logic, events

import PY.input as input #assume we live in the PY folder


# Update Joysticks !HACKY! lives on first scene
logic.getSceneList()[0].pre_draw.append(input.GAMEPADDER)

# Change Exit Key
logic.setExitKey(events.PAUSEKEY)

print("Exit Key Changed: [events.PAUSEKEY]")


## LOAD KEYBINDS ##
## These Binds were pulled right out of my project.  Gamepad set up for blender 2.74 xbox 360 controller ##
MOUSELOOK = input.MouseLook(5, SMOOTH=10)
BINDS = {

## Global ##
"ACTIVATE":          input.KeyBase("000.A",  "Activate",           events.MIDDLEMOUSE,    "Mouse", JOYBUTTON=10),
"ENTERVEH":          input.KeyBase("001.A",  "Enter/Exit Vehicle", events.ENTERKEY,       "Keyboard", JOYBUTTON=13),
"TOGGLEMODE":        input.KeyBase("002.A",  "Mode Switch",        events.FKEY,           "Keyboard", JOYBUTTON=12),
"TOGGLECAM":         input.KeyBase("003.A",  "Camera Switch",      events.VKEY,           "Keyboard", JOYBUTTON=7),
"TOGGLEHUD":         input.KeyBase("004.A",  "HUD Display Switch", events.HKEY,           "Keyboard", JOYBUTTON=5),
"ZOOM_IN":           input.KeyBase("005.A",  "Camera In",          events.WHEELUPMOUSE,   "Mouse", SHIFT=True, JOYBUTTON=0),
"ZOOM_OUT":          input.KeyBase("006.A",  "Camera Out",         events.WHEELDOWNMOUSE, "Mouse", SHIFT=True, JOYBUTTON=1),

## Player Movement ##
"PLR_FORWARD":       input.KeyBase("100.P",  "Move Forward",  events.WKEY,          "Keyboard", JOYAXIS=1, JOYAXISTYPE=("NEG", "B")),
"PLR_BACKWARD":      input.KeyBase("101.P",  "Move Backward", events.SKEY,          "Keyboard", JOYAXIS=1, JOYAXISTYPE=("POS", "B")),
"PLR_STRAFELEFT":    input.KeyBase("102.P",  "Strafe Left",   events.AKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("NEG", "A")),
"PLR_STRAFERIGHT":   input.KeyBase("103.P",  "Strafe Right",  events.DKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("POS", "A")),
"PLR_LOOKUP":        input.KeyBase("104.P",  "Look Up",       events.UPARROWKEY,    "Keyboard", JOYAXIS=3, JOYAXISTYPE=("NEG", "A")),
"PLR_LOOKDOWN":      input.KeyBase("105.P",  "Look Down",     events.DOWNARROWKEY,  "Keyboard", JOYAXIS=3, JOYAXISTYPE=("POS", "A")),
"PLR_TURNLEFT":      input.KeyBase("106.P",  "Turn Left",     events.LEFTARROWKEY,  "Keyboard", JOYAXIS=2, JOYAXISTYPE=("NEG", "A")),
"PLR_TURNRIGHT":     input.KeyBase("107.P",  "Turn Right",    events.RIGHTARROWKEY, "Keyboard", JOYAXIS=2, JOYAXISTYPE=("POS", "A")),
"PLR_JUMP":          input.KeyBase("108.P",  "Jump",          events.SPACEKEY,      "Keyboard", JOYBUTTON=9),
"PLR_DUCK":          input.KeyBase("109.P",  "Duck",          events.CKEY,          "Keyboard", JOYBUTTON=8),
"PLR_RUN":           input.KeyBase("110.P",  "Toggle Run",    events.RKEY,          "Keyboard", JOYBUTTON=6),
"PLR_EDIT":          input.KeyBase("111.P",  "Toggle Edit",   events.BACKSLASHKEY,  "Keyboard"),

## Vehicle Movement ##
"VEH_THROTTLEUP":    input.KeyBase("200.V",  "Vehicle Throttle Up",   events.WKEY,          "Keyboard", JOYAXIS=5, JOYAXISTYPE=("SLIDER", "B")),
"VEH_THROTTLEDOWN":  input.KeyBase("201.V",  "Vehicle Throttle Down", events.SKEY,          "Keyboard", JOYAXIS=4, JOYAXISTYPE=("SLIDER", "B")),
"VEH_YAWLEFT":       input.KeyBase("202.V",  "Vehicle Yaw Left",      events.AKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("NEG", "A")),
"VEH_YAWRIGHT":      input.KeyBase("203.V",  "Vehicle Yaw Right",     events.DKEY,          "Keyboard", JOYAXIS=0, JOYAXISTYPE=("POS", "A")),
"VEH_PITCHUP":       input.KeyBase("204.V",  "Vehicle Pitch Up",      events.DOWNARROWKEY,  "Keyboard", JOYAXIS=3, JOYAXISTYPE=("POS", "A")),
"VEH_PITCHDOWN":     input.KeyBase("205.V",  "Vehicle Pitch Down",    events.UPARROWKEY,    "Keyboard", JOYAXIS=3, JOYAXISTYPE=("NEG", "A")),
"VEH_BANKLEFT":      input.KeyBase("206.V",  "Vehicle Bank Left",     events.LEFTARROWKEY,  "Keyboard", SHIFT=False, JOYAXIS=2, JOYAXISTYPE=("NEG", "A")),
"VEH_BANKRIGHT":     input.KeyBase("207.V",  "Vehicle Bank Right",    events.RIGHTARROWKEY, "Keyboard", SHIFT=False, JOYAXIS=2, JOYAXISTYPE=("POS", "A")),
"VEH_ASCEND":        input.KeyBase("208.V",  "Vehicle Ascend",        events.SPACEKEY,      "Keyboard", JOYBUTTON=9),
"VEH_DESCEND":       input.KeyBase("209.V",  "Vehicle Descend",       events.CKEY,          "Keyboard", JOYBUTTON=8),
"VEH_STRAFELEFT":    input.KeyBase("210.V",  "Vehicle Strafe Left",   events.LEFTARROWKEY,  "Keyboard", SHIFT=True),
"VEH_STRAFERIGHT":   input.KeyBase("211.V",  "Vehicle Strafe Right",  events.RIGHTARROWKEY, "Keyboard", SHIFT=True),
"VEH_FIRE":          input.KeyBase("212.V",  "Vehicle Weapon Fire",   events.FKEY,          "Keyboard", JOYBUTTON=12),
"VEH_ACTION":        input.KeyBase("213.V",  "Vehicle Action Key",    events.BACKSPACEKEY,  "Keyboard", JOYBUTTON=11),
"CAM_ORBIT":         input.KeyBase("299.V",  "Rotate Camera",         events.RKEY,          "Keyboard"),

## Weapons ##
"WP_UP":             input.KeyBase("300.W",  "Weapon Up",        events.WHEELUPMOUSE,   "Mouse", SHIFT=False),
"WP_DOWN":           input.KeyBase("301.W",  "Weapon Down",      events.WHEELDOWNMOUSE, "Mouse", SHIFT=False),
"WP_MODE":           input.KeyBase("302.W",  "Weapon Mode",      events.QKEY,           "Keyboard", JOYBUTTON=11),
"ATTACK_ONE":        input.KeyBase("303.W",  "Primary Attack",   events.LEFTMOUSE,      "Mouse"),
"ATTACK_TWO":        input.KeyBase("304.W",  "Secondary Attack", events.RIGHTMOUSE,     "Mouse"),
"SHEALTH":           input.KeyBase("305.W",  "Shealth Weapon",   events.XKEY,           "Keyboard"),

## Slot Keys ##
"SLOT_ZERO":         input.KeyBase("900.S",  "Slot 0", events.ZEROKEY,  "Keyboard"),
"SLOT_ONE":          input.KeyBase("901.S",  "Slot 1", events.ONEKEY,   "Keyboard"),
"SLOT_TWO":          input.KeyBase("902.S",  "Slot 2", events.TWOKEY,   "Keyboard"),
"SLOT_THREE":        input.KeyBase("903.S",  "Slot 3", events.THREEKEY, "Keyboard"),
"SLOT_FOUR":         input.KeyBase("904.S",  "Slot 4", events.FOURKEY,  "Keyboard"),
"SLOT_FIVE":         input.KeyBase("905.S",  "Slot 5", events.FIVEKEY,  "Keyboard"),
"SLOT_SIX":          input.KeyBase("906.S",  "Slot 6", events.SIXKEY,   "Keyboard"),
"SLOT_SEVEN":        input.KeyBase("907.S",  "Slot 7", events.SEVENKEY, "Keyboard"),
"SLOT_EIGHT":        input.KeyBase("908.S",  "Slot 8", events.EIGHTKEY, "Keyboard"),
"SLOT_NINE":         input.KeyBase("909.S",  "Slot 9", events.NINEKEY,  "Keyboard"),

## System/Extras ##
"KILL":              input.KeyBase("999.Z",  "Terminate/Kill",     events.TKEY,           "Keyboard"),
"SHUFFLE":           input.KeyBase("999.Z",  "Arrange Slots",      events.ACCENTGRAVEKEY, "Keyboard", ALT=False),
"SUPER_DROP":        input.KeyBase("999.Z",  "Drop All",           events.ACCENTGRAVEKEY, "Keyboard", ALT=True),
"SPECIAL":           input.KeyBase("999.Z",  "Alternative",        None,                  "Keyboard", ALT=True),
"ESCAPE":            input.KeyBase("999.Z",  "Escape Key",         events.ESCKEY,         "Keyboard", JOYBUTTON=4)

}

print("keymap.py Imported")

