import unittest
from eve import Eve
from eve_mongoengine import EveMongoengine
import mongoengine

class Dummy(mongoengine.Document):
    foo = mongoengine.StringField()
    

class TestInitApp(unittest.TestCase):
    
    def test_init_app(self):
        ext = EveMongoengine()
        ext.add_model(Dummy)
        self.assertEqual(ext.models, {})
        app = Eve(settings={
            'MONGO_HOST': 'localhost',
            'MONGO_PORT': 27017,
            'MONGO_DBNAME': 'eve_mongoengine_test',
            'DOMAIN': {}
        })
        ext.init_app(app)
        self.assertEqual(ext.models, {'dummy': Dummy})
        
        
if __name__ == "__main__":
    unittest.main()