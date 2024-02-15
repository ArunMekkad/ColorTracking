import cv2
import numpy as np
import tkinter as tk

# HSV COLOR DEFINITION
color_ranges = {
    'red': [([0, 120, 70], [10, 255, 255]), ([160, 120, 70], [180, 255, 255])],
    'green': [([36, 25, 25], [86, 255,255])],
    'blue': [([94, 80, 2], [126, 255, 255])]
}

# RED IS TRACKED FIRST
color = 'red'

def select_color(new_color):
    global color
    color = new_color

# CREATION OF BUTTONS
window = tk.Tk()
window.title("Color Selection")
tk.Button(window, text="Red", command=lambda: select_color('red')).pack(side=tk.LEFT)
tk.Button(window, text="Green", command=lambda: select_color('green')).pack(side=tk.LEFT)
tk.Button(window, text="Blue", command=lambda: select_color('blue')).pack(side=tk.LEFT)

# ACCESSING THE VIDEO FILE
cap = cv2.VideoCapture('video.mp4')

def on_close():
    cap.release()
    cv2.destroyAllWindows()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)

while True:
    # FRAME-BY-FRAME VIDEO ANALYSIS
    ret, frame = cap.read()

    # VIDEO PLAYING IN A LOOP
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # HSV CONVERSION
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # THRESHOLD DEFINITION FOR DETECTION
    mask = None
    for (lower, upper) in color_ranges[color]:
        lower = np.array(lower)
        upper = np.array(upper)
        mask_i = cv2.inRange(hsv, lower, upper)
        if mask is None:
            mask = mask_i
        else:
            mask = cv2.bitwise_or(mask, mask_i)

    # FINDING CONTOURS
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # DRAWING BOUNDING BOXES
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # SHOWING THE FRAME
    cv2.imshow('Frame', frame)

    # GUI WINDOW UPDATE
    window.update_idletasks()
    window.update()