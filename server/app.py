from flask import Flask, request, make_response, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Review, Game

app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)


@app.route('/reviews')
def view_reviews():
    reviews = Review.query.all()
    return render_template('reviews.html', reviews=reviews)



@app.route('/game/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game_detail.html', game=game)

@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'GET':
        games = []
        for game in Game.query.all():
            game_dict = {
                "title": game.title,
                "genre": game.genre,
                "platform": game.platform,
                "price": game.price,
            }
            games.append(game_dict)
        response = make_response(games, 200)
        return response
    elif request.method == 'POST':
        data = request.json
        new_game = Game(
            title=data['title'],
            genre=data['genre'],
            platform=data['platform'],
            price=data['price']
        )
        db.session.add(new_game)
        db.session.commit()
        return make_response(new_game.to_dict(), 201)

@app.route('/games/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def game_by_id(id):
    game = Game.query.get_or_404(id)
    if request.method == 'GET':
        game_dict = game.to_dict()
        response = make_response(game_dict, 200)
        return response
    elif request.method == 'PUT':
        data = request.json
        game.title = data.get('title', game.title)
        game.genre = data.get('genre', game.genre)
        game.platform = data.get('platform', game.platform)
        game.price = data.get('price', game.price)
        db.session.commit()
        return make_response(game.to_dict(), 200)
    elif request.method == 'DELETE':
        db.session.delete(game)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Game deleted."
        }
        response = make_response(response_body, 200)
        return response

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'GET':
        reviews = []
        for review in Review.query.all():
            review_dict = review.to_dict()
            reviews.append(review_dict)
        response = make_response(reviews, 200)
        return response
    elif request.method == 'POST':
        data = request.json
        new_review = Review(
            score=data['score'],
            comment=data['comment'],
            game_id=data['game_id'],
            user_id=data['user_id']
        )
        db.session.add(new_review)
        db.session.commit()
        return make_response(new_review.to_dict(), 201)

@app.route('/reviews/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def review_by_id(id):
    review = Review.query.get_or_404(id)
    if request.method == 'GET':
        review_dict = review.to_dict()
        response = make_response(review_dict, 200)
        return response
    elif request.method == 'PUT':
        data = request.json
        review.score = data.get('score', review.score)
        review.comment = data.get('comment', review.comment)
        db.session.commit()
        return make_response(review.to_dict(), 200)
    elif request.method == 'DELETE':
        db.session.delete(review)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Review deleted."
        }
        response = make_response(response_body, 200)
        return response

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = []
        for user in User.query.all():
            user_dict = user.to_dict()
            users.append(user_dict)
        response = make_response(users, 200)
        return response
    elif request.method == 'POST':
        data = request.json
        new_user = User(name=data['name'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_by_id(id):
    user = User.query.get_or_404(id)
    if request.method == 'GET':
        user_dict = user.to_dict()
        response = make_response(user_dict, 200)
        return response
    elif request.method == 'PUT':
        data = request.json
        user.name = data.get('name', user.name)
        db.session.commit()
        return make_response(user.to_dict(), 200)
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "User deleted."
        }
        response = make_response(response_body, 200)
        return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
