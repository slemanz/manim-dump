# 01 — Hello Manim

Your very first animation. The goal here is simple: 
**make sure everything works**.

## What you'll learn

- How to write a Manim `Scene`
- The `construct()` method — where all animation code lives
- `self.play()` — runs an animation
- `self.wait()` — pauses the scene
- Render quality flags (`-ql`, `-qm`, `-qh`, `-qk`)
- Where output files end up

## Scenes in this folder

| File | Scene | What it does |
|------|-------|-------------|
| `scene_hello.py` | `HelloWorld` | Text appears, transforms, fades out |
| `scene_hello.py` | `HelloCircle` | A circle draws itself, changes color, shrinks |
| `scene_hello.py` | `HelloCombo` | Combines text + shapes + basic animation flow |

## How to render

```bash
# Fast preview (480p) — use this while developing
manim -pql scene_hello.py HelloWorld

# High quality (1080p) — use for final output
manim -pqh scene_hello.py HelloWorld

# Render all scenes in the file
manim -pql -a scene_hello.py
```

## Key takeaways

Every Manim script follows the same pattern:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # 1. Create objects
        # 2. Animate them with self.play(...)
        # 3. Pause with self.wait(...)
        pass
```

That's it. Everything else builds on top of this.

## Output

Rendered files go to `media/videos/<filename>/<quality>/`. Manim tells you the
exact path after each render.
