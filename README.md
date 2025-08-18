# x265 x265-3.5 (Major v3)

VFX Platform 2025 compatible build package for x265.

## Package Information

- **Package Name**: x265
- **Version**: x265-3.5
- **Major Version**: 3
- **Repository**: vfxplatform-2025/x265-3
- **Description**: VFX Platform 2025 build package

## Build Instructions

```bash
rez-build -i
```

## Package Structure

```
x265/
├── x265-3.5/
│   ├── package.py      # Rez package configuration
│   ├── rezbuild.py     # Build script
│   ├── get_source.sh   # Source download script (if applicable)
│   └── README.md       # This file
```

## Installation

When built with `install` target, installs to: `/core/Linux/APPZ/packages/x265/x265-3.5`

## Version Strategy

This repository contains **Major Version 3** of x265. Different major versions are maintained in separate repositories:

- Major v3: `vfxplatform-2025/x265-3`

## VFX Platform 2025

This package is part of the VFX Platform 2025 initiative, ensuring compatibility across the VFX industry standard software stack.
