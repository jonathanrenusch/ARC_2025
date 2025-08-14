#!/usr/bin/env python3
"""
ARC Data Explorer - Interactive version

This script provides additional functionality for exploring ARC data,
including statistics and interactive features.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from collections import Counter
import random

def analyze_data_statistics(challenges, solutions):
    """Analyze and print statistics about the ARC dataset."""
    print("=== ARC Dataset Statistics ===")
    print(f"Total challenges: {len(challenges)}")
    print(f"Total solutions: {len(solutions)}")
    
    # Training examples statistics
    train_counts = []
    test_counts = []
    input_sizes = []
    output_sizes = []
    unique_values = set()
    
    for challenge_id, challenge in challenges.items():
        train_counts.append(len(challenge['train']))
        test_counts.append(len(challenge['test']))
        
        # Analyze training examples
        for example in challenge['train']:
            input_grid = np.array(example['input'])
            output_grid = np.array(example['output'])
            
            input_sizes.append(input_grid.shape)
            output_sizes.append(output_grid.shape)
            
            # Collect unique values
            unique_values.update(input_grid.flatten())
            unique_values.update(output_grid.flatten())
    
    print(f"\nTraining examples per challenge:")
    print(f"  Min: {min(train_counts)}, Max: {max(train_counts)}, Avg: {np.mean(train_counts):.1f}")
    
    print(f"\nTest examples per challenge:")
    print(f"  Min: {min(test_counts)}, Max: {max(test_counts)}, Avg: {np.mean(test_counts):.1f}")
    
    print(f"\nGrid sizes (height x width):")
    input_areas = [h * w for h, w in input_sizes]
    output_areas = [h * w for h, w in output_sizes]
    
    print(f"  Input sizes - Min: {min(input_sizes)}, Max: {max(input_sizes)}")
    print(f"  Output sizes - Min: {min(output_sizes)}, Max: {max(output_sizes)}")
    print(f"  Input areas - Min: {min(input_areas)}, Max: {max(input_areas)}, Avg: {np.mean(input_areas):.1f}")
    print(f"  Output areas - Min: {min(output_areas)}, Max: {max(output_areas)}, Avg: {np.mean(output_areas):.1f}")
    
    print(f"\nUnique values in dataset: {sorted(unique_values)}")
    
    return {
        'train_counts': train_counts,
        'test_counts': test_counts,
        'input_sizes': input_sizes,
        'output_sizes': output_sizes,
        'unique_values': sorted(unique_values)
    }

def find_interesting_challenges(challenges, solutions):
    """Find challenges with interesting properties."""
    print("\n=== Interesting Challenges ===")
    
    # Find challenges with different properties
    large_grids = []
    small_grids = []
    many_colors = []
    simple_patterns = []
    size_changes = []
    
    for challenge_id, challenge in challenges.items():
        for example in challenge['train']:
            input_grid = np.array(example['input'])
            output_grid = np.array(example['output'])
            
            input_size = input_grid.size
            output_size = output_grid.size
            
            # Large grids (> 200 cells)
            if input_size > 200 or output_size > 200:
                large_grids.append(challenge_id)
            
            # Small grids (< 10 cells)
            if input_size < 10 or output_size < 10:
                small_grids.append(challenge_id)
            
            # Many colors (> 5 unique values)
            unique_input = len(set(input_grid.flatten()))
            unique_output = len(set(output_grid.flatten()))
            if unique_input > 5 or unique_output > 5:
                many_colors.append(challenge_id)
            
            # Simple patterns (only 1-2 colors)
            if unique_input <= 2 and unique_output <= 2:
                simple_patterns.append(challenge_id)
            
            # Size changes
            if input_grid.shape != output_grid.shape:
                size_changes.append(challenge_id)
    
    # Remove duplicates and show samples
    large_grids = list(set(large_grids))
    small_grids = list(set(small_grids))
    many_colors = list(set(many_colors))
    simple_patterns = list(set(simple_patterns))
    size_changes = list(set(size_changes))
    
    print(f"Challenges with large grids (>200 cells): {len(large_grids)}")
    if large_grids:
        print(f"  Examples: {random.sample(large_grids, min(3, len(large_grids)))}")
    
    print(f"Challenges with small grids (<10 cells): {len(small_grids)}")
    if small_grids:
        print(f"  Examples: {random.sample(small_grids, min(3, len(small_grids)))}")
    
    print(f"Challenges with many colors (>5): {len(many_colors)}")
    if many_colors:
        print(f"  Examples: {random.sample(many_colors, min(3, len(many_colors)))}")
    
    print(f"Challenges with simple patterns (1-2 colors): {len(simple_patterns)}")
    if simple_patterns:
        print(f"  Examples: {random.sample(simple_patterns, min(3, len(simple_patterns)))}")
    
    print(f"Challenges with size changes: {len(size_changes)}")
    if size_changes:
        print(f"  Examples: {random.sample(size_changes, min(3, len(size_changes)))}")
    
    return {
        'large_grids': large_grids,
        'small_grids': small_grids,
        'many_colors': many_colors,
        'simple_patterns': simple_patterns,
        'size_changes': size_changes
    }

def create_statistics_plots(stats, save_dir=None):
    """Create plots showing dataset statistics."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('ARC Dataset Statistics', fontsize=16, fontweight='bold')
    
    # Training examples per challenge
    axes[0, 0].hist(stats['train_counts'], bins=range(1, max(stats['train_counts']) + 2), 
                    alpha=0.7, edgecolor='black')
    axes[0, 0].set_xlabel('Number of Training Examples')
    axes[0, 0].set_ylabel('Number of Challenges')
    axes[0, 0].set_title('Training Examples per Challenge')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Test examples per challenge
    axes[0, 1].hist(stats['test_counts'], bins=range(1, max(stats['test_counts']) + 2), 
                    alpha=0.7, color='orange', edgecolor='black')
    axes[0, 1].set_xlabel('Number of Test Examples')
    axes[0, 1].set_ylabel('Number of Challenges')
    axes[0, 1].set_title('Test Examples per Challenge')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Input grid areas
    input_areas = [h * w for h, w in stats['input_sizes']]
    axes[0, 2].hist(input_areas, bins=50, alpha=0.7, color='green', edgecolor='black')
    axes[0, 2].set_xlabel('Grid Area (cells)')
    axes[0, 2].set_ylabel('Frequency')
    axes[0, 2].set_title('Input Grid Areas')
    axes[0, 2].grid(True, alpha=0.3)
    
    # Output grid areas
    output_areas = [h * w for h, w in stats['output_sizes']]
    axes[1, 0].hist(output_areas, bins=50, alpha=0.7, color='red', edgecolor='black')
    axes[1, 0].set_xlabel('Grid Area (cells)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Output Grid Areas')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Grid dimensions scatter plot
    input_heights, input_widths = zip(*stats['input_sizes'])
    axes[1, 1].scatter(input_widths, input_heights, alpha=0.5, s=10)
    axes[1, 1].set_xlabel('Width')
    axes[1, 1].set_ylabel('Height')
    axes[1, 1].set_title('Input Grid Dimensions')
    axes[1, 1].grid(True, alpha=0.3)
    
    # Color usage
    axes[1, 2].bar(range(len(stats['unique_values'])), 
                   [1] * len(stats['unique_values']),  # Placeholder for actual color frequency
                   color=[f"C{i}" for i in stats['unique_values']])
    axes[1, 2].set_xlabel('Color Value')
    axes[1, 2].set_ylabel('Present in Dataset')
    axes[1, 2].set_title('Colors Used in Dataset')
    axes[1, 2].set_xticks(range(len(stats['unique_values'])))
    axes[1, 2].set_xticklabels(stats['unique_values'])
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_dir:
        save_path = Path(save_dir) / 'arc_statistics.png'
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved statistics plots to {save_path}")
    else:
        plt.show()

