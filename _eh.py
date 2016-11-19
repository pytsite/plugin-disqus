"""Disqus Package Event Handlers.
"""
from pytsite import settings as _settings, auth as _auth, lang as _lang, router as _router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    if not _settings.get('disqus.pub_id'):
        if _auth.get_current_user().has_permission('disqus.settings.manage'):
            msg = _lang.t('disqus@plugin_setup_required_warning')
            if not _settings.get('disqus.short_name') or not _settings.get('disqus.secret_key'):
                _router.session().add_warning_message(msg)
            else:
                _router.session().get_warning_message(msg)
