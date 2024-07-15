# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
    # Normalize the coordinates
    x = op('coordinates')['arousal']
    y = op('coordinates')['valence']
    
    u = (x + 1) / 2
    v = y
    
    # Calculate the weights for each corner
    weight_bl = (1 - u) * (1 - v)
    weight_br = u * (1 - v)
    weight_tl = (1 - u) * v
    weight_tr = u * v

    op('multiplier_serenity').par.const0value.val = weight_tl 
    op('multiplier_ecstasy').par.const0value.val = weight_tr 
    op('multiplier_grief').par.const0value.val = weight_bl
    op('multiplier_terror').par.const0value.val = weight_br  
    
    return 


    