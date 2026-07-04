# Draw Using Mouse Movements

A simple Python application built with **Tkinter** that lets you draw freehand on a canvas using mouse movements.

## Concepts Used

- **Canvas Widget** – Tkinter's `Canvas` widget is used as the drawing surface.
- **Mouse Events** – Mouse button press and drag events are used to capture drawing actions:
  - `<Button-1>` – Detects when the left mouse button is pressed and records the starting position.
  - `<B1-Motion>` – Detects mouse movement while the left button is held down and draws lines between points.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## How to Run

1. Save the code file as `mouse_draw.py`.
2. Open a terminal in the folder containing the file.
3. Run the following command:

   ```
   python mouse_draw.py
   ```

## How to Use

1. A window will open with a white canvas and a **Clear** button.
2. Click and hold the left mouse button, then move the mouse to draw on the canvas.
3. Release the mouse button to stop drawing.
4. Click the **Clear** button to erase everything and start over.

## File Structure

```
mouse_draw.py    Main application file
README.md        Project documentation
```

## Possible Enhancements

- Add a color picker to change the drawing color.
- Add a slider to control the brush size.
- Add an "Undo" feature.
- Add a "Save as Image" option to export the drawing.

## License

Free to use and modify for learning purposes.
