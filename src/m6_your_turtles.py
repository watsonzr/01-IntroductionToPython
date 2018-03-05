"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zack Watson.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window=rg.TurtleWindow()
window.delay(50)

zack=rg.SimpleTurtle('turtle')
zack.pen = rg.Pen('green',10)
zack.speed = 10

callan=rg.SimpleTurtle('turtle')
callan.pen=rg.Pen('magenta',5)
callan.speed = 10

zack.pen_up()
zack.right(45)
zack.backward(500)
zack.left(45)
zack.pen_down()
zack.forward(800)
zack.left(40)
zack.backward(1000)
zack.right(40)
zack.forward(750)
zack.pen_up()

callan.pen_up()
callan.left(45)
callan.backward(350)
callan.right(45)
callan.pen_down()
callan.draw_square(500)
callan.pen_up()
callan.forward(250)
radius = 250
callan.pen=rg.Pen('yellow',10)

for k in range(12):

    callan.pen_down()
    callan.draw_circle(radius)
    callan.pen_up()
    callan.left(90)
    callan.forward(10)
    callan.right(90)
    radius = radius-20

zack.right(40)
zack.backward(1000)
zack.right(50)
zack.pen = rg.Pen('cyan',5)
zack.speed = 20

for j in range(14):

    zack.pen_down()
    zack.forward(50)
    zack.pen_up()
    zack.left(90)
    zack.forward(50)
    zack.right(90)

window.close_on_mouse_click()