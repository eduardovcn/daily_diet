from flask import Flask, request, jsonify
from datetime import datetime
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meals.db'

db.init_app(app)

@app.route("/meals", methods=["POST"])
def create_meal():
    data = request.get_json()
    
    if not data or 'name' not in data or 'description' not in data or 'date_time' not in data or 'in_diet' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_meal = Meal(
        name=data["name"],
        description=data["description"],
        date=datetime.strptime(data["date_time"], '%Y-%m-%d %H:%M'),
        in_diet=data["in_diet"]
    )
    db.session.add(new_meal)
    db.session.commit()
    return jsonify({"message": "Successful meal addition", "id": new_meal.id})

@app.route("/meals", methods=["GET"])
def get_meals():
    meals = Meal.query.all()
    return jsonify([meal.to_dict() for meal in meals])  # to_dict() utilizado aqui

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    return jsonify(meal.to_dict())  # to_dict() utilizado aqui

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    data = request.get_json()
    meal.name = data["name"]
    meal.description = data["description"]
    meal.date = datetime.strptime(data["date"], '%Y-%m-%d %H:%M')
    meal.in_diet = data["in_diet"]
    db.session.commit()
    return jsonify(meal.to_dict())  # to_dict() utilizado aqui para retornar a refeição atualizada

@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": "Meal deleted", "id": meal.id})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)












