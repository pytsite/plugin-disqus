"""Pytsite Disqus Plugin.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_uwsgi():
    from pytsite import tpl, lang, router
    from plugins import comments, settings
    from . import _eh, _comments, _settings_form

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('disqus_admin_settings_url', lambda language, args: settings.form_url('disqus'))

    # Comments driver
    comments.register_driver(_comments.Driver())

    # Settings
    settings.define('disqus', _settings_form.Form, 'disqus@disqus', 'fa fa-comments', 'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
