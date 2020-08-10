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


class DragAndDropNodeListWidget(QtWidgets.QListWidget):


    def __init__(self, parent=None):
        super(DragAndDropNodeListWidget, self).__init__(parent)


class MeshVisibilityDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Mesh Visibility"

    def __init__(self, parent=maya_main_window()):
        super(MeshVisibilityDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.refresh_lists()

    def create_widgets(self):
        self.visible_mesh_list_wdg = DragAndDropNodeListWidget()
        self.visible_mesh_list_wdg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.hidden_mesh_list_wdg = DragAndDropNodeListWidget()
        self.hidden_mesh_list_wdg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.hide_btn = QtWidgets.QPushButton(">>")
        self.hide_btn.setFixedWidth(24)
        self.show_btn = QtWidgets.QPushButton("<<")
        self.show_btn.setFixedWidth(24)

        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        visible_mesh_layout = QtWidgets.QVBoxLayout()
        visible_mesh_layout.addWidget(QtWidgets.QLabel("Visible Meshes:"))
        visible_mesh_layout.addWidget(self.visible_mesh_list_wdg)

        hidden_mesh_layout = QtWidgets.QVBoxLayout()
        hidden_mesh_layout.addWidget(QtWidgets.QLabel("Hidden Meshes:"))
        hidden_mesh_layout.addWidget(self.hidden_mesh_list_wdg)

        show_hide_button_layout = QtWidgets.QVBoxLayout()
        show_hide_button_layout.addStretch()
        show_hide_button_layout.addWidget(self.hide_btn)
        show_hide_button_layout.addWidget(self.show_btn)
        show_hide_button_layout.addStretch()

        list_layout = QtWidgets.QHBoxLayout()
        list_layout.addLayout(visible_mesh_layout)
        list_layout.addLayout(show_hide_button_layout)
        list_layout.addLayout(hidden_mesh_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(4)
        button_layout.addStretch()
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addLayout(list_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.hide_btn.clicked.connect(self.hide_selected)
        self.show_btn.clicked.connect(self.show_selected)

        self.refresh_btn.clicked.connect(self.refresh_lists)
        self.close_btn.clicked.connect(self.close)

    def refresh_lists(self):
        self.visible_mesh_list_wdg.clear()
        self.hidden_mesh_list_wdg.clear()

        meshes = cmds.ls(type="mesh", long=True)
        meshes.sort()

        for mesh in meshes:
            transform_short_name = cmds.listRelatives(mesh, parent=True, type="transform")[0]
            transform_long_name = cmds.listRelatives(mesh, parent=True, type="transform", fullPath=True)[0]

            item = QtWidgets.QListWidgetItem(transform_short_name)
            item.setData(QtCore.Qt.UserRole, transform_long_name)

            if self.is_node_visible(transform_long_name):
                self.visible_mesh_list_wdg.addItem(item)
            else:
                self.hidden_mesh_list_wdg.addItem(item)

    def is_node_visible(self, name):
        return cmds.getAttr("{0}.visibility".format(name))

    def set_node_visible(self, name, visible):
        cmds.setAttr("{0}.visibility".format(name), visible)

    def show_nodes(self, nodes):
        for node in nodes:
            self.set_node_visible(node, True)

        self.refresh_lists()

        for i in range(self.visible_mesh_list_wdg.count()):
            item = self.visible_mesh_list_wdg.item(i)
            if item.data(QtCore.Qt.UserRole) in nodes:
                self.visible_mesh_list_wdg.setCurrentRow(i, QtCore.QItemSelectionModel.Select)

    def hide_nodes(self, nodes):
        for node in nodes:
            self.set_node_visible(node, False)

        self.refresh_lists()

        for i in range(self.hidden_mesh_list_wdg.count()):
            item = self.hidden_mesh_list_wdg.item(i)
            if item.data(QtCore.Qt.UserRole) in nodes:
                self.hidden_mesh_list_wdg.setCurrentRow(i, QtCore.QItemSelectionModel.Select)


    def show_selected(self):
        nodes = []
        selected_items = self.hidden_mesh_list_wdg.selectedItems()

        for item in selected_items:
            nodes.append(item.data(QtCore.Qt.UserRole))

        self.show_nodes(nodes)

    def hide_selected(self):
        nodes = []
        selected_items = self.visible_mesh_list_wdg.selectedItems()
        for item in selected_items:
            nodes.append(item.data(QtCore.Qt.UserRole))

        self.hide_nodes(nodes)



if __name__ == "__main__":

    try:
        mesh_dialog.close() # pylint: disable=E0601
        mesh_dialog.deleteLater()
    except:
        pass

    mesh_dialog = MeshVisibilityDialog()
    mesh_dialog.show()
