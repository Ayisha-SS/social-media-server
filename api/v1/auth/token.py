# # backend/api/v1/auth/token.py
# from flask import request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)

# @app.route('/api/v1/auth/token/', methods=['POST'])
# def login_user():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']

#     # Query the database to retrieve the user
#     user = User.query.filter_by(username=username).first()

#     if user and check_password_hash(user.password, password):
#         # Generate an access token
#         access_token = create_access_token(identity=user.id)

#         return jsonify({'access_token': access_token}), 200
#     else:
#         return jsonify({'error': 'Invalid credentials'}), 401