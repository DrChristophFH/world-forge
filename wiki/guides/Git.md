---
category: guide
---

- [Working with Git](#working-with-git)
  - [Commit Messages](#commit-messages)
    - [Types and Sub-Types](#types-and-sub-types)
    - [Examples](#examples)


# Working with Git

If you're new to Git and GitHub and just want to contribute the next section is for you. Especially if you have never used Git or another version control system before. If you are already familiar with Git and GitHub, you can skip to the [Commit Messages](#commit-messages) section.

For all the others, follow me to the [✨Total Beginners Guide✨](/wiki/guides/Beginners.md) to get a step by step introduction to everything you need to know to contribute to the World Forge wiki!

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