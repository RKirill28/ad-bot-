from aiogram.fsm.state import StatesGroup, State


class AdminStates(StatesGroup):
    """Coстояния отвечающие за админку"""

    add_new_moder: State = State()
    delete_moder: State = State()
