# ARC Data Visualization System

This repository contains a comprehensive visualization system for the ARC (Abstraction and Reasoning Corpus) 2025 competition data. The system provides multiple tools to explore, analyze, and visualize the training challenges and solutions.

## Features

### 🎨 Main Visualizer (`arc_visualizer.py`)
- **Individual Challenge Visualization**: Each challenge is saved as a separate PNG file
- **Test Output Display**: Shows test inputs, expected outputs (if available), and solutions
- **Grid Visualization**: Each integer (0-9) is displayed in a unique color with clear cell boundaries
- **Automatic Padding**: Handles variable grid sizes (1x1 to 30x30) with intelligent padding
- **Timestamped Organization**: Creates unique timestamped directories for each run
- **Batch Processing**: Visualize multiple random challenges at once
- **Flexible Selection**: Choose specific challenges or random samples

### 📊 Data Explorer (`arc_explorer.py`)
- **Dataset Statistics**: Comprehensive analysis of the ARC dataset
- **Pattern Detection**: Identifies challenges with interesting properties
- **Recommendations**: Suggests diverse challenges for visualization practice
- **Statistical Plots**: Visual analysis of grid sizes, color usage, and complexity

## Installation

### Requirements
- Python 3.7+
- matplotlib
- numpy

### Setup
```bash
# Install required packages
pip install matplotlib numpy

# Make scripts executable
chmod +x arc_visualizer.py arc_explorer.py
```

## Usage

### Default Behavior - Random Challenges
```bash
# Visualize 10 random challenges (default)
python3 arc_visualizer.py

# Visualize specific number of random challenges
python3 arc_visualizer.py --n-samples 5

# Save to custom directory
python3 arc_visualizer.py --n-samples 3 --save-dir my_visualizations
```

### Specific Challenge Visualization
```bash
# Visualize a specific challenge
python3 arc_visualizer.py --challenge-id "00576224"

# Visualize specific challenge to custom directory
python3 arc_visualizer.py --challenge-id "00576224" --save-dir single_challenges
```

### Data Exploration and Statistics
```bash
# Analyze dataset and get recommendations
python3 arc_explorer.py
```

### Advanced Options
```bash
# Different data directory
python3 arc_visualizer.py --data-dir /path/to/data --n-samples 8

# Get help
python3 arc_visualizer.py --help
```

## File Structure

```
arc/
├── data/                          # ARC dataset files
│   ├── arc-agi_training_challenges.json
│   ├── arc-agi_training_solutions.json
│   └── ...
├── arc_visualizer.py             # Main visualization script
├── arc_explorer.py               # Data analysis and exploration
├── README.md                     # This file
└── examples/                     # Generated visualizations
    ├── 20250811_172316/         # Timestamped directories
    │   ├── challenge_d0f5fe59.png
    │   ├── challenge_5582e5ca.png
    │   └── challenge_1fad071e.png
    ├── 20250811_172423/         # Another timestamp
    │   └── ...
    └── old_examples/            # Previous manual runs
```

## Color Mapping

The visualization uses a consistent color scheme for the integer values 0-9:

| Value | Color | Hex Code |
|-------|-------|----------|
| 0 | Black | #000000 |
| 1 | Blue | #0074D9 |
| 2 | Red | #FF4136 |
| 3 | Green | #2ECC40 |
| 4 | Yellow | #FFDC00 |
| 5 | Gray | #AAAAAA |
| 6 | Fuchsia | #F012BE |
| 7 | Orange | #FF851B |
| 8 | Aqua | #7FDBFF |
| 9 | Maroon | #870C25 |

## Dataset Statistics

Based on the analysis of 1000 training challenges:

- **Training Examples**: 2-10 per challenge (avg: 3.2)
- **Test Examples**: 1-4 per challenge (avg: 1.1)
- **Grid Sizes**: From 1×5 to 30×30
- **Grid Areas**: 1-900 cells (avg: ~154 cells)
- **Colors Used**: All values 0-9 are present in the dataset

## Challenge Categories

The explorer identifies several interesting challenge types:

### 🔍 **Simple Patterns** (128 challenges)
- Use only 1-2 colors
- Good for understanding basic transformations
- Example: `d749d46f`

### 📏 **Size Changes** (320 challenges)  
- Input and output grids have different dimensions
- Focus on transformation rules that change grid size
- Example: `9af7a82c`

### 🌈 **Many Colors** (243 challenges)
- Use more than 5 different colors
- Complex color-based transformations
- Example: `20fb2937`

### 📐 **Large Grids** (420 challenges)
- Grids with more than 200 cells
- Test spatial reasoning at scale
- Example: `ccd554ac`

### 🔬 **Small Grids** (201 challenges)
- Grids with fewer than 10 cells
- Focus on precise, minimal transformations
- Example: `ac0a08a4`

## Example Visualizations

### Individual Challenge Files
Each challenge is saved as a separate PNG file showing:
- **Training Examples**: All input/output pairs for learning the pattern  
- **Test Examples**: Test inputs with their corresponding solutions from the solutions file

### Layout Structure
- **Top Row**: Training examples (Input → Output pairs)
- **Bottom Row**: Test examples (Input → Solution pairs)
- Each visualization shows the complete challenge with all available data

### Timestamped Organization  
Each run creates a new timestamped directory (e.g., `examples/20250811_172316/`) containing:
- Individual challenge files named `challenge_{id}.png`
- Easy navigation and comparison between runs
- No file conflicts between different visualization sessions

## Tips for Analysis

1. **Start with Simple Patterns**: Use the explorer to find challenges with 1-2 colors
2. **Understand Size Changes**: Look for challenges where input/output dimensions differ
3. **Color Mapping**: Pay attention to how colors are transformed between input and output
4. **Spatial Relationships**: Notice how patterns are preserved, rotated, or transformed
5. **Edge Cases**: Small grids often reveal core transformation rules clearly

## Contributing

Feel free to extend the visualization system with:
- Interactive features
- Additional statistical analysis
- Custom color schemes
- Export formats (SVG, PDF)
- Animation for transformation visualization

## Competition Context

This visualization system is designed for the ARC 2025 competition. The ARC dataset tests abstract reasoning capabilities through visual puzzles that require understanding patterns and applying them to new situations.

### Key ARC Concepts to Visualize:
- **Pattern Recognition**: Identifying repeated structures
- **Transformation Rules**: Understanding how inputs become outputs  
- **Spatial Reasoning**: Position, rotation, reflection relationships
- **Object Identification**: Recognizing distinct entities in grids
- **Counting and Quantity**: Numerical relationships in patterns

---

*Happy pattern hunting! 🎯*
