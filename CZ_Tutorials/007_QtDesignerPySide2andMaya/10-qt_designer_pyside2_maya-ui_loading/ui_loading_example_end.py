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

    def __init__(self, parent=maya_main_window()):
        super(DesignerUI, self).__init__(parent)

        self.setWindowTitle("UI Loading")

        self.init_ui()
        self.create_layout()
        self.create_connections()

    def init_ui(self):
        f = QtCore.QFile("C:/Users/syurskyi/PycharmProjects/TD/__syurskyi_repository__/maya/tutorials/Maya_Programming/CZ_Tutorials/007_QtDesignerPySide2andMaya/10-qt_designer_pyside2_maya-ui_loading/ui_loading_example.ui")
        f.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        # self.ui = loader.load(f, parentWidget=self)
        self.ui = loader.load(f, parentWidget=None)

        f.close()

    def create_layout(self):
        # self.ui.layout().setContentsMargins(6, 6, 6, 6)
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.ui)

    def create_connections(self):
        self.ui.cancelButton.clicked.connect(self.close)


if __name__ == "__main__":

    try:
        designer_ui.close() # pylint: disable=E0601
        designer_ui.deleteLater()
    except:
        pass

    designer_ui = DesignerUI()
    designer_ui.show()
