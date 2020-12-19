from flask import request
from flask_restx import Namespace, Resource, reqparse, fields, marshal
from functools import wraps
import json
from flask_restx import abort

from Util.logger import Logger
from DB.db import DataStore as DB

namespace = Namespace('query', description='To Query Data from Tree')

logger = Logger().get_application_logger

PARSE_VAL = reqparse.RequestParser()
PARSE_VAL.add_argument('country', type=str, required=False,
                        help='For multiple email give comma separated value without space')
PARSE_VAL.add_argument('device', type=str, required=False,
                        help='For multiple email give comma separated value without space')

# MODEL = namespace.model('Model', {  
#     'country': fields.List(fields.String),
# })


@namespace.route('')
@namespace.response(200, 'SUCCESS')
@namespace.response(401, 'BAD INPUT')
class QueryController(Resource):
    @namespace.doc(parser=PARSE_VAL)
    # @namespace.model
    # @namespace.doc('get_request', model=MODEL)
    # @namespace.marshal_with(model)

    @namespace.doc(
        'Workflow',
        security='None',
        description='''
            <b>Query Data from Tree

            This api is to query data from tree

            REQUEST
            POST /query

            body :- {}
            RESPONSE
                'DATA'
        ''',
    )

    def get(self):
        try:
            args = PARSE_VAL.parse_args()
            countries = args['country'].split(',') if args['country'] else []
            countries = list(map(lambda x: x.strip().upper(), countries))
            logger.info('Fetching data from Tree DB having params => {}'.format(args))
            devices = args['device'].split(',') if args['device'] else []
            devices = list(map(lambda x: x.strip(), devices))
            return DB.get_stat(countries, devices), 200
        except Exception as err:
            logger.critical(err.__str__())
            abort(500)
