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

# Assume we live in the "PY" folder
import PY.input as input


# Change Exit Key
logic.setExitKey(events.PAUSEKEY)

print("Exit Key Changed: [events.PAUSEKEY]")


## LOAD KEYBINDS ##
## These Binds were pulled right out of my project.  Gamepad set up for blender 2.74 xbox 360 controller ##

MOUSELOOK = input.MouseLook(5, SMOOTH=10)

BINDS = {

## Global ##
"ACTIVATE":          input.KeyBase("000.A",  "MIDDLEMOUSE",    "Activate",           JOYBUTTON=10),
"ENTERVEH":          input.KeyBase("001.A",  "ENTERKEY",       "Enter/Exit Vehicle", JOYBUTTON=13),
"TOGGLEMODE":        input.KeyBase("002.A",  "FKEY",           "Mode Switch",        JOYBUTTON=12),
"TOGGLECAM":         input.KeyBase("003.A",  "VKEY",           "Camera Switch",      JOYBUTTON=7),
"TOGGLEHUD":         input.KeyBase("004.A",  "HKEY",           "HUD Display Switch", JOYBUTTON=5),
"ZOOM_IN":           input.KeyBase("005.A",  "WHEELUPMOUSE",   "Camera In",          JOYBUTTON=0, SHIFT=True),
"ZOOM_OUT":          input.KeyBase("006.A",  "WHEELDOWNMOUSE", "Camera Out",         JOYBUTTON=1, SHIFT=True),

## Player Movement ##
"PLR_FORWARD":       input.KeyBase("100.P",  "WKEY",           "Move Forward",  JOYAXIS=(1, "NEG", "B")),
"PLR_BACKWARD":      input.KeyBase("101.P",  "SKEY",           "Move Backward", JOYAXIS=(1, "POS", "B")),
"PLR_STRAFELEFT":    input.KeyBase("102.P",  "AKEY",           "Strafe Left",   JOYAXIS=(0, "NEG", "A")),
"PLR_STRAFERIGHT":   input.KeyBase("103.P",  "DKEY",           "Strafe Right",  JOYAXIS=(0, "POS", "A")),
"PLR_LOOKUP":        input.KeyBase("104.P",  "UPARROWKEY",     "Look Up",       JOYAXIS=(3, "NEG", "A")),
"PLR_LOOKDOWN":      input.KeyBase("105.P",  "DOWNARROWKEY",   "Look Down",     JOYAXIS=(3, "POS", "A")),
"PLR_TURNLEFT":      input.KeyBase("106.P",  "LEFTARROWKEY",   "Turn Left",     JOYAXIS=(2, "NEG", "A")),
"PLR_TURNRIGHT":     input.KeyBase("107.P",  "RIGHTARROWKEY",  "Turn Right",    JOYAXIS=(2, "POS", "A")),
"PLR_JUMP":          input.KeyBase("108.P",  "SPACEKEY",       "Jump",          JOYBUTTON=9),
"PLR_DUCK":          input.KeyBase("109.P",  "CKEY",           "Duck",          JOYBUTTON=8),
"PLR_RUN":           input.KeyBase("110.P",  "RKEY",           "Toggle Run",    JOYBUTTON=6),
"PLR_EDIT":          input.KeyBase("111.P",  "BACKSLASHKEY",   "Toggle Edit"),

## Vehicle Movement ##
"VEH_THROTTLEUP":    input.KeyBase("200.V",  "WKEY",           "Vehicle Throttle Up",   JOYAXIS=(5, "SLIDER", "B")),
"VEH_THROTTLEDOWN":  input.KeyBase("201.V",  "SKEY",           "Vehicle Throttle Down", JOYAXIS=(4, "SLIDER", "B")),
"VEH_YAWLEFT":       input.KeyBase("202.V",  "AKEY",           "Vehicle Yaw Left",      JOYAXIS=(0, "NEG", "A")),
"VEH_YAWRIGHT":      input.KeyBase("203.V",  "DKEY",           "Vehicle Yaw Right",     JOYAXIS=(0, "POS", "A")),
"VEH_PITCHUP":       input.KeyBase("204.V",  "DOWNARROWKEY",   "Vehicle Pitch Up",      JOYAXIS=(3, "POS", "A")),
"VEH_PITCHDOWN":     input.KeyBase("205.V",  "UPARROWKEY",     "Vehicle Pitch Down",    JOYAXIS=(3, "NEG", "A")),
"VEH_BANKLEFT":      input.KeyBase("206.V",  "LEFTARROWKEY",   "Vehicle Bank Left",     JOYAXIS=(2, "NEG", "A"), SHIFT=False),
"VEH_BANKRIGHT":     input.KeyBase("207.V",  "RIGHTARROWKEY",  "Vehicle Bank Right",    JOYAXIS=(2, "POS", "A"), SHIFT=False),
"VEH_ASCEND":        input.KeyBase("208.V",  "SPACEKEY",       "Vehicle Ascend",        JOYBUTTON=9),
"VEH_DESCEND":       input.KeyBase("209.V",  "CKEY",           "Vehicle Descend",       JOYBUTTON=8),
"VEH_STRAFELEFT":    input.KeyBase("210.V",  "LEFTARROWKEY",   "Vehicle Strafe Left",   SHIFT=True),
"VEH_STRAFERIGHT":   input.KeyBase("211.V",  "RIGHTARROWKEY",  "Vehicle Strafe Right",  SHIFT=True),
"VEH_FIRE":          input.KeyBase("212.V",  "FKEY",           "Vehicle Weapon Fire",   JOYBUTTON=12),
"VEH_ACTION":        input.KeyBase("213.V",  "BACKSPACEKEY",   "Vehicle Action Key",    JOYBUTTON=11),
"CAM_ORBIT":         input.KeyBase("299.V",  "RKEY",           "Rotate Camera"),

## Weapons ##
"WP_UP":             input.KeyBase("300.W",  "WHEELUPMOUSE",   "Weapon Up",        SHIFT=False),
"WP_DOWN":           input.KeyBase("301.W",  "WHEELDOWNMOUSE", "Weapon Down",      SHIFT=False),
"WP_MODE":           input.KeyBase("302.W",  "QKEY",           "Weapon Mode",      JOYBUTTON=11),
"ATTACK_ONE":        input.KeyBase("303.W",  "LEFTMOUSE",      "Primary Attack"),
"ATTACK_TWO":        input.KeyBase("304.W",  "RIGHTMOUSE",     "Secondary Attack"),
"SHEALTH":           input.KeyBase("305.W",  "XKEY",           "Shealth Weapon"),

## Slot Keys ##
"SLOT_ZERO":         input.KeyBase("900.S",  "ZEROKEY",        "Slot 0"),
"SLOT_ONE":          input.KeyBase("901.S",  "ONEKEY",         "Slot 1"),
"SLOT_TWO":          input.KeyBase("902.S",  "TWOKEY",         "Slot 2"),
"SLOT_THREE":        input.KeyBase("903.S",  "THREEKEY",       "Slot 3"),
"SLOT_FOUR":         input.KeyBase("904.S",  "FOURKEY",        "Slot 4"),
"SLOT_FIVE":         input.KeyBase("905.S",  "FIVEKEY",        "Slot 5"),
"SLOT_SIX":          input.KeyBase("906.S",  "SIXKEY",         "Slot 6"),
"SLOT_SEVEN":        input.KeyBase("907.S",  "SEVENKEY",       "Slot 7"),
"SLOT_EIGHT":        input.KeyBase("908.S",  "EIGHTKEY",       "Slot 8"),
"SLOT_NINE":         input.KeyBase("909.S",  "NINEKEY",        "Slot 9"),

## System/Extras ##
"KILL":              input.KeyBase("999.Z",  "TKEY",           "Terminate/Kill"),
"SHUFFLE":           input.KeyBase("999.Z",  "ACCENTGRAVEKEY", "Arrange Slots",   ALT=False),
"SUPER_DROP":        input.KeyBase("999.Z",  "ACCENTGRAVEKEY", "Drop All",        ALT=True),
"SPECIAL":           input.KeyBase("999.Z",  "NONE",           "Alternative",     ALT=True),
"ESCAPE":            input.KeyBase("999.Z",  "ESCKEY",         "Escape Key",      JOYBUTTON=4)

}

print("keymap.py Imported")

