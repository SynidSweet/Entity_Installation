def onCook(scriptOp):
    # Get the timer count
    timer_count = op('timer_count')
    
    # If the timer count reaches the limit, reset the count and select a new interval and emotion
    if timer_count[0] >= timer_count.par.limitmax.val:
        # Select a random emotion
        emotion_table = op('emotion_table')
        random_index = random.randint(1, emotion_table.numRows - 1)  # Skip header row
        selected_emotion = emotion_table[random_index, 0].val
        op('selected_emotion_text').text = selected_emotion
        
        # Set a new random interval
        new_interval = random.uniform(30, 180)
        timer_count.par.limitmax.val = new_interval
        
        # Reset the timer count
        timer_count.par.reset.pulse()
    
    return
