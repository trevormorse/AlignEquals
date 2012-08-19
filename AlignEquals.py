###############################################################################
# AlignEquals
#
# Plugin for Sublime Text 2 to align equals (=) of all lines in a selection.
#
# Created by Trevor Morse <trevor.morse@gmail.com>
###############################################################################
import sublime, sublime_plugin

class AlignEqualsCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Determine highest/furtherest = in the selection
        selections = self.view.sel()
        for selection in selections:
            max_equals = 0
            for line in self.view.substr(selection).split('\n'):
                if line.find('=') > max_equals:
                    max_equals = line.find('=')

            # Add necessary spaces before all =
            lines = ''
            for line in self.view.substr(selection).split('\n'):
                if (line.find('=') < max_equals) and line.find('=') != -1:
                    equal_pos = line.find('=')
                    beginning = line[0:equal_pos]
                    end       = line[equal_pos:]
                    line      = beginning + ' '*(max_equals - equal_pos) + end;
                lines += line + '\n';
            lines = lines[:-1]

            # replace selection with properly spaced
            self.view.replace(edit, selection, lines)

