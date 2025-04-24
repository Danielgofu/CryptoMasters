import unittest
from app import create_app, db
from app.models import Cryptocurrency

class CryptoRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            db.session.add(Cryptocurrency(name="Bitcoin", symbol="BTC", current_price=30000, percentage_change=2.5))
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_list_cryptos(self):
        response = self.client.get('/api/cryptos')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bitcoin', response.get_data(as_text=True))

    def test_get_crypto(self):
        response = self.client.get('/api/cryptos/BTC')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bitcoin', response.get_data(as_text=True))

    def test_add_crypto(self):
        response = self.client.post('/api/cryptos', json={
            'name': 'Ethereum',
            'symbol': 'ETH',
            'current_price': 2000,
            'percentage_change': 1.8
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Ethereum', response.get_data(as_text=True))