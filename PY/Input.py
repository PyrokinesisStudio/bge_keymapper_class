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


print("Input.py Imported")


class KEYBASE:

	def __init__(self, ID, SIMPLE, KEY, DEVICE, SHIFT=None, CTRL=None, ALT=None, JOYINDEX=0, JOYBUTTON=None, JOYAXIS=None, JOYAXISTYPE=("POS", "A")):

		## Catch Failures ##
		if JOYINDEX >= len(logic.joysticks):
			JOYINDEX = None
		elif logic.joysticks[JOYINDEX] == None or KEY == None:
			JOYINDEX = None
		else:
			if JOYAXIS != None:
				if JOYAXIS >= len(logic.joysticks[JOYINDEX].axisValues):
					JOYINDEX = None
			if JOYBUTTON != None:
				if JOYBUTTON >= logic.joysticks[JOYINDEX].numButtons:
					JOYINDEX = None

		self.id = ID
		self.simple_name = SIMPLE
		self.input = KEY
		self.device_name = DEVICE
		self.input_name = events.EventToString(KEY)
		self.modifiers = {"S":SHIFT, "C":CTRL, "A":ALT}
		self.isWheel = False
		self.autoDevice()
		self.gamepad = {"Index":JOYINDEX, "Button":JOYBUTTON, "Axis":JOYAXIS, "Type":JOYAXISTYPE}

	def update(self, NEWKEY, NEWDEVICE=None):
		self.input = NEWKEY
		if NEWDEVICE != None:
			self.device_name = NEWDEVICE
		if NEWKEY != None:
			self.input_name = events.EventToString(self.input)
		else:
			self.input_name = "NONE"
			self.gamepad["Index"] = None
		self.autoDevice()

	def autoDevice(self):
		if self.device_name == "Keyboard":
			self.device = logic.keyboard

		elif self.device_name == "Mouse":
			self.device = logic.mouse

			if self.input == events.WHEELDOWNMOUSE or self.input == events.WHEELUPMOUSE:
				self.isWheel = True

	def checkInput(self, INPUT):
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

				if self.isWheel == True and INPUT == logic.KX_INPUT_JUST_ACTIVATED:
					if self.device.events[self.input] == logic.KX_INPUT_ACTIVE:
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

class MOUSELOOK:

	def __init__(self, ID, SIMPLE, KEY, DEVICE):
		self.id = ID
		self.simple_name = SIMPLE
		self.input = KEY
		self.device_name = DEVICE
		self.input_name = "MOUSEPOS"
		SCREEN = [render.getWindowWidth(), render.getWindowHeight()]
		self.ratio = SCREEN[1]/SCREEN[0]
		self.smoothing = int(10)
		self.OLD_X = [0]*self.smoothing
		self.OLD_Y = [0]*self.smoothing
		self.interp = True

	def update(self,NEWKEY,NEWDEVICE=None):
		self.input = NEWKEY
		if NEWDEVICE != None:
			self.device_name = NEWDEVICE

	def center(self):
		self.OLD_X = [0]*self.smoothing
		self.OLD_Y = [0]*self.smoothing

		logic.mouse.position = (0.5, 0.5)

	def active(self):

		RAW_X, RAW_Y = logic.mouse.position

		if self.interp == True and self.smoothing > 1:
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




