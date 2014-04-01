# Slugify

Sublime Text 2 & 3 package that adds a command for converting the selected text to a slug.

Installation
------------
This package is available through [Package Control](https://sublime.wbond.net/), it’s called “Slugify”.

Usage
-----
Select a piece of text and run “Slugify” from the Command Palette. You can then enter what separator to use in the slug; the default is dash, and just pressing enter will use that. All characters will be converted to ASCII, removing any punctuation and such, and spaces converted to the previously entered separator.

Credits
-------
The [slugify function itself](http://flask.pocoo.org/snippets/5/) is by Armin Ronacher. The plugin part is based on [sublime-slug](https://github.com/madeingnecca/sublime-slug) by [Damiano Seno](https://github.com/madeingnecca).
