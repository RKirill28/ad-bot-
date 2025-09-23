from db.models import Ad
from db.schemas import AdData

from repositories.base import BaseRepository


class AdRepo(BaseRepository[Ad, AdData]): 
    # NOTE: Here will special methods for AdRepo
    model = Ad

