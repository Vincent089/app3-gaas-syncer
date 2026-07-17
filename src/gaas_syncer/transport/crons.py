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
from corekit.cron import CronRouter

syncer_crons = CronRouter()

# Define every task that should be handled by cronjob
# @cron_router.task(<cron_job_name>)
# def cron_job_name(<args and kwargs are allowed>):
#     <processed data> = <some service>.<some functions>(...)
#     return <processed data> or <meaning full output>
