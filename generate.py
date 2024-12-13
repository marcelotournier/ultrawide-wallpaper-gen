import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import random
from typing import Tuple, List, Callable
from enum import Enum
import math
import uuid


class Shape(Enum):
    CUBE = "cube"
    PYRAMID = "pyramid"
    HEXAGON = "hexagon"
    OCTAGON = "octagon"
    CRYSTAL = "crystal"

def create_smooth_gradient(width: int, height: int) -> Image.Image:
    """Create a very smooth gradient from dark grey to dark blue."""
    img = Image.new('RGB', (width, height))
    
    # Define gradient colors
    left_color = (25, 25, 25)        # Dark grey
    mid_color = (20, 22, 35)         # Dark blue-grey
    right_color = (15, 20, 45)       # Dark blue
    
    for x in range(width):
        # Two-phase gradient for smoother transition
        if x < width / 2:
            ratio = x / (width / 2)
            r = int(left_color[0] * (1 - ratio) + mid_color[0] * ratio)
            g = int(left_color[1] * (1 - ratio) + mid_color[1] * ratio)
            b = int(left_color[2] * (1 - ratio) + mid_color[2] * ratio)
        else:
            ratio = (x - width / 2) / (width / 2)
            r = int(mid_color[0] * (1 - ratio) + right_color[0] * ratio)
            g = int(mid_color[1] * (1 - ratio) + right_color[1] * ratio)
            b = int(mid_color[2] * (1 - ratio) + right_color[2] * ratio)
        
        # Apply color with subtle noise for texture
        for y in range(height):
            noise = random.randint(-2, 2)
            pixel_color = (
                max(0, min(255, r + noise)),
                max(0, min(255, g + noise)),
                max(0, min(255, b + noise))
            )
            img.putpixel((x, y), pixel_color)
    
    return img.filter(ImageFilter.GaussianBlur(radius=3))  # Smooth out any remaining noise

def get_outline_color() -> Tuple[int, int, int]:
    """Generate a light grey-white color for outlines."""
    base = random.randint(180, 200)
    return (base, base, base + random.randint(0, 15))

def draw_cube_outline(draw: ImageDraw, x: int, y: int, size: int, color: Tuple[int, int, int]) -> None:
    """Draw an isometric cube outline."""
    points = [
        (x + size//2, y),           # top
        (x + size, y + size//3),    # right
        (x + size//2, y + size//1.5),# bottom
        (x, y + size//3)            # left
    ]
    
    # Draw all edges with thin lines
    for i in range(len(points)):
        draw.line([points[i], points[(i+1)%4]], fill=color, width=1)
    draw.line([points[0], points[2]], fill=color, width=1)
    draw.line([points[1], points[3]], fill=color, width=1)

def draw_pyramid_outline(draw: ImageDraw, x: int, y: int, size: int, color: Tuple[int, int, int]) -> None:
    """Draw a pyramid outline."""
    tip = (x + size//2, y)
    base = [
        (x, y + size),
        (x + size, y + size),
        (x + size//2, y + size//2)
    ]
    
    for point in base:
        draw.line([tip, point], fill=color, width=1)
    for i in range(len(base)):
        draw.line([base[i], base[(i+1)%3]], fill=color, width=1)

def draw_crystal_outline(draw: ImageDraw, x: int, y: int, size: int, color: Tuple[int, int, int]) -> None:
    """Draw a crystal-like shape outline."""
    points = [
        (x + size//2, y),           # top
        (x + size, y + size//3),    # right
        (x + size*3//4, y + size),  # bottom right
        (x + size//4, y + size),    # bottom left
        (x, y + size//3)            # left
    ]
    
    for i in range(len(points)):
        draw.line([points[i], points[(i+1)%5]], fill=color, width=1)
    draw.line([points[0], points[2]], fill=color, width=1)
    draw.line([points[0], points[3]], fill=color, width=1)

def draw_shape(draw: ImageDraw, shape: Shape, x: int, y: int, size: int, color: Tuple[int, int, int]) -> None:
    """Draw the specified shape."""
    if shape == Shape.CUBE:
        draw_cube_outline(draw, x, y, size, color)
    elif shape == Shape.PYRAMID:
        draw_pyramid_outline(draw, x, y, size, color)
    elif shape == Shape.CRYSTAL:
        draw_crystal_outline(draw, x, y, size, color)

def create_wallpaper(width: int = 5120, height: int = 1440) -> Image.Image:
    """Generate an ultrawide wallpaper with varied geometric patterns."""
    img = create_smooth_gradient(width, height)
    draw = ImageDraw.Draw(img)
    
    # Generate shapes with more size variation
    base_sizes = [80, 100, 120, 140, 160]
    
    # Reduced number of shapes with more variation
    for _ in range(70):
        x = int(random.gauss(width * 0.6, width * 0.3))
        if x < 0 or x > width:
            continue
            
        y = random.randint(0, height - 160)
        base_size = random.choice(base_sizes)
        # Add size variation
        size = base_size + random.randint(-20, 20)
        
        # Get shape type based on position
        position_ratio = x / width
        if position_ratio > 0.7:
            shape = random.choice(list(Shape))
        elif position_ratio > 0.4:
            shape = random.choice([Shape.CUBE, Shape.CRYSTAL])
        else:
            shape = random.choice([Shape.CUBE, Shape.PYRAMID])
        
        # Add slight position randomness
        x += random.randint(-15, 15)
        y += random.randint(-15, 15)
        
        if 0 <= x <= width - size and 0 <= y <= height - size:
            outline_color = get_outline_color()
            draw_shape(draw, shape, x, y, size, outline_color)
    
    # Very subtle final blur
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    return img

if __name__ == "__main__":
    wallpaper = create_wallpaper()
    filename = f"geometric_wallpaper_{uuid.uuid4()}.png"
    wallpaper.save(filename, "PNG")
    print(f"Geometric wallpaper {filename} generated successfully!")
