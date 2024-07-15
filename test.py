

# Assuming 'lamp_table' is your table DAT
lamp_table = op('lamp_table')

# Assuming 'combined_dmx' is your constant CHOP
combined_dmx = op('combined_dmx')

# Define suffixes for channel names
suffixes = [' R', ' G', ' B', ' W']

# Iterate over each row in the table
for i, row in enumerate(lamp_table.rows()):
    # Get the string value from the first column of the current row
    string_value = row[0].val
    
    # Set expressions and names for 4 channels in the constant CHOP
    for j in range(4):
        channel_index = i * 4 + j
        channel_name = f'{string_value}{suffixes[j]}'
        channel_name = channel_name.replace(" ", "_")
        
        # Construct the expression
        expression = f"op('{string_value}/out1')[{j}]"
        
        # Set the name and expression for the current channel
        combined_dmx.par['const' + str(channel_index) + 'name'].val = channel_name
        combined_dmx.par['const' + str(channel_index) + 'value'].expr = expression

print("Channel names and expressions have been set for all channels in the constant CHOP.")
