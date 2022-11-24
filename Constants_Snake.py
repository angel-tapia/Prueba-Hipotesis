#Constant variables
pixelSize = 10
speed = 10
foodSize = 10
screenSize = 500
directions = ["Left", "Up", "Right", "Down"]
movMap = { 
    "Left"  : (-speed, 0),
    "Up"    : (0, -speed), 
    "Right" : (speed, 0),
    "Down"  : (0, speed),
}
lim = ((screenSize//pixelSize)-1)
