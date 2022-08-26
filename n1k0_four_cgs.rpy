init:
    image n1k0_four_remy4_kiss = "cg/n1k0/remy4_kiss.jpg"


label n1k0_four_remy4_kiss:
    show black with dissolve
    show n1k0_four_remy4_kiss:
        anchor (0.5, 0)
        pos (0.5, 0)
        linear 4.0 ypos -0.8
    with dissolveslow
    $ renpy.pause (4.5)
    hide n1k0_four_remy4_kiss
    hide black
    hide remyrom
    hide remy
    with fade
    jump n1k0_four_remy4_kiss_end


init:
    image n1k0_four_remycomic_notice = "cg/n1k0/remynotice.jpg"
    image n1k0_four_remycomic_smile = "cg/n1k0/remysmile.jpg"
    image n1k0_four_remycomic_love = "cg/n1k0/remylove.jpg"

label n1k0_four_remycomic_hatchery:
    show black with dissolve
    show n1k0_four_remycomic_notice:
        anchor (0.5, 1.0)
        pos (0.4, 1.0)
        linear 1.0 xpos 0.5
    with dissolve
    $ renpy.pause (2.5)
    if remystatus == "good":
        show n1k0_four_remycomic_love:
            anchor (0.5, 1.0)
            pos (0.4, 1.0)
            linear 1.0 xpos 0.5
        with dissolvemed
    else:
        show n1k0_four_remycomic_smile:
            anchor (0.5, 1.0)
            pos (0.4, 1.0)
            linear 1.0 xpos 0.5
        with dissolvemed
    $ renpy.pause (2.5)

    hide n1k0_four_remycomic_notice
    hide n1k0_four_remycomic_smile
    hide n1k0_four_remycomic_love
    hide black
    with dissolve
    return