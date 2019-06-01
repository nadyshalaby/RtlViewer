import sublime
import sublime_plugin

class RrlViewer(sublime_plugin.TextCommand):
    def run(self, edit):
      	sel = self.view.sel()
      	region1 = sel[0]
      	ch = self.view.substr(region1)
      	if ('\u0600' <= ch <= '\u06FF' or '\u0750' <= ch <= '\u077F' or '\u08A0' <= ch <= '\u08FF' or '\uFB50' <= ch <= '\uFDFF' or '\uFE70' <= ch <= '\uFEFF' or '\U00010E60' <= ch <= '\U00010E7F' or '\U0001EE00' <= ch <= '\U0001EEFF'):
      		max_width= self.SETTINGS.get("window_max_width",1080)
          self.view.show_popup(ch, max_width)
