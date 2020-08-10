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


class TestDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Test Dialog"

    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)

        # Set the UI name so that it can be used as a parent for script jobs.
        # Script jobs are then deleted automatically when the UI is deleted.
        self.setObjectName("MyUniqueObjectName")

        self.setFixedSize(300, 160)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        # Use parent flag to parent the scriptJob to the UI
        job_number = cmds.scriptJob(event=["DagObjectCreated", "on_dag_object_created()"], parent="MyUniqueObjectName")
        print("Added job: {0}".format(job_number))

    def create_widgets(self):
        pass

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

    def create_connections(self):
        pass


if __name__ == "__main__":

    try:
        test_dialog.close() # pylint: disable=E0601
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()
