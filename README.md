# bge_keymapper_class
Simple class based keymapper for the Blender Game Engine with Gamepad support.  Not Compatible with UPBGE yet.


Example:


import bge

import PY.keymap as keys #this line can change depending on where the files are in relation to the blend.

x, y = keys.MOUSELOOK.axis()

if keys.BINDS["PLR_FORWARD"].active() == True:

#Do Something


Documentation coming soon...
