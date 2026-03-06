from importlib.metadata import version
import os.path

try:
    __version__ = version("django-fields")
except importlib.metadata.PackageNotFoundError:
    __version__ = 'Please install this project with a supported installer'

VERSION = __version__
