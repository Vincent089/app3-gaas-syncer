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
import sys

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from config import Config
from gaas_syncer.api import clients_v1, vlans_v1
from gaas_syncer.db import init_db
from corekit.flask import register_middleware
from corekit.logging import setup_logging

setup_logging(service_name=Config.SERVICE_NAME, log_level=Config.LOG_LEVEL)
init_db(url=Config.DB_URL)


def create_flask_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    register_middleware(app)

    # prevent viewing reverse proxy chain ips
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, )

    app.register_blueprint(clients_v1, url_prefix='/v1/gaas/clients')
    app.register_blueprint(vlans_v1, url_prefix='/v1/gaas/vlans')

    return app


def run_cron(command: str):
    logger = logging.getLogger(f'cron')

    logger.info('Starting cron', extra={ 'command': command })
    output = dict()

    if command == '<name of the cronjob>':
        pass
    else:
        logger.error('Unknown cron command', extra={ 'command': command })
        sys.exit(1)

    logger.info('Cron completed', extra={ 'command': command, **output })
    sys.exit()


app = create_flask_app()

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'cron':
        run_cron(sys.argv[2])
    else:
        app.run(host=Config.HOST, port=Config.PORT)
