def onTableChange(dat):
    # Reference the Trigger CHOP
    trigger_chop = op('trigger1')  # Change to the correct path of your Trigger CHOP
    
    # Get the current string from the In_DAT (assuming it's in the first cell)
    current_string = dat[0, 0].val  # Adjust if the string is in a different cell
    
    # Retrieve the previous string from storage
    previous_string = parent().fetch('previous_string', None)
    
    # Check if the string has changed
    if current_string != previous_string:
        # Pulse the Trigger CHOP
        trigger_chop.par.triggerpulse.pulse()
        
        # Store the current string as the new previous string
        parent().store('previous_string', current_string)

# Attach the callback to the In_DAT
op('in1').setChangeCallback(onTableChange)
