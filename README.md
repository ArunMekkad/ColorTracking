# Color Tracking Program

This Python program is designed to track specific colors in a video stream. It uses OpenCV for video processing and Tkinter for the graphical user interface.

## How it Works

The program defines color ranges for red, green, and blue in the HSV color space. It then opens a video file and processes each frame to detect the presence of the selected color.

The color selection is done through a simple Tkinter GUI, where the user can choose between red, green, and blue. The selected color is then used for tracking in the video stream.

When a color is detected in a frame, the program draws a bounding box around the detected area. The video stream is displayed in a window, with the bounding boxes overlaid on the video.

## Code Structure

The code is divided into several sections:

1. **Color Definition**: This section defines the color ranges for red, green, and blue in the HSV color space.

2. **Color Selection**: This section creates a Tkinter GUI with buttons for each color. When a button is clicked, the corresponding color is selected for tracking.

3. **Video Processing**: This section opens the video file and processes each frame. It converts the frame to the HSV color space, applies a mask based on the selected color, and finds contours in the masked image. It then draws bounding boxes around the detected areas.

4. **GUI Update**: This section updates the Tkinter GUI and the video display window.

# Results

After running this program, you will see a video stream with the selected color being tracked in real-time. The tracked objects will be highlighted with bounding boxes. This allows you to visually confirm the effectiveness of the color tracking algorithm.

![Result3](https://github.com/ArunMekkad/ColorTracking/blob/main/Result3.png)

![Result2](https://github.com/ArunMekkad/ColorTracking/blob/main/Result2.png)

Remember, the accuracy of the tracking can vary depending on the lighting conditions and the quality of the video. Therefore, it's always a good idea to test the program under different conditions to ensure robust performance. Happy tracking!

## Future Scope

This program has a wide range of potential real-time applications:

1. **Robotics**: This program can be used in robotics for object tracking and navigation. For example, a robot could be programmed to follow a red ball or avoid green obstacles.

2. **Augmented Reality**: In augmented reality applications, this program could be used to track colored markers in the real world, allowing virtual objects to be overlaid on the markers.

3. **Sports Analysis**: In sports analysis, this program could be used to track the movement of players or the ball. For example, tracking a green ball in a game of tennis.

4. **Video Editing**: In video editing, this program could be used for color-based effects, such as highlighting all the red objects in a video.

5. **Surveillance**: In surveillance applications, this program could be used to track the movement of specific colored vehicles or clothing.
