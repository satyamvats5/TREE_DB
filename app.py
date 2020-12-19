import os
import sys
import getopt
from flask import Flask, request

from Controller import api
from Config import main as cfg
from Util.logger import Logger

sudo_logger = Logger()

def create_app():
    app = Flask(__name__)
    logger = sudo_logger.get_network_logger
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        logger.info('host: {0}, url: {1}, remote_addr: {2}, referrer: {3}, body: {4}, status: {5}'.format(
            request.headers['host'],
            request.url,
            request.remote_addr,
            request.referrer,
            request.get_data(),
            response.status_code
        ))
        return response

    api.init_app(app)
    return app

# Environment Variables CONFIG for APP 
hostEnv   = cfg.API_HOST
portEnv   = cfg.API_PORT
debugFlag = False
app = None
if __name__ == '__main__':
    logger = sudo_logger.get_application_logger
    if len(sys.argv) > 1:
        argList = sys.argv[1:]
        unixOpt = "h:p:d"
        gnuOpt  = [ "host=", "port=", "debug" ]
        try:
            arguments, values = getopt.getopt(argList, unixOpt, gnuOpt)
            for arg, value in arguments:
                if arg in ("-h", "--host"):
                    hostEnv = value.__str__()
                elif arg in ("-p", "--port"):
                    portEnv = int(value)
                elif arg in ("-d", "--debug"):
                    debugFlag = True

        except getopt.error as err:
            logger.critical(err.__str__(), exc_info=2)
            sys.exit(2)
    try:
        logger.info('App UP and running!')
        app = create_app().run(host=hostEnv, port=portEnv, debug=debugFlag)
    except Exception as err:
        logger.critical(err, exc_info=1)
        sys.exit(1)
    finally:
        pass
