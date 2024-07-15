def onValueChange(channel, sampleIndex, val, prev):
    # Access the Constant CHOP named 'RGBW_255'
    constant_chop = op('RGBW_255')

    # Access the Table DAT named 'all_DMX_channels'
    table_dat = op('all_DMX_channels')

    # Define the specific rows where you want the values to be written
    row_indices = [0, 1, 2, 3]

    # Ensure the table has enough rows and columns
    required_rows = 1024
    required_cols = 1  # Assuming we are writing values in the second column

    if table_dat.numRows < required_rows:
        table_dat.appendRows([['0'] * table_dat.numCols for _ in range(required_rows - table_dat.numRows)])

    # Write the CHOP values to the specified rows in the Table DAT
    for i, row in enumerate(row_indices):
        table_dat[row, 0] = constant_chop[i].eval()

    # Print to the console for debugging purposes
    print("Values written to table:", [constant_chop[i].eval() for i in range(len(row_indices))])

    return
