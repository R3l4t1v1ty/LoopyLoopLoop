
screen loopy_screen():

    modal True

    frame:
        xsize 1215
        ysize 945
        padding (0,0)
        background u'#0000'
        xalign 0.5
        yalign 0.5

        for i in range(len(loopy.tileset)):

            for j in range(len(loopy.tileset[i])):
                
                if loopy.tileset[i][j] is not None:

                    imagebutton:

                        idle loopy.image[loopy.tileset[i][j].code]

                        xpos 135*j
                        ypos 135*i

                        action [Function(loopy.tileset[i][j].rotate90), Jump("loopy_label")]
                        #action NullAction()
                        at rotation(angle = 90*loopy.tileset[i][j].angle, anim = loopy.tileset[i][j].anim)#, anim = loopy.anim)

    if loopy.is_solved():

        frame:

            xsize 1215
            ysize 945
            padding (0,0)
            background u'#191316aa'
            modal True
            xalign 0.5
            yalign 0.5

            vbox:
                xalign 0.5
                yalign 0.5
                text "You Won!" size 100 xalign 0.5 yalign 0.5

                textbutton _("Play again"):
                    xalign 0.5
                    yalign 0.5
                    action [Hide("loopy_screen"), Jump("start")]


            at transform:
                alpha 0.0
                linear 0.2
                linear 2.0 alpha 1.0

transform rotation(angle, anim):
    
    linear 0.17*anim rotate angle

label loopy_label:
    $ renpy.checkpoint()
    jump scr

label start:
    scene white
    $ loopy = LoopyLoopLoop(
        dim = (random.randint(4,7),random.randint(5,10))
        )
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label scr:
    show screen loopy_screen()

    pause

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return