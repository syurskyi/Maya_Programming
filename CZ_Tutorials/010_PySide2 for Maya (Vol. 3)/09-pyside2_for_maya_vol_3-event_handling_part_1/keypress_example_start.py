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


class CustomPlainTextEdit(QtWidgets.QPlainTextEdit):

    def __init__(self, parent=None):
        super(CustomPlainTextEdit, self).__init__(parent)


class KeypressExample(QtWidgets.QDialog):

    WINDOW_TITLE = "Keypress Example"

    def __init__(self, parent=maya_main_window()):
        super(KeypressExample, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.plain_text = CustomPlainTextEdit()

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addWidget(self.plain_text)


if __name__ == "__main__":

    try:
        keypress_dialog.close() # pylint: disable=E0601
        keypress_dialog.deleteLater()
    except:
        pass

    keypress_dialog = KeypressExample()
    keypress_dialog.show()
