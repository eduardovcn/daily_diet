from app import app, db

with app.app_context():
    db.drop_all()  # Apagar todas as tabelas
    db.create_all()  # Criar todas as tabelas
    print("Banco de dados recriado com sucesso!")
