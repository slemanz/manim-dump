"""
01-hello-manim/scene_hello.py

Your first Manim scenes. Three of them, each a tiny step forward.

Run any of them with:
    manim -pql scene_hello.py HelloWorld
    manim -pql scene_hello.py HelloCircle
    manim -pql scene_hello.py HelloCombo
"""

from turtle import right

from manim import *

class HelloWorld(Scene):
    """
    Scene 1: Text on screen.

    This is the absolute minimum. You create a Text object,
    animate it appearing with Write(), wait a bit, then fade it out.
    """
    def construct(self):
        # Create a text object. It doesn't appear yet — it just exists in memory.
        greeting = Text("Hello, Manim!", font_size=64)

        # Write() draws the text stroke-by-stroke, like handwriting.
        self.play(Write(greeting))

        # Pause for 1 second so the viewer can read it.
        self.wait(1)

        # Now swap it for something else using Transform.
        # Transform morphs one object into another smoothly.
        new_text = Text("Let's animate some embedded stuff.", font_size=36)
        self.play(Transform(greeting, new_text))
        self.wait(2)

        # Clean exit: fade everything out.
        self.play(FadeOut(greeting))
        self.wait(2)

class HelloCircle(Scene):
    """
    Scene 2: A shape with property changes.

    Here you learn that Manim objects have properties (color, size, position)
    and you can animate changes to any of them using .animate
    """
    def construct(self):
        # Create a circle. fill_opacity=0 means just the outline.
        circle = Circle(radius=1.5, color=BLUE, stroke_width=4)

        # Create() draws the shape by tracing its border.
        self.play(Create(circle))
        self.wait(1)

        # .animate is the magic word. It turns any property change
        # into a smooth animation.
        #
        # Without .animate:  circle.set_fill(BLUE, opacity=0.5)  → instant, no animation
        # With .animate:     circle.animate.set_fill(...)         → smooth transition

        self.play(circle.animate.set_fill(BLUE, opacity=0.5))
        self.wait(1)

        # Chain multiple changes in one .animate call:
        self.play(
            circle.animate
            .set_color(GREEN)
            .set_fill(GREEN, opacity=0.5)
            .scale(0.6),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Move it around. shift() moves relative to current position.
        self.play(circle.animate.shift(RIGHT*3))
        self.play(circle.animate.shift(LEFT*6))
        self.play(circle.animate.move_to(ORIGIN))

        self.wait(2.5)
        self.play(ShrinkToCenter(circle))

