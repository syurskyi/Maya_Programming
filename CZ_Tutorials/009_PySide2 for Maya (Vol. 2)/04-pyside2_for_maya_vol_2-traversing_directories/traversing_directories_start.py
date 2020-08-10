from PySide2 import QtCore
from PySide2 import QtGui
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


class FileExplorerDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "File Explorer"

    DIRECTORY_PATH = "{0}scripts".format(cmds.internalVar(userAppDir=True))

    def __init__(self, parent=maya_main_window()):
        super(FileExplorerDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.refresh_list()

    def create_widgets(self):
        self.path_label = QtWidgets.QLabel(self.DIRECTORY_PATH)

        self.tree_wdg = QtWidgets.QTreeWidget()
        self.tree_wdg.setHeaderHidden(True)

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addWidget(self.path_label)
        main_layout.addWidget(self.tree_wdg)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.close_btn.clicked.connect(self.close)

    def refresh_list(self):
        print("TODO: Refresh List")


if __name__ == "__main__":

    try:
        my_dialog.close() # pylint: disable=E0601
        my_dialog.deleteLater()
    except:
        pass

    my_dialog = FileExplorerDialog()
    my_dialog.show()
