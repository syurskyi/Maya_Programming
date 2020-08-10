from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class StandaloneWindow(QtWidgets.QWidget):

    wnd_instance = None

    def __init__(self):
        super(StandaloneWindow, self).__init__(parent=maya_main_window())

        self.setWindowTitle("Standalone App")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(400, 300)

        self.close_btn = QtWidgets.QPushButton("Close", self)
        self.close_btn.clicked.connect(self.close)

    @classmethod
    def display(cls):
        if not cls.wnd_instance:
            cls.wnd_instance = StandaloneWindow()

        if cls.wnd_instance.isHidden():
            cls.wnd_instance.show()
        else:
            cls.wnd_instance.raise_()
            cls.wnd_instance.activateWindow()


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = StandaloneWindow()
    test_dialog.show()

