# Slugify

Sublime Text 2 & 3 package that adds a command for converting the selected text to a slug.

Installation
------------
This package is available through [Package Control](https://sublime.wbond.net/), it’s called “Slugify”.

Usage
-----
Select a piece of text and run “Slugify” from the Command Palette. You can then enter what separator to use in the slug; the default is dash, and just pressing enter will use that. All characters will be converted to ASCII, removing any punctuation and such, and spaces converted to the previously entered separator.

### Adding a key binding
To add a keyboard shortcut for the Slugify command, just bind the name “slugify” to keys of your choice. For example, this binds it to cmd-alt-y:

    [
        {
            "keys": ["super+alt+y"],
            "command": "slugify"
        }
    ]

For more information on key bindings, see the [Unofficial Sublime Text Documentation](http://docs.sublimetext.info/en/latest/reference/key_bindings.html).

Credits
-------
The [slugify function itself](http://flask.pocoo.org/snippets/5/) is by Armin Ronacher. The plugin part is based on [sublime-slug](https://github.com/madeingnecca/sublime-slug) by [Damiano Seno](https://github.com/madeingnecca).
