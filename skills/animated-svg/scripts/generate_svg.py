#!/usr/bin/env python3
"""Generate simple SVG animations from command-line config."""

import argparse
import sys
from typing import Optional


def generate_pulse(shape: str, color: str, duration: str, size: int = 100) -> str:
    """Generate a pulsing animation."""
    if shape == "circle":
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <circle cx="{size//2}" cy="{size//2}" r="{size//5}" fill="{color}">
    <animate attributeName="r" values="{size//5};{size//3};{size//5}" dur="{duration}" repeatCount="indefinite" />
  </circle>
</svg>'''
    elif shape == "square":
        s = size // 4
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <rect x="{size//2-s//2}" y="{size//2-s//2}" width="{s}" height="{s}" fill="{color}">
    <animate attributeName="width" values="{s};{s*2};{s}" dur="{duration}" repeatCount="indefinite" />
    <animate attributeName="height" values="{s};{s*2};{s}" dur="{duration}" repeatCount="indefinite" />
    <animate attributeName="x" values="{size//2-s//2};{size//2-s};{size//2-s//2}" dur="{duration}" repeatCount="indefinite" />
    <animate attributeName="y" values="{size//2-s//2};{size//2-s};{size//2-s//2}" dur="{duration}" repeatCount="indefinite" />
  </rect>
</svg>'''
    else:
        sys.exit(f"Unknown shape: {shape}")


def generate_rotate(shape: str, color: str, duration: str, size: int = 100) -> str:
    """Generate a rotating animation."""
    cx, cy = size // 2, size // 2
    if shape == "triangle":
        pts = f"{cx},{cy-size//4} {cx+size//4},{cy+size//4} {cx-size//4},{cy+size//4}"
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <polygon points="{pts}" fill="{color}">
    <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="{duration}" repeatCount="indefinite" />
  </polygon>
</svg>'''
    elif shape == "square":
        s = size // 3
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <rect x="{cx-s//2}" y="{cy-s//2}" width="{s}" height="{s}" fill="{color}">
    <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="{duration}" repeatCount="indefinite" />
  </rect>
</svg>'''
    else:
        sys.exit(f"Unknown shape: {shape}")


def generate_move(color: str, duration: str, size: int = 200) -> str:
    """Generate a moving animation."""
    return f'''<svg viewBox="0 0 {size} {size//4}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="{size//8}" width="{size//8}" height="{size//8}" fill="{color}">
    <animate attributeName="x" from="0" to="{size-size//8}" dur="{duration}" repeatCount="indefinite" />
  </rect>
</svg>'''


def generate_path_follow(color: str, duration: str, size: int = 200) -> str:
    """Generate a path-following animation."""
    return f'''<svg viewBox="0 0 {size} {size//2}" xmlns="http://www.w3.org/2000/svg">
  <path d="M0,{size//4} Q{size//2},0 {size},{size//4}" fill="none" stroke="#ccc" />
  <circle r="{size//20}" fill="{color}">
    <animateMotion path="M0,{size//4} Q{size//2},0 {size},{size//4}" dur="{duration}" repeatCount="indefinite" rotate="auto" />
  </circle>
</svg>'''


def main():
    parser = argparse.ArgumentParser(description="Generate SVG animations")
    parser.add_argument("--type", required=True, choices=["pulse", "rotate", "move", "path"],
                        help="Animation type")
    parser.add_argument("--shape", help="Shape (circle, square, triangle)")
    parser.add_argument("--color", default="royalblue", help="Fill color")
    parser.add_argument("--duration", default="2s", help="Animation duration (e.g., 2s, 500ms)")
    parser.add_argument("--size", type=int, default=100, help="Canvas size")
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    if args.type == "pulse" and not args.shape:
        parser.error("--shape required for pulse")
    if args.type == "rotate" and not args.shape:
        parser.error("--shape required for rotate")

    if args.type == "pulse":
        svg = generate_pulse(args.shape, args.color, args.duration, args.size)
    elif args.type == "rotate":
        svg = generate_rotate(args.shape, args.color, args.duration, args.size)
    elif args.type == "move":
        svg = generate_move(args.color, args.duration, args.size)
    elif args.type == "path":
        svg = generate_path_follow(args.color, args.duration, args.size)

    if args.output:
        with open(args.output, "w") as f:
            f.write(svg)
        print(f"Written to {args.output}")
    else:
        print(svg)


if __name__ == "__main__":
    main()