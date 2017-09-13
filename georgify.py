import sublime
import sublime_plugin
import urllib.request
import json

class GeorgifyCommand(sublime_plugin.TextCommand):
	x = None
	def run(self, edit):
		outputPanel = self.view.window().create_output_panel('output')
		self.view.window().run_command('show_panel', { 'panel': 'output.output' })
		screenText = self.view.substr(sublime.Region(0, self.view.size())).encode('ascii')
		req = urllib.request.Request(url='https://www.student.cs.uwaterloo.ca/~se212/george/ask-george/cgi-bin/george.cgi/check', data=screenText)
		req.add_header('Content-Type', 'text/plain')
		response = urllib.request.urlopen(req).read()
		# if self.x == None or self.view.window().get_view_index(self.x)[1] == -1:
		# 	self.x = self.view.window().new_file()
		# else:
		# 	self.view.window().focus_view(self.x)
		# self.x.insert(edit, 0, response.decode())
		outputPanel.insert(edit, outputPanel.size(), response.decode())
