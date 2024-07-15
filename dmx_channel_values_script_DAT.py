def onCook(scriptOp):
    return

def onOffToOn(channel, sampleIndex, val, prev):
    return

def onOnToOff(channel, sampleIndex, val, prev):
    return

def onValueChange(channel, sampleIndex, val, prev):
    # Access the Constant CHOP named 'RGBW_255'
    constant_chop = op('RGBW_255')

    # Access the Table DAT named 'all_DMX_channels'
    table_dat = op('all_DMX_channels')

    # Define the specific rows where you want the values to be written
    row_indices = [1, 2, 3, 4]

    # Ensure the table has enough rows and columns
    required_rows = max(row_indices) + 1  # Because row_indices are 0-based
    required_cols = 2  # Assuming we are writing values in the second column

    if table_dat.numRows < required_rows:
        table_dat.appendRows([[''] * table_dat.numCols for _ in range(required_rows - table_dat.numRows)])
    if table_dat.numCols < required_cols:
        table_dat.appendCols([[''] * (required_cols - table_dat.numCols) for _ in range(table_dat.numRows)])

    # Write the CHOP values to the specified rows in the Table DAT
    for i, row in enumerate(row_indices):
        table_dat[row, 1] = constant_chop[i].eval()

    # Print to the console for debugging purposes
    print("Values written to table:", [constant_chop[i].eval() for i in range(len(row_indices))])

    return

def onPulse(channel, sampleIndex, val, prev):
    return

def onThreshold(channel, sampleIndex, val, prev):
    return
