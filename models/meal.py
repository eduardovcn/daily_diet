from database import db

    
class Meal(db.Model):
        id = db.Column(db.Integer, primary_key=True) #chave primária 
        name = db.Column(db.String(100), nullable=False) #nullable =False significa que não pode ser nulo
        description = db.Column(db.String(250), nullable=False)
        date = db.Column(db.DateTime(), nullable=False)
        in_diet = db.Column(db.Boolean(), nullable=False)

        def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'date_time': self.date,
                'in_diet': self.in_diet
            }

