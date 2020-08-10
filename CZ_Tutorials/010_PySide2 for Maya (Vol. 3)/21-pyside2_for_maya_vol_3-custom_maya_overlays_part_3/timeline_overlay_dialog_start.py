from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TimelineOverlay(QtWidgets.QWidget):

    KEYFRAME_COLOR = QtGui.QColor(QtCore.Qt.green)

    def __init__(self):
        self.time_control = mel.eval("$tempVar = $gPlayBackSlider")
        time_control_ptr = omui.MQtUtil.findControl(self.time_control)
        time_control_widget = wrapInstance(long(time_control_ptr), QtWidgets.QWidget)

        super(TimelineOverlay, self).__init__(time_control_widget)

        self.set_context_menu_enabled(False)

    def add_frame(self):
        print("TODO: Add Frame")

    def remove_frame(self):
        print("TODO: Remove Frame")

    def set_context_menu_enabled(self, enabled):
        self.context_menu_enabled = enabled

        if enabled:
            print("TODO: Add Context Menu")

    def paintEvent(self, paint_event):
        parent = self.parentWidget()
        if parent:
            self.setGeometry(parent.geometry())

            painter = QtGui.QPainter(self)

            fill_color = QtGui.QColor(TimelineOverlay.KEYFRAME_COLOR)
            fill_color.setAlpha(63)

            painter.fillRect(0, 0, self.width(), self.height(), fill_color)



if __name__ == "__main__":
    try:
        TimelineOverlayDialog.delete_overlays() # pylint: disable=E0601
    except:
        pass


class TimelineOverlayDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "Timeline Overlay"

    timeline_overlay = None

    @classmethod
    def delete_overlays(cls):
        if TimelineOverlayDialog.timeline_overlay:
            TimelineOverlayDialog.timeline_overlay.setParent(None)
            TimelineOverlayDialog.timeline_overlay.deleteLater()
            TimelineOverlayDialog.timeline_overlay = None

    def __init__(self, parent=maya_main_window()):
        super(TimelineOverlayDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)

        self.setMinimumSize(280, 160)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

        self.set_overlay_visible(True)

    def create_widgets(self):
        self.overlay_visible_cb = QtWidgets.QCheckBox("Show Overlay")

        self.context_menu_cb = QtWidgets.QCheckBox("Context Menu Enabled")
        self.context_menu_cb.setChecked(True)

        self.add_frame_btn = QtWidgets.QPushButton("Add Frame")
        self.remove_frame_btn = QtWidgets.QPushButton("Remove Frame")

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        frame_layout = QtWidgets.QHBoxLayout()
        frame_layout.setSpacing(4)
        frame_layout.addWidget(self.add_frame_btn)
        frame_layout.addWidget(self.remove_frame_btn)
        frame_layout.addStretch()

        overlay_layout = QtWidgets.QVBoxLayout()
        overlay_layout.addWidget(self.overlay_visible_cb)
        overlay_layout.addWidget(self.context_menu_cb)
        overlay_layout.addLayout(frame_layout)

        options_grp = QtWidgets.QGroupBox("Overlay Options")
        options_grp.setLayout(overlay_layout)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addWidget(options_grp)
        main_layout.addStretch()
        main_layout.addLayout(btn_layout)

    def create_connections(self):
        self.overlay_visible_cb.toggled.connect(self.set_overlay_visible)

        self.close_btn.clicked.connect(self.close)

    def set_overlay_visible(self, visible):
        if visible:
            if not TimelineOverlayDialog.timeline_overlay:
                TimelineOverlayDialog.timeline_overlay = TimelineOverlay()
                TimelineOverlayDialog.timeline_overlay.set_context_menu_enabled(self.context_menu_cb.isChecked())

                self.context_menu_cb.toggled.connect(TimelineOverlayDialog.timeline_overlay.set_context_menu_enabled)
                self.add_frame_btn.clicked.connect(TimelineOverlayDialog.timeline_overlay.add_frame)
                self.remove_frame_btn.clicked.connect(TimelineOverlayDialog.timeline_overlay.remove_frame)


        if TimelineOverlayDialog.timeline_overlay:
            TimelineOverlayDialog.timeline_overlay.setVisible(visible)

        self.overlay_visible_cb.setChecked(visible)



if __name__ == "__main__":

    try:
        overlay_dialog.close() # pylint: disable=E0601
        overlay_dialog.deleteLater()
    except:
        pass

    overlay_dialog = TimelineOverlayDialog()
    overlay_dialog.show()
