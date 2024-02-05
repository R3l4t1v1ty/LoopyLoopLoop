
# init python:
#     import random

#     class LoopyLoopLoop:

#         def __init__(self, dimensions, tiles):

#             self.dim = dimensions;
#             self.tiles = tiles;
#             self.randomize()
#             self.image = [
#             "images/loop0.png",
#             "images/loop1.png",
#             "images/loop2.png",
#             "images/loop3.png",
#             "images/loop4.png"
#             ]
#             self.anim = 0
#             return

#         def randomize(self):

#             for i in range(len(self.tiles)):

#                 for j in range(len(self.tiles[i])):

#                     if self.tiles[i][j][0] is not None:
                        
#                         self.tiles[i][j][1] = random.randint(0,3); 

#             return



#         def check_if_done(self):

#             for i in range(len(self.tiles)):

#                 for j in range(len(self.tiles[i])):

#                     if self.tiles[i][j][0] is not None:

#                         if self.tiles[i][j][0] == 0:

#                             if self.tiles[i][j][1]%2 != self.tiles[i][j][2]%2:

#                                 return False

#                         if self.tiles[i][j][0] != 4 and self.tiles[i][j][0] != 0:

#                             if self.tiles[i][j][1]%4 != self.tiles[i][j][2]%4:

#                                 return False


#             return True


#         def rotate90(self, ver, hor):

#             self.anim = 1
#             self.tiles[ver][hor][1] += 1

#             #self.tiles[ver][hor][1] %= 4

            
#             return

# transform rotation(angle, anim):
    
#     linear 0.17*anim rotate angle

# screen loopy_screen():

#     modal True
#     zorder 20

#     frame:
#         xsize 1215
#         ysize 945
#         padding (0,0)
#         background u'#0000'
#         xalign 0.5
#         yalign 0.5

#         for i in range(len(loopy.tiles)):

#             for j in range(len(loopy.tiles[i])):
                
#                 if loopy.tiles[i][j][0] is not None:

#                     imagebutton:

#                         idle loopy.image[loopy.tiles[i][j][0]]

#                         xpos 135*j
#                         ypos 135*i

#                         action [Function(loopy.rotate90, ver=i, hor=j), Jump("loopy_label")]

#                         at rotation(angle = 90*loopy.tiles[i][j][1], anim = loopy.anim)

#     if loopy.check_if_done():

#         frame:

#             xsize 1215
#             ysize 945
#             padding (0,0)
#             background u'#191316aa'
#             modal True
#             xalign 0.5
#             yalign 0.5

#             text "You Won!" size 100 xalign 0.5 yalign 0.5

#             at transform:
#                 alpha 0.0
#                 linear 0.2
#                 linear 2.0 alpha 1.0

# label loopy_label:
#     $ renpy.checkpoint()
#     jump scr

# label start:

#     $ loopy = LoopyLoopLoop(
#         dimensions = (7,9), 
#         tiles=[ # [type, start rot, end rot]
#         [[None],[1,0,0],[None],[1,0,0],[2,0,0],[0,0,1],[3,0,0],[2,0,1],[None]],
#         [[None],[3,0,3],[2,0,1],[2,0,3],[3,0,1],[2,0,0],[2,0,2],[2,0,3],[1,0,1]],
#         [[None],[1,0,2],[3,0,3],[0,0,1],[4,0,0],[3,0,1],[1,0,0],[None],[None]],
#         [[1,0,3],[0,0,1],[4,0,0],[1,0,1],[0,0,0],[2,0,3],[4,0,0],[0,0,1],[1,0,1]],
#         [[None],[2,0,0],[4,0,0],[2,0,1],[3,0,3],[0,0,1],[2,0,2],[None],[None]],
#         [[None],[3,0,3],[3,0,1],[2,0,3],[4,0,0],[1,0,1],[1,0,0],[2,0,0],[1,0,1]],
#         [[None],[2,0,3],[3,0,2],[0,0,1],[3,0,2],[0,0,1],[3,0,2],[2,0,2],[None]]
#         ]
#         )
#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
# label scr:
#     show screen loopy_screen()

#     pause

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return
