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

class LabelsWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(LabelsWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Label 01"))
        layout.addWidget(QtWidgets.QLabel("Label 02"))
        layout.addWidget(QtWidgets.QLabel("Label 03"))
        layout.addWidget(QtWidgets.QLabel("Label 04"))

class ButtonsWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ButtonsWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QPushButton("Button 01"))
        layout.addWidget(QtWidgets.QPushButton("Button 02"))
        layout.addWidget(QtWidgets.QPushButton("Button 03"))
        layout.addWidget(QtWidgets.QPushButton("Button 04"))

class OthersWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(OthersWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Label"))
        layout.addWidget(QtWidgets.QPushButton("Button"))
        layout.addWidget(QtWidgets.QCheckBox("Check Box"))
        layout.addWidget(QtWidgets.QLineEdit())


class CustomTabWidget(QtWidgets.QWidget):

    def __init__(self, parent=maya_main_window()):
        super(CustomTabWidget, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        pass

    def create_layout(self):
        pass

    def create_connections(self):
        pass

    def addTab(self, widget, label):
        pass


class TabWidgetDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Custom Tab Widget Example"

    def __init__(self, parent=maya_main_window()):
        super(TabWidgetDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.labels_wdg = LabelsWidget()
        self.buttons_wdg = ButtonsWidget()
        self.others_wdg = OthersWidget()

        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.addTab(self.labels_wdg, "Labels")
        self.tab_widget.addTab(self.buttons_wdg, "Buttons")
        self.tab_widget.addTab(self.others_wdg, "Others")


    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tab_widget)
        layout.addStretch()

    def create_connections(self):
        pass


if __name__ == "__main__":

    try:
        customtabwidget_dialog.close() # pylint: disable=E0601
        customtabwidget_dialog.deleteLater()
    except:
        pass

    customtabwidget_dialog = TabWidgetDialog()
    customtabwidget_dialog.show()
