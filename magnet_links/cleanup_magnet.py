# coding: utf-8

import appex
from cleanup_url import cleanup_url


def getUrl():
    if not appex.is_running_extension():
        raise RuntimeError(
            'This script is intended to be run from the sharing extension.')
    url = appex.get_text()
    if not url:
        raise TypeError('No input URL found.')

    return url


def main():
    print(cleanup_url(getUrl()))

if __name__ == '__main__':
    main()
