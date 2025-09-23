from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import settings


engine: AsyncEngine = create_async_engine(
    url=str(settings.db_config.url),
    # echo=settings.db_config.echo,
    # echo_pool=settings.db_config.echo_pool,
)
session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)  # async_sessionmaker is class
