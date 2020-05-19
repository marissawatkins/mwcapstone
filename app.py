import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import json
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth
from flask_migrate import Migrate

QUESTIONS_PER_PAGE = 10

def paginate_response(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_selection = [item.format() for item in selection]
    paginated_selection = formatted_selection[start:end]

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, resources={r"/api/": {"origins": "*"}})
    # setup_db(app)
    # CORS(app)

    # migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response
    setup_db(app)

    # ---- one GET Actors ---- #
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors():
        try:
            return jsonify({
                'success': True,
                'actors': paginated_selection(request, Actor.query.order_by(Actor.id).all())
            })
        except:
            abort(422)

    # --- second GET Movies --- #
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        try:
            return jsonify({
                'success': True,
                'movies': paginated_selection(request, Movie.query.order_by(Movie.id).all())
            })
        except:
            abort(422)

    # --- DELETE Actors and Movies --- #
    @app.route('/actors/delete/<int:id_actor>', methods=["DELETE"])
    @requires_auth('delete:actors')
    def delete_actors(id_actor):
        Actor.query.filter(Actor.id == id_actor).delete()
        db.session.commit()
        db.session.close()
        return jsonify({
            'success': True,
            'message': "Delete success"
        })

    @app.route('/movies/delete/<int:id_movies>', methods=["DELETE"])
    @requires_auth('delete:movies')
    def delete_movies(id_movies):
        Movie.query.filter(Movie.id == id_movies).delete()
        db.session.commit()
        db.session.close()
        return jsonify({
            'success': True,
            'message': "Delete success"
        })

    # --- POST actors and movies --- #
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors')
    def new_actors():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        if name in list(map(Actor.get_name, Actor.query.all())):
            abort(400, 'Name is occupied')

        if any(arg is None for arg in [name, age, gender]) or '' in [name, age, gender]:
            abort(400, 'Must fill in required fields')

        new_actor = Actor(name=name, age=age, gender=gender)
        new_actor.insert()

        return jsonify({
            'success': True,
            'actors': [Actor.query.get(new_actor.id).format()]
        })

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def new_movies():
        body = request.json
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        if title in list(map(Movie.get_title, Movie.query.all())):
            abort(400, 'Title is oppupied')

        if any(arg in None for arg in [title, release_date]) or '' in [title, release_date]:
            abort(400, 'Must fill in required fields')

        new_movie = Movie(title=title, release_date=release_date)
        new_movie.insert()

        return jsonify({
            'success': True,
            'movies': [Movie.query.get(new_movie.id).format()]
        })

    # --- PATCH Actors and Movies --- #
    @app.route('/actors/patch/<int:id_actor>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(id_actor):
        actor = Actor.query.get(id_actor)

        if actor is None:
            abort(404)

        body = request.json
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        if any(arg is None for arg in [name, age, gender]) or '' in [name, age, gender]:
            abort(400, 'm=Must fill in required fields')

        actor.name = name
        actor.age = age
        actor.gender = gender
        actor.update()

        return jsonify({
            'success': True,
            'actors': [Actor.query.get(id_actor).format()]
        })

    @app.route('/movies/patch/<int:id_movies>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(id_movies):
        movie = Movie.query.get(id_movies)

        if movie is None:
            abort(404)

        body = request.json
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
            abort(400, 'm=Must fill in required fields')

        movie.title = title
        movie.release_date = release_date
        movie.update()

        return jsonify({
            'success': False,
            'movies': [Movie.query.get(id_movies).format()]
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproccessable'
        })

    @app.errorhandler(AuthError)
    def auth_error(auth_error):
        return jsonify({
            'success': False,
            'error': auth_error.status_code,
            'message': auth_error.error['description']
        }), auth_error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=poart, debug=True)


