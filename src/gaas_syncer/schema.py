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
from marshmallow import Schema, fields

class ClientSchema(Schema):
    id = fields.UUID()
    gcode = fields.Str()
    name = fields.Str()
    acronym = fields.Str()

class VlanSchema(Schema):
    id = fields.UUID()
    core_id = fields.Int()
    number = fields.Int()
    subnet = fields.Str()
    gcode = fields.Str()
    purpose = fields.Str()
    name = fields.Str()
    description = fields.Str()