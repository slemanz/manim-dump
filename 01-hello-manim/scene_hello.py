"""
01-hello-manim/scene_hello.py

Your first Manim scenes. Three of them, each a tiny step forward.

Run any of them with:
    manim -pql scene_hello.py HelloWorld
    manim -pql scene_hello.py HelloCircle
    manim -pql scene_hello.py HelloCombo
"""

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