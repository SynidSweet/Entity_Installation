import random

def onDone(timerOp):
    # Select a random emotion
    selected_emotion = select_random_emotion()
    # Update the Text DAT
    op('selected_emotion_text').text = selected_emotion
    # Set a new random interval
    new_interval = set_random_interval()
    # Restart the timer with the new interval
    timerOp.par.length = new_interval
    timerOp.par.start.pulse()

def select_random_emotion():
    # Get the emotion table
    emotion_table = op('emotion_table')
    # Get a random row index
    random_index = random.randint(1, emotion_table.numRows - 1)  # Skip header row
    # Get the emotion from the selected row
    selected_emotion = emotion_table[random_index, 0].val
    return selected_emotion

def set_random_interval():
    return random.uniform(30, 180)

# Set initial timer interval and start it
initial_interval = set_random_interval()
op('random_interval_timer').par.length = initial_interval
op('random_interval_timer').par.start.pulse()
