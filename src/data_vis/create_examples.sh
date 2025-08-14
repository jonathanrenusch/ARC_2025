#!/bin/bash
# Batch visualization script for ARC data
# Creates example visualizations of different challenge types

echo "🎨 Creating ARC Visualization Examples"
echo "======================================"

# Create output directory
mkdir -p examples

# Generate summary visualization
echo "📊 Creating summary visualization..."
python3 arc_visualizer.py --summary --n-samples 4 --save examples/summary_4_challenges.png

# Create larger summary
echo "📊 Creating extended summary..."
python3 arc_visualizer.py --summary --n-samples 8 --save examples/summary_8_challenges.png

# Get challenge recommendations from explorer
echo "🔍 Getting challenge recommendations..."
python3 arc_explorer.py > examples/dataset_analysis.txt 2>&1

# Extract recommended challenge IDs (this is a simple approach)
# In practice, you might want to modify the explorer to output JSON
echo "🎯 Creating specific challenge examples..."

# Some known interesting challenges from different categories
challenges=(
    "00576224"  # Example from our testing
    "007bbfb7"  # Small grid
    "025d127b"  # Another example
    "045e512c"  # Different pattern
)

for challenge in "${challenges[@]}"; do
    echo "  📋 Visualizing challenge: $challenge"
    python3 arc_visualizer.py --challenge-id "$challenge" --save "examples/challenge_${challenge}.png"
done

echo ""
echo "✅ Visualization examples created in 'examples/' directory:"
echo "   - summary_4_challenges.png (4 random challenges)"
echo "   - summary_8_challenges.png (8 random challenges)" 
echo "   - challenge_*.png (specific challenge examples)"
echo "   - dataset_analysis.txt (statistical analysis)"
echo ""
echo "🚀 To create your own visualizations:"
echo "   python3 arc_visualizer.py --summary"
echo "   python3 arc_visualizer.py --challenge-id [ID]"
echo "   python3 arc_explorer.py"
