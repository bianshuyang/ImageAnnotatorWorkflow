# Image Rectangle Drawer - README

## Introduction

The Image Rectangle Drawer is a PyQt6-based application that allows users to load an image and draw rectangles on it using a graphical interface. It provides simple controls for zooming in and out, and it supports saving and loading rectangle data associated with each image.

## Getting Started

To run the Image Rectangle Drawer application, ensure you have Python and PyQt6 installed on your system. If you don't have PyQt6 installed, you can install it using the following command:

```bash
pip install PyQt6
```
Once you have PyQt6 installed, you can execute the provided Python script to launch the application:
```bash
python3 image_rectangle_drawer.py
```

## Features
### Loading Images
Upon launching the application, it will display a list of image files (in JPEG format) located in the same directory as the script. You can select an image from the drop-down list, and the application will load and display the chosen image in the main window.

### Drawing Rectangles
To draw a rectangle on the loaded image, click and drag the left mouse button to create the desired rectangle. The rectangle will be displayed on the image with a red outline. Additionally, green and red points will appear at the starting and ending positions of the rectangle, respectively.

### Zooming
The Image Rectangle Drawer provides zooming capabilities to allow users to view the image and rectangles more clearly. You can use the "+" and "-" buttons in the control panel to zoom in and out, respectively. The zoom level increases or decreases by 0.05 with each click.

### Saving and Loading Rectangle Data
The application allows you to save the drawn rectangles' data associated with each image. The data includes the starting and ending points of each rectangle drawn on the image. When you switch between images, the application will automatically load the saved rectangle data, if any, and display the rectangles accordingly.

### How to Use
1. Run the application using the provided Python script.

2. Choose an image file from the drop-down list to load and display the image in the main window.

3. To draw a rectangle on the image, click and drag the left mouse button to define the rectangle's size and position.

4. Use the "+" button to zoom in and the "-" button to zoom out for a better view of the image and rectangles.

5. Right-click on a drawn rectangle to open a context menu. From the menu, you can choose to remove the selected rectangle from the image.

6. The application automatically saves the rectangle data for each image in a corresponding text file with the same name as the image file but with the ".txt" extension. The data includes the coordinates of the starting and ending points of each rectangle.

## Important Notes
The Image Rectangle Drawer supports loading JPEG images (files with a ".jpg" extension) located in the same directory as the script. Make sure to place the image files in the correct location for the application to detect them.

When you switch between images, the application will automatically load the saved rectangle data for the newly selected image, if any. This allows you to resume your work from the previous session.

The application updates the rectangle data and saves it automatically whenever you draw or remove a rectangle.

You can close the application by closing the main window or using the standard window close button.

## Dependencies
The Image Rectangle Drawer application relies on the following Python libraries:

1. PyQt6: To provide the graphical user interface and interaction components.
2. os and sys: To handle file operations and system-level functionality.
Make sure you have these libraries installed to run the application successfully.

## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the project's repository.

## License
The Image Rectangle Drawer application is open-source software licensed under the MIT License. You can find the full license text in the LICENSE file provided with the source code.

