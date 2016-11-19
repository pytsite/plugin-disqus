"""PytSite Disqus Plugin Widget.
"""
from pytsite import widget as _widget, html as _html, tpl as _tpl, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Comments(_widget.Abstract):
    """Disqus Comments Widget.
    """
    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, **kwargs)

        self._short_name = _settings.get('disqus.short_name')
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

    def get_html_em(self, **kwargs) -> _html.Element:
        """Render the widget.
        :param **kwargs:
        """
        return _html.Div(_tpl.render('disqus@widget', {'widget': self}), uid=self._uid)
