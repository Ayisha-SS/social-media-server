# # backend/api/v1/auth/create.py
# from flask import request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)

# @app.route('/api/v1/auth/create/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     username = data['username']
#     email = data['email']
#     password = data['password']

#     # Hash the password
#     hashed_password = generate_password_hash(password)

#     # Create a new user
#     user = User(username=username, email=email, password=hashed_password)
#     db.session.add(user)
#     db.session.commit()

#     return jsonify({'message': 'User created successfully'}), 201