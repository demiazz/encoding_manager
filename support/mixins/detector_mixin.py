# coding: utf-8

import re


SHEBANG_PATTERN   = r'^#!.*$'
ENCODING_PATTERNS = []


class DetectorMixin:
  """
  Bundle of useful methods for detecting headers of the file.
  """

  def __init__(self, user_patterns = list()):
    self.__shebang_pattern   = re.compile(SHEBANG_PATTERN)
    self.__encoding_patterns = [re.compile(p)
                                  for p in ENCODING_PATTERNS + user_patterns]
    return

  def is_shebang_exists(self, view):
    """
    Detect existing of shebang header in editing file.
    """
    line = view.substr(view.full_line(0))
    return not not self.__shebang_pattern.match(line)

  def is_encoding_exists(self, view):
    """
    Detect existing of encoding declaration in editing file.
    """
    if self.is_shebang_exists(view):
      line = view.substr(view.full_line(1))
    else:
      line = view.substr(view.full_line(0))

    for pattern in self.__encoding_patterns:
      if pattern.match(line):
        return True
    return False
