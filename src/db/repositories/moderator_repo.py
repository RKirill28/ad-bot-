from db.models import Moderator
from db.schemas import ModeratorData

from repositories.base import BaseRepository


class ModeratorRepo(BaseRepository[Moderator, ModeratorData]): 
    # NOTE: Here will special methods for ModeratorRepo(for example add_ad_for_moderate)
    model = Moderator
