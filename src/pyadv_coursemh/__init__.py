"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-coursemh")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Your Name"
__email__ = "first.last@example.com"
