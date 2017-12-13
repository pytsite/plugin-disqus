"""Pytsite Disqus Plugin.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import tpl, lang, router
    from plugins import comments, permissions, settings
    from . import _eh, _comments, _settings_form

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('disqus_admin_settings_url', lambda language, args: settings.form_url('disqus'))

    # Comments driver
    comments.register_driver(_comments.Driver())

    # Permissions
    permissions.define_permission('disqus.settings.manage', 'disqus@manage_disqus_settings', 'app')

    # Settings
    settings.define('disqus', _settings_form.Form, 'disqus@disqus', 'fa fa-comments', 'disqus.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
