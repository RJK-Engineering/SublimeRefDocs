import sublime, sublime_plugin, re

class ConvertIndentToFourCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        n = self.view.settings().get("tab_size")
        nNew = 4
        self._convert(edit, n, nNew)
        self.view.run_command('set_setting', {"setting": "tab_size", "value": nNew})

    def _convert(self, edit, nOld, nNew):
        if (nOld == nNew) : return

        region = sublime.Region(0, self.view.size())
        text = self.view.substr(region)
        newtext = ""

        for line in text.split('\n'):
            matchObj = re.match(r'\s+', line)
            if matchObj:
                indent = matchObj.group()
                l = len(indent)
                tabs = int(l / nOld)
                newIndent = " " * (tabs * nNew + (l - tabs * nOld))
                line = re.sub(r'^\s+', newIndent, line)

            newtext += line + "\n"

        self.view.replace(edit, region, newtext)

    def description(self):
        return "Convert number of spaces in indentation"
