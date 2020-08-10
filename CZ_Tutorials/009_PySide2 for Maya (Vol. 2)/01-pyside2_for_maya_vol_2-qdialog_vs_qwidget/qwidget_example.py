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


class QWidgetExample(QtWidgets.QWidget):

    WINDOW_TITLE = "QWidget Example"

    def __init__(self, parent=maya_main_window()):
        super(QWidgetExample, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(QtCore.Qt.WindowType.Window)

        self.setMinimumSize(300, 200)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.setMinimumWidth(80)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.setMinimumWidth(80)

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        pass


if __name__ == "__main__":

    try:
        widget.close() # pylint: disable=E0601
        widget.deleteLater()
    except:
        pass

    widget = QWidgetExample()
    widget.show()
