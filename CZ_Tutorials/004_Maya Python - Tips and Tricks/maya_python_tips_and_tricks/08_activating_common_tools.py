import maya.cmds as cmds
import maya.mel as mel


def get_global_variable(var_name):
    """Return the value contained in a MEL global variable"""
    return mel.eval("$tempVar = {0}".format(var_name))
    
def set_tool_to(name):
    
    context_lookup = {"select":"$gSelect",
                      "move":"$gMove",
                      "rotate":"$gRotate",
                      "scale":"$gScale"
                      }
    
    tool_context = get_global_variable(context_lookup[name])
    cmds.setToolTo(tool_context)
    

if __name__ == "__main__":
    
    set_tool_to("move")
