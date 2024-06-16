import json
import matplotlib.pyplot as plt
import numpy as np

# settings
text_offset = 0.06
dot_size = 9
text_size = 7
figure_size = 9

# Load the JSON data
with open('E:\Projects\Glade\Entity\emotions_coordinates2.json') as f:
    data = json.load(f)

# Function to convert valence and arousal to y, x coordinates
def to_coordinates(valence, arousal):
    y = valence  # Valence now maps to y
    x = arousal  # Arousal now maps to x
    return x, y

# Plotting
fig, ax = plt.subplots(figsize=(figure_size, figure_size))
ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Name the axes
ax.set_xlabel('Arousal')
ax.set_ylabel('Valence')

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
plt.title('Emotion Diagram')
plt.show()
