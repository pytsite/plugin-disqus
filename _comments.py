"""PytSite Disqus Comments Driver.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import requests
from typing import Iterable
from pytsite import reg, logger
from plugins import auth, comments
from ._widget import Comments as DisqusWidget


class Driver(comments.driver.Abstract):
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

    def get_widget(self, widget_uid: str, thread_uid: str) -> DisqusWidget:
        """Get comments widget.
        """
        return DisqusWidget(widget_uid, thread_uid=thread_uid)

    def get_comments_count(self, thread_uid: str) -> int:
        """Get comments count for particular thread.
        """
        short_name = reg.get('disqus.short_name')
        secret_key = reg.get('disqus.secret_key')

        if not short_name or not secret_key:
            return 0

        count = 0

        try:
            r = requests.get('https://disqus.com/api/3.0/forums/listThreads.json', {
                'api_secret': secret_key,
                'forum': short_name,
                'thread': 'ident:' + thread_uid,
                'limit': 1,
            }).json()

            if r['code'] == 0 and r['response']:
                count = r['response'][0]['posts']

        except Exception as e:
            logger.error(e)

        return count

    def create_comment(self, thread_uid: str, body: str, author: auth.model.AbstractUser,
                       status: str = 'published', parent_uid: str = None) -> comments.model.AbstractComment:
        """Create new comment.
        """
        raise NotImplementedError("Not implemented yet.")

    def get_comments(self, thread_uid: str, limit: int = 0, skip: int = 0) \
            -> Iterable[comments.model.AbstractComment]:
        raise NotImplementedError("Not implemented yet.")

    def get_comment(self, uid: str) -> comments.model.AbstractComment:
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

    def get_permissions(self, user: auth.model.AbstractUser = None) -> dict:
        """Get permissions definition for user.
        """
        return {'create': True}
