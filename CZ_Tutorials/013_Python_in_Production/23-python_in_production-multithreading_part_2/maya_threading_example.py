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


class ThreadWorker(QtCore.QObject):

    operation_started = QtCore.Signal()
    operation_ended = QtCore.Signal()

    message_sent = QtCore.Signal(str)

    def __init__(self):
        super(ThreadWorker, self).__init__()
        self.running = False

    def run(self, duration):
        if not self.running:
            self.running = True

            self.operation_started.emit()

            self.message_sent.emit("Sleeping...")
            for i in reversed(range(duration)):
                time_remaining = i + 1

                self.message_sent.emit(str(time_remaining))

                time.sleep(1)

                QtCore.QCoreApplication.processEvents()
                if not self.running:
                    self.message_sent.emit("Operation Cancelled")
                    break

            self.running = False
            self.operation_ended.emit()

    def cancel(self):
        self.running = False


class ThreadingExampleDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Threading Example"

    run_threaded_operation = QtCore.Signal(int)
    cancel_threaded_operation = QtCore.Signal()


    def __init__(self, parent=maya_main_window()):
        super(ThreadingExampleDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(200)

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.create_thread()

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

    def create_thread(self):
        self.long_operation_thread = QtCore.QThread(self)
        self.thread_worker = ThreadWorker()

        self.run_threaded_operation.connect(self.thread_worker.run)
        self.cancel_threaded_operation.connect(self.thread_worker.cancel)

        self.thread_worker.operation_started.connect(self.on_operation_started)
        self.thread_worker.operation_ended.connect(self.on_operation_ended)
        self.thread_worker.message_sent.connect(self.on_message_received)

        self.thread_worker.moveToThread(self.long_operation_thread)
        self.long_operation_thread.start()

    def start_long_operation(self):
        duration = 5
        self.run_threaded_operation.emit(duration)


    def cancel_long_operation(self):
        print("Cancelling...")
        self.cancel_threaded_operation.emit()

    def on_operation_started(self):
        self.long_operation_btn.setVisible(False)
        self.cancel_btn.setVisible(True)

    def on_operation_ended(self):
        self.cancel_btn.setVisible(False)
        self.long_operation_btn.setVisible(True)

    def on_message_received(self, message):
        print(message)


if __name__ == "__main__":

    try:
        example_dialog.close() # pylint: disable=E0601
        example_dialog.deleteLater()
    except:
        pass

    example_dialog = ThreadingExampleDialog()
    example_dialog.show()
