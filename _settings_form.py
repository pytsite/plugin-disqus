"""PytSite Disqus Plugin Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang
from plugins import widget, settings


class Form(settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(widget.input.Text(
            uid='setting_short_name',
            weight=10,
            label=lang.t('disqus@short_name'),
            required=True,
            help=lang.t('disqus@short_name_setup_help'),
        ))

        self.add_widget(widget.input.Text(
            uid='setting_secret_key',
            weight=20,
            label=lang.t('disqus@secret_key'),
            required=True,
            help=lang.t('disqus@secret_key_setup_help'),
        ))

        super()._on_setup_widgets()
