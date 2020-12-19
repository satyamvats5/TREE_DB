from flask_restx import Api

from Controller.health import namespace as health_ns
from Controller.insert import namespace as insert_ns
from Controller.query import namespace as query_ns

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Api(title='G Games API', 
            version=1,
            description='TREE DB API',
            prefix='/api/v1',
            authorizations=authorizations,
            security='apikey'
        )

api.add_namespace(health_ns)
api.add_namespace(insert_ns)
api.add_namespace(query_ns)
