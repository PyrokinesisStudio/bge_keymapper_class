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

## INPUT PROCESSING ##


from bge import logic, events, render


## Find Available Gamepads ##
events.JOYBUTTONS = {}

for JOYID in range(len(logic.joysticks)):
	if logic.joysticks[JOYID] != None:
		events.JOYBUTTONS[JOYID] = {"Buttons":{}, "Axis":{}}
		print("Gamepad Found:", logic.joysticks[JOYID], "ID:", JOYID)

		for BUTID in range(logic.joysticks[JOYID].numButtons):
			events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 0

		for AXIS in range(len(logic.joysticks[JOYID].axisValues)):
			events.JOYBUTTONS[JOYID]["Axis"][AXIS] = {"NEG":0, "POS":0, "SLIDER":0, "VALUE":0.0}


## Base Class for Inputs ##
class KeyBase:

	GROUP = "Default"

	def __init__(self, ID, KEY, SIMPLE, JOYINDEX=0, JOYBUTTON=None, JOYAXIS=(None, "POS", "A"), SHIFT=None, CTRL=None, ALT=None):

		## Catch Failures ##
		if JOYINDEX >= len(logic.joysticks):
			JOYINDEX = None
		elif logic.joysticks[JOYINDEX] == None or KEY == "NONE":
			JOYINDEX = None
		else:
			if JOYAXIS[0] != None:
				if JOYAXIS[0] >= len(logic.joysticks[JOYINDEX].axisValues):
					JOYINDEX = None
			if JOYBUTTON != None:
				if JOYBUTTON >= logic.joysticks[JOYINDEX].numButtons:
					JOYINDEX = None

		self.id = ID
		self.simple_name = SIMPLE
		self.modifiers = {"S":SHIFT, "C":CTRL, "A":ALT}
		self.gamepad = {"Index":JOYINDEX, "Button":JOYBUTTON, "Axis":JOYAXIS[0], "Type":(JOYAXIS[1], JOYAXIS[2])}
		self.update(KEY)

	def update(self, NEWKEY):
		self.input_name = NEWKEY

		if NEWKEY != "NONE":
			self.input = getattr(events, self.input_name)
		else:
			self.input = None
			self.gamepad["Index"] = None

		self.autoDevice()

	def autoDevice(self):
		if self.input == None:
			self.device = logic.keyboard
			self.isWheel = False

		elif self.input_name in ["LEFTMOUSE", "MIDDLEMOUSE", "RIGHTMOUSE"]:
			self.device = logic.mouse
			self.isWheel = False

		elif self.input_name in ["WHEELDOWNMOUSE", "WHEELUPMOUSE", "MOUSEX", "MOUSEY"]:
			self.device = logic.mouse
			self.isWheel = True

		else:
			self.device = logic.keyboard
			self.isWheel = False

	def sceneGamepadCheck(self):
		if GAMEPADDER not in logic.getSceneList()[0].pre_draw:
			print("NOTICE: GAMEPADDER() Scene Fix -", logic.getSceneList()[0].name)
			GAMEPADDER()
			logic.getSceneList()[0].pre_draw.append(GAMEPADDER)
			return False

		return True

	def checkInput(self, INPUT):
		if self.sceneGamepadCheck() == False:
			return False

		JOYID = self.gamepad["Index"]
		BUTID = self.gamepad["Button"]
		AXIS = self.gamepad["Axis"]
		TYPE = self.gamepad["Type"]

		PAD = False
		KEY = False

		## Check Gamepad ##
		if JOYID != None:
			if BUTID != None:
				if events.JOYBUTTONS[JOYID]["Buttons"][BUTID] == INPUT:
					PAD = True

			if AXIS != None and TYPE[1] == "B":
				if events.JOYBUTTONS[JOYID]["Axis"][AXIS][TYPE[0]] == INPUT:
					PAD = True

		elif INPUT == logic.KX_INPUT_NONE:
			PAD = True

		## Check Keyboard/Mouse ##
		if self.checkModifiers() == True or INPUT == logic.KX_INPUT_NONE:
			if self.input == None:
				KEY = True
			else:
				if self.device.events[self.input] == INPUT:
					KEY = True

				if self.isWheel == True:
					if INPUT == logic.KX_INPUT_JUST_ACTIVATED:
						if self.device.events[self.input] == logic.KX_INPUT_ACTIVE:
							KEY = True
					if INPUT == logic.KX_INPUT_ACTIVE:
						if self.device.events[self.input] == logic.KX_INPUT_JUST_ACTIVATED:
							KEY = True

		## Returns ##
		if INPUT == logic.KX_INPUT_NONE:
			if KEY == True and PAD == True:
				return True
		else:
			if KEY == True or PAD == True:
				return True

		return False

	def checkModifiers(self):
		KEYBOARD = logic.keyboard.events
		ACTIVE = logic.KX_INPUT_ACTIVE

		S = False
		C = False
		A = False

		if self.modifiers["S"] == None:
			S = None
		elif KEYBOARD[events.LEFTSHIFTKEY] == ACTIVE or KEYBOARD[events.RIGHTSHIFTKEY] == ACTIVE:
			S = True

		if self.modifiers["C"] == None:
			C = None
		elif KEYBOARD[events.LEFTCTRLKEY] == ACTIVE or KEYBOARD[events.RIGHTCTRLKEY] == ACTIVE:
			C = True

		if self.modifiers["A"] == None:
			A = None
		elif KEYBOARD[events.LEFTALTKEY] == ACTIVE or KEYBOARD[events.RIGHTALTKEY] == ACTIVE:
			A = True

		if self.input == None:
			if S == None and C == None and A == None:
				return False

		if self.modifiers["S"] == S and self.modifiers["C"] == C and self.modifiers["A"] == A:
			return True

		return False

	## KEY EVENTS ##
	def active(self):
		if self.checkInput(logic.KX_INPUT_ACTIVE) == True:
			return True

		return False

	def tap(self):
		if self.checkInput(logic.KX_INPUT_JUST_ACTIVATED) == True:
			return True

		return False

	def released(self):
		if self.checkInput(logic.KX_INPUT_JUST_RELEASED) == True:
			return True

		return False

	def inactive(self):
		if self.checkInput(logic.KX_INPUT_NONE) == True:
			return True

		return False

	def axis(self):
		if self.sceneGamepadCheck() == False:
			return 0.0

		JOYID = self.gamepad["Index"]
		AXIS = self.gamepad["Axis"]
		TYPE = self.gamepad["Type"]

		if JOYID == None or AXIS == None or TYPE[1] != "A":
			return 0.0

		VALUE = events.JOYBUTTONS[JOYID]["Axis"][AXIS]["VALUE"]
		ABSVAL = abs(VALUE)

		if TYPE[0] == "POS":
			if VALUE > 0:
				return ABSVAL

		elif TYPE[0] == "NEG":
			if VALUE < 0:
				return ABSVAL

		elif TYPE[0] == "SLIDER":
			if VALUE > 0:
				SLIDER = (VALUE+1)*0.5
				return SLIDER

		return 0.0


