# coding: utf-8

import os.path
import re


EXTENSION_PATTERN = r'^(.*)\.(?P<extension>\w+)$'
SYNTAX_PATTERN    = r'^(?P<syntax>.*)\.tmLanguage$'


class MatchMixin:
  """
  Bundle of useful methods for matching file for strategy.
  """

  def __init__(self, patterns):
    self.__extension_pattern  = re.compile(EXTENSION_PATTERN)
    self.__syntax_pattern     = re.compile(SYNTAX_PATTERN)

    self.__extension_patterns = patterns.get("extensions", [])
    self.__filename_patterns  = patterns.get("filenames", [])
    self.__syntax_patterns    = patterns.get("syntaxes", [])
    return

  def match(self, view):
    """
    Match view by patterns.
    """
    filename = view.file_name()
    syntax   = view.settings.get("syntax")

    if filename:
      return (self.__match_by_extension(filename)
                or
              self.__match_by_filename(filename)
                or
              self.__match_by_syntax(syntax)
             )
    else:
      return self.__match_by_syntax(syntax)

  def __match_by_extension(self, filename):
    """
    Match view by file extension.
    """
    extension = self.__extract_extension(filename)
    if extension:
      return extension in self.__extension_patterns
    else:
      return False

  def __match_by_filename(self, filename):
    """
    Match view filename.
    """
    return os.path.basename(filename) in self.__filename_patterns

  def __match_by_syntax(self, filename):
    """
    Match view by syntax.
    """
    return self.__extract_syntax(syntax) in self.__syntax_patterns

  def __extract_extension(self, filename):
    """
    Extract file extension from filename.
    """
    match = self.__extension_pattern.match(os.path.basename(filename))
    if match:
      return match.groupdict()["extension"]

  def __extract_syntax(self, syntax):
    """
    Extract syntax name from syntax filename.
    """
    match = self.__syntax_pattern.match(os.path.basename(syntax))
    if match:
      return match.groupdict()["syntax"]
