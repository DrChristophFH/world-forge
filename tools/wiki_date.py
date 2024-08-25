import os
import re
import argparse
from pathlib import Path
from typing import List, Tuple, Optional

class FantasyDate:
    def __init__(self, year: int, month: int = 1, day: int = 1):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str: str) -> 'FantasyDate':
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 1
        day = int(parts[2]) if len(parts) > 2 else 1
        return cls(year, month, day)

    def __lt__(self, other: 'FantasyDate') -> bool:
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other: 'FantasyDate') -> bool:
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    def __eq__(self, other: 'FantasyDate') -> bool:
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __str__(self) -> str:
        suffix = "AB" if self.year >= 0 else "BB"
        year_str = f"{abs(self.year)} {suffix}"
        # month_name = ["Frostwon", "Siniir", "Albater", "Famester", "Sement", "Ros", "Deniir", "Flor", "Caloret", "Dutemt", "Varis", "Fringres"][self.month - 1]
        return f"{self.day}.{self.month}.{year_str}"

def parse_flexible_date(date_str: str) -> Tuple[FantasyDate, FantasyDate]:
    """Parse a flexible date string and return start and end FantasyDates."""
    date_str = date_str.strip()
    before_bulwarks = False

    if date_str[0] == "-":
        date_str = date_str[1:]
        before_bulwarks = True

    parts = date_str.split('-')
    year = int(parts[0]) * (-1 if before_bulwarks else 1)

    if len(parts) == 1:  # Only year
        return FantasyDate(year, 1, 1), FantasyDate(year, 12, 30)
    elif len(parts) == 2:  # Year and month
        month = int(parts[1])
        return FantasyDate(year, month, 1), FantasyDate(year, month, 30)
    else:  # Full date
        return FantasyDate.from_string(date_str), FantasyDate.from_string(date_str)

def extract_date_info(file_path: Path) -> Tuple[str, Optional[FantasyDate], Optional[FantasyDate]]:
    """Extract the title and date information from a file's frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else file_path.stem
    
    # Extract date or date range
    date_match = re.search(r'date:\s*(\S+)', content)
    date_range_match = re.search(r'date_range:\s*\n\s*start:\s*(\S+)\s*\n\s*end:\s*(\S+)', content)
    
    if date_match:
        start, end = parse_flexible_date(date_match.group(1))
        return title, start, end
    elif date_range_match:
        start, _ = parse_flexible_date(date_range_match.group(1))
        _, end = parse_flexible_date(date_range_match.group(2))
        return title, start, end
    
    return title, None, None

def search_wiki_by_date(wiki_path: str, start_date: FantasyDate, end_date: FantasyDate) -> List[Tuple[str, FantasyDate, FantasyDate, Path]]:
    """Search the wiki for articles within the specified date range."""
    results = []
    
    unwanted_dirs = ['templates']
    
    for root, dirs, files in os.walk(wiki_path, topdown=True):
        # Skip unwanted directories
        dirs[:] = [d for d in dirs if d not in unwanted_dirs]
        
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                title, file_start, file_end = extract_date_info(file_path)
                
                if file_start and file_end:
                    if (file_start <= end_date and file_end >= start_date):
                        results.append((title, file_start, file_end, file_path))
    
    return sorted(results, key=lambda x: (x[1], x[2]))

def main():
    parser = argparse.ArgumentParser(
        description="Search wiki articles by date or date range in the fantasy world timeline.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Search for articles on a specific date:
    python wiki_date_search.py /path/to/wiki 1501-03-15

  Search for articles in a specific month:
    python wiki_date_search.py /path/to/wiki 1501-03

  Search for articles in a specific year:
    python wiki_date_search.py /path/to/wiki 1501

  Search for articles within a date range:
    python wiki_date_search.py /path/to/wiki 1501-03-15 1501-04-02

Note:
  - Dates can be in the format YYYY-MM-DD, YYYY-MM, or YYYY.
  - The tool automatically handles AB (Age of Bulwarks) and BB (Before Bulwarks) dates.
  - Negative years represent BB (Before Bulwarks), positive years represent AB (Age of Bulwarks).
  - If only a start date is provided, it will search for articles on that specific date/month/year.
  - Date ranges in article frontmatter are also supported and will be included if they overlap with the search range.
  - The fantasy calendar has 12 months of 30 days each.
        """
    )
    parser.add_argument("wiki_path", help="Path to the wiki directory")
    parser.add_argument("start_date", help="Start date (YYYY-MM-DD, YYYY-MM, or YYYY)")
    parser.add_argument("end_date", nargs="?", help="End date (optional, same format as start_date)")
    args = parser.parse_args()
    
    if not os.path.isdir(args.wiki_path):
        print(f"Error: The path '{args.wiki_path}' is not a valid directory.")
        return
    
    start_date, start_end = parse_flexible_date(args.start_date)
    if args.end_date:
        _, end_date = parse_flexible_date(args.end_date)
    else:
        end_date = start_end
    
    results = search_wiki_by_date(args.wiki_path, start_date, end_date)
    
    if results:
        print(f"\nArticles found between {start_date} and {end_date}:")
        for title, file_start, file_end, file_path in results:
            if file_start == file_end:
                print(f"- {title} ({file_start})")
            else:
                print(f"- {title} ({file_start} to {file_end})")
            print(f"  File: {file_path}")
    else:
        print(f"No articles found between {start_date} and {end_date}.")

if __name__ == "__main__":
    main()