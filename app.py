import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import json
from models import Actor, Movie, setup_db
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
    setup_db(app)
    CORS(app)

    # migrate = Migrate(app, db)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "hello"
        if excited == 'true': greeting = greeting + "!"
        return greeting

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response
    # setup_db(app)

    # ---- one GET Actors ---- #
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors():
        try:
            actors = Actor.query.order_by(Actor.created).all()
            formatted_actors = [actor.format() for actor in actors]
            selected_actors = paginate_response(request, formatted_actors)

            if len(selected_actors) == 0:
                abort(404)
            
            return jsonify({
                'success': True,
                'actors': paginated_selection(request, Actor.query.order_by(Actor.id).all())
            })
        except:
            abort(422)

    # --- second GET Movies --- #
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies():
        try:
            movies = Movie.query.order_by(Movie.created).all()
            formatted_movies = [movie.format() for movie in movies]
            selected_movies = paginate_response(request, formatted_movies)
            if len(selected_movies) == 0:
                abort(404)

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
        try:
            actors = Actor.query.filter(Actor.id == id_actor).one_or_none()
            if actors is None:
                abort(404)

            actors.delete()
            # db.session.commit()
            # db.session.close()
            return jsonify({
                'success': True,
                'message': "Delete success",
                'delete': id_actor,
                'total_actors': len(Actor.query.all())
            }), 200
        except:
            abort(422)

    @app.route('/movies/delete/<int:id_movies>', methods=["DELETE"])
    @requires_auth('delete:movies')
    def delete_movies(id_movies):
        try:
            movies = Movie.query.filter(Movie.id == id_movies).delete()
            if movies is None:
                abort(404)

            movies.delete()
            # db.session.commit()
            # db.session.close()
            return jsonify({
                'success': True,
                'message': "Delete success",
                'delete': id_movies,
                'total_movies': len(Movie.query.all())
            }), 200
        except:
            abort(422)

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

        try: 
            new_actor = Actor(name=new_name, age=new_age, gender=new_gender)
            new_actor.insert()

            return jsonify({
                'success': True,
                'created': new_actor.id,
                'actors': [Actor.query.get(new_actor.id).format()]
            }), 200
        except:
            abort(422)

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def new_movies():
        body = request.json
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        # if title in list(map(Movie.get_title, Movie.query.all())):
        #     abort(400, 'Title is oppupied')

        if any(arg in None for arg in [new_title, new_release_date]) or '' in [new_title, new_release_date]:
            abort(400, 'Must fill in required fields')

        new_movie = Movie(title=new_title, release_date=new_release_date)
        new_movie.insert()

        return jsonify({
            'success': True,
            'created': new_movie.id,
            'movies': [Movie.query.get(new_movie.id).format()]
        }), 200
    

    # --- PATCH Actors and Movies --- #
    @app.route('/actors/patch/<int:id_actor>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(id_actor):
        actor = Actor.query.filter(Actor.id == id_actor).one_or_none()

        if actor is None:
            abort(404)

        data = request.get_json()
        # body = request.json
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')

        try:
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.update()
        except:
            abort(422)
        actors = Actor.query.all()
        try:
            actors = [actor.format() for actor in actors]
            # if any(arg is None for arg in [name, age, gender]) or '' in [name, age, gender]:
            #     abort(400, 'm=Must fill in required fields')
            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except:
            abort(500)

    @app.route('/movies/patch/<int:id_movies>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(id_movies):
        movie = Movie.query.get(id_movies)

        if movie is None:
            abort(404)

        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        #
        try:
            movie = Movie.query.filter(Movie.id == id_movies).one_or_none()
            if movie is None:
                abort(404)
            if any(arg is None for arg in [new_title, new_release_date]) or '' in [new_title, new_release_date]:
                abort(400, 'm=Must fill in required fields')

            movie.title = new_title
            movie.release_date = new_release_date
            movie.update()

            return jsonify({
                'success': False,
                'movie': [Movie.query.get(id_movies).format()]
            }), 200
        except:
            abort(401)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unproccessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "unproccessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unathorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "unathorized"
        }), 401

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
    # port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=8080, debug=True)


