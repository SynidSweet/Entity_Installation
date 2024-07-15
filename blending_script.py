import numpy as np

# Define the updated emotions with their arousal and valence values
updated_emotions = {
    "Acceptance": {"arousal": 0.14, "valence": 0.6},
    "Acknowledged": {"arousal": 0.12, "valence": 0.5},
    # Add all other emotions here...
}

# Function to get plot points for a given emotion
def get_emotion_plot_points(emotion):
    if emotion in updated_emotions:
        values = updated_emotions[emotion]
        arousal = values["arousal"]
        valence = values["valence"]
        return (arousal, valence)
    else:
        return (0.5, 0.5)  # Default to a neutral point if emotion not found

# Function to calculate blending weights
def calculate_blending_weights(arousal, valence):
    # Define the positions of the extreme points
    extreme_points = {
        "scene1": (1, 0),
        "scene2": (1, 1),
        "scene3": (-1, 0),
        "scene4": (0, 1),
        "scene5": (-1, 1),
    }
    
    # Calculate distances to the extreme points
    distances = {}
    for scene, point in extreme_points.items():
        distances[scene] = np.sqrt((arousal - point[0])**2 + (valence - point[1])**2)
    
    # Calculate weights based on inverse distance
    total_distance = sum(distances.values())
    weights = {scene: (total_distance - distance) / total_distance for scene, distance in distances.items()}
    
    return weights

# Example usage
emotion = 'Acceptance'  # This would be your input emotion
arousal, valence = get_emotion_plot_points(emotion)
weights = calculate_blending_weights(arousal, valence)

# Print the weights (or use them to set values in your final light container)
print(weights)
