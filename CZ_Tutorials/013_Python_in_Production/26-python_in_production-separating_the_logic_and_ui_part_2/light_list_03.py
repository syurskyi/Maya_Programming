from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

from maya_helpers import MayaHelpers


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class LightListDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Light List"

    LIGHT_FILTERS = {
        "<All>": None,
        "Ambient Light": "ambientLight",
        "Area Light": "areaLight",
        "Directional Light": "directionalLight",
        "Point Light": "pointLight",
        "Spot Light": "spotLight"
    }

    def __init__(self, parent=maya_main_window()):
        super(LightListDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.refresh_list()

    def create_widgets(self):
        self.light_filter_cmb = QtWidgets.QComboBox()
        for light_filter in LightListDialog.LIGHT_FILTERS.keys():
            self.light_filter_cmb.addItem(light_filter)

        self.light_list_widget = QtWidgets.QListWidget()

    def create_layout(self):

        light_filter_layout = QtWidgets.QHBoxLayout()
        light_filter_layout.addWidget(QtWidgets.QLabel("Filter:"))
        light_filter_layout.addWidget(self.light_filter_cmb)
        light_filter_layout.addStretch()

        light_list_layout = QtWidgets.QVBoxLayout()
        light_list_layout.addLayout(light_filter_layout)
        light_list_layout.addWidget(self.light_list_widget)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(light_list_layout)

    def create_connections(self):
        self.light_filter_cmb.currentTextChanged.connect(self.refresh_list)
        self.light_list_widget.currentItemChanged.connect(self.select_light)

    def refresh_list(self):
        light_filter = LightListDialog.LIGHT_FILTERS[self.light_filter_cmb.currentText()]

        light_nodes = MayaHelpers.get_light_nodes(light_filter)

        self.light_list_widget.clear()
        self.light_list_widget.addItems(light_nodes)

    def select_light(self, item):
        if item:
            node = item.text()
        else:
            node = None

        MayaHelpers.select_node(node)



if __name__ == "__main__":

    try:
        light_list_dialog.close() # pylint: disable=E0601
        light_list_dialog.deleteLater()
    except:
        pass

    light_list_dialog = LightListDialog()
    light_list_dialog.show()
