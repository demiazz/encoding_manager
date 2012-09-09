# coding: utf-8

import os.path
import re


EXTENSION_PATTERN = re.compile(r'^(.*)\.(?P<extension>\w+)$')
SYNTAX_PATTERN    = re.compile(r'^(?P<syntax>.*)\.tmLanguage$')


class AllowingMixin:
  """
  Bundle of useful methods for check allowing view for strategy.
  """

  def __init__(self, patterns):
    extension_patterns = patterns.get("extensions", {})
    filenames_patterns = patterns.get("filenames", {})
    syntaxes_patterns  = patterns.get("syntaxes", {})

    self.__included_extensions = extension_patterns.get("included", {})
    self.__excluded_extensions = extension_patterns.get("excluded", {})
    self.__included_filenames  = filenames_patterns.get("included", {})
    self.__excluded_filenames  = filenames_patterns.get("excluded", {})
    self.__included_syntaxes   = syntaxes_patterns.get("included", {})
    self.__excluded_syntaxes   = syntaxes_patterns.get("excluded", {})
    return

  def is_allowed(self, view):
    """
    Check view by patterns.
    """
    filename = view.file_name()
    syntax   = view.settings.get("syntax")

    if filename:
      return (self.__check_by_extension(filename)
                or
              self.__check_by_filename(filename)
                or
              self.__check_by_syntax(syntax)
             )
    else:
      return self.__check_by_syntax(syntax)

  # Matcher methods

  def __check_by_extension(self, filename):
    """
    Check allowing view by file extension.
    """
    extension = self.__extract_extension(filename)
    if extension:
      return ((extension in self.__included_extensions)
                and
              (extension not in self.__excluded_extensions))
    else:
      return False

  def __check_by_filename(self, filename):
    """
    Check allowing view by filename.
    """
    basename = os.path.basename(filename)
    return ((basename in self.__included_filenames)
              and
            (basename not in self.__excluded_filenames))

  def __check_by_syntax(self, filename):
    """
    Check allowing view by syntax.
    """
    syntax = self.__extract_syntax(syntax)
    return ((syntax in self.__included_syntaxes)
              and
            (syntax not in self.__excluded_syntaxes))

  # Extractors

  def __extract_extension(self, filename):
    """
    Extract file extension from filename.
    """
    match = EXTENSION_PATTERN.match(os.path.basename(filename))
    if match:
      return match.groupdict()["extension"]

  def __extract_syntax(self, syntax):
    """
    Extract syntax name from syntax filename.
    """
    match = SYNTAX_PATTERN.match(os.path.basename(syntax))
    if match:
      return match.groupdict()["syntax"]
