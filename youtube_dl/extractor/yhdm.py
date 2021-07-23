# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class YhdmIE(InfoExtractor):
    # https://docs.python.org/3/library/re.html#re.MatchObject.groupdict
    _VALID_URL = r'https?://(?:www\.)?yhdm\.so/v/(?P<id>[0-9\-]+)'
    _TEST = {
        'url': 'http://www.yhdm.so/v/5259-1.html',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '5259-1',
            'title': '完美世界 01集—在线播放—樱花动漫，视频高清在线观看',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<title>(.+?)</title>', webpage, 'title')
        content = self._html_search_regex(r'<div[^>]+data\-vid="([^"]+)"', webpage, 'url')
        if content.endswith('$mp4'):
            content = content.replace('$mp4', '')


        return {
            'id': 'yhdm-'+video_id,
            'title': title,
            'url': content,
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
