#!/usr/bin/env python3
"""
ARC Challenge Integer Histogram Generator

This script creates a histogram showing the frequency distribution of all integers (0-9)
used across all ARC challenge samples (training and test data, inputs and outputs).
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from pathlib import Path
import argparse
from datetime import datetime


def load_arc_data(data_dir="data"):
    """Load ARC challenge and solution data."""
    data_path = Path(data_dir)
    
    # Load training data
    train_challenges_file = data_path / "arc-agi_training_challenges.json"
    train_solutions_file = data_path / "arc-agi_training_solutions.json"
    
    # Load test data (evaluation)
    test_challenges_file = data_path / "arc-agi_evaluation_challenges.json"
    test_solutions_file = data_path / "arc-agi_evaluation_solutions.json"
    
    with open(train_challenges_file, 'r') as f:
        train_challenges = json.load(f)
    
    with open(train_solutions_file, 'r') as f:
        train_solutions = json.load(f)
        
    with open(test_challenges_file, 'r') as f:
        test_challenges = json.load(f)
    
    with open(test_solutions_file, 'r') as f:
        test_solutions = json.load(f)
    
    return train_challenges, train_solutions, test_challenges, test_solutions


def extract_all_integers(challenges, solutions):
    """Extract all integers from challenge grids (inputs and outputs)."""
    all_integers = []
    
    for challenge_id, challenge_data in challenges.items():
        # Process training examples
        for example in challenge_data.get('train', []):
            # Input grid
            for row in example['input']:
                all_integers.extend(row)
            
            # Output grid
            for row in example['output']:
                all_integers.extend(row)
        
        # Process test examples (inputs)
        for example in challenge_data.get('test', []):
            # Input grid
            for row in example['input']:
                all_integers.extend(row)
        
        # Process test solutions if available
        if challenge_id in solutions:
            solution_outputs = solutions[challenge_id]
            for solution in solution_outputs:
                for row in solution:
                    all_integers.extend(row)
    
    return all_integers


def create_histogram(all_integers, save_path=None, title="ARC Challenge Integer Distribution"):
    """Create and display histogram of integer frequencies."""
    
    # Count frequencies
    counter = Counter(all_integers)
    
    # Ensure we have all integers 0-9, even if some have 0 count
    integers = list(range(10))
    frequencies = [counter.get(i, 0) for i in integers]
    
    # Create the histogram
    plt.figure(figsize=(12, 8))
    
    # Create color map similar to the visualization colors
    colors = ['black', 'blue', 'red', 'green', 'yellow', 
              'gray', 'magenta', 'orange', 'lightblue', 'brown']
    
    bars = plt.bar(integers, frequencies, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Customize the plot
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Integer Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(integers)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on top of bars
    for bar, freq in zip(bars, frequencies):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + max(frequencies)*0.01,
                f'{freq:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Add statistics text box
    total_count = sum(frequencies)
    stats_text = f'Total Cells: {total_count:,}\n'
    stats_text += f'Unique Values: {len([f for f in frequencies if f > 0])}\n'
    stats_text += f'Most Common: {integers[np.argmax(frequencies)]} ({max(frequencies):,} times)\n'
    stats_text += f'Least Common: {integers[np.argmin([f if f > 0 else float("inf") for f in frequencies])]}'
    
    plt.text(0.98, 0.98, stats_text, transform=plt.gca().transAxes, 
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8),
             fontsize=10, fontfamily='monospace')
    
    plt.tight_layout()
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Histogram saved to: {save_path}")
    
    plt.show()
    
    return counter


def print_statistics(counter):
    """Print detailed statistics about integer frequencies."""
    print("\n" + "="*60)
    print("ARC CHALLENGE INTEGER STATISTICS")
    print("="*60)
    
    total = sum(counter.values())
    print(f"Total cells analyzed: {total:,}")
    print(f"Unique values found: {len([v for v in counter.values() if v > 0])}")
    
    print("\nFrequency Distribution:")
    print("-" * 40)
    print(f"{'Value':<8}{'Count':<12}{'Percentage':<12}{'Bar':<20}")
    print("-" * 40)
    
    for i in range(10):
        count = counter.get(i, 0)
        percentage = (count / total * 100) if total > 0 else 0
        bar_length = int(percentage / 5)  # Scale bar to reasonable length
        bar = "█" * bar_length
        
        print(f"{i:<8}{count:<12,}{percentage:<8.2f}%    {bar}")
    
    print("-" * 40)
    print(f"{'TOTAL':<8}{total:<12,}{'100.00%':<12}")
    
    # Find most/least common
    most_common = max(counter.items(), key=lambda x: x[1])
    least_common = min([(k, v) for k, v in counter.items() if v > 0], key=lambda x: x[1])
    
    print(f"\nMost common value: {most_common[0]} ({most_common[1]:,} occurrences)")
    print(f"Least common value: {least_common[0]} ({least_common[1]:,} occurrences)")
    print(f"Ratio (most/least): {most_common[1] / least_common[1]:.2f}x")


def main():
    parser = argparse.ArgumentParser(description="Generate histogram of ARC challenge integer frequencies")
    parser.add_argument('--data-dir', default='data', 
                       help='Directory containing ARC data files')
    parser.add_argument('--save-path', default=None,
                       help='Path to save the histogram image')
    parser.add_argument('--training-only', action='store_true',
                       help='Include only training data')
    parser.add_argument('--test-only', action='store_true',
                       help='Include only test data')
    parser.add_argument('--auto-save', action='store_true', 
                       help='Automatically save with timestamp')
    
    args = parser.parse_args()
    
    print("Loading ARC data...")
    try:
        train_challenges, train_solutions, test_challenges, test_solutions = load_arc_data(args.data_dir)
        print(f"Loaded {len(train_challenges)} training challenges")
        print(f"Loaded {len(test_challenges)} test challenges")
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        print("Make sure the data directory contains the required JSON files.")
        return
    
    # Determine what data to include
    include_training = not args.test_only
    include_test = not args.training_only
    
    # Collect integers from specified datasets
    all_integers = []
    title_parts = []
    
    if include_training:
        print("Extracting integers from training data...")
        train_integers = extract_all_integers(train_challenges, train_solutions)
        all_integers.extend(train_integers)
        title_parts.append("Training")
        print(f"Found {len(train_integers):,} integers in training data")
    
    if include_test:
        print("Extracting integers from test data...")
        test_integers = extract_all_integers(test_challenges, test_solutions)
        all_integers.extend(test_integers)
        title_parts.append("Test")
        print(f"Found {len(test_integers):,} integers in test data")
    
    if not all_integers:
        print("No data selected! Please include training and/or test data.")
        return
    
    print(f"\nTotal integers collected: {len(all_integers):,}")
    
    # Generate title
    title = f"ARC Challenge Integer Distribution ({' + '.join(title_parts)} Data)"
    
    # Determine save path
    save_path = args.save_path
    if args.auto_save and not save_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"arc_histogram_{timestamp}.png"
    
    # Create histogram
    print("\nGenerating histogram...")
    counter = create_histogram(all_integers, save_path, title)
    
    # Print statistics
    print_statistics(counter)


if __name__ == "__main__":
    main()
