#!/usr/bin/env python3
"""Validate SVG syntax and check for common SMIL animation issues."""

import sys
import re
from pathlib import Path


def validate_svg(svg_content: str) -> list[str]:
    """Validate SVG and return list of issues."""
    issues = []

    # Check for required elements
    if "<svg" not in svg_content:
        issues.append("Missing <svg> root element")
        return issues  # Can't continue without root

    # Check for valid XML structure
    if svg_content.count("<svg") != svg_content.count("</svg>"):
        issues.append("Unbalanced <svg> tags")

    # Check animation elements
    anim_elements = ["animate", "animateTransform", "animateMotion", "set"]
    for elem in anim_elements:
        if f"<{elem}" in svg_content:
            # Check for required attributes
            if elem != "set":
                if "attributeName" not in svg_content:
                    issues.append(f"<{elem}> missing attributeName")
                if "dur" not in svg_content:
                    issues.append(f"<{elem}> missing dur")

    # Check for common issues
    if "repeatCount" in svg_content and "indefinite" not in svg_content:
        # Good - has specific repeat count
        pass

    # Check animateTransform has type
    if "<animateTransform" in svg_content and "type=" not in svg_content:
        issues.append("<animateTransform> missing type attribute (rotate, scale, translate, skewX, skewY)")

    # Check animateMotion has path
    if "<animateMotion" in svg_content and "path=" not in svg_content:
        issues.append("<animateMotion> missing path attribute")

    # Check for deprecated/removed calcMode (warning only)
    if "calcMode=" in svg_content:
        issues.append("WARNING: calcMode is deprecated in some browsers")

    # Validate transform values have center for rotate
    if "type=\"rotate\"" in svg_content:
        if not re.search(r'to="\d+\s+\d+\s+\d+"', svg_content):
            issues.append("Rotate transform should include center point (e.g., '360 60 60')")

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_svg.py <file.svg>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    svg_content = path.read_text()
    issues = validate_svg(svg_content)

    if issues:
        print(f"Issues found in {path}:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print(f"✓ {path} is valid")


if __name__ == "__main__":
    main()