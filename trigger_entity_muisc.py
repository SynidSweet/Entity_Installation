# Import necessary modules
import time

# Initialize variables
if 'last_played_happy' not in me.fetchDict:
    me.store('last_played_happy', 'entity_happy3')

if 'last_played_sad' not in me.fetchDict:
    me.store('last_played_sad', 'entity_sad3')

if 'last_trigger_time' not in me.fetchDict:
    me.store('last_trigger_time', 0)

# Define the onValueChange function
def onValueChange(channel, sampleIndex, val, prev):
    if val == 1:
        current_time = time.time()
        last_trigger_time = me.fetch('last_trigger_time')
        time_diff = current_time - last_trigger_time

        select_valence = op('select_valence')[0, 0]

        if time_diff > 600:  # Greater than 10 minutes (600 seconds)
            op('entity_intro').par.Trigger.pulse()
            me.store('last_trigger_time', current_time)
            return

        if 0.5 <= select_valence <= 1.0:
            last_played_happy = me.fetch('last_played_happy')
            if last_played_happy == 'entity_happy1':
                op('entity_happy2').par.Trigger.pulse()
                me.store('last_played_happy', 'entity_happy2')
            elif last_played_happy == 'entity_happy2':
                op('entity_happy3').par.Trigger.pulse()
                me.store('last_played_happy', 'entity_happy3')
            elif last_played_happy == 'entity_happy3':
                op('entity_happy1').par.Trigger.pulse()
                me.store('last_played_happy', 'entity_happy1')
            else:
                op('entity_happy1').par.Trigger.pulse()
                me.store('last_played_happy', 'entity_happy1')
        
        elif 0 <= select_valence < 0.5:
            last_played_sad = me.fetch('last_played_sad')
            if last_played_sad == 'entity_sad1':
                op('entity_sad2').par.Trigger.pulse()
                me.store('last_played_sad', 'entity_sad2')
            elif last_played_sad == 'entity_sad2':
                op('entity_sad3').par.Trigger.pulse()
                me.store('last_played_sad', 'entity_sad3')
            elif last_played_sad == 'entity_sad3':
                op('entity_sad1').par.Trigger.pulse()
                me.store('last_played_sad', 'entity_sad1')
            else:
                op('entity_sad1').par.Trigger.pulse()
                me.store('last_played_sad', 'entity_sad1')
        
        me.store('last_trigger_time', current_time)
        
    return

