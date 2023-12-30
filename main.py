# Using Tkinter as a way to count the interior lattice points of a circle of any radius and position
# This program is very minimalistic and also the function may seem oddly specific as it was just created to get a better catch on a math problem (PROMYS 2024 application set P3)

import tkinter as tk
from tkinter import ttk
import math

class CartesianGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lattice Point Counter")

        self.canvas = tk.Canvas(root, bg="black", width=600, height=400)
        self.canvas.pack(pady=10)

        self.radius_label = tk.Label(root, text="Radius:")
        self.radius_label.pack()

        self.radius_slider = ttk.Scale(root, from_=1, to=100, orient="horizontal", length=200, command=self.update_circle)
        self.radius_slider.set(1)  # Set initial radius to 1
        self.radius_slider.pack()

        self.circle = None
        self.lattice_points = set()

        # Additional label to display the radius
        self.radius_display_label = tk.Label(root, text="")
        self.radius_display_label.pack()

        self.radius_slider.bind("<B1-Motion>", self.update_circle)

        self.move_increment = 2  # Number of pixels to move the circle on each arrow key press
        self.circle_center = [300, 200]  # Initial center of the circle

        # Bind arrow keys to move_circle function
        self.root.bind("<Left>", lambda event: self.move_circle(-self.move_increment, 0))
        self.root.bind("<Right>", lambda event: self.move_circle(self.move_increment, 0))
        self.root.bind("<Up>", lambda event: self.move_circle(0, -self.move_increment))
        self.root.bind("<Down>", lambda event: self.move_circle(0, self.move_increment))

        # Move this line to the end of the __init__ method
        self.update_circle()

    def draw_circle(self, x, y, radius):
        return self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="red")

    def draw_lattice_point(self, x, y):
        return self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white")

    def update_circle(self, event=None):
        if self.circle:
            self.canvas.delete(self.circle)
            for lattice_point in self.lattice_points:
                self.canvas.delete(lattice_point)

        radius = self.radius_slider.get()
        x, y = self.circle_center  # Center of the circle

        self.circle = self.draw_circle(x, y, radius)

        # Calculate lattice points within the circle
        num_points = 0
        for i in range(-100, 700, 20):
            for j in range(-100, 500, 20):
                lattice_point = self.draw_lattice_point(i, j)
                self.lattice_points.add(lattice_point)
                if math.sqrt((i - x) ** 2 + (j - y) ** 2) < radius:
                    num_points += 1

        self.update_label(num_points)

        # Update the radius display label
        radius_in_units = radius / 20  # Assuming 20 pixels = 1 unit
        self.radius_display_label.config(text=f"Radius: {radius_in_units} units")

    def update_label(self, num_points):
        label_text = f"Number of Interior Lattice Points: {num_points}"
        self.radius_label.config(text=label_text)

    def move_circle(self, dx, dy):
        if self.circle:
            self.circle_center[0] += dx
            self.circle_center[1] += dy

            self.canvas.move(self.circle, dx, dy)

            self.update_circle()

if __name__ == "__main__":
    root = tk.Tk()
    app = CartesianGraphApp(root)
    root.mainloop()
