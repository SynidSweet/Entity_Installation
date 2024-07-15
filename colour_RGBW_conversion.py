import numpy as np

def convert_rgba_to_rgbw(ri, gi, bi, ai):
    M = max(ri, gi, bi)  # The maximum value between R, G, and B.
    wo = 0  # White output
    ro = 0  # Red output
    go = 0  # Green output
    bo = 0  # Blue output

    av = 0  # Average between the two minimum values
    hr = 0  # Red with 100% hue
    hg = 0  # Green with 100% hue
    hb = 0  # Blue with 100% hue

    # These 4 lines serve to figure out what the input color is with 100% hue.
    if M != 0:
        multiplier = 255.0 / M
        hr = int(ri * multiplier)
        hg = int(gi * multiplier)
        hb = int(bi * multiplier)

    # Determine the weighted average of the two minimum color values
    if M == ri:
        if hb + hg != 0:
            av = (bi * hb + gi * hg) // (hb + hg)
        else:
            av = 0
    elif M == gi:
        if hr + hb != 0:
            av = (ri * hr + bi * hb) // (hr + hb)
        else:
            av = 0
    elif M == bi:
        if hg + hr != 0:
            av = (gi * hg + ri * hr) // (hg + hr)
        else:
            av = 0

    # Set the RGBW values
    wo = av
    bo = bi - av
    ro = ri - av
    go = gi - av

    # Ensure the RGBW values are within the valid range (0 to 255)
    wo = clamp(wo, 0, 255)
    bo = clamp(bo, 0, 255)
    ro = clamp(ro, 0, 255)
    go = clamp(go, 0, 255)

    return ro, go, bo, wo, ai

def clamp(value, min_value, max_value):
    return max(min_value, min(max_value, value))

def export_to_artnet(r, g, b, w):
    # Create an array with the 4 channels in the order R, G, B, W, A
    return [r, g, b, w]

def main():
    # Fetching the RGBA values from the 'rgb_key_to_channels' CHOP
    rgb_key_to_channels = op('rgb_key_to_channels')
    rgba_values = rgb_key_to_channels.samples(0)  # Assuming the first sample

    # Convert the values to integers
    ri, gi, bi, ai = [int(value) for value in rgba_values]

    # Call the conversion method
    output = convert_rgba_to_rgbw(ri, gi, bi, ai)

    # Print the results
    print(f'R: {output[0]}, G: {output[1]}, B: {output[2]}, W: {output[3]}, A: {output[4]}')

    # Export the output in a format that ArtNet DAT will understand
    artnet_data = export_to_artnet(output[0], output[1], output[2], output[3], output[4])

    # Print the ArtNet data array
    print('ArtNet Data:', artnet_data)

    # You can now send artnet_data to the DMX Out CHOP or further process it as needed

# Execute the main function
main()