def main():
    data_dir = 'data'
    
    # Load data
    print("Loading ARC data...")
    
    challenges_path = Path(data_dir) / 'arc-agi_training_challenges.json'
    solutions_path = Path(data_dir) / 'arc-agi_training_solutions.json'
    
    with open(challenges_path, 'r') as f:
        challenges = json.load(f)
    
    with open(solutions_path, 'r') as f:
        solutions = json.load(f)
    
    print(f"Loaded {len(challenges)} challenges and {len(solutions)} solutions")
    
    # Analyze statistics
    stats = analyze_data_statistics(challenges, solutions)
    
    # Find interesting challenges
    interesting = find_interesting_challenges(challenges, solutions)
    
    # Create statistics plots
    create_statistics_plots(stats)
    
    print("\n=== Recommendations ===")
    print("For visualization practice, try these challenges:")
    
    # Recommend some diverse challenges
    recommendations = []
    
    if interesting['simple_patterns']:
        recommendations.append(f"Simple patterns: {random.choice(interesting['simple_patterns'])}")
    
    if interesting['size_changes']:
        recommendations.append(f"Size changes: {random.choice(interesting['size_changes'])}")
    
    if interesting['many_colors']:
        recommendations.append(f"Many colors: {random.choice(interesting['many_colors'])}")
    
    if interesting['large_grids']:
        recommendations.append(f"Large grids: {random.choice(interesting['large_grids'])}")
    
    for rec in recommendations:
        print(f"  {rec}")
    
    print(f"\nUse the main visualizer script to view these:")
    for rec in recommendations:
        challenge_id = rec.split(': ')[1]
        print(f"  python3 arc_visualizer.py --challenge-id {challenge_id}")

if __name__ == '__main__':
    main()
