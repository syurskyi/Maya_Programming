import os

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


class DesignerUI(QtWidgets.QDialog):

    def __init__(self, ui_path=None, parent=maya_main_window()):
        super(DesignerUI, self).__init__(parent)

        self.setWindowTitle("UI Path Example")

        self.init_ui(ui_path)
        self.create_layout()
        self.create_connections()

    def init_ui(self, ui_path=None):
        if not ui_path:
            ui_path = "{0}/ui_path_example.ui".format(os.path.dirname(__file__))

        f = QtCore.QFile(ui_path)
        f.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f, parentWidget=self)

        f.close()

    def create_layout(self):
        self.ui.layout().setContentsMargins(6, 6, 6, 6)

    def create_connections(self):
        self.ui.cancelButton.clicked.connect(self.close)


if __name__ == "__main__":

    try:
        designer_ui.close() # pylint: disable=E0601
        designer_ui.deleteLater()
    except:
        pass

    ui_path = "C:/Users/syurskyi/PycharmProjects/TD/__syurskyi_repository__/maya/tutorials/Maya_Programming/CZ_Tutorials/007_QtDesignerPySide2andMaya/11-qt_designer_pyside2_maya-pipeline_tips/ui_path_example.ui"

    designer_ui = DesignerUI(ui_path)
    designer_ui.show()
