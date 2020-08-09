import maya.OpenMayaUI as omui

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from shiboken2 import wrapInstance

def maya_main_window():
    '''
    Return the Maya main window widget as a Python object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def hello_world():
    label = QtWidgets.QLabel("Hello World", parent=maya_main_window())
    label.setWindowFlags(QtCore.Qt.Window)
    label.show()

if __name__ == "__main__":
    hello_world()