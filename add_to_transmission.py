# coding: utf-8

import appex
from magnet_links.cleanup_url import cleanup_url
from transmission.transmission import Transmission


def getUrl():
    if not appex.is_running_extension():
        raise RuntimeError(
            'This script is intended to be run from the sharing extension.')
    url = appex.get_text()
    if not url:
        raise TypeError('No input URL found.')

    return url


def main():
  url = getUrl()
  clean_url = cleanup_url(url)
  print(clean_url)
  transmission = Transmission()
  result = transmission.Add(clean_url)
  print(result)

if __name__ == '__main__':
    main()
