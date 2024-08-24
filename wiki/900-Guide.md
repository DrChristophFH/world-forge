---
category: guide
---

# Guide

## Working with Git

Git is a distributed version control system that helps track changes in source code during software development. GitHub is a web-based platform that uses Git for version control and collaboration. To get started with Git and GitHub, we recommend the following resources:

- [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Git - the simple guide](https://rogerdudler.github.io/git-guide/)

For contributing to this project, we primarily use forks and pull requests (PRs). Here's a basic workflow:

1. Fork the main repository to your GitHub account.
2. Clone your fork to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them to your branch.
5. Push your branch to your fork on GitHub.
6. Open a pull request from your branch to the main repository.

For a more detailed guide on forking and creating pull requests, see [GitHub's guide on forking projects](https://guides.github.com/activities/forking/).

## Writing Articles

Writing articles is the core activity of our wiki. Articles should be written in Markdown format. Markdown is a lightweight markup language with plain-text formatting syntax. It is easy to read and write and can be converted to HTML or other formats. For a quick reference on Markdown syntax, see [GitHub's Markdown guide](https://guides.github.com/features/mastering-markdown/).

### The right Place

Before writing a new article, make sure to check if the article already exists. This is best done by searching for what you want to write and looking in related articles. If it does exist, consider updating the existing article instead of creating a new one. If you are unsure about where to place your article, feel free to ask for help. 

Generally the structure of the wiki is very open, though there are a few rules:

- If there is a folder for grouping related articles under a topic that also has an article, that article should be at the same level as the folder. For example: `geography` has a folder `eides` for all articles of locations in Eides, but the article `Eides.md` should also be in the root of the `geography` folder like so: `geography/Eides.md`. This makes it straightforward to reference the main article of a topic. Where one can reference `geography/Eides.md` instead of `geography/eides/Eides.md`.

### The right Name

Article filenames should be capitalized and use hyphens to separate words. For example, an article about the "Arch-God Kingdom" should be named `Arch-God-Kingdom.md`. This makes it easier to reference articles in other articles and ensures consistency in naming. 

In contrast all folders should be lowercase and use hyphens to separate words. For example, a folder for the "Arch-God Kingdom" should be named `arch-god-kingdom`.

## Frontmatter

Each note in our wiki requires a frontmatter section at the beginning of the file. The frontmatter is written in YAML and is enclosed between triple-dashes (`---`). Currently, we use the following frontmatter elements:

1. `category`: A string indicating the category the article belongs to. Multiple categories can be specified by comma-separating them. The available categories are listed below.
2. `date` or `date_range`: The date or date range relevant to the article content. This is optional and depends on the context of the article. Do not include dates if the article is not tied to a specific date or date range.

Here's an example of how to format the frontmatter:

```yaml
---
category: history
date: 1501-03-15
---
```

Or for a date range:

```yaml
---
category: event
date_range: 
  start: 1501-03-15
  end: 1501-04-02
---
```

Please note that dates should be formatted as YYYY-MM-DD. All dates should be in [AB (Age of Bulwarks) format](/wiki/history/Calendar.md#suffix). It is allowed to only specify the year or the year and month if the exact date is unknown. For dates before the construction of the Bulwarks, prefix the date with a minus sign (e.g., -632 AB).

Remember, consistent use of frontmatter helps in organizing and searching our wiki content effectively.

## Category Hierarchy

- index
- history
  - event
- magic
  - phenomenon
- geography
  - location
    - kingdom
- culture
  - law
  - language
- biography

## Available Tools

This section explains the tools available for managing and exploring the World Forge wiki. These tools help you organize, search, and analyze the content.

### 1. Wiki Statistics Tool (wiki_stats.py)

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

### 2. Date Search Tool (wiki_date_search.py)

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

### Tips for Using the Tools

1. Always provide the correct path to your wiki directory when running the tools. You can use relative or absolute paths, as well as just subsections of the wiki.
2. Use the `--help` flag with any tool to see detailed usage instructions and examples.
3. The Date Search Tool uses a custom calendar system specific the world. Familiarize yourself with the AB/BB dating system.
4. When using date ranges, the start date should always be earlier than or equal to the end date.
5. These tools read the frontmatter of the markdown files, so ensure your articles are properly formatted with the required metadata.

By using these tools, you can efficiently manage and explore the vast content of our world-building project. They help maintain consistency in our world's timeline and provide valuable insights into the structure and content of the wiki.

More tools and features will be added in the future to enhance the wiki management experience. Stay tuned for updates and new releases!