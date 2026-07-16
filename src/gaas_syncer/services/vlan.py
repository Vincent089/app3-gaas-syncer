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

from corekit.execptions import NotFoundError
from corekit.logging import log_service_call

logger = logging.getLogger(__name__)


class VlanService:

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
