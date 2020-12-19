from flask import request
from flask_restx import Namespace, Resource, reqparse, fields, marshal
from functools import wraps
from flask_restx import abort

from Util.logger import Logger
from DB.db import DataStore as DB

namespace = Namespace('insert', description='To Insert Data Into Node')

logger = Logger().get_application_logger

PARSE_VAL = reqparse.RequestParser()
PARSE_VAL.add_argument('country', type=str, required=True, default='IN',
                        help='Enter Country Code')
PARSE_VAL.add_argument('device', type=str, required=True, default='web',
                        help='Enter device name', choices=('web', 'tablet', 'mobile'))
PARSE_VAL.add_argument('webreq', type=int, required=False, default=0,
                        help='Enter the no of web requests by this device')
PARSE_VAL.add_argument('timespent', type=str, required=False,
                        help='Enter total time spent on this device', default=0)

@namespace.route('')
@namespace.response(201, 'CREATED')
@namespace.response(400, 'BAD REQUEST')
class InsertController(Resource):
    @namespace.doc(parser=PARSE_VAL)

    @namespace.doc(
        'Workflow',
        security='None',
        description='''
            <b>Insert Data into Tree

            This api is to insert data into tree

            REQUEST
            POST /insert

            body :- {}
            RESPONSE
                'OK CREATED'
        ''',
    )

    def post(self):
        try:
            args = PARSE_VAL.parse_args()
            country_code = args.get('country').strip().upper()
            device_name = args.get('device').strip()
            web_req = int(args.get('webreq'))
            timespent = int(args.get('timespent'))
            logger.info('Creating an entry in Tree DB having body => {}'.format(args))
            DB.update_country_stat(country_code, device_name, web_req, timespent)
            return 'OK CREATED', 200
        except Exception as err:
            logger.critical(err.__str__())
            abort(500)
