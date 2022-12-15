from .src import sdk as sdk
from .src import core as core
from .src import environments as environments

from .src import interfaces as interfaces
from .src import utilities as utilities

from .src.environments.session.data import items as items

events = core.events.EventSetCollection(**{
    **utilities.modules.get_content_from_module(getattr(environments.base.data,'events',[]), src.core.events.EventSet),
    **utilities.modules.get_content_from_module(getattr(environments.session.data,'events',[]), src.core.events.EventSet),
    **utilities.modules.get_content_from_module(getattr(environments.share.data,'events',[]), src.core.events.EventSet),
})