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
import sys

from corekit.cron import CronRunner
from corekit.flask import register_middleware
from corekit.logging import setup_logging
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

import config
from gaas_syncer.adapters.db import init_db
from gaas_syncer.transport.api import clients_v1, vlans_v1

setup_logging(service_name=config.SERVICE_NAME, log_level=config.LOG_LEVEL)
init_db(url=config.DB_URL)


def create_flask_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    register_middleware(app)

    # prevent viewing reverse proxy chain ips
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, )

    app.register_blueprint(clients_v1, url_prefix='/v1/gaas/clients')
    app.register_blueprint(vlans_v1, url_prefix='/v1/gaas/vlans')

    return app


def create_cron_runner():
    cron_runner = CronRunner()
    #cron_runner.include_router()

    return cron_runner


app = create_flask_app()
cron_runner = create_cron_runner()

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'cron':
        cron_runner.execute(sys.argv[2])
    else:
        app.run(host=config.HOST, port=config.PORT)
