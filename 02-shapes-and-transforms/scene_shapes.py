"""
02-shapes-and-transforms/scene_shapes.py

The building blocks of every animation. Master these and you can
draw anything — from simple diagrams to full MCU block diagrams.

Run:
    manim -pql scene_shapes.py ShapeGallery
    manim -pql scene_shapes.py PositioningGuide
    manim -pql scene_shapes.py TransformShowcase
    manim -pql scene_shapes.py ChipPinout
"""

from manim import *

class ShapeGallery(Scene):
    """
    A visual catalog of every shape you'll actually use.

    This is your reference — come back to it whenever you forget
    what constructor args a shape takes.
    """

    def construct(self):
        Text.set_default(font="Lato")
        #Text.set_default(font="CMU Serif")
        Text.set_default(disable_ligatures=True)

        title = Text("Shape Gallery", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- Row 1: Basic shapes ---
        shapes_rowl = VGroup(
            Circle(radius=0.5, color=BLUE, fill_opacity=0.5),
            Square(side_length=1, color=RED, fill_opacity=0.5),
            Rectangle(width=1.5, height=0.8, color=GREEN, fill_opacity=0.5),
            Triangle(color=ORANGE, fill_opacity=0.5).scale(0.6),
            RoundedRectangle(corner_radius=0.2, width=1.3, height=0.8, color=PURPLE, fill_opacity=0.5)
        )

        shapes_rowl.arrange(RIGHT, buff=0.6)
        shapes_rowl.next_to(title, DOWN, buff=0.8)

        names_rowl = VGroup(
            Text("Circle", font_size=16),
            Text("Square", font_size=16),
            Text("Rectangle", font_size=16),
            Text("Triangle", font_size=16, disable_ligatures=True),
            Text("Rounded\nRect", font_size=14),
        )

        for name, shape in zip(names_rowl, shapes_rowl):
            name.next_to(shape, DOWN, buff=0.2)

        self.play(
            AnimationGroup(*[GrowFromCenter(s) for s in shapes_rowl], lag_ratio=0.25)
        )
        self.play(*[FadeIn(n) for n in names_rowl])
        self.wait(3)