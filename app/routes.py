from flask import Blueprint, request, jsonify, render_template
from app.models import Cryptocurrency
from app import db
from sqlalchemy.exc import IntegrityError

crypto_bp = Blueprint('crypto', __name__)
main = Blueprint('main', __name__)

def crypto_to_dict(crypto):
    return {
        'id': crypto.id,
        'name': crypto.name,
        'symbol': crypto.symbol,
        'current_price': crypto.current_price,
        'percentage_change': crypto.percentage_change
    }

@crypto_bp.route('/cryptos', methods=['GET'])
def list_cryptos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    cryptos = Cryptocurrency.query.paginate(page=page, per_page=per_page)
    return jsonify({
        'data': [crypto_to_dict(c) for c in cryptos.items],
        'total': cryptos.total,
        'pages': cryptos.pages,
        'current_page': cryptos.page
    })

@crypto_bp.route('/cryptos/<string:symbol>', methods=['GET'])
def get_crypto(symbol):
    crypto = Cryptocurrency.query.filter_by(symbol=symbol).first()
    if not crypto:
        return jsonify({'error': 'Cryptocurrency not found'}), 404
    return jsonify(crypto_to_dict(crypto))

@crypto_bp.route('/cryptos', methods=['POST'])
def add_crypto():
    data = request.json
    try:
        crypto = Cryptocurrency(**data)
        db.session.add(crypto)
        db.session.commit()
        return jsonify(crypto_to_dict(crypto)), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cryptocurrency with this symbol already exists'}), 400

@crypto_bp.route('/cryptos/stats', methods=['GET'])
def crypto_stats():
    total_cryptos = Cryptocurrency.query.count()
    avg_price = db.session.query(db.func.avg(Cryptocurrency.current_price)).scalar()
    return jsonify({
        'total_cryptos': total_cryptos,
        'average_price': avg_price
    })

@main.route('/')
def home():
    return render_template('index.html')
