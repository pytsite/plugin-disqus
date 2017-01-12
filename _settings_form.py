"""PytSite Disqus Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_short_name',
            weight=10,
            label=_lang.t('disqus@short_name'),
            required=True,
            help=_lang.t('disqus@short_name_setup_help'),
        ))

        self.add_widget(_widget.input.Text(
            uid='setting_secret_key',
            weight=20,
            label=_lang.t('disqus@secret_key'),
            required=True,
            help=_lang.t('disqus@secret_key_setup_help'),
        ))

        super()._on_setup_widgets()
