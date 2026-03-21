"""
01-hello-manim/scene_hello.py

Your first Manim scenes. Three of them, each a tiny step forward.

Run any of them with:
    manim -pql scene_hello.py HelloWorld
    manim -pql scene_hello.py HelloCircle
    manim -pql scene_hello.py HelloCombo
"""

from os import write
from turtle import right, title

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

class HelloCombo(Scene):
    """
    Scene 3: Multiple objects working together.

    This is closer to what a real animation looks like:
    title at the top, objects in the middle, annotations below.
    """
    def construct(self):
        # --- Title ---
        title = Text("Manim Basics", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # --- Three shapes ---
        circle = Circle(radius=0.8, color=BLUE, fill_opacity=0.4)
        square = Square(side_length=1.4, color=RED, fill_opacity=0.4)
        triangle = Triangle(color=GREEN, fill_opacity=0.4).scale(0.9)

        # VGroup = "Visual Group". It lets you treat multiple objects as one.
        shapes = VGroup(circle, square, triangle)

        # arrange() places them in a row (or column) with spacing.
        shapes.arrange(RIGHT, buff=1.2)

        # Animate all three appearing at once with a stagger effect.
        # lag_ratio controls the delay between each object starting.
        self.play(
            AnimationGroup(
                *[GrowFromCenter(s) for s in shapes],
                lag_ratio=0.3,  # each shape starts 0.3s after the previous
            )
        )
        self.wait(0.5)

        # --- Labels below each shape ---
        labels = VGroup(
            Text("Circle", font_size=24, color=BLUE),
            Text("Square", font_size=24, color=RED),
            Text("Triangle", font_size=24, color=GREEN),
        )

        for label, shape in zip(labels, shapes):
            label.next_to(shape, DOWN, buff=0.4)
        
        self.play(*[FadeIn(l, shift=UP*0.3) for l in labels])
        self.wait(1)

        # --- Transform all shapes into circles ---
        # ReplacementTransform removes the original and adds the target.
        # Regular Transform keeps the original (it just looks like the target).
        circles = VGroup(*[
            Circle(radius=0.6, color=YELLOW, fill_opacity=0.5)
            for _ in shapes
        ])
        for c, s in zip(circles, shapes):
            c.move_to(s)

        self.play(
            *[ReplacementTransform(s, c) for s, c in zip(shapes, circles)],
            *[FadeOut(l) for l in labels],
        )
        self.wait(0.5)

        # --- Group everything and shrink to corner ---
        # This is a common pattern: you'll often "park" objects in a
        # corner to make room for the next section of your video.
        everything = VGroup(circles, title)
        self.play(
            everything.animate.scale(0.3).to_corner(UL),
            run_time=1.5,
        )
        self.wait(0.3)

        # --- Final message ---
        done = Text("Setup works. Let's build something real.", font_size=36)
        self.play(Write(done))
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])

        self.wait(1.5)