# manim-dump

A hands-on learning repository for [Manim](https://www.manim.community/) — the
animation engine behind 3Blue1Brown's videos — with a focus on **embedded
systems visualization**.

The goal: go from zero to producing professional explainer videos about
registers, memory maps, communication protocols, and microcontroller internals.

Each folder has its own README explaining what you'll learn and how to run it.

## Quick start

```bash
# System deps (Ubuntu/Debian)
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg texlive-latex-base dvisvgm

# Install manim
pip install manim

# Render any scene
cd manim-dump
manim -pql 01-hello-manim/scene_hello.py HelloWorld
```

## Render quality flags

| Flag | Resolution | Use case |
|------|-----------|----------|
| `-ql` | 480p 15fps | Development / fast iteration |
| `-qm` | 720p 30fps | Preview |
| `-qh` | 1080p 60fps | Final output |
| `-qk` | 4K 60fps | YouTube upload |

Add `-p` to auto-preview after render. Add `-a` to render all scenes in a file.