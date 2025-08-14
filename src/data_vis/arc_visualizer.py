#!/usr/bin/env python3
"""
ARC Data Visualization Script

This script creates visualizations of ARC (Abstraction and Reasoning Corpus) data,
displaying input/output pairs from the training challenges and solutions.
Each challenge is saved as a separate PNG file with test outputs included.

Author: ARC Competition Participant  
Date: 2025
"""

#TODO: Add some stats on histo of colors, sizes etc.
# Document your state space model approach in the readme
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import argparse
from pathlib import Path
from datetime import datetime

# Color map for integers 0-9 (using distinct colors)
COLOR_MAP = {
    0: '#000000',  # Black
    1: '#0074D9',  # Blue  
    2: '#FF4136',  # Red
    3: '#2ECC40',  # Green
    4: '#FFDC00',  # Yellow
    5: '#AAAAAA',  # Gray
    6: '#F012BE',  # Fuchsia
    7: '#FF851B',  # Orange
    8: '#7FDBFF',  # Aqua
    9: '#870C25',  # Maroon
}

# Special color for padding (light gray with different tone)
PADDING_COLOR = '#F0F0F0'  # Very light gray for padding

def load_data(data_dir):
    """Load ARC training challenges and solutions."""
    challenges_path = Path(data_dir) / 'arc-agi_training_challenges.json'
    solutions_path = Path(data_dir) / 'arc-agi_training_solutions.json'
    
    with open(challenges_path, 'r') as f:
        challenges = json.load(f)
    
    with open(solutions_path, 'r') as f:
        solutions = json.load(f)
    
    return challenges, solutions

def plot_grid(ax, grid, title, max_size=30):
    """Plot a single grid with proper colors and padding."""
    original_grid = np.array(grid)
    original_height, original_width = original_grid.shape
    
    # Create padding info
    use_padding = original_height < max_size or original_width < max_size
    
    if use_padding:
        # Create a padded grid filled with a special padding value (-1)
        padded_grid = np.full((max_size, max_size), -1)  # -1 indicates padding
        # Center the original grid in the padded area
        start_h = (max_size - original_height) // 2
        start_w = (max_size - original_width) // 2
        padded_grid[start_h:start_h + original_height, start_w:start_w + original_width] = original_grid
        
        display_grid = padded_grid
        display_height, display_width = max_size, max_size
    else:
        display_grid = original_grid
        display_height, display_width = original_height, original_width
    
    # Clear the axes
    ax.clear()
    ax.set_xlim(0, display_width)
    ax.set_ylim(0, display_height)
    ax.set_aspect('equal')
    ax.invert_yaxis()  # Invert y-axis to match standard image coordinates
    
    # Draw each cell
    for i in range(display_height):
        for j in range(display_width):
            value = int(display_grid[i, j])
            
            # Choose color based on whether it's padding or actual data
            if value == -1:  # Padding
                color = PADDING_COLOR
                edge_color = '#D0D0D0'  # Lighter edge for padding
            else:  # Actual data
                color = COLOR_MAP[value]
                edge_color = 'gray'
            
            # Create rectangle for each cell
            rect = patches.Rectangle((j, i), 1, 1, 
                                   linewidth=0.5, 
                                   edgecolor=edge_color, 
                                   facecolor=color)
            ax.add_patch(rect)
    
    # Set title
    ax.set_title(title, fontsize=10, pad=5)
    ax.set_xticks([])
    ax.set_yticks([])

