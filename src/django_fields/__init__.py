from importlib.metadata import version, PackageNotFoundError
import os.path

try:
    __version__ = version("django-fields")
except PackageNotFoundError:
    __version__ = 'Please install this project with a supported installer'

VERSION = __version__
