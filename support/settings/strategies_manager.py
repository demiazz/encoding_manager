# coding: utf-8

import re

import sublime


DEFAULT_STRATEGIES_FILE = 'Encoding Manager Strategies - Default.sublime-settings'
USER_STRATEFIES_FILE    = 'Encoding Manager Strategies - User.sublime-settings'


class StrategiesManager:
  """
  Load and manage strategies for plugin.
  """

  def __init__(self):
    default = sublime.load_settings(DEFAULT_STRATEGIES_FILE)
    user    = sublime.load_settings(USER_STRATEGIES_FILE)

    self.formats = self.__extract_formats(default, user)
    return

  #----- Formats dealing

  def __extract_formats(self, default, user):
    """
    Extract default and user formats and compile them.
    """
    raw_formats = default.get("formats", {})
    raw_formats.update(user.get("formats", {}))

    formats = {}

    for name, pattern in raw_formats.iteritems():
      formats[name] = self.__compile_format(pattern)

    return formats

  def __compile_format(self, format):
    """
    Compile format to regexp.

    * escape regexp characters in string;
    * replace `$encoding$` substring to group;
    * compile regexp.
    """
    return re.compile(re.escape(format)
                        .replace("\$encoding\$", "(?P<encoding> [\w|\d|\-]+)"))
