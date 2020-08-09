from PySide2 import QtCore
from PySide2 import QtUiTools
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


class PreferencesDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(PreferencesDialog, self).__init__(parent)

        self.setWindowTitle("Preferences")
        self.setMinimumWidth(500)

        self.init_ui()
        self.create_layout()
        self.create_connections()

    def init_ui(self):
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load("C:/Users/syurskyi/PycharmProjects/TD/__syurskyi_repository__/maya/tutorials/Maya_Programming/CZ_Tutorials/007_QtDesignerPySide2andMaya/14-qt_designer_pyside2_maya-preferences_dialog_part_2/preferences.ui", parentWidget=None)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.ui)

    def create_connections(self):
        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.close)

    def get_option_a(self):
        return self.ui.checkBoxA.isChecked()

    def get_option_b(self):
        return self.ui.checkBoxB.isChecked()

    def get_option_c(self):
        return self.ui.checkBoxC.isChecked()


class TestDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Test Dialog"

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(300, 200)

        self.create_actions()
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_actions(self):
        self.preferences_action = QtWidgets.QAction("Preferences...", self)

    def create_widgets(self):
        self.menu_bar = QtWidgets.QMenuBar()
        edit_menu = self.menu_bar.addMenu("Edit")
        edit_menu.addAction(self.preferences_action)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.setMenuBar(self.menu_bar)

    def create_connections(self):
        self.preferences_action.triggered.connect(self.show_preferences)

    def show_preferences(self):
        preferences_dialog = PreferencesDialog(self)
        result = preferences_dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            print("Option A Checked: {0}".format(preferences_dialog.get_option_a()))
            print("Option B Checked: {0}".format(preferences_dialog.get_option_b()))
            print("Option C Checked: {0}".format(preferences_dialog.get_option_c()))


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
