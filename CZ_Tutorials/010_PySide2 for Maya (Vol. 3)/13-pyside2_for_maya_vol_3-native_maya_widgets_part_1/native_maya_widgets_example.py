from PySide2 import QtCore
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


class NativeMayaWidgetsExample(QtWidgets.QDialog):

    WINDOW_TITLE = "Native Maya Widgets"

    def __init__(self, parent=maya_main_window()):
        super(NativeMayaWidgetsExample, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setMinimumSize(200, 100)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timer_fired)
        # self.timer.start()

    def create_widgets(self):
        pass

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

    def create_connections(self):
        app = QtWidgets.QApplication.instance()
        app.focusChanged.connect(self.on_focus_changed)

    def print_hierarchy(self, widget):
        if widget:
            output = []

            name = widget.objectName()
            if not name:
                name = "<Object name not set>"

            output.append("Widget: {0}".format(name))

            parent_widget = widget.parentWidget()
            while parent_widget:
                parent_name = parent_widget.objectName()
                if parent_name == "CharcoalEditor2":
                    return

                output.append("--> Parent: {0}".format(parent_name))
                parent_widget = parent_widget.parentWidget()

            output.append("---")

            print("\n".join(output))

    def on_timer_fired(self):
        focus_widget = QtWidgets.QApplication.focusWidget()
        if focus_widget:
            print("Widget with focus (object name): {0}".format(focus_widget.objectName()))

    def on_focus_changed(self, old_widget, new_widget):
        if self.isVisible():
            if new_widget:
                # print("Widget with focus (object name): {0}".format(new_widget.objectName()))
                self.print_hierarchy(new_widget)

    def closeEvent(self, event):
        self.timer.stop()


if __name__ == "__main__":

    try:
        example_dialog.close() # pylint: disable=E0601
        example_dialog.deleteLater()
    except:
        pass

    example_dialog = NativeMayaWidgetsExample()
    example_dialog.show()
