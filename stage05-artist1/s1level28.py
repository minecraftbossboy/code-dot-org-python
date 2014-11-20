"""Stage 5: Puzzle 5 of 10

Now, for practice, draw a triangle and then a square to draw an envelope.
Hint: delete the 'pass' (which does nothing) with your code.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level28')

for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)


artist.turn_right(60)
for count in range(3):
    artist.move_forward(100)    
    artist.turn_left(120)
artist.check()
