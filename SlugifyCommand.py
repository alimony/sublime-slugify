# encoding: utf-8

'''This adds a "slugify" command to be invoked by Sublime Text. It is made
available as "Slugify" in the command palette by Default.sublime-commands.
Parts of these commands are borrowed from the sublime-slug package:
https://github.com/madeingnecca/sublime-slug
'''

from __future__ import unicode_literals

import sublime
import sublime_plugin
try:
    # This import method works in Sublime Text 2.
    import slugify
except ImportError:
    # While this works in Sublime Text 3.
    from .slugify import slugify

class SlugifyCommand(sublime_plugin.TextCommand):
    separator = '-'

    def run(self, edit):
        def done(value):
            self.separator = value
            self.view.run_command('slug_replace', {'separator': self.separator})

        window = self.view.window()
        window.show_input_panel('Separator', self.separator, done, None, None)


class SlugifyReplaceCommand(sublime_plugin.TextCommand):

    def run(self, edit, separator):
        regions = self.view.sel()

        # Only run if there is a selection.
        if len(regions) > 1 or not regions[0].empty():
            for region in regions:
                text = self.view.substr(region)
                self.view.replace(edit, region, slugify(text, separator))
