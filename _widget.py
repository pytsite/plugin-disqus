"""PytSite Disqus Plugin Widget.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from pytsite import tpl, reg
from plugins import widget


class Comments(widget.Abstract):
    """Disqus Comments Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, **kwargs)

        self._short_name = reg.get('disqus.short_name')
        self._thread_uid = kwargs.get('thread_uid')

        self._css += ' widget-disqus'

    @property
    def short_name(self) -> str:
        """Get Disqus short name.
        """
        return self._short_name

    @property
    def thread_uid(self) -> str:
        """Get thread ID.
        """
        return self._thread_uid

    def _get_element(self, **kwargs) -> htmler.Element:
        """Render the widget.
        :param **kwargs:
        """
        return htmler.Div(tpl.render('disqus@widget', {'widget': self}), uid=self._uid)
