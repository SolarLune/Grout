# targetscreen indicates where the currently selected window should tile.
# "mouse": Apply the tile to whichever screen the mouse is over. 
# "primary": Apply the tiling on the primary screen.
# "auto": Apply the tiling to the screen the window is already on.
targetScreen = "mouse"

# The border variables indicate how much of each edge of each screen tiling should avoid (in pixels).
# This is useful for panels or other objects that prevent window placement.
leftBorder = 0
rightBorder = 0
topBorder = 0
bottomBorder = 0

# margin indicates the distance in pixels to leave around the border of each tile 
# and the program's edges.
margin = 8

# fillExtents indicates whether windows should fill their tiles completely, or leave 
# space according to the window manager's hints (GTK apps are inset something fierce
# around their actual border). This also ensures windows take titlebars into account
# when applying the tiling.
fillExtents = True

# currentLayout is the currently specified tile layout in the layout library, referenced by name. 
# If you want to have a different layout for each screen, simply specify the name of the layouts in the 
# currentLayout list. The screens are organized horizontally, from left-to-right, like so:
# currentLayout = [
# 	"full",       #   Screen #1
# 	"squares",    #   Screen #2
# 	"halvesH",    #   Screen #3
# ]

currentLayout = [
	"major minor",
]

# The layout library; you can make a new layout by just adding one below.
# The numbers indicate the size and position of each tile. Running grout.py and passing the number as 
# the argument will set the currently active window to correspond to the number in the layout.
layoutLibrary = {

	"major minor": [
		[1, 2],
		[1, 3],
	],

	"halfH":[
		[1, 2],
	],

	"halfV":[
		[1],
		[2],
	],
	
	"thirdsH":[
		[1, 2, 3],
	],

	"thirdsV":[
		[1],
		[2],
		[3],
	],

	"fourthsH":[
		[1, 2, 3, 4],
	],

	"fourthsV":[
		[1],
		[2],
		[3],
		[4],
	],

	"centeredV":[
		[0, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 1, 1, 1, 1, 1, 0],
		[0, 2, 2, 2, 2, 2, 2, 0],
		[0, 2, 2, 2, 2, 2, 2, 0],
		[0, 2, 2, 2, 2, 2, 2, 0],
		[0, 2, 2, 2, 2, 2, 2, 0],
	],

	"centeredH":[
		[0, 0, 0, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 2, 2, 2, 2],
		[1, 1, 1, 1, 2, 2, 2, 2],
		[1, 1, 1, 1, 2, 2, 2, 2],
		[0, 0, 0, 0, 0, 0, 0, 0],
	],

	"squares":[
		[1, 2, 2],
		[1, 2, 2],
		[4, 3, 3],
	],

	"grid2x2":[
		[1, 2],
		[4, 3],
	],

	"columns":[
		[1, 2],
		[1, 3],
		[1, 4],
	],

	"columns 2":[
		[1, 2, 3],
		[1, 2, 4],
		[1, 2, 5],
	],

	"rows": [
		[1, 1, 1],
		[2, 3, 4]
	],

	"rows 2": [
		[1, 1, 1],
		[2, 2, 2],
		[3, 4, 5],
	],

	"full": [
		[1],
	],

}