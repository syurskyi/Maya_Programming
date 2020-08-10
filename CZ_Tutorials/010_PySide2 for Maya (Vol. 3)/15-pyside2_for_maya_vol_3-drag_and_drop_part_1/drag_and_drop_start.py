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


class TextEditor(QtWidgets.QPlainTextEdit):

    def __init__(self, parent=None):
        super(TextEditor, self).__init__(parent)

    def set_drop_enabled(self, enabled):
        print("TODO: Implement set_drop_enabled()")


class TextEditorDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Drag and Drop Example"

    def __init__(self, parent=maya_main_window()):
        super(TextEditorDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(500, 400)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.editor = TextEditor()

        self.drop_enabled_cb = QtWidgets.QCheckBox("Drop Enabled")
        self.drop_enabled_cb.setChecked(True)

        self.clear_btn = QtWidgets.QPushButton("Clear")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(4)
        button_layout.addWidget(self.drop_enabled_cb)
        button_layout.addStretch()
        button_layout.addWidget(self.clear_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addWidget(self.editor)

        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.drop_enabled_cb.toggled.connect(self.editor.set_drop_enabled)

        self.clear_btn.clicked.connect(self.clear_editor)
        self.close_btn.clicked.connect(self.close)

    def clear_editor(self):
        self.editor.setPlainText("")


if __name__ == "__main__":

    try:
        text_editor_dialog.close() # pylint: disable=E0601
        text_editor_dialog.deleteLater()
    except:
        pass

    text_editor_dialog = TextEditorDialog()
    text_editor_dialog.show()
