"""
main.py

Main file, config and create the main window for the application, also receive
all the exception not catched by the classes that raises.

It also handles the comunications between classes with events.

                                                                      2023-03-09
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from loguru import logger


class MainWindow(QMainWindow):
    """
    Class to create the main windows of the application.

    """

    # --- Constructor ----------------------------------------------------------
    """
    Config the Main Window of the application, set the size, icon, status bar
    menu bar, title, status and MDI.
    
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._path = sys.path[0] + '\\'

        self.setGeometry(0, 0, 1024, 768)
        self.setWindowIcon(QtGui.QIcon(self._path + 'SIM.ico'))
        self.setWindowTitle("SIM")

        # Set MDI area
        self.mdi = self.config_mdi()
        self.menu_bar = self.config_menubar()
        self.stat_bar = self.config_statusbar()

        self.showMaximized()

        self.show()

        # --- End __init__()

    # --- Override Events/Methods ----------------------------------------------
    """
    Override the keypress event to control the maximmized/minimized window with
    the F11 key, and close the application with the F12 key.
    
    """
    def keyPressEvent(self, e):
        """
        Overrided KeyPressEvent to control the maximmized/minimized window.

        :param e: key pressed
        :return: None

        """

        if e.key() == QtCore.Qt.Key_F12:
            self.close()  # TODO: add confirmation dialog
        if e.key() == QtCore.Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

        # --- End keyPressEvent()

    # --- Config Main Window ---------------------------------------------------
    """
    Methods uses to config the main windows:
    
        * config_mdi()
        * config_menubar()
        * config_statusbar()
    
    """
    def config_mdi(self):
        """
        Configure the MDI window.

        :return: Configured MDI Windows
        """

        mdi = QMdiArea(self)

        self.setCentralWidget(mdi)

        return mdi

        # --- End config_mdi()

    def config_menubar(self):
        """
        Configure the main window menu bar.

        :return: Configured main menubar
        """

        # --- Main menubar -----------------------------------------------------
        mb = self.menuBar()

        # --- Define items of the menu bar -------------------------------------
        # --- Menu File ---
        menu_file = mb.addMenu('&File')

        # Define actions (File dropdown items)
        ac_new = QtWidgets.QAction('&New', self)
        ac_open = QtWidgets.QAction('&Open', self)
        ac_exit = QtWidgets.QAction('E&xit', self)

        # Set statusbar tips

        # Add actions
        menu_file.addAction(ac_new)
        menu_file.addAction(ac_open)
        menu_file.addSeparator()
        menu_file.addAction(ac_exit)

        # Connect Actions
        ac_exit.triggered.connect(self.close)

        # --- Menu ADM ---
        menu_adm = mb.addMenu('&ADM')

        # Define actions (File dropdown items)
        ac_process = QtWidgets.QAction('&Office AMD', self)
        ac_task = QtWidgets.QAction('&Task AMD', self)

        # Set statusbar tips
        ac_process.setStatusTip('Process AMD')
        ac_task.setStatusTip('Task AMD')

        # Add actions
        menu_adm.addAction(ac_process)
        menu_adm.addAction(ac_task)

        # Connect Actions
        pass

        # --- Menu Help ---
        menu_help = mb.addMenu('&Ayuda')

        # Define actions (File dropdown items)
        ac_help = QtWidgets.QAction('&Help', self)
        ac_about = QtWidgets.QAction('A&bout...', self)

        # Set statusbar tips

        # Add actions
        menu_help.addAction(ac_help)
        menu_help.addSeparator()
        menu_help.addAction(ac_about)

        # Connect Actions
        pass

        # --- return configured menubar ----------------------------------------
        return mb

        pass    # --- End config_menubar()

    def config_statusbar(self):
        """
        Configure the main window status bar.

        :return: Configured main statusbar
        """

        # --- Main menubar -----------------------------------------------------
        sb = self.statusBar()

        sb.setFixedHeight(20)
        sb.setStyleSheet("background-color :lightgrey")

        sb.showMessage('Ready', 5000)

        # --- return configured menubar ----------------------------------------
        return sb

        # --- End config_statusbar()

    pass  # END of CLASS


# --- Main Process -------------------------------------------------------------
def main():
    """
    Main precces for the application.

    :return: NONE
    """
    try:

        # --- Get application path
        _path = sys.path[0] + '\\'

        # --- Create application
        sim = QApplication(sys.argv)
        main_window = MainWindow()
        logger.info("Application created.")

        # --- Create Event Handler
        # TODO: Create EventHandler
        logger.info("EventHandler created.")

        # --- Execute application
        sys.exit(sim.exec_())

    except Exception as e:
        logger.error(e)
        # TODO: Log the exception and show a windows with the message

    # --- End main()


# Duh ! ------------------------------------------------------------------------
if __name__ == '__main__':
    main()
