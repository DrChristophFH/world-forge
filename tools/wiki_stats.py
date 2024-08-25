import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

def extract_category(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'^---\n.*?category:\s*(.+?)\n.*?^---', content, re.DOTALL | re.MULTILINE)
        if match:
            categories = match.group(1).split(',')
            return categories[0].strip()
    return "Uncategorized"

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Remove YAML frontmatter
        content = re.sub(r'^---\n.*?^---\n', '', content, flags=re.DOTALL | re.MULTILINE)
        # Remove markdown links
        content = re.sub(r'\[\[.*?\]\]', '', content)
        # Count words
        words = content.split()
        return len(words)

def walk_wiki(wiki_path, group_by_category=False):
    total_files = 0
    total_words = 0
    category_stats = defaultdict(lambda: {"files": 0, "words": 0})
    
    unwanted_dirs = ['templates']
    
    for root, dirs, files in os.walk(wiki_path, topdown=True):
        # Skip unwanted directories
        dirs[:] = [d for d in dirs if d not in unwanted_dirs]
        
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                word_count = count_words(file_path)
                total_files += 1
                total_words += word_count
                
                if group_by_category:
                    category = extract_category(file_path)
                    category_stats[category]["files"] += 1
                    category_stats[category]["words"] += word_count
    
    return total_files, total_words, category_stats

def main():
    parser = argparse.ArgumentParser(description="Count files and words in the wiki.")
    parser.add_argument("wiki_path", help="Path to the wiki directory")
    parser.add_argument("--category", action="store_true", help="Group statistics by category")
    args = parser.parse_args()
    
    if not os.path.isdir(args.wiki_path):
        print(f"Error: The path '{args.wiki_path}' is not a valid directory.")
        return
    
    file_count, word_count, category_stats = walk_wiki(args.wiki_path, args.category)
    
    print(f"\nWiki Statistics:")
    print(f"Total number of files: {file_count:,}")
    print(f"Total number of words: {word_count:,}")
    
    if args.category:
        print("\nStatistics by Category:")
        for category, stats in category_stats.items():
            print(f"\n{category}:")
            print(f"  Files: {stats['files']:,}")
            print(f"  Words: {stats['words']:,}")

if __name__ == "__main__":
    main()