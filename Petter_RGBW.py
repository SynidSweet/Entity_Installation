
r = op('light').par.fillcolorr
g = op('light').par.fillcolorg
b = op('light').par.fillcolorb



smallest = min(r, g, b)


r = r - smallest
g = g - smallest
b = b - smallest
w = smallest


op('light').par.fillcolorr - op('min_rgb').par.const0value


min(op('light').par.fillcolorr, op('light').par.fillcolorg, op('light').par.fillcolorb)

