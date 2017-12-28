from aqt import mw, dialogs
from aqt.utils import showInfo
from aqt.qt import *
import anki


def translate():
    pass

def bunch_translate():
    browser = aqt.dialogs.open('Browser', mw)
    for card in browser.model.cards[:10]:
        note = mw.col.getCard(card).note()
        note.fields[0] += "[test]"
        #print(note["word"], note["translation"])
        note.flush()
        #mw.col.save()

def on_setup_menus(browser):
    menu = QMenu("&Bunch", browser.form.menubar)
    browser.form.menubar.addMenu(menu)

    translate = QAction('Bunch &Translate', browser)
    translate.triggered.connect(bunch_translate)
    menu.addAction(translate)

# add hook to setup browser menus
anki.hooks.addHook(
    'browser.setupMenus', on_setup_menus,
)
