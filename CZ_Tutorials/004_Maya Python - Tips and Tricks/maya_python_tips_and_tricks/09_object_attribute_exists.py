import maya.cmds as cmds
from maya.OpenMaya import MGlobal


def obj_exists(obj_name, attribute_name=None):
    
    full_name = obj_name
    if attribute_name:
        full_name = "{0}.{1}".format(full_name, attribute_name)
        
    if cmds.objExists(full_name):
        return True
    else:
        MGlobal.displayWarning("Object does not exist: {0}".format(full_name))
        return False
        

if __name__ == "__main__":
    
    if obj_exists("pCube1", "translate"):
        print("Object/attribute exists")
