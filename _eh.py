"""Disqus Package Event Handlers.
"""
from pytsite import lang as _lang, router as _router
from plugins import auth as _auth, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if not _settings.get('disqus.short_name') and _auth.get_current_user().has_permission('disqus.settings.manage'):
        _router.session().add_warning_message(_lang.t('disqus@plugin_setup_required_warning'))
