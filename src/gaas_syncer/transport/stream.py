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
from corekit.message_queue import StreamRouter, error_response, success_response

event_router = StreamRouter()

# Define events to listens to
# @event_router.event(<event_name>)
# def event_name(data: dict):
#    errors = <schema>.validate(data)
#    if errors:
#        return error_response('ValidationError', errors)
#
#     <processed data> = <some service>.<some functions>(...)
#
#    return success_response(<schema>.dump(<processed data>))
