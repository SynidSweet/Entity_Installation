import json
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os

# settings
text_offset = 0.06
dot_size = 9
text_size = 7
figure_size = 9

script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'updated_emotions.json'
file_path = os.path.join(script_dir, file_name)

# Load the JSON data
def load_json(file_name):
    file_path = os.path.join(script_dir, file_name)
    with open(file_path) as f:
        return json.load(f)

# Save functions
def save_json(data, file_name):
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

data = load_json(file_name)

# Function to convert valence and arousal to y, x coordinates
def to_coordinates(valence, arousal):
    y = valence  # Valence now maps to y
    x = arousal  # Arousal now maps to x
    return x, y

# Draggable points class
class DraggablePoint:
    dragging_point = None  # Class variable to track the currently dragged point

    def __init__(self, point, annotation, emotion, attributes, ax):
        self.point = point
        self.annotation = annotation
        self.press = None
        self.emotion = emotion
        self.attributes = attributes
        self.ax = ax
        self.background = None

    def connect(self):
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        if DraggablePoint.dragging_point is not None:
            return
        if event.inaxes != self.point.axes: return
        contains, _ = self.point.contains(event)
        if not contains: return
        self.press = self.point.get_data(), event.xdata, event.ydata
        self.background = self.point.figure.canvas.copy_from_bbox(self.ax.bbox)
        DraggablePoint.dragging_point = self

    def on_motion(self, event):
        if DraggablePoint.dragging_point is not self: return
        if self.press is None: return
        if event.inaxes != self.point.axes: return
        data, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        new_x = data[0][0] + dx
        new_y = data[1][0] + dy

        # Clear the background
        self.point.figure.canvas.restore_region(self.background)

        # Update data and redraw
        self.point.set_data([new_x], [new_y])
        self.annotation.set_position((new_x, new_y - text_offset))
        self.attributes['Arousal'] = new_x
        self.attributes['Valence'] = new_y

        # Draw the updated point and annotation
        self.ax.draw_artist(self.point)
        self.ax.draw_artist(self.annotation)
        self.point.figure.canvas.blit(self.ax.bbox)

    def on_release(self, event):
        if DraggablePoint.dragging_point is not self: return
        self.press = None
        self.background = None
        DraggablePoint.dragging_point = None
        self.point.figure.canvas.draw()

    def disconnect(self):
        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)

# Save functions
def save(event):
    save_json(data, file_name)

def save_as(event):
    filename = input("Enter the filename to save as (with .json extension): ")
    save_json(data, filename)

# Plotting
fig, ax = plt.subplots(figsize=(figure_size, figure_size))
ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Name the axes
ax.set_xlabel('Arousal')
ax.set_ylabel('Valence')

draggable_points = []

# Plot each emotion
for emotion_data in data:
    emotion = emotion_data["Emotion"]
    valence = emotion_data["Valence"]
    arousal = emotion_data["Arousal"]
    x, y = to_coordinates(valence, arousal)
    point, = ax.plot(x, y, 'o', markersize=dot_size)  # Note the comma to unpack the tuple
    annotation = ax.text(x, y-text_offset, emotion, fontsize=text_size, ha='center', va='center')
    draggable_point = DraggablePoint(point, annotation, emotion, emotion_data, ax)
    draggable_point.connect()
    draggable_points.append(draggable_point)

plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.title('Emotion Diagram')

# Adding save buttons
ax_save = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_save_as = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_save = Button(ax_save, 'Save')
btn_save_as = Button(ax_save_as, 'Save As')
btn_save.on_clicked(save)
btn_save_as.on_clicked(save_as)

plt.show()
