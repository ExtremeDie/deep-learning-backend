from flask_restplus import Api
from .api import api as model

api = Api(
    title='Deep Learning Backend',
    version='1.0',
    description='Backend for Deep Learning',
)

api.add_namespace(model, path='/api')