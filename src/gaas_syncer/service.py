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
import abc

from corekit.execptions import NotFoundError
from corekit.logging import log_service_call

logger = logging.getLogger(__name__)


class AbcService(abc.ABC):
    def __init__(self, uow_factory=None):
        if uow_factory is None:
            from gaas_syncer.uow import UnitOfWork
            uow_factory = UnitOfWork
        self._uow = uow_factory


class ClientService(AbcService):

    @log_service_call
    def list_clients(self):
        with self._uow() as uow:
            clients = uow.clients.list()

        logger.info('Listing clients', extra={ 'count': len(clients) })
        return clients

    @log_service_call
    def get_client(self, gcode):
        logger.info('Retrieving client', extra={ 'gcode': gcode })

        with self._uow() as uow:
            client = uow.clients.get(gcode)

            if client is None:
                raise NotFoundError(f'Client {gcode} not found')

        return client


class VlanService(AbcService):

    @log_service_call
    def list_vlans(self):
        with self._uow() as uow:
            vlans = uow.vlans.list()

        logger.info('Listing vlans', extra={ 'count': len(vlans) })
        return vlans

    @log_service_call
    def get_vlan(self, gcode):
        logger.info('Retrieving vlan', extra={ 'gcode': gcode })

        with self._uow() as uow:
            vlan = uow.vlans.get(gcode)

            if vlan is None:
                raise NotFoundError(f'VLAN {gcode} not found')

        return vlan
