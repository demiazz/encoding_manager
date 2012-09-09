# coding: utf-8

import re


SHEBANG_REGEXP = re.compile(r'^#!.*$')


class DetectorMixin:
  """
  Bundle of usefull methods for detecting headers of the file.
  """

  def is_shebang_exists(self, view):
    """
    Detect existing of shebang header in editing file.
    """
    line = view.substr(view.full_line(0))

    return not not SHEBANG_REGEXP.match(line)
