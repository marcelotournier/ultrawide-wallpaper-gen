# Ultrawide Desktop Wallpaper Generator

A Python script that generates visually appealing 5K ultrawide (5120x1440) desktop wallpapers featuring cubic patterns. The wallpapers are designed to be both aesthetically pleasing and functional, with careful consideration for icon readability and eye comfort.

## Features

- **High Resolution**: Generates 5120x1440 pixel wallpapers (5K ultrawide)
- **Smart Design**:
  - Cubic patterns with 3D shading effects
  - Higher pattern density on the right side
  - Darker, subtle patterns on the left side
  - Gradient background for visual comfort
  - Designed to improve desktop icon visibility
- **Eye Comfort**:
  - Soft color transitions between grey and dark blue
  - Subtle gaussian blur
  - No harsh contrasts
  - Strategic pattern placement to reduce eye strain

## Prerequisites

You'll need Python 3.6 or higher installed on your system. You can download Python from [python.org](https://python.org).

## Installation

1. Clone this repository or download the script:
```bash
git clone [repository-url]
# or download the .py file directly
```

2. Install the required dependency (Pillow):
```bash
pip install Pillow numpy
```

## Usage

1. Navigate to the script directory:
```bash
cd [script-directory]
```

2. Run the script:
```bash
python wallpaper_generator.py
```

3. The script will generate a new wallpaper and save it as `ultrawide_wallpaper.png` in the same directory.

## Customization

You can modify the following parameters in the script to customize your wallpaper:

- `cube_sizes`: List of possible cube sizes (currently [60, 80, 100, 120])
- `width` and `height`: Resolution of the output image
- Color generation in the `generate_color()` function
- Number of cubes (currently set to 300 in the main loop)

### Example Modifications

To change the resolution, modify the parameters in the `create_wallpaper()` call:
```python
wallpaper = create_wallpaper(width=3840, height=1080)  # For a different resolution
```

To adjust the color scheme, modify the `generate_color()` function:
```python
def generate_color() -> Tuple[int, int, int]:
    grey = random.randint(100, 180)
    # Modify these values for different color ranges
    return (grey, grey, random.randint(grey, min(grey + 20, 255)))
```

## How It Works

1. **Background Creation**:
   - Creates a base image with a dark gradient background
   - Gradient goes from darker on the left to lighter on the right

2. **Cube Generation**:
   - Generates 3D isometric cubes with varying sizes
   - Uses exponential distribution to place more cubes on the right side
   - Applies different shading to each face of the cube for 3D effect

3. **Visual Comfort**:
   - Applies gaussian blur for smoother transitions
   - Uses carefully selected color ranges
   - Ensures pattern spacing for icon visibility

## Contributing

Feel free to fork this repository and submit pull requests with improvements or create issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Original Request

This script was created based on the following requirements:
- Generate ultrawide 5K x 1440 pixel desktop backgrounds
- Use cubic forms in random patterns
- Colors ranging from grey to dark blue
- Cubes should occupy the right side of the screen
- Darker patterns on the left side
- Patterns should improve desktop icon readability
- Design should minimize eye strain

## Future Improvements

Potential areas for enhancement:
- Add command line arguments for easy customization
- Implement additional geometric shapes
- Add color scheme presets
- Create a GUI interface
- Add pattern density controls
- Implement wallpaper preview
