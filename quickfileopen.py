import sublime
import sublime_plugin


class QuickFileOpenCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        files = settings.get('files')
        if type(files) == list:
            self.window.show_quick_panel(files, self.on_done)
        elif files is None:
            self.window.show_quick_panel(['Set the \'files\' setting to use QuickFileOpen'], None)
        else:
            sublime.error_message('The \'files\' setting must be a list')

    def on_done(self, selected):
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        files = settings.get('files')
        fileName = files[selected]
        self.window.open_file(fileName)
