from app import create_app, db
from app.models import Cryptocurrency


app = create_app()


with app.app_context():
    db.create_all()

    if not Cryptocurrency.query.first():

        initial_data = [
            Cryptocurrency(name="Bitcoin", symbol="BTC", current_price=30000, percentage_change=2.5),
            Cryptocurrency(name="Ethereum", symbol="ETH", current_price=2000, percentage_change=1.8),
            Cryptocurrency(name="Cardano", symbol="ADA", current_price=0.35, percentage_change=-0.5),
            Cryptocurrency(name="Solana", symbol="SOL", current_price=25, percentage_change=3.2),
        ]
        db.session.bulk_save_objects(initial_data)
        db.session.commit()
        print("Base de datos inicializada con datos de ejemplo.")


if __name__ == '__main__':
    app.run(debug=True)