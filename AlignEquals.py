import sublime, sublime_plugin

class AlignEqualsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        max_equals = 0
        selections = self.view.sel()
        for selection in selections:
            for line in self.view.substr(selection).split('\n'):
                if line.find('=') > max_equals:
                    max_equals = line.find('=')

        lines = ''
        for selection in selections:
            for line in self.view.substr(selection).split('\n'):
                if (line.find('=') < max_equals) and line.find('=') != -1:
                    equal_pos = line.find('=')
                    beginning = line[0:equal_pos]
                    end       = line[equal_pos:]
                    line      = beginning + ' '*(max_equals - equal_pos) + end;
                lines += line + '\n';
            lines = lines[:-1]
            self.view.replace(edit, selection, lines)

