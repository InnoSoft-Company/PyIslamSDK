from . import __version__
import sys

def main():
  if "--version" in sys.argv: print(f"PyIslamSDK Version: {__version__}") 
