import time

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


class ThreadingExampleDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Threading Example"


    def __init__(self, parent=maya_main_window()):
        super(ThreadingExampleDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(200)

        self.running = False

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.long_operation_btn = QtWidgets.QPushButton("Really Long Operation")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.cancel_btn.setHidden(True)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.long_operation_btn)
        main_layout.addWidget(self.cancel_btn)

    def create_connections(self):
        self.long_operation_btn.clicked.connect(self.start_long_operation)
        self.cancel_btn.clicked.connect(self.cancel_long_operation)

    def start_long_operation(self):
        if not self.running:
            self.running = True

            duration = 5

            self.on_operation_started()

            print("Sleeping...")
            for i in reversed(range(duration)):
                time_remaining = i + 1

                print(time_remaining)

                time.sleep(1)

                # QtCore.QCoreApplication.processEvents()
                if not self.running:
                    print("Operation Cancelled")
                    break

            self.running = False
            self.on_operation_ended()

    def cancel_long_operation(self):
        print("Cancelling...")
        self.running = False

    def on_operation_started(self):
        self.long_operation_btn.setVisible(False)
        self.cancel_btn.setVisible(True)

    def on_operation_ended(self):
        self.cancel_btn.setVisible(False)
        self.long_operation_btn.setVisible(True)


if __name__ == "__main__":

    try:
        example_dialog.close() # pylint: disable=E0601
        example_dialog.deleteLater()
    except:
        pass

    example_dialog = ThreadingExampleDialog()
    example_dialog.show()
