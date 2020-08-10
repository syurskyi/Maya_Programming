from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import getCppPointer

import maya.OpenMayaUI as omui
import maya.cmds as cmds


class WorkspaceControl(object):

    def __init__(self, name):
        self.name = name
        self.widget = None


if __name__ == "__main__":

    workspace_control_name = "MyWorkspaceControl"
    if cmds.window(workspace_control_name, exists=True):
        cmds.deleteUI(workspace_control_name)