def visualize_challenge(challenge_id, challenge_data, solution_data=None, save_path=None):
    """Visualize a single challenge with its training examples and test cases."""
    train_examples = challenge_data['train']
    test_examples = challenge_data['test']
    
    # Calculate total columns needed
    # Each training example needs 2 columns (input, output)
    # Each test example needs 2 columns (input, solution)
    n_train = len(train_examples)
    n_test = len(test_examples)
    
    train_cols = n_train * 2
    test_cols = n_test * 2  # Just input and solution for test cases
    max_cols = max(train_cols, test_cols)
    
    # Create figure with 2 rows (training, test)
    fig = plt.figure(figsize=(max_cols * 2.5, 6))
    fig.suptitle(f'ARC Challenge: {challenge_id}', fontsize=16, fontweight='bold')
    
    # Plot training examples in first row
    for i, example in enumerate(train_examples):
        # Input
        ax_input = plt.subplot(2, max_cols, i * 2 + 1)
        plot_grid(ax_input, example['input'], f'Train {i+1} Input')
        
        # Output
        ax_output = plt.subplot(2, max_cols, i * 2 + 2)
        plot_grid(ax_output, example['output'], f'Train {i+1} Output')
    
    # Plot test examples in second row
    for i, example in enumerate(test_examples):
        # Calculate positions in second row (row index 2)
        input_pos = max_cols + (i * 2) + 1   # Second row, correct column for input
        solution_pos = max_cols + (i * 2) + 2  # Second row, correct column for solution
        
        # Test Input
        ax_input = plt.subplot(2, max_cols, input_pos)
        plot_grid(ax_input, example['input'], f'Test {i+1} Input')
        
        # Test Solution (from solutions file)
        if solution_data and i < len(solution_data):
            ax_solution = plt.subplot(2, max_cols, solution_pos)
            plot_grid(ax_solution, solution_data[i], f'Test {i+1} Solution')
        else:
            # Show placeholder if no solution available
            ax_solution = plt.subplot(2, max_cols, solution_pos)
            ax_solution.text(0.5, 0.5, 'No Solution\nAvailable', 
                           horizontalalignment='center', verticalalignment='center',
                           fontsize=12, color='red')
            ax_solution.set_xlim(0, 1)
            ax_solution.set_ylim(0, 1)
            ax_solution.set_title(f'Test {i+1} Solution', fontsize=10, pad=5)
            ax_solution.set_xticks([])
            ax_solution.set_yticks([])
            ax_solution.set_yticks([])
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved visualization to {save_path}")
        plt.close(fig)  # Close to free memory
    else:
        plt.show()

def create_timestamped_directory():
    """Create a timestamped directory for saving visualizations."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = Path('examples') / timestamp
    save_dir.mkdir(parents=True, exist_ok=True)
    return save_dir

def visualize_random_challenges(challenges, solutions, n_samples=10, save_dir=None):
    """Visualize n random challenges as separate PNG files."""
    if save_dir is None:
        save_dir = create_timestamped_directory()
    
    # Select random challenges
    challenge_ids = random.sample(list(challenges.keys()), min(n_samples, len(challenges)))
    
    print(f"Visualizing {len(challenge_ids)} random challenges...")
    print(f"Saving to directory: {save_dir}")
    
    for i, challenge_id in enumerate(challenge_ids, 1):
        print(f"Processing challenge {i}/{len(challenge_ids)}: {challenge_id}")
        
        challenge_data = challenges[challenge_id]
        solution_data = solutions.get(challenge_id)
        
        save_path = save_dir / f"challenge_{challenge_id}.png"
        visualize_challenge(challenge_id, challenge_data, solution_data, save_path)
    
    print(f"\nCompleted! All visualizations saved to: {save_dir}")
    return save_dir

def main():
    parser = argparse.ArgumentParser(description='Visualize ARC competition data')
    parser.add_argument('--data-dir', default='/home/iwsatlas1/jrenusch/arc/data', 
                       help='Directory containing ARC data files')
    parser.add_argument('--challenge-id', 
                       help='Specific challenge ID to visualize')
    parser.add_argument('--n-samples','-n', type=int, default=100,
                       help='Number of random challenges to visualize (default: 100)')
    parser.add_argument('--save-dir',
                       help='Directory to save visualizations (default: timestamped directory in examples/)')
    
    args = parser.parse_args()
    
    # Load data
    print("Loading ARC data...")
    challenges, solutions = load_data(args.data_dir)
    print(f"Loaded {len(challenges)} challenges and {len(solutions)} solutions")
    
    if args.challenge_id:
        # Visualize specific challenge
        if args.challenge_id not in challenges:
            print(f"Challenge ID '{args.challenge_id}' not found!")
            return
        
        # Create save directory
        if args.save_dir:
            save_dir = Path(args.save_dir)
            save_dir.mkdir(parents=True, exist_ok=True)
        else:
            save_dir = create_timestamped_directory()
        
        save_path = save_dir / f"challenge_{args.challenge_id}.png"
        visualize_challenge(args.challenge_id, challenges[args.challenge_id], 
                          solutions.get(args.challenge_id), save_path)
    
    else:
        # Visualize random challenges (default behavior)
        save_dir = Path(args.save_dir) if args.save_dir else None
        visualize_random_challenges(challenges, solutions, args.n_samples, save_dir)
    
    print("Visualization complete!")

if __name__ == '__main__':
    main()
