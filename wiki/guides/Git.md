---
category: guide
---

- [Working with Git](#working-with-git)
  - [Commit Messages](#commit-messages)
    - [Types and Sub-Types](#types-and-sub-types)
    - [Examples](#examples)


# Working with Git

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

## Commit Messages

When making changes, it's important to write clear and descriptive commit messages. For this reason, we follow a specific format for commit messages:

```
<type>:<sub-type> <description>
```

### Types and Sub-Types

- **Article**: For changes related to articles.
  - **Add**: For new articles.
  - **Update**: For updates to existing articles.
  - **Delete**: For deleting articles.
- **Formatting**: For fixing issues in articles.
  - **Typo**: For fixing typos.
  - **Links**: For fixing/adding links.
- **Meta**: For changes related to article metadata (e.g., frontmatter, categories).
- **Other**: For any other changes that don't fit into the above categories.

Sub-types are optional and can be omitted if not applicable. The description should be concise and clearly explain the changes made.

In detail descriptions can be added to the message by leaving a blank line after the first line and then writing the detailed description:

```
Article:New Free Lands

This article describes the Free Lands, a collection of independent 
territories that have agreed to open borders and free trade, while 
maintaining their individual sovereignty.
```

### Examples

```
Article:New Free Lands
```

Would be used for a new article about the Free Lands.

---

```
Article:Update Trading in the Free Lands
```

Would be used for updating the Free Lands article (and others) with information about trading.