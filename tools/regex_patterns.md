## Find Words Not in Links

Find all instances of a word that are not part of a link yet:

```
(?<![\[//])SomeWord
```

Searches for "SomeWord" without "[" or "/" before it, as would be the case in a link: 

```
[Aegolith](/wiki/objects/material/Aegolith.md)
```