from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TabBarDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "QTabBar Example"

    def __init__(self, parent=maya_main_window()):
        super(TabBarDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.tab_bar = QtWidgets.QTabBar()

        self.tab_bar.addTab("Labels")
        self.tab_bar.addTab("Buttons")
        self.tab_bar.addTab("Other")

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tab_bar)
        layout.addStretch()

    def create_connections(self):
        pass


if __name__ == "__main__":

    try:
        tabbar_dialog.close() # pylint: disable=E0601
        tabbar_dialog.deleteLater()
    except:
        pass

    tabbar_dialog = TabBarDialog()
    tabbar_dialog.show()
