import maya.cmds as cmds
import maya.OpenMaya as om

class DisplayColorOverride(object):
    '''
    Class for modifying the drawing overrides of selected objects.
    No UI code is contained in this class. 
    '''
    
    # The total number of override colors available
    MAX_OVERRIDE_COLORS = 32
    
    @classmethod
    def override_color(cls, color_index):
        '''
        Enables drawing overrides on the selected nodes and
        sets the override color
        '''
        if (color_index >= cls.MAX_OVERRIDE_COLORS or color_index < 0):
            om.MGlobal.displayError("Color index out-of-range (must be between 0-31)")
            return False
            
        shapes = cls.shape_nodes()
        if not shapes:
            om.MGlobal.displayError("No shape nodes selected")
            return False
            
        for shape in shapes:
            try:
                cmds.setAttr("{0}.overrideEnabled".format(shape), True)
                cmds.setAttr("{0}.overrideColor".format(shape), color_index)
            except:
                om.MGlobal.displayWarning("Failed to override color: {0}".format(shape))
            
        return True
        
    @classmethod
    def use_defaults(cls):
        '''
        Disables drawing overrides on the selected nodes
        '''
        shapes = cls.shape_nodes()
        if not shapes:
            om.MGlobal.displayError("No shapes nodes selected")
            return False
            
        for shape in shapes:
            try:
                cmds.setAttr("{0}.overrideEnabled".format(shape), False)
            except:
                om.MGlobal.displayWarning("Failed to restore defaults: {0}".format(shape))
            
        return True
    
    @classmethod
    def shape_nodes(cls):
        '''
        Returns a list of shapes nodes for the current selection
        '''
        selection = cmds.ls(selection=True)
        if not selection:
            return None
            
        shapes = []
        for node in selection:
            shapes.extend(cmds.listRelatives(node, shapes=True))
            
        return shapes
    
    
class DisplayColorOverrideUi(object):
    
    
    # Name of the UI window
    WINDOW_NAME = "tdnDisplayColorOverride"
    
    # Width of each color palette cell
    COLOR_PALETTE_CELL_WIDTH = 17
    
    # Edge offset of the form layout
    FORM_OFFSET = 2
    
    # Palette port control name
    color_palette = None
    
    @classmethod
    def display(cls):
        '''
        Creates a GUI that can override the drawing color
        of selected objects.
        '''
        
        # Delete the UI (if it exists)
        cls.delete()
        
        # Create the window and assign a form layout
        main_window = cmds.window(cls.WINDOW_NAME, title="Display Color Override", rtf=True, sizeable=False)
        main_layout = cmds.formLayout(parent=main_window)
        
        # Create the palettePort control (2 rows, 16 columns)
        rows = 2
        columns = DisplayColorOverride.MAX_OVERRIDE_COLORS / rows
        width = columns * cls.COLOR_PALETTE_CELL_WIDTH
        height = rows * cls.COLOR_PALETTE_CELL_WIDTH
        cls.color_palette = cmds.palettePort(dimensions=(columns, rows),
                                             transparent=0,
                                             width=width,
                                             height=height,
                                             topDown=True,
                                             colorEditable=False,
                                             parent=main_layout);
        
        # Set the color for at each index of the palettePort control                                     
        for index in range(1, DisplayColorOverride.MAX_OVERRIDE_COLORS):
            color_component = cmds.colorIndex(index, q=True)
            cmds.palettePort(cls.color_palette,
                             edit=True,
                             rgbValue=(index, color_component[0], color_component[1], color_component[2]))
            
        cmds.palettePort(cls.color_palette,
                         edit=True,
                         rgbValue=(0, 0.6, 0.6, 0.6))
        
        # Create the override and default buttons
        override_button = cmds.button(label="Override",
                                      command="DisplayColorOverrideUi.override()",
                                      parent=main_layout)
        
        default_button = cmds.button(label="Default",
                                      command="DisplayColorOverrideUi.default()",
                                      parent=main_layout)
        
        # Layout the Color Palette
        cmds.formLayout(main_layout, edit=True,
                        attachForm=(cls.color_palette, "top", cls.FORM_OFFSET))
        cmds.formLayout(main_layout, edit=True,
                        attachForm=(cls.color_palette, "right", cls.FORM_OFFSET))
        cmds.formLayout(main_layout, edit=True,
                        attachForm=(cls.color_palette, "left", cls.FORM_OFFSET))   
             
        # Layout the override and default buttons
        cmds.formLayout(main_layout, edit=True,
                        attachControl=(override_button, "top", cls.FORM_OFFSET, cls.color_palette))
        cmds.formLayout(main_layout, edit=True,
                        attachForm=(override_button, "left", cls.FORM_OFFSET))
        cmds.formLayout(main_layout, edit=True,
                        attachPosition=(override_button, "right", 0, 50))
        
        cmds.formLayout(main_layout, edit=True,
                        attachOppositeControl=(default_button, "top", 0, override_button))
        cmds.formLayout(main_layout, edit=True,
                        attachControl=(default_button, "left", 0, override_button))
        cmds.formLayout(main_layout, edit=True,
                        attachForm=(default_button, "right", cls.FORM_OFFSET))
        
        # Display the UI
        cmds.showWindow(main_window)
        
    @classmethod
    def delete(cls):
        '''
        Deletes the UI window (if it exists)
        '''
        if cmds.window(cls.WINDOW_NAME, exists=True):
            cmds.deleteUI(cls.WINDOW_NAME, window=True)
        
    @classmethod
    def override(cls):
        '''
        Overrides the display color using the current palettePort color
        '''
        color_index = cmds.palettePort(cls.color_palette, query=True, setCurCell=True)
        DisplayColorOverride.override_color(color_index)
        
    @classmethod
    def default(cls):
        '''
        Disables drawing overrides
        '''
        DisplayColorOverride.use_defaults()
    
    
if __name__ == "__main__":
    DisplayColorOverrideUi.display()

    
    
    
