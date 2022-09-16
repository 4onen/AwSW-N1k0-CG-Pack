init:
    image n1k0_four_adine_tree = im.Scale("cg/n1k0/adinetree/adinetree.jpg", 1920, 1920)
    image n1k0_four_adine_tree_leaves = Fixed(
        SnowBlossom("cg/n1k0/adinetree/adinetree_leafr.png", 29, xspeed=(-25, 25), yspeed=(60, 180), fast=True), # start=3),
        SnowBlossom("cg/n1k0/adinetree/adinetree_leafc.png", 29, xspeed=(-25, 25), yspeed=(60, 180), fast=True), # start=3),
        SnowBlossom("cg/n1k0/adinetree/adinetree_leafl.png", 29, xspeed=(-25, 25), yspeed=(60, 180), fast=True), # start=3),
    )

label n1k0_four_adine_tree:
    m "I saw her feeble attempt to regain control as she barely managed to steady herself enough to get back to the beach. Sand jumped up behind her as the air under her wings slammed into the beach, ground effect sending her practically bouncing off and into the treeline."
    c "Adine! Are you alright?"
    show n1k0_four_adine_tree at Pan((0,0),(0,600), 3.0)
    show n1k0_four_adine_tree_leaves
    with dissolvemed
    $ renpy.pause (2.5)
    Ad disappoint "H... help..."
    m "I immediately set about untangling Adine from the ropes she'd become caught in."
    c "What are these ropes even from?"
    hide n1k0_four_adine_tree_leaves with dissolveslow
    m "Looking around, I spotted a wicker basket on its side, a little ways into the forest."
    Ad disappoint "I spotted this basket hanging from upper branches of the trees. I thought it'd be a less painful collision than with the branches."
    Ad disappoint "Maybe someone wanted to keep their picnic away from small scavengers?"
    Ad disappoint "Obviously I wasn't supposed to be hitting the treeline at all."

    hide n1k0_four_adine_tree with dissolve

    m "Freeing Adine, she was able to get back to her feet. I handed back her goggles from the grass nearby."

    show adine disappoint b with dissolve

    jump n1k0_four_adine_tree_end

label n1k0_four_adine_tree_basketreturn:
    Ad disappoint b "Yeah, let's put the basket up again, then head back."
    jump n1k0_four_adine_tree_basketreturn_end




init:
    image n1k0_four_ipsum_coffee = im.Scale("cg/n1k0/ipsum_coffee.jpg", 1920, 2496)

label n1k0_four_ipsum_coffee:
    Lo normal flip "And there he goes. Charming fellow isn't--"
    show lorem shy flip with dissolve
    Ip happy "Success!"
    show n1k0_four_ipsum_coffee at Pan((0,0), (0,400), 4.0) with dissolveslow
    Lo think flip "Ipsum? What succeeded?"
    show n1k0_four_ipsum_coffee at Transform(ypos=-1100) with ease
    m "My gaze dropped to the mug in his hand, and the heady aroma arising from it."
    Ip happy "The coffeemaker works again."
    Lo relieved flip "You put some dangerous chemicals through that. Are you sure it's safe to be drinking from again?"
    show n1k0_four_ipsum_coffee at Transform(ypos=-728) with ease
    Ip normal "Would I be drinking from it if it wasn't?"
    Lo think flip "Honestly? With you I'm not sure."
    Ip happy "Either way, other experiments to finish up as well. I'll be out later."
    hide n1k0_four_ipsum_coffee with fade
    play sound "fx/door/close2.wav"
    $ renpy.pause (0.8)
    Lo normal flip "As I was saying. Charming fellow, isn't he?"
    jump n1k0_four_ipsum_coffee_end




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