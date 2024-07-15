import numpy as np
from matplotlib.colors import hex2color

def interpolate_color(valence_norm, arousal):
    color_00 = np.array(hex2color("#FFFFFF"))  # White
    color_01 = np.array(hex2color("#00008B"))  # Dark Blue
    color_10 = np.array(hex2color("#8B0000"))  # Dark Red
    color_11 = np.array(hex2color("#FFFF00"))  # Yellow

    color_0 = (1 - valence_norm) * color_01 + valence_norm * color_00
    color_1 = (1 - valence_norm) * color_10 + valence_norm * color_11
    color = (1 - arousal) * color_0 + arousal * color_1

    return color

def cook(scriptOp):
    valence = op('math1')[0]
    arousal = op('constant_arousal')[0]

    valence_norm = (valence + 1) / 2
    color = interpolate_color(valence_norm, arousal)

    scriptOp.clear()
    scriptOp.appendChan('R')
    scriptOp.appendChan('G')
    scriptOp.appendChan('B')
    scriptOp[0] = color[0]
    scriptOp[1] = color[1]
    scriptOp[2] = color[2]

    return

