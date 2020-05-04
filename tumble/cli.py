"""
__main__.py
Manages the CLI portion of the program. Acts as the entrypoint for the program, and parses arguments into processes.
"""

import docopt

__doc__ = """Tumble.

Usage:
    tumble <blog_id>...
    tumble -h | --help
    tumble -v | --version

Options:
  -h --help     Show this screen.
  -v --version  Show the version.
"""


def main() -> None:
    """
    CLI entrypoint for the application.
    See setup.py for function reference.
    """
    args = docopt.docopt(__doc__)
    print(args)


if __name__ == "__main__":
    main()
