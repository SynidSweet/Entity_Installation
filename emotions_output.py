import matplotlib.pyplot as plt
import numpy as np

# Define the updated emotions with their arousal and valence values
updated_emotions = {
    "Acceptance": {"arousal": 0.14, "valence": 0.6},
    "Acknowledged": {"arousal": 0.12, "valence": 0.5},
    "Admiration": {"arousal": 0.4, "valence": 0.75},
    "Aggression": {"arousal": 0.8, "valence": -0.7},
    "Amazement": {"arousal": 0.8, "valence": 0.72},
    "Anger": {"arousal": 0.9, "valence": -0.8},
    "Annoyance": {"arousal": 0.47, "valence": -0.18},
    "Anxiety": {"arousal": 0.76, "valence": -0.25},
    "Apprehension": {"arousal": 0.31, "valence": -0.1},
    "Aroused": {"arousal": 0.93, "valence": 0.5},
    "Awe": {"arousal": 0.35, "valence": 0.86},
    "Confident": {"arousal": 0.3, "valence": 0.67},
    "Contempt": {"arousal": 0.67, "valence": -0.53},
    "Content": {"arousal": 0.04, "valence": 0.75},
    "Courage": {"arousal": 0.6, "valence": 0.62},
    "Curiosity": {"arousal": 0.22, "valence": 0.27},
    "Disappointment": {"arousal": 0.17, "valence": -0.49},
    "Disapproval": {"arousal": 0.23, "valence": -0.29},
    "Disgust": {"arousal": 0.5, "valence": -0.97},
    "Desirable": {"arousal": 0.7, "valence": 0.6},
    "Ecstasy": {"arousal": 1.0, "valence": 1.0},
    "Excitement": {"arousal": 0.93, "valence": 0.43},
    "Fear": {"arousal": 0.9, "valence": -0.8},
    "Grateful": {"arousal": 0.14, "valence": 0.75},
    "Grief": {"arousal": 0.14, "valence": -1},
    "Guilt": {"arousal": 0.3, "valence": -0.9},
    "Hostility": {"arousal": 0.67, "valence": -0.8},
    "Installation Resting": {"arousal": 0.45, "valence": 1},
    "Joyful": {"arousal": 0.68, "valence": 0.69},
    "Love": {"arousal": 0.83, "valence": 0.95},
    "Motivated": {"arousal": 0.6, "valence": 0.47},
    "Optimistic": {"arousal": 0.25, "valence": 0.35},
    "Playful": {"arousal": 0.85, "valence": 0.62},
    "Proud": {"arousal": 0.2, "valence": 0.47},
    "Rage": {"arousal": .93, "valence": -0.87},
    "Revulsion": {"arousal": 0.5, "valence": -0.73},
    "Sadness": {"arousal": 0.2, "valence": -0.68},
    "Serenity": {"arousal": 0.04, "valence": 0.9},
    "Shock": {"arousal": 0.9, "valence": -0.25},
    "Surprise": {"arousal": .61, "valence": 0.0},
    "Surrender": {"arousal": 0.04, "valence": 0.17},
    "Terror": {"arousal": 1.0, "valence": -0.97},
    "Trust": {"arousal": 0.04, "valence": 0.57},
    "Vigilance": {"arousal": 0.8, "valence": 0.25},
}

# Function to plot emotions without colors
def plot_emotions_without_colors(emotions):
    plt.figure(figsize=(14, 10))
    
    for emotion, values in emotions.items():
        arousal = values["arousal"]
        valence = values["valence"]
        
        # Adding the text without color information
        plt.text(arousal, valence, emotion, fontsize=8, ha='center', va='center')
    
    # Set plot limits and labels
    plt.xlim(0, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.xlabel('Arousal (0 to 1)')
    plt.ylabel('Valence (-1 to +1)')
    plt.title('Visitor\'s Emotions')
    plt.grid(True)
    plt.show()

# Function to get plot points for a given emotion
def get_emotion_plot_points(emotion):
    if emotion in updated_emotions:
        values = updated_emotions[emotion]
        arousal = values["arousal"]
        valence = values["valence"]
        return (arousal, valence)
    else:
        return "Installation Resting"

# Plot the emotions without colors
plot_emotions_without_colors(updated_emotions)
