import json
import matplotlib.pyplot as plt
import numpy as np

# settings
text_offset = 0.06
dot_size = 10
text_size = 8
figure_size = 8

# Load the JSON data
with open('E:\Projects\Glade\Entity\emotions_coordinates.json') as f:
    data = json.load(f)

# Function to convert valence and arousal to x, y coordinates
def to_coordinates(valence, arousal):
    angle = (valence + 1) * np.pi / 2  # Map valence [-1, 1] to angle [0, pi]
    radius = arousal  # Map arousal [0, 1] to radius [0, 1]
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    return x, y

# Plotting
fig, ax = plt.subplots(figsize=(figure_size, figure_size))
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Draw circle
circle = plt.Circle((0, 0), 1, color='lightgrey', fill=False)
ax.add_artist(circle)

# Plot each emotion
for category, emotions in data.items():
    for emotion, attributes in emotions.items():
        if 'Valence' in attributes and 'Arousal' in attributes:
            valence = attributes['Valence']
            arousal = attributes['Arousal']
            x, y = to_coordinates(valence, arousal)
            ax.plot(x, y, 'o', label=emotion, markersize=dot_size)
            ax.text(x, y-text_offset, emotion, fontsize=text_size, ha='center', va='center')
        else:
            for sub_emotion, sub_attributes in attributes.items():
                valence = sub_attributes['Valence']
                arousal = sub_attributes['Arousal']
                x, y = to_coordinates(valence, arousal)
                ax.plot(x, y, 'o', label=sub_emotion, markersize=dot_size)
                ax.text(x, y-text_offset, sub_emotion, fontsize=text_size, ha='center', va='center')

plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.title('Emotion Circle Diagram')
plt.show()
