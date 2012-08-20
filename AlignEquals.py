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

        # Determine highest/furthest = in the selection
        selections = self.view.sel()
        for selection in selections:
            max_len = 0
            for line in self.view.substr(selection).split('\n'):
                pre_len = self.get_len_before_equals(line);
                if  pre_len > max_len:
                    max_len = pre_len

            # Add necessary padding around =
            lines = ''
            for line in self.view.substr(selection).split('\n'):

                # Make sure there is actually an = in this line
                pre_len = self.get_len_before_equals(line);
                if pre_len != 0:
                    line = self.format_line(line, pre_len, max_len)
                lines += line + '\n';
            lines = lines[:-1]

            # replace selection with properly spaced
            self.view.replace(edit, selection, lines)

    def get_len_before_equals(self, line):
        return len(line[0:line.find('=')].rstrip())

    def format_line(self, line, pre_len, max_len):
        beginning = line[0:pre_len]
        equal_pos = line.find('=')
        end       = line[equal_pos+1:].lstrip() # skip over =
        line      = beginning + ' '*(max_len - len(beginning)) + ' = ' + end

        return line
