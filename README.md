**Playing Contra was always fun as a kid. But, it just got more interesting!!!<br>
In this project Computer Vision enables us to play the game using real-life actions like jumping, crouching, etc.**<br>

<h2>Controls to play -</h2>

<h5>Movement :</h5>
Move forward - Stretch your right hand horizontally to go forward.<br>
Move backward - Stretch your left hand horizontally to go backward.<br>
<h5>Jumping :</h5>
Jump in real life to make the character jump in game.<br>
<h5>Crouching :</h5>
Crouch in real life to make the character jump in game.<br>
<h5>Shooting :</h5>
Make gun sign with your hand to start shooting.<br>
Point in the direction you want to shoot, to make the player shoot in that direction.<br>
<br>
This project explores the use of computer vision to control a video game, specifically the classic run-and-gun game Contra.<br>
The program utilizes a camera to capture the player's movements and translates them into real-time controls for the game character.<br>
The goal is to achieve a level of interaction where the player's physical actions become the controller for the in-game character.<br>
<br>
The project leverages the capabilities of Python and OpenCV (Open Source Computer Vision Library) to achieve the following:<br>
<br>
Video Capture: The program utilizes the webcam to capture live video frames of the player.<br>
Movement Detection: OpenCV's image processing techniques are employed to identify the player's pose and actions within the video frame. <br>
Techniques like pose estimation libraries have be explored for this purpose.<br>
MediaPipe has been used for pose detection.<br>
Control Mapping: Based on the identified actions (jumping, running, etc.), the program translates them into corresponding keyboard presses or joystick movements to control the Contra character. <br>
PyAutoGUI has be used to send these inputs to the game.<br>
<br>
Background: A static background is ideal for background subtraction. A busy background can introduce false positives (changes that aren't the player). <br>
If a static background isn't feasible, explore background subtraction techniques that can adapt to some degree of background changes<br>
Lighting: Variations in lighting can affect both background subtraction and pose estimation. Bright or uneven lighting might create noise, leading to misinterpretations of movement. <br>
Consider using consistent lighting or explore techniques to normalize lighting conditions in your video processing.<br>
<br>
Explore more sophisticated pose estimation techniques for recognizing complex in-game actions.<br>
Enhance Processing Power:<br>
Hardware Upgrade: Consider upgrading your computer's CPU (Central Processing Unit) or GPU (Graphics Processing Unit) to handle the demands of real-time computer vision processing more effectively.<br>
Modern CPUs and GPUs offer significant performance improvements compared to older models.<br>
Optimize Code for Efficiency:<br>
Review and Refine: Conduct a code review to identify potential bottlenecks or inefficiencies. Look for areas where simpler algorithms or libraries could be used for specific tasks.
