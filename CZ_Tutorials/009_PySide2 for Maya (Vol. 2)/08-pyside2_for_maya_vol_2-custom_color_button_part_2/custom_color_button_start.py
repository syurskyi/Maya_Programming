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


class CustomColorButton(QtWidgets.QLabel):

    def __init__(self, color=QtCore.Qt.white, parent=None):
        super(CustomColorButton, self).__init__(parent)

        self._color = QtGui.QColor() # Invalid color

        self.set_size(50, 14)
        self.set_color(color)

    def set_size(self, width, height):
        self.setFixedSize(width, height)

    def set_color(self, color):
        color = QtGui.QColor(color)

    def get_color(self):
        return self._color

    def select_color(self):
        color = QtWidgets.QColorDialog.getColor(self.get_color(), self, options=QtWidgets.QColorDialog.DontUseNativeDialog)
        if color.isValid():
            self.set_color(color)


class TestDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Custom Color Example"

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(320, 150)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.foreground_color_btn = CustomColorButton(QtCore.Qt.white)
        self.background_color_btn = CustomColorButton(QtCore.Qt.black)

        self.print_btn = QtWidgets.QPushButton("Print")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        color_layout = QtWidgets.QFormLayout()
        color_layout.addRow("Foreground:", self.foreground_color_btn)
        color_layout.addRow("Background:", self.background_color_btn)

        color_grp = QtWidgets.QGroupBox("Color Options")
        color_grp.setLayout(color_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(2)
        button_layout.addStretch()
        button_layout.addWidget(self.print_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.addWidget(color_grp)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.print_btn.clicked.connect(self.print_colors)
        self.close_btn.clicked.connect(self.close)

    def print_colors(self):
        print("Foreground Color: [{0}, {1}, {2}]".format(self.foreground_color.red(), self.foreground_color.green(), self.foreground_color.blue()))
        print("Background Color: [{0}, {1}, {2}]".format(self.background_color.red(), self.background_color.green(), self.background_color.blue()))


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
