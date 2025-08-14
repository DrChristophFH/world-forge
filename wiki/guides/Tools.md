---
category: guide
---

# Available Tools

This section explains the tools available for managing and exploring the World Forge wiki. These tools help you organize, search, and analyze the content.

> [!NOTE]
> Tools are experimental and may not be fully functional yet. A full guide on how to use them and install necessary dependencies will be provided in the future.

## 1. Wiki Statistics Tool (wiki_stats.py)

**Purpose:** This tool provides an overview of the wiki's size and content distribution.

**Features:**
- Counts the total number of files and words in the wiki
- Groups statistics by category when requested

**How to Run:**
```
python wiki_stats.py /path/to/wiki
python wiki_stats.py /path/to/wiki --category
```

**Example Output:**
```
Wiki Statistics:
Total number of files: 150
Total number of words: 75,000

Statistics by Category:
History:
  Files: 50
  Words: 25,000
Geography:
  Files: 30
  Words: 15,000
...
```

## 2. Date Search Tool (wiki_date_search.py)

**Purpose:** This tool allows you to search for articles within specific dates or date ranges in the world's timeline.

**Features:**
- Supports flexible date formats (YYYY, YYYY-MM, YYYY-MM-DD)
- Searches through date and date_range frontmatter fields

**How to Run:**
```
python wiki_date_search.py /path/to/wiki <start_date> [end_date]
```

**Example Usage:**
- Search for articles on a specific date:
  ```
  python wiki_date_search.py /path/to/wiki 1501-03-15
  ```
- Search for articles in a specific month:
  ```
  python wiki_date_search.py /path/to/wiki 1501-03
  ```
- Search for articles in a specific year:
  ```
  python wiki_date_search.py /path/to/wiki 1501
  ```
- Search for articles within a date range:
  ```
  python wiki_date_search.py /path/to/wiki 1501-03-15 1501-04-02
  ```
- Search for articles Before Bulwarks:
  ```
  python wiki_date_search.py /path/to/wiki -1501-03-15
  ```

**Example Output:**
```
Articles found between 1.1.21 BB and 30.12.21 BB:
- Ipso (1.1.532 BB to 30.12.365 AB)
  File: ..\wiki\people\Ipso.md
- Bartholomew Slater (1.1.41 BB to 30.12.29 AB)
  File: ..\wiki\people\Bartholomew-Slater.md
```

## Tips for Using the Tools

1. Always provide the correct path to your wiki directory when running the tools. You can use relative or absolute paths, as well as just subsections of the wiki.
2. Use the `--help` flag with any tool to see detailed usage instructions and examples.
3. The Date Search Tool uses a custom calendar system specific the world. Familiarize yourself with the AB/BB dating system.
4. When using date ranges, the start date should always be earlier than or equal to the end date.
5. These tools read the frontmatter of the markdown files, so ensure your articles are properly formatted with the required metadata.

By using these tools, you can efficiently manage and explore the vast content of our world-building project. They help maintain consistency in our world's timeline and provide valuable insights into the structure and content of the wiki.

More tools and features will be added in the future to enhance the wiki management experience. Stay tuned for updates and new releases!