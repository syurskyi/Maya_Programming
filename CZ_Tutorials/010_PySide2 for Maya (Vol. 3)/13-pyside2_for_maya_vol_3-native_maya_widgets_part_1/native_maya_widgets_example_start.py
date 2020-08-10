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


class NativeMayaWidgetsExample(QtWidgets.QDialog):

    WINDOW_TITLE = "Native Maya Widgets"

    def __init__(self, parent=maya_main_window()):
        super(NativeMayaWidgetsExample, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setMinimumSize(200, 100)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        pass

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

    def create_connections(self):
        pass


if __name__ == "__main__":

    try:
        example_dialog.close() # pylint: disable=E0601
        example_dialog.deleteLater()
    except:
        pass

    example_dialog = NativeMayaWidgetsExample()
    example_dialog.show()
