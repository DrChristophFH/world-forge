---
category: guide
---

- [Writing Articles](#writing-articles)
  - [The right Place](#the-right-place)
  - [The right Name](#the-right-name)
  - [The right Content](#the-right-content)
  - [Frontmatter](#frontmatter)
  - [Category Hierarchy](#category-hierarchy)


# Writing Articles

Writing articles is the core activity of our wiki. Articles should be written in Markdown format. Markdown is a lightweight markup language with plain-text formatting syntax. It is easy to read and write and can be converted to HTML or other formats. For a quick reference on Markdown syntax, see [GitHub's Markdown guide](https://guides.github.com/features/mastering-markdown/).

## The right Place

Before writing a new article, make sure to check if the article already exists. This is best done by searching for what you want to write and looking in related articles. If it does exist, consider updating the existing article instead of creating a new one. If you are unsure about where to place your article, feel free to ask for help. 

Generally the structure of the wiki is very open, though there are a few rules:

- If there is a folder for grouping related articles under a topic that also has an article, that article should be at the same level as the folder. For example: `geography` has a folder `eides` for all articles of locations in Eides, but the article `Eides.md` should also be in the root of the `geography` folder like so: `geography/Eides.md`. This makes it straightforward to reference the main article of a topic. Where one can reference `geography/Eides.md` instead of `geography/eides/Eides.md`.

## The right Name

Article filenames should be capitalized and use hyphens to separate words. For example, an article about the "Arch-God Kingdom" should be named `Arch-God-Kingdom.md`. This makes it easier to reference articles in other articles and ensures consistency in naming. 

In contrast all folders should be lowercase and use hyphens to separate words. For example, a folder for the "Arch-God Kingdom" should be named `arch-god-kingdom`.

## The right Content

Writing an article can be hard, but there is a nice starting point for common article types. You can find templates for different article types in the `wiki/templates` folder. These templates are a good starting point for your article and can be copied and pasted into your new article file.

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

The categories in our wiki are organized in a hierarchy. This helps to structure the content and makes it easier to find related articles. Here is the current category hierarchy:

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

The list of categories is not exhaustive and can be extended as needed. You can propose new categories or subcategories if you think they would help organize the content better any time.