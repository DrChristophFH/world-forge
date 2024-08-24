---
category: guide
---

# Guide

## Wiki

### Working with Git

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

### Writing Articles

When writing articles for the wiki:

1. Place each file in the correct folder. If a suitable folder doesn't exist, create one.
2. Ensure that each new article is referenced by at least one other note. This makes the new article visible and accessible within the wiki structure.
3. Use meaningful file names that reflect the content of the article.

### Frontmatter

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

### Category Hierarchy

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