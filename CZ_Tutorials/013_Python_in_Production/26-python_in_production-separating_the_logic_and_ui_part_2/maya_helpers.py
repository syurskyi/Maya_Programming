import maya.cmds as cmds

class MayaHelpers(object):

    @classmethod
    def get_light_nodes(cls, light_filter, transform=True):
        nodes = []

        lights = cmds.ls(lights=True)
        for light in lights:
            if not light_filter or light_filter == cmds.nodeType(light):

                if transform:
                    nodes.append(cmds.listRelatives(light, parent=True)[0])
                else:
                    nodes.append(light)

        return nodes

    @classmethod
    def select_node(cls, node):
        if node:
            cmds.select(node, replace=True)
        else:
            cmds.select(clear=True)
