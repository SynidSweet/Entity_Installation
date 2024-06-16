import json
import matplotlib.pyplot as plt

# Load emotions from JSON file
with open('plutchik_emotions.json', 'r') as f:
    data = json.load(f)

emotions = data['emotions']

# Extract emotions and coordinates
labels = list(emotions.keys())
coordinates = list(emotions.values())

# Separate x and y coordinates
x_coords = [coord[0] for coord in coordinates]
y_coords = [coord[1] for coord in coordinates]

# Create plot
plt.figure(figsize=(8, 8))
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plot each emotion
for label, x, y in zip(labels, x_coords, y_coords):
    plt.scatter(x, y, label=label)
    plt.text(x, y, label, fontsize=12, ha='right')

# Set plot limits and labels
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel('Valence')
plt.ylabel('Arousal')
plt.title('Plutchik\'s Emotions on Circumplex Model')
plt.legend()
plt.show()
