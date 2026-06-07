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
import uuid
from typing import Optional
from sqlalchemy.orm import Session
from gaas_syncer.models import Client, Vlan


class ClientRepository:

    def __init__(self, session: Session):
        self.session = session

    def add(self, client: Client):
        self.session.add(client)

    def get(self, gcode: str) -> Optional[Client]:
        return self.session.query(Client).filter_by(gcode=gcode).first()

    def list(self) -> list[type[Client]]:
        return self.session.query(Client).all()

    def delete(self, client: Client):
        self.session.delete(client)


class VlanRepository:

    def __init__(self, session: Session):
        self.session = session

    def add(self, vlan: Vlan):
        self.session.add(vlan)

    def get(self, vlan_id: uuid.UUID) -> Optional[Vlan]:
        return self.session.query(Vlan).filter_by(id=vlan_id).first()

    def list(self) -> list[type[Vlan]]:
        return self.session.query(Vlan).all()

    def delete(self, vlan: Vlan):
        self.session.delete(vlan)