## Mouse Look Base Class ##
class MouseLook:

	def __init__(self, SPEED, SMOOTH=10):
		self.ratio = render.getWindowHeight()/render.getWindowWidth()
		self.update(SPEED, SMOOTH)
		self.center()

	def update(self, SPEED=None, SMOOTH=None):
		if SPEED != None:
			self.input = SPEED
		if SMOOTH != None:
			self.smoothing = int(SMOOTH)

	def center(self):
		self.OLD_X = [0]*self.smoothing
		self.OLD_Y = [0]*self.smoothing

		logic.mouse.position = (0.5, 0.5)

	def axis(self):

		RAW_X, RAW_Y = logic.mouse.position

		if self.smoothing > 1:
			NEW_X = (0.5-RAW_X)*2
			NEW_Y = (0.5-RAW_Y)*2

			AVG_X = 0
			AVG_Y = 0

			for IX in range(self.smoothing):
				AVG_X += self.OLD_X[IX]

			for IY in range(self.smoothing):
				AVG_Y += self.OLD_Y[IY]

			msX = AVG_X/self.smoothing
			msY = AVG_Y/self.smoothing

			self.OLD_X.insert(0, NEW_X)
			self.OLD_Y.insert(0, NEW_Y)
			self.OLD_X.pop()
			self.OLD_Y.pop()

		else:
			msX = (0.5-RAW_X)*2
			msY = (0.5-RAW_Y)*2

		X = msX*(self.input*0.4)
		Y = msY*(self.input*0.4)*self.ratio

		logic.mouse.position = (0.5, 0.5)

		return (X,Y)


## Updates Joystick Values ##
def GAMEPADDER():

	for JOYID in events.JOYBUTTONS:
		if logic.joysticks[JOYID] != None:

			for BUTID in events.JOYBUTTONS[JOYID]["Buttons"]:

				if BUTID in logic.joysticks[JOYID].activeButtons:
					if events.JOYBUTTONS[JOYID]["Buttons"][BUTID] == 0 or events.JOYBUTTONS[JOYID]["Buttons"][BUTID] == 3:
						events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 1
					else:
						events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 2
				else:
					if events.JOYBUTTONS[JOYID]["Buttons"][BUTID] == 2 or events.JOYBUTTONS[JOYID]["Buttons"][BUTID] == 1:
						events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 3
					else:
						events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 0

			for AXIS in events.JOYBUTTONS[JOYID]["Axis"]:

				RAWINPUT = logic.joysticks[JOYID].axisValues[AXIS]
				VALUE = 0.0
				ZONE = 0.2

				if RAWINPUT > ZONE:
					VALUE = (RAWINPUT-ZONE)*(1/(1-ZONE))
				if RAWINPUT < -ZONE:
					VALUE = (RAWINPUT+ZONE)*(1/(1-ZONE))

				events.JOYBUTTONS[JOYID]["Axis"][AXIS]["VALUE"] = VALUE

				if RAWINPUT > 0.5:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] == 0 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] == 3:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] = 1
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] = 2
				else:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] == 2 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] == 1:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] = 3
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["POS"] = 0

				if RAWINPUT < -0.5:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] == 0 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] == 3:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] = 1
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] = 2
				else:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] == 2 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] == 1:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] = 3
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["NEG"] = 0

				if RAWINPUT > -0.5:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] == 0 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] == 3:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] = 1
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] = 2
				else:
					if events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] == 2 or events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] == 1:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] = 3
					else:
						events.JOYBUTTONS[JOYID]["Axis"][AXIS]["SLIDER"] = 0

		else:
			print("GAMEPAD ERROR:", JOYID, "Not Found!")


## Reset Condition of all Gamepad Values ##
def RESET_GAMEPAD():
	for JOYID in events.JOYBUTTONS:
		for BUTID in events.JOYBUTTONS[JOYID]["Buttons"]:
			events.JOYBUTTONS[JOYID]["Buttons"][BUTID] = 0

		for AXIS in events.JOYBUTTONS[JOYID]["Axis"]:
			events.JOYBUTTONS[JOYID]["Axis"][AXIS] = {"NEG":0, "POS":0, "SLIDER":0, "VALUE":0.0}


# Update Joysticks - This lives on the first scene
logic.getSceneList()[0].pre_draw.append(GAMEPADDER)

print("input.py Imported")

