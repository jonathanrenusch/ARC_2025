# ARC 2025 Visualization Tool

> An open-source toolkit for visualizing and exploring the ARC (Abstraction and Reasoning Corpus) 2025 dataset from Kaggle

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Overview

This repository provides a comprehensive visualization system for the **ARC 2025 challenge dataset** available on Kaggle. Whether you're a researcher, competitor, or just curious about abstract reasoning puzzles, this tool makes it easy to explore and understand the ARC dataset through beautiful, intuitive visualizations.

The ARC (Abstraction and Reasoning Corpus) is a benchmark designed to measure an AI system's ability to efficiently learn new skills. This toolkit helps you visualize the training challenges, analyze patterns, and gain insights into the dataset's structure.

## 🖼️ Example Gallery

**Want to see it in action?** Check out the [`examples/`](examples/) directory containing **100+ pre-generated visualization examples** showcasing different challenge types, patterns, and complexities from the ARC dataset. These examples demonstrate the visualization capabilities and give you a preview of what the dataset looks like!

## ✨ Features

### 🎨 Visual Challenge Explorer (`arc_visualizer.py`)
- **Beautiful Grid Visualizations**: Each cell is rendered with distinct colors and clear boundaries
- **Individual Challenge Export**: Save each challenge as a separate PNG file
- **Batch Processing**: Visualize multiple random challenges at once
- **Smart Padding**: Automatically handles variable grid sizes (1×1 to 30×30)
- **Test Case Display**: Shows training examples alongside test inputs and expected outputs
- **Timestamped Output**: Organized export with automatic timestamped directories

### 📊 Statistical Analysis (`arc_explorer.py`)
- **Dataset Statistics**: Comprehensive analysis of grid sizes, color distributions, and complexity
- **Pattern Detection**: Automatically identifies challenges with interesting properties:
  - Simple patterns (1-2 colors)
  - Size transformations (dimension changes)
  - Complex color challenges (5+ colors)
  - Large and small grid challenges
- **Smart Recommendations**: Suggests diverse challenges for exploration
- **Visual Reports**: Generates statistical plots for data insights

### 📈 Distribution Analysis (`arc_histogram.py`)
- **Color Frequency Analysis**: Histogram showing distribution of integers (0-9) across the dataset
- **Training/Test Comparison**: Analyze training and test data separately or combined
- **Statistical Summaries**: Detailed frequency counts and percentages

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- matplotlib
- numpy

### Installation

```bash
# Clone the repository
git clone https://github.com/jonathanrenusch/ARC_2025.git
cd ARC_2025

# Install dependencies
pip install matplotlib numpy

# Download the ARC dataset from Kaggle and place it in the data/ directory
# Expected files:
#   - data/arc-agi_training_challenges.json
#   - data/arc-agi_training_solutions.json
```

### Basic Usage

```bash
# Visualize 10 random challenges
python3 src/data_vis/arc_visualizer.py --n-samples 10

# Visualize a specific challenge by ID
python3 src/data_vis/arc_visualizer.py --challenge-id "00576224"

# Analyze dataset statistics and get recommendations
python3 src/data_vis/arc_explorer.py

# Generate color distribution histogram
python3 src/data_vis/arc_histogram.py --auto-save
```

## 📖 Usage Examples

### Explore Random Challenges
```bash
# Visualize 5 random challenges
python3 src/data_vis/arc_visualizer.py --n-samples 5

# Save to a custom directory
python3 src/data_vis/arc_visualizer.py --n-samples 3 --save-dir my_visualizations
```

### Analyze Specific Challenges
```bash
# Visualize a specific challenge
python3 src/data_vis/arc_visualizer.py --challenge-id "00576224"

# Use a custom data directory
python3 src/data_vis/arc_visualizer.py --data-dir /path/to/data --challenge-id "abc123"
```

### Generate Dataset Insights
```bash
# Get comprehensive dataset statistics
python3 src/data_vis/arc_explorer.py

# Create histogram of color frequencies
python3 src/data_vis/arc_histogram.py --training-only
```

## 🎨 Color Scheme

The visualizer uses a consistent, distinct color palette for integers 0-9:

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

## 📂 Repository Structure

```
ARC_2025/
├── src/
│   └── data_vis/
│       ├── arc_visualizer.py      # Main visualization script
│       ├── arc_explorer.py        # Statistical analysis tool
│       ├── arc_histogram.py       # Color distribution analyzer
│       ├── create_examples.sh     # Batch processing script
│       └── README.md              # Detailed documentation
├── data/                          # Place ARC dataset here
│   ├── arc-agi_training_challenges.json
│   └── arc-agi_training_solutions.json
├── examples/                      # 100+ pre-generated visualizations ⭐
│   ├── challenge_00576224.png
│   ├── challenge_007bbfb7.png
│   └── ... (100+ examples)
└── LICENSE                        # MIT License
```

## 📊 Dataset Insights

The ARC 2025 dataset includes:
- **400 training challenges** with solutions
- **2-10 training examples** per challenge (average: 3.2)
- **1-4 test cases** per challenge (average: 1.1)
- **Grid sizes**: From 1×5 to 30×30 cells
- **Color values**: Integers 0-9, each with semantic meaning

## 🤝 Contributing

This is an **open-source project** and contributions are welcome! Whether you want to:
- Add new visualization features
- Improve statistical analysis
- Create interactive tools
- Add export formats (SVG, PDF)
- Enhance documentation

Feel free to open an issue or submit a pull request!

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use this tool for research or competition
- ✅ Modify and distribute the code
- ✅ Use it commercially
- ✅ Share with others

## 🙏 Acknowledgments

- **Kaggle** for hosting the ARC 2025 competition and dataset
- The **ARC challenge creators** for developing this fascinating benchmark
- The open-source community for Python visualization tools (matplotlib, numpy)

## 🔗 Resources

- [ARC 2025 Kaggle Competition](https://www.kaggle.com/competitions/arc-prize-2025)
- [Original ARC Paper](https://arxiv.org/abs/1911.01547)
- [ARC Dataset Documentation](https://github.com/fchollet/ARC)

## 📧 Contact

Created by [@jonathanrenusch](https://github.com/jonathanrenusch)

---

**Happy Visualizing! 🎨✨**

If you find this tool useful, please consider giving it a ⭐ on GitHub!
