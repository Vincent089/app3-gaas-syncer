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
import logging
import gaas_syncer.adapters.db as db
from gaas_syncer.adapters.repository import ClientRepository, VlanRepository

logger = logging.getLogger(__name__)


class UnitOfWork:

    def __enter__(self):
        self.session = db.SessionLocal()

        self.clients = ClientRepository(self.session)
        self.vlans = VlanRepository(self.session)

        logger.debug("Starting transaction")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.rollback()
        else:
            self.commit()

    def commit(self):
        self.session.commit()
        logger.debug("Transaction committed")

    def rollback(self):
        self.session.rollback()
        logger.debug("Transaction rolled back")
