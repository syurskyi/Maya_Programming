from functools import partial

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


class CustomColorButton(QtWidgets.QWidget):

    color_changed = QtCore.Signal(QtGui.QColor)


    def __init__(self, color=QtCore.Qt.white, parent=None):
        super(CustomColorButton, self).__init__(parent)

        self.setObjectName("CustomColorButton")

        self.create_control()

        self.set_size(50, 14)
        self.set_color(color)

    def create_control(self):
        """ 1) Create the colorSliderGrp """
        window = cmds.window()
        self._name = cmds.colorSliderGrp()
        # print("original name: {0}".format(self._name))

        """ 2) Find the colorSliderGrp widget """
        color_slider_obj = omui.MQtUtil.findControl(self._name)
        if color_slider_obj:
            self._color_slider_widget = wrapInstance(long(color_slider_obj), QtWidgets.QWidget)

            """ 3) Reparent the colorSliderGrp widget to this widget """
            main_layout = QtWidgets.QVBoxLayout(self)
            main_layout.setObjectName("main_layout")
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.addWidget(self._color_slider_widget)

            """ 4) Update the colorSliderGrp control name (used by Maya) """
            self._name = omui.MQtUtil.fullName(long(color_slider_obj))
            # print("new name: {0}".format(self._name))

            """ 5) Identify/store the colorSliderGrp’s child widgets (and hide if necessary)  """
            # children = self._color_slider_widget.children()
            # for child in children:
            #     print(child)
            #     print(child.objectName())
            # print("---")

            self._slider_widget = self._color_slider_widget.findChild(QtWidgets.QWidget, "slider")
            if self._slider_widget:
                self._slider_widget.hide()

            self._color_widget = self._color_slider_widget.findChild(QtWidgets.QWidget, "port")

            cmds.colorSliderGrp(self._name, e=True, changeCommand=partial(self.on_color_changed))


        cmds.deleteUI(window, window=True)

    def set_size(self, width, height):
        self._color_slider_widget.setFixedWidth(width)
        self._color_widget.setFixedHeight(height)

    def set_color(self, color):
        color = QtGui.QColor(color)

        cmds.colorSliderGrp(self._name, e=True, rgbValue=(color.redF(), color.greenF(), color.blueF()))
        self.on_color_changed()

    def get_color(self):
        # color = cmds.colorSliderGrp(self._color_slider_widget.objectName(), q=True, rgbValue=True)
        color = cmds.colorSliderGrp(self._name, q=True, rgbValue=True)

        color = QtGui.QColor(color[0] * 255, color[1] * 255, color[2] * 255)
        return color

    def on_color_changed(self, *args):
        self.color_changed.emit(self.get_color())


class TestDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Embedding Maya Controls"

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setObjectName("TestDialog")

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(320, 150)

        self.foreground_color = QtCore.Qt.white
        self.background_color = QtCore.Qt.black

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.foreground_color_btn = CustomColorButton(self.foreground_color)
        self.background_color_btn = CustomColorButton(self.background_color)

        self.print_fg_color_btn = QtWidgets.QPushButton("Get FG")
        self.print_bg_color_btn = QtWidgets.QPushButton("Get BG")

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        color_layout = QtWidgets.QFormLayout()
        color_layout.setObjectName("color_layout")
        color_layout.addRow("Foreground:", self.foreground_color_btn)
        color_layout.addRow("Background:", self.background_color_btn)

        color_grp = QtWidgets.QGroupBox("Color Options")
        color_grp.setObjectName("colorGrp")
        color_grp.setLayout(color_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(2)
        button_layout.addWidget(self.print_fg_color_btn)
        button_layout.addWidget(self.print_bg_color_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setObjectName("test_dialog_main_layout")
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.addWidget(color_grp)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.foreground_color_btn.color_changed.connect(self.on_foreground_color_changed)
        self.background_color_btn.color_changed.connect(self.on_background_color_changed)

        self.print_fg_color_btn.clicked.connect(self.print_foreground_color)
        self.print_bg_color_btn.clicked.connect(self.print_background_color)

        self.close_btn.clicked.connect(self.close)

    def on_foreground_color_changed(self, new_color):
        print("New foreground color: ({0}, {1}, {2})".format(new_color.red(), new_color.green(), new_color.blue()))

    def on_background_color_changed(self, new_color):
        print("New background color: ({0}, {1}, {2})".format(new_color.red(), new_color.green(), new_color.blue()))

    def print_foreground_color(self):
        color = self.foreground_color_btn.get_color()
        print("Foreground color: ({0}, {1}, {2})".format(color.red(), color.green(), color.blue()))

    def print_background_color(self):
        color = self.background_color_btn.get_color()
        print("Background color: ({0}, {1}, {2})".format(color.red(), color.green(), color.blue()))


if __name__ == "__main__":

    try:
        embedded_test_dialog.close() # pylint: disable=E0601
        embedded_test_dialog.deleteLater()
    except:
        pass

    embedded_test_dialog = TestDialog()
    embedded_test_dialog.show()
