## bge_keymapper_class
Simple class based keymapper for the Blender Game Engine with Gamepad support.  Not Compatible with UPBGE yet.

---
### Example:

`import bge`  
`import PY.keymap as keys` (this line can change depending on where the files are in relation to the blend.)  

`x, y = keys.MOUSELOOK.axis()`  

`if keys.BINDS["PLR_FORWARD"].active() == True:`  

---
### Extras Folder:

`gamepad_finder.blend`: a quick little utility to find joystick button and axis IDs to reference in binds.  change the ["ID"] game property to get logic.joysticks[ID].  multiple joysticks can be examined by creating any number of objects that run the "Text" script with different "ID" property (copy the camera).

---
Documentation coming soon...
