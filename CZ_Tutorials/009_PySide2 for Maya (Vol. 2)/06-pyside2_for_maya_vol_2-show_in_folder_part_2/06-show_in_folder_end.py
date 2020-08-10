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


class FileExplorerDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "File Explorer"

    DIRECTORY_PATH = "{0}scripts".format(cmds.internalVar(userAppDir=True))

    def __init__(self, parent=maya_main_window()):
        super(FileExplorerDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.create_actions()
        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.tree_wdg.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_wdg.customContextMenuRequested.connect(self.show_context_menu)

        self.refresh_list()

    def create_actions(self):
        self.show_in_folder_action = QtWidgets.QAction("Show in Folder", self)

    def create_widgets(self):
        self.path_label = QtWidgets.QLabel(self.DIRECTORY_PATH)

        self.tree_wdg = QtWidgets.QTreeWidget()
        self.tree_wdg.setHeaderHidden(True)

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addWidget(self.path_label)
        main_layout.addWidget(self.tree_wdg)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.show_in_folder_action.triggered.connect(self.show_in_folder)
        self.close_btn.clicked.connect(self.close)

    def refresh_list(self):
        self.tree_wdg.clear()

        self.add_children(None, self.DIRECTORY_PATH)

    def add_children(self, parent_item, dir_path):
        directory = QtCore.QDir(dir_path)
        files_in_directory = directory.entryList(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllEntries, QtCore.QDir.DirsFirst | QtCore.QDir.IgnoreCase)

        for file_name in files_in_directory:
            self.add_child(parent_item, dir_path, file_name)

    def add_child(self, parent_item, dir_path, file_name):
        file_path = "{0}/{1}".format(dir_path, file_name)
        file_info = QtCore.QFileInfo(file_path)

        if file_info.suffix().lower() == "pyc":
            return

        item = QtWidgets.QTreeWidgetItem(parent_item, [file_name])
        item.setData(0, QtCore.Qt.UserRole, file_path)

        if file_info.isDir():
            self.add_children(item, file_info.absoluteFilePath())

        if not parent_item:
            self.tree_wdg.addTopLevelItem(item)

    def show_context_menu(self, pos):
        item = self.tree_wdg.itemAt(pos)
        if not item:
            return

        file_path = item.data(0, QtCore.Qt.UserRole)
        self.show_in_folder_action.setData(file_path)

        context_menu = QtWidgets.QMenu()
        context_menu.addAction(self.show_in_folder_action)
        context_menu.exec_(self.tree_wdg.mapToGlobal(pos))

    def show_in_folder(self):
        file_path = self.show_in_folder_action.data()

        # OS specific implementations to show in folder (Explorer or Finder) and select the file
        if cmds.about(windows=True):
            if self.open_in_explorer(file_path):
                return
        elif cmds.about(macOS=True):
            if self.open_in_finder(file_path):
                return

        # Qt fallback for Linux or if the OS-specific implementation fails.
        # This only open the directory. It does not select the file.
        file_info = QtCore.QFileInfo(file_path)
        if file_info.isDir():
            QtGui.QDesktopServices.openUrl(file_path)
        else:
            QtGui.QDesktopServices.openUrl(file_info.path())

    def open_in_explorer(self, file_path):
        # Windows specific implementation
        file_info = QtCore.QFileInfo(file_path)
        args = []
        if not file_info.isDir():
            args.append("/select,")

        args.append(QtCore.QDir.toNativeSeparators(file_path))

        if QtCore.QProcess.startDetached("explorer", args):
            return True

        return False

    def open_in_finder(self, file_path):
        # macOS specific implmentation
        args = []
        args.append('-e')
        args.append('tell application "Finder"')
        args.append('-e')
        args.append('activate')
        args.append('-e')
        args.append('select POSIX file "{0}"'.format(file_path))
        args.append('-e')
        args.append('end tell')
        args.append('-e')
        args.append('return')

        if(QtCore.QProcess.startDetached("/usr/bin/osascript", args)):
            return True

        return False


if __name__ == "__main__":

    try:
        my_dialog.close() # pylint: disable=E0601
        my_dialog.deleteLater()
    except:
        pass

    my_dialog = FileExplorerDialog()
    my_dialog.show()
