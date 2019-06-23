# encoding: utf-8

'''This adds a "slugify" command to be invoked by Sublime Text. It is made
available as "Slugify" in the command palette by Default.sublime-commands.
Parts of these commands are borrowed from the sublime-slug package:
https://github.com/madeingnecca/sublime-slug
'''

from __future__ import unicode_literals

import sublime
import sublime_plugin

# For this plugin to work on Windows, we need to include the path of the Sublime
# Text application itself to the import search path.
import os
import sys
sys.path.append(os.path.dirname(sys.executable))

try:
    # This import method works in Sublime Text 2.
    from slugify import slugify
except ImportError:
    # While this works in Sublime Text 3.
    from .slugify import slugify


class SlugifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        regions = self.view.sel()

        # Only run if there is a selection.
        if len(regions) > 1 or not regions[0].empty():

            separator = sublime.load_settings('Slugify.sublime-settings').get('slugify_separator', '-')

            for region in regions:
                text = self.view.substr(region)
                self.view.replace(edit, region, slugify(text, separator))
