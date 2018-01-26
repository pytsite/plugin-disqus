"""PytSite Disqus Comments Driver.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import requests as _requests
from typing import Iterable as _Iterable
from pytsite import reg as _reg, logger as _logger
from plugins import auth as _auth, comments as _comments
from ._widget import Comments as _DisqusWidget


class Driver(_comments.driver.Abstract):
    """Disqus Comments Driver.
    """

    def get_name(self) -> str:
        """Get driver's name.
        """
        return 'disqus'

    def get_description(self) -> str:
        """Get driver's description.
        """
        return 'Disqus'

    def get_widget(self, widget_uid: str, thread_uid: str) -> _DisqusWidget:
        """Get comments widget.
        """
        return _DisqusWidget(widget_uid, thread_uid=thread_uid)

    def get_comments_count(self, thread_uid: str) -> int:
        """Get comments count for particular thread.
        """
        short_name = _reg.get('disqus.short_name')
        secret_key = _reg.get('disqus.secret_key')

        if not short_name or not secret_key:
            return 0

        count = 0

        try:
            r = _requests.get('https://disqus.com/api/3.0/forums/listThreads.json', {
                'api_secret': secret_key,
                'forum': short_name,
                'thread': 'ident:' + thread_uid,
                'limit': 1,
            }).json()

            if r['code'] == 0 and r['response']:
                count = r['response'][0]['posts']

        except Exception as e:
            _logger.error(e)

        return count

    def create_comment(self, thread_uid: str, body: str, author: _auth.model.AbstractUser,
                       status: str = 'published', parent_uid: str = None) -> _comments.model.AbstractComment:
        """Create new comment.
        """
        raise NotImplementedError("Not implemented yet.")

    def get_comments(self, thread_uid: str, limit: int = 0, skip: int = 0) \
            -> _Iterable[_comments.model.AbstractComment]:
        raise NotImplementedError("Not implemented yet.")

    def get_comment(self, uid: str) -> _comments.model.AbstractComment:
        """Get single comment by UID.
        """
        raise NotImplementedError("Not implemented yet.")

    def delete_comment(self, uid: str):
        """Mark comment as deleted.
        """
        raise NotImplementedError("Not implemented yet.")

    def delete_thread(self, thread_uid: str):
        """Physically remove comments for particular thread.
        """
        raise NotImplementedError("Not implemented yet.")

    def get_permissions(self, user: _auth.model.AbstractUser = None) -> dict:
        """Get permissions definition for user.
        """
        return {'create': True}
