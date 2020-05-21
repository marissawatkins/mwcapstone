
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

assistant_token = "Bearer {}".format(os.environ.get('ASSISTANT_JWT'))
director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
producer_token = "Bearer {}".format(os.environ.get('PRODUCER_JWT'))

class CastingTestCase(unittest.TestCase):
    # """This class represents the test case"""

    def setUp(self):
        # """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        # 'postgres://npugwmlqsehgdt:f404256bb4085249a9eb47ed884aba19cd28f3951b7c9e49799231ac27515811@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d745rtq4tte8gi'

        self.new_actor = {
            'name': 'Ariel Kirkpatrick',
            'age': 22,
            'gender': 'female'
        }

        self.new_movie = {
            'title': 'New Movie',
            'release_date': '2030-05-05'
        }        

        self.patch_actor = {
            'name':'Johnny Depp',
            'age': 200,
            'genger': 'Male'
        }

        self.patch_movie = {
            'title': 'back to the future',
            'release_date': '1985-07-04'
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

# ---- Test get actors ---- #
    # def test_get_actors_fail(self):
    #     res = self.client().get('/actors')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)

    def test_get_actors(self):
        res = self.client().get('/actors', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertTrue(data['actor'])
        self.assertTrue(len(data['actors']) >= 0)

# ---- Test get movies ---- #
    # def test_get_movies_fail(self):
    #     res = self.client().get('/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)

    def test_get_movies(self):
        res = self.client().get('/movies', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) >= 0)

# ---- Test create actors ---- #
    def test_create_actors(self):
        res = self.client().post('/actors/create', json=self.new_actor, headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']) == 1)

# ---- Test create movies ---- #
    def test_create_movies(self):
        res = self.client().post('/movies/create', json=self.new_movie, headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']) == 1)

# ---- Test update actors ---- #
    # def test_update_actors_fail(self):
    #     res = self.client().patch('/actors/2000', json=self.new_actor)
    #     self.assertEqual(res.status_code, 404)

    def test_update_actors(self):
        res = self.client().patch('/actors/patch/1', json=self.patch_actor, headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']) == 1)

# ---- Test update movies ---- #
    # def test_update_movies_fails(self):
    #     res = self.client().patch('/movies/2000', json=self.new_movie)
    #     self.assertEqual(res.status_code, 404)

    def test_update_movies(self):
        res = self.client().patch('/movies/patch/1', json=self.patch_movie, headers={"Authorization": (director_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data['movies']) == 1)

# ---- Test delete actors ---- #
    # def test_delete_actors_fail(self):
    #     res = self.client().delete('/actors/2000')
    #     self.assertEqual(res.status_code, 404)

    def test_delete_actors(self):
        res = self.client().delete('/actors/delete/2', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(actor, None)
        self.assertTrue(data['delete'])
        self.assertEqual(data['success'], True)

# ---- Test delete movies ---- #
    # def test_delete_movies_fail(self):
    #     res = self.client().delete('/movies/2000')
    #     self.assertEqual(res.status_code, 404)

    def test_delete_movies(self):
        res = self.client().delete('/movies/delete/2', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(movie, None)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

# ---- Error behavior tests ---- #
    # def test_401_get_actors (self):
    #     res = self.client().get('/actors')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])

    # def test_401_get_movies (self):
    #     res = self.client().get('/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])
    
    # def test_401_create_actors (self):
    #     res = self.client().post('/actors', json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])

    # def test_401_create_movies (self):
    #     res = self.client().post('/movies', json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertFalse(data['success'])

    # def test_404_update_actors (self):
    #     res = self.client().patch('/actors/1000', json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertFalse(data['success'])

    # def test_404_update_movies (self):
    #     res = self.client().patch('/movies/1000', json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertFalse(data['success'])
    
    # def test_404_delete_actors (self):
    #     res = self.client().delete('/actors/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertFalse(data['success'])
    
    # def test_404_delete_movies (self):
    #     res = self.client().delete('/movies/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertFalse(data['success'])

    if __name__ == "__main__":
        unittest.main()