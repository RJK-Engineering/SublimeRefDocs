import sublime, sublime_plugin, webbrowser, re

class RefDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit, browser=""):
        if self.view.sel()[0].empty():
            self.view.run_command("select_quoted")

        region = self.view.substr(self.view.sel()[0])

        settings = sublime.load_settings('RefDocs.sublime-settings')

        url = ""
        for mapping in settings.get('mapping'):
            replace = mapping['replace']
            if replace:
                p = re.compile(replace[0])
                name = p.sub(replace[1], region)
            else:
                name = region

            p = re.compile(mapping['pattern'])
            if p.match(name):
                url = mapping['url'].format(name=name)
                break

        if not url:
            sublime.message_dialog("Invalid name:\n\n" + region if region else "Nothing selected")
            return

        if browser:
            webbrowser.get(browser + " %s").open_new_tab(url)
        else:
            webbrowser.open_new_tab(url)

    def description(self):
        return "Open reference docs"
