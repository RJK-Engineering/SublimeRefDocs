import sublime, sublime_plugin, webbrowser

class RefDocsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.sel()[0].empty():
            self.view.run_command("select_quoted")

        region = self.view.substr(self.view.sel()[0])
        region = region.replace("/", ".")

        if (region.startswith('icm.')):
            url = "SSCTJ4_5.3.2/com.ibm.casemgmt.development.doc/jsdoc/symbols/" + region + ".html"
        elif (region.startswith('ecm.')):
            url = "SSEUEX_3.0.1/com.ibm.developingeuc.doc/doc/JavaScriptdoc/symbols/" + region + ".html"
        else:
            sublime.message_dialog("Invalid name:\n\n" + region)

        if (url):
            webbrowser.open("https://www.ibm.com/support/knowledgecenter/" + url)

    def description(self):
        return "Open reference docs"
