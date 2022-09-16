from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

def ipsum_coffee():
    ( ml.find_label('lorem2')
        .search_say("Oh, my experiment is done.", depth=10000)
        .search_hide('ipsum')
        .search_with()
        .hook_to('n1k0_four_ipsum_coffee', return_link=False)
        .search_menu("He sounds fun.")
        .link_from('n1k0_four_ipsum_coffee_end')
    )

def kalinth_introduction():
    ( ml.find_label('nohelp')
        .hook_to('n1k0_four_kalinth_introduction', return_link=False)
        .search_say("Anyway, you can find all the files here. I'll leave the rest to you.")
        .link_from('n1k0_four_kalinth_introduction_end')
    )

def remy4_and_me():
    ( ml.find_label('remy4skip2')
        .search_if('remystatus == "neutral"')
        .branch_else()
        .search_menu("Kiss him.")
        .branch()
        .hook_to('n1k0_four_remy4_kiss', return_link=False, condition='player_name.lower() in ("n1k0",)')
        .search_with()
        .link_behind_from('n1k0_four_remy4_kiss_end')
    )

def remy_c4_hatchery():
    adineif = ml.find_label('c4hatchery').search_if('adinestatus == "bad"')

    branches = [
        adineif.branch('adinestatus == "none"').search_if('remygoodending == True'),
        adineif.branch('adinestatus == "none"').search_if('persistent.remygoodending == True'),
        adineif.branch_else().search_if('remygoodending == True'),
        adineif.branch_else().search_if('persistent.remygoodending == True'),
    ]

    for branch in branches:
        ( branch
            .branch()
            .search_say("Adine! Wait for me.")
            .hook_call_to('n1k0_four_remycomic_hatchery')
        )

def link_scenes():
    ipsum_coffee()
    kalinth_introduction()
    remy4_and_me()
    remy_c4_hatchery()

@loadable_mod
class AwSWMod(Mod):
    name = "N1k0 CG Pack"
    version = "v0.0"
    author = "N1k0" # Code by 4onen, art by N1k0
    dependencies = ["MagmaLink"]

    @staticmethod
    def mod_load():
        link_scenes()

    @staticmethod
    def mod_complete():
        pass
