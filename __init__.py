from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

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
    print("remy4_and_me()")

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
