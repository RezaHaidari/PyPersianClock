#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bidi.algorithm import get_display
import arabic_reshaper
import time
from kivy.app import App 
from kivy.core.text import LabelBase
from kivy.core.window import Window 
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout




class ClockLayout(BoxLayout):
	time_prop = ObjectProperty(None)

class ClockApp(App):
	sw_started = False
	sw_seconds = 0
	

	def start_stop(self):
		self.root.ids.start_stop.text = (self.reshaper(u'شروع')
			if self.sw_started else self.reshaper(u'ایست'))
		self.sw_started = not self.sw_started

			
	def reset(self):
		if self.sw_started:
			self.root.ids.start_stop.text = self.reshaper(u'شروع')
			self.sw_started = False
		self.sw_seconds = 0
		self.root.ids.stopwatch.text = (
			'%02d:%02d.[size=40] %02d [/size]' %
			(00,00, 
			00))


	def update(self, nap):
		if self.sw_started:

			self.sw_seconds += nap
			minutes, seconds = divmod(self.sw_seconds, 60)
			self.root.ids.stopwatch.text = (
			'%02d:%02d.[size=40] %2d [/size]' %
			(int(minutes),int(seconds), 
			int(seconds*100%100)))



	def update_time(self, nap):
		self.root.time_prop.text = time.strftime('[color=#ff0000][b]%H[/b][/color]:%M:%S')
	def on_start(self):
		Clock.schedule_interval(self.update_time, 1)
		Clock.schedule_interval(self.update, 0)
		self.root.ids.start_stop.text = self.reshaper(u'شروع')
		self.root.ids.reset.text = self.reshaper(u'رستارت')



	def reshaper(self, text):
		reshaped_text = arabic_reshaper.reshape(text)
		return get_display(reshaped_text)
	








if __name__ == '__main__':

	Window.clearcolor = get_color_from_hex('#101216')
	LabelBase.register(name='Roboto',
	fn_regular='Far_Nazanin.ttf',
	fn_bold='Far_Nazanin.ttf')
	ClockApp().run()
