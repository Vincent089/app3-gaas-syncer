#   -----------------------------------------------------------------------------
#  Copyright (c) 2026. Vincent Corriveau (vincent.corriveau89@gmail.com)
#
#  Licensed under the MIT License. You may obtain a copy of the License at
#  https://opensource.org/licenses/MIT
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  -----------------------------------------------------------------------------
import pytest
from sqlalchemy.orm import sessionmaker, scoped_session


def pytest_configure(config):
    from gaas_syncer.db import init_db
    init_db(url='sqlite:///:memory:', echo=False)


@pytest.fixture(scope='function')
def uow_session():
    import gaas_syncer.db as db_module

    connection = db_module.engine.connect()
    transaction = connection.begin()

    session = scoped_session(
            sessionmaker(bind=connection, expire_on_commit=False)
    )()

    db_module.SessionLocal = lambda: session

    yield session

    session.close()
    transaction.rollback()
    connection.close()
