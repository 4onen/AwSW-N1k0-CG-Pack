init:
    image n1k0_four_kalinth_introduction = im.Scale("cg/n1k0/kalinth_intro.jpg", 1920, 2400)

label n1k0_four_kalinth_introduction:
    $ renpy.pause (0.5)
    m "When I arrived at the station, I didn't see any of the police dragons I recognized."
    m "Spotting a blue dragoness at a desk not far from the entrance, I approached her."
    play music "mx/chronos.ogg" fadein 2.0
    show n1k0_four_kalinth_introduction:
        anchor (0.0, 0.0)
        pos (0.0, 0.0)
        linear 4.0 ypos -0.7
    with dissolveslow
    $ renpy.pause (2.0)
    Character(_("???"), color="#516bbb", image="kalinth") "Ah, [player_name]. Can I help you with something?"
    c "I don't think we've been introduced."
    Kl "I'm Kalinth, the police archivist."
    menu:
        "Nice to meet you.":
            $ renpy.pause (0.5)
            Kl "Likewise."
            Kl "But I assume you're not here just to meet me."
            c "Right. You wouldn't happen to have the documents on the portal put together somewhere, would you?"
            Kl "You're in luck, [player_name]! Bryce compiled all the case files a while ago."
        "I'm here to review the documents on the portal.":
            $ renpy.pause (1.0)
            $ evilpoints += 1
            Kl "Well, you're in luck. Bryce compiled all the case files a while ago."
    Kl "Just follow me to his office."
    $ renpy.pause (0.3)
    scene office at Pan ((64, 250), (0, 250), 1.5) with fade
    $ renpy.pause (0.5)
    show kalinth normal flip at Position (xpos = 0.3) with dissolve
    Kl "Ever since you came to our world, he seems to be a lot more interested in these human mysteries. I wonder if it has something to do with you?"

    jump n1k0_four_kalinth_introduction_end




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