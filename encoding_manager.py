# coding: utf-8

import sublime
import sublime_plugin


class EncodingManagerCommand(sublime_plugin.TextCommand):
  """
  Text command implementation for Encoding Manager plugin.
  """

  def __init__(self, *args, **kwargs):
    sublime_plugin.TextCommand(self, *args, **kwargs)


class EncodingManagerEventListener(sublime_plugin.EventListener):
  """
  Event listener implementation for Encoding Manager plugin.
  """

  def __init__(self, *args, **kwargs):
    sublime_plugin.EventListener.__init__(self, *args, **kwargs)
