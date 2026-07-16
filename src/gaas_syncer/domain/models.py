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
import uuid
from dataclasses import dataclass
from typing import Optional

from sqlalchemy import Integer, String, Text, UUID
from sqlalchemy.orm import Mapped, mapped_column

from gaas_syncer.adapters.db import Base

logger = logging.getLogger(__name__)


@dataclass
class Client(Base):
    """Gaas client entity to act as DTO"""

    gcode: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    acronym: Mapped[str] = mapped_column(String(255))

    __tablename__ = 'clients'


@dataclass
class Vlan(Base):
    """Gaas vlan entity to act as DTO"""

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True)
    core_id: Mapped[int] = mapped_column(Integer)
    number: Mapped[int] = mapped_column(Integer)
    subnet: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    gcode: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    purpose: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    name: Mapped[Optional[str]] = mapped_column(String(255), default=None)
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)

    __tablename__ = 'vlans'
