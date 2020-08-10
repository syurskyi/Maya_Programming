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


class EventFilteringExample(QtWidgets.QDialog):

    WINDOW_TITLE = "Event Filtering Example"

    def __init__(self, parent=maya_main_window()):
        super(EventFilteringExample, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setFixedSize(300, 200)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.line_edit = QtWidgets.QLineEdit()
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems(["High", "Medium", "Low"])

    def create_layout(self):
        main_layout = QtWidgets.QFormLayout(self)
        main_layout.setContentsMargins(6, 6, 6, 6)

        main_layout.addRow("Name:", self.line_edit)
        main_layout.addRow("Quality:", self.combo_box)



if __name__ == "__main__":

    try:
        event_filtering_dialog.close() # pylint: disable=E0601
        event_filtering_dialog.deleteLater()
    except:
        pass

    event_filtering_dialog = EventFilteringExample()
    event_filtering_dialog.show()
