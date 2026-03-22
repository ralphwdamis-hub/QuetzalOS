from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milpa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèles
class Vendeur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    nom_nahuatl = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    description = db.Column(db.Text)
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_fr = db.Column(db.String(200), nullable=False)
    nom_nah = db.Column(db.String(200))
    description_fr = db.Column(db.Text)
    description_nah = db.Column(db.Text)
    prix = db.Column(db.Float, nullable=False)
    categorie = db.Column(db.String(100))
    vendeur_id = db.Column(db.Integer, db.ForeignKey('vendeur.id'))
    disponible = db.Column(db.Boolean, default=True)
    date_ajout = db.Column(db.DateTime, default=datetime.utcnow)

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'))
    quantite = db.Column(db.Integer, default=1)
    statut = db.Column(db.String(50), default='en_attente')
    date_commande = db.Column(db.DateTime, default=datetime.utcnow)

# Routes API
@app.route('/api/produits', methods=['GET'])
def get_produits():
    produits = Produit.query.filter_by(disponible=True).all()
    return jsonify([{
        'id': p.id,
        'nom_fr': p.nom_fr,
        'nom_nah': p.nom_nah,
        'description_fr': p.description_fr,
        'description_nah': p.description_nah,
        'prix': p.prix,
        'categorie': p.categorie
    } for p in produits])

@app.route('/api/produits/<int:id>', methods=['GET'])
def get_produit(id):
    p = Produit.query.get_or_404(id)
    return jsonify({
        'id': p.id,
        'nom_fr': p.nom_fr,
        'nom_nah': p.nom_nah,
        'description_fr': p.description_fr,
        'description_nah': p.description_nah,
        'prix': p.prix,
        'categorie': p.categorie
    })

@app.route('/api/vendeurs', methods=['GET'])
def get_vendeurs():
    vendeurs = Vendeur.query.all()
    return jsonify([{
        'id': v.id,
        'nom': v.nom,
        'nom_nahuatl': v.nom_nahuatl,
        'description': v.description
    } for v in vendeurs])

@app.route('/api/commande', methods=['POST'])
def passer_commande():
    data = request.json
    commande = Commande(
        produit_id=data['produit_id'],
        quantite=data.get('quantite', 1)
    )
    db.session.add(commande)
    db.session.commit()
    return jsonify({'message': 'Commande reçue', 'id': commande.id})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('Base de données Milpa Market créée')
    app.run(host='localhost', port=5000, debug=True)
