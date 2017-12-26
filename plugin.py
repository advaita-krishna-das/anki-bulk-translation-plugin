from aqt import mw, dialogs
from aqt.utils import showInfo
from aqt.qt import *
import anki


def bunch_translate():
    showInfo("Let me bunch-translete something", mw)

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
