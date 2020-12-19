from flask import request
from flask_restx import Namespace, Resource
from functools import wraps

from Util.logger import Logger

namespace = Namespace('health', description='To Check Health')

logger = Logger().get_application_logger

@namespace.route('')
@namespace.response(200, 'Success')
class HealthController(Resource):
    ''' Check status of user Doc '''
    @namespace.doc(
        'Workflow',
        security='None',
        description='''

        <b>Get response of application liveliness status check </b><p>&nbsp;</p>

        This API is to check health status.

        REQUEST

        GET  /health 

        RESPONSE

            'OK'

        ''',
    )

    def get(self):
        return 'OK', 200
