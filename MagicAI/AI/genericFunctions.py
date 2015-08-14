
def tapForRed(spell, player):
    if not spell.tapped():
        addRedMana(player)
        spell.tap()


def addRedMana(player):
    player.addMana(RED)
    
def flying(spell):
    pass
