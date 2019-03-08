import sublime, sublime_plugin, webbrowser

class UnwrapCommand(sublime_plugin.TextCommand):

    def run(self, edit, at):
        # self.view.input(args)
        region = sublime.Region(0, self.view.size())
        # source = self.view.substr(region).encode('utf-8')
        text = self.view.substr(region)
        lines  = text.split('\n')
        newtext = ""
        for line in lines:
            if len(line) == at:
                newtext += line
            else:
                newtext += line + '\n'

        self.view.replace(edit, region, newtext)

    def description(self):
        return "Unwrap lines"
