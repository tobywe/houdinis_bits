
import hou

def set_preset(node_path, preset_name):
    cmd = 'oppresetload %s "%s"' % (node_path, preset_name)
    hou.hscript(cmd)
    
    return None