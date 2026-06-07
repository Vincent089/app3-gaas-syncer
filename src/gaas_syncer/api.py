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
from uuid import UUID

from flask import Blueprint, request
from corekit.flask import success_response, bad_response

from gaas_syncer.schema import ClientSchema, VlanSchema
from gaas_syncer.service import ClientService, VlanService

logger = logging.getLogger(__name__)

clients_v1 = Blueprint('clients', __name__)
client_service = ClientService()
client_schema = ClientSchema()

vlans_v1 = Blueprint('vlans', __name__)
vlan_service = VlanService()
vlan_schema = VlanSchema()


@clients_v1.route('/', methods=['GET'])
def list_clients():
    clients = client_service.list_clients()
    return success_response(client_schema.dump(clients, many=True), 200)


@clients_v1.route('/<gcode>', methods=['GET'])
def get_client(gcode: str):
    client = client_service.get_client(gcode)
    return success_response(client_schema.dump(client), 200)


@vlans_v1.route('/', methods=['GET'])
def list_vlans():
    vlans = vlan_service.list_vlans()
    return success_response(vlan_schema.dump(vlans, many=True), 200)


@vlans_v1.route('/<uuid:vlan_id>', methods=['GET'])
def get_vlan(vlan_id: UUID):
    vlan = vlan_service.get_vlan(vlan_id)
    return success_response(vlan_schema.dump(vlan), 200)
