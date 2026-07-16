#   -----------------------------------------------------------------------------
#  Copyright (c) 2026. Vincent Corriveau (vincent.corriveau89@gmail.com)
#
#  Licensed under the MIT License. You may obtain a copy of the License at
#  https://opensource.org/licenses/MIT
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  -----------------------------------------------------------------------------
from sqlalchemy import QueuePool, create_engine, event
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker

engine = None
SessionLocal = None


class Base(DeclarativeBase):
    def to_dict(self, include=None, exclude=None):
        mapper = inspect(self)

        data = { }

        for column in mapper.mapper.column_attrs:
            key = column.key

            if include and key not in include:
                continue

            if exclude and key in exclude:
                continue

            data[key] = getattr(self, key)

        return data


def _add_to_session_on_append(target, value, initiator):
    session = Session.object_session(target)
    if session is not None and value not in session:
        session.add(value)


def register_collection_listeners():
    from sqlalchemy import inspect as sa_inspect  # noqa

    for mapper in Base.registry.mappers:
        for rel in mapper.relationships:
            event.listen(
                    rel.class_attribute,
                    'append',
                    _add_to_session_on_append,
            )


def init_db(url: str, echo: bool = False):
    global engine, SessionLocal

    engine = create_engine(
            url,
            echo=echo,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_pre_ping=True,
            pool_recycle=1800
    )
    SessionLocal = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

    from gaas_syncer.domain import models  # noqa
    Base.metadata.create_all(bind=engine)
    register_collection_listeners()
