"""Module contains main unittest for api"""

import unittest
from base64 import b64encode

from project import app


class GetFilmsTestCases(unittest.TestCase):
    """Test cases for all possible GET requests to films"""
    def test_get_film_by_id(self):
        """Testing GET request film by id that is present in database
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/films/7")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_film_not_found_by_id(self):
        """Testing GET request film by id that is not present in database
        :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/films/105")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_search_all_films_by_name(self):
        """Testing GET request to partial search films by name or some part of name
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/films/The wolf")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_search_all_films_by_name_that_doesnt_exists(self):
        """Testing GET request to partial search films by name or some
        part of name that does not exist in database :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/films/The lonely soul")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_search_all_films_by_genre(self):
        """Testing GET request film by Genre that is not present in database
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/films/genres/Drama")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_search_all_films_by_genre_that_doesnt_exists(self):
        """Testing GET request film by Genre that is not present in database
        :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/films/genres/Science_Fiction")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_get_all_film_by_director_full_name(self):
        """Testing GET request film by it directors` name and surname present in database
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/films/director-film/", json={"director_name": "Guy", "director_surname": "Ritchie"})
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_all_film_by_director_id(self):
        """Testing GET request film by it directors` id present in database
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/films/director-film/5")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_all_film_by_director_full_name_that_doesnt_exist(self):
        """Testing GET request film by it directors` name and surname that is not present in database
        :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/films/director-film/",
                              json={"director_name": "Some", "director_surname": "Director"})
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_get_all_film_by_director_id_that_doesnt_exist(self):
        """Testing GET request film by it directors` id that is not present in database
        :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/films/director-film/99")
        status_code = response.status_code
        self.assertEqual(status_code, 404)


class PostDeleteFilmTestCase(unittest.TestCase):
    """Test cases responsible for POST request to add new film and film DELETE request"""
    def test_post_new_film_from_user(self):
        """Testing POST request to add new film
        :return 200"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Semen21:yyslf888@").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"name": "Mysterious Cat", "release_date": "2014-03-25", "rating": 9.1,
                "poster_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest."
                              "ru%2Fpin%2F376261743866615679%2F&psig=AOvVaw2wMx_9O2PeowbNxiJPLPx"
                              "W&ust=1626776694731000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKjv"
                              "49n17vECFQAAAAAdAAAAABAJ",
                "description": "Mystery things around mystery cat",
                "director_name": "Shane", "director_surname": "Carring", "genres": ["Comedy", "Mystery", "Action"]}
        response = tester.post("/api/film/", headers=headers, json=data)

        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_film_by_user(self):
        """Testing DELETE request to delete film by id
        :return 204"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Semen21:yyslf888@").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        response = tester.delete("/api/films/14", headers=headers)
        status_code = response.status_code
        self.assertEqual(status_code, 204)


class PutUserFilmTestCase(unittest.TestCase):
    """Test case PUT request from user who added film"""
    def test_put_change_info_about_film_by_user(self):
        """Testing changing some info about film by user who added it
        :return 200"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Semen21:yyslf888@").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"rating": 8.8}
        response = tester.put("/api/films/17", headers=headers, json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class PutAdminFilmTestCase(unittest.TestCase):
    """Test case PUT request from admin"""
    def test_put_change_info_about_film_by_admin(self):
        """Testing changing some info about film by admin
        :return 200"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Oleg97:pbf312*").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"name": "Panda Chang"}
        response = tester.put("/api/films/17", headers=headers, json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class PutUserThatDidntAddThisFilmTestCase(unittest.TestCase):
    """Test case PUT request from user who did not add film"""
    def test_put_change_info_about_film_by_user(self):
        """Testing changing some info about film by user who did not add it
        :return 403"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Viktor29:test444**").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"rating": 9.8}
        response = tester.put("/api/films/17", headers=headers, json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 403)


class PutIncorrectRatingFilmTestCase(unittest.TestCase):
    """Test case PUT request from user with incorrect data"""
    def test_put_incorrect_rating(self):
        """Testing PUT request with bad data
        :return 400"""

        tester = app.test_client(self)
        user_and_pass = b64encode(b"Oleg97:pbf312*").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"rating": 12.9}
        response = tester.put("/api/films/17", headers=headers, json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 400)


class UnauthorizedAccessFilmTestCase(unittest.TestCase):
    """Test case PUT request from unauthorized user"""
    def test_put_rating_unauthorized_access(self):
        """Testing PUT request from unauthorized user
        :return 401"""
        tester = app.test_client(self)
        data = {"rating": 12.9}
        response = tester.put("/api/films/17", json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 401)


class DirectorTestCase(unittest.TestCase):
    """Test cases associated with GET and POST request to director"""
    def test_get_director_by_id(self):
        """Testing GET request to director by id that present in database
        :return 200"""
        tester = app.test_client(self)
        response = tester.get("/api/directors/7")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_director_by_id_that_doesnt_exists(self):
        """Testing GET request to director by id that is not present in database
        :return 404"""
        tester = app.test_client(self)
        response = tester.get("/api/directors/104")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_post_director(self):
        """Testing POST request from authorized to director to create new director
        :return 200"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Viktor29:test444**").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        data = {"name": "Isaac", "surname": "Walter"}
        response = tester.post("/api/director/", headers=headers, json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class PostDirectorUnauthorizedUserTestCase(unittest.TestCase):
    """Test case to POST new director in the database"""
    def test_post_director_unauthorized(self):
        """Testing POST request from unauthorized to director to create new director
        :return 200"""
        tester = app.test_client(self)
        data = {"name": "Isaac", "surname": "Walter"}
        response = tester.post("/api/director/", json=data)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class DeleteDirectorAdminTestCase(unittest.TestCase):
    """Test case to DELETE director from admin"""
    def test_delete_director_by_id(self):
        """Testing DELETE director request from admin
        :return 204"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Oleg97:pbf312*").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        response = tester.delete("/api/directors/15", headers=headers)
        status_code = response.status_code
        self.assertEqual(status_code, 204)


class DeleteDirectorUserTestCase(unittest.TestCase):
    """Test case to DELETE director from user"""
    def test_delete_director_by_id_user(self):
        """Testing DELETE director request from user
        :return 403"""
        tester = app.test_client(self)
        user_and_pass = b64encode(b"Viktor29:test444**").decode("ascii")
        headers = {'Authorization': 'Basic %s' % user_and_pass}
        response = tester.delete("/api/directors/21", headers=headers)
        status_code = response.status_code
        self.assertEqual(status_code, 403)


class DeleteDirectorUnauthorizedUserTestCase(unittest.TestCase):
    """Test case to DELETE director from unauthorized user"""
    def test_delete_director_by_id_unauth_user(self):
        """Testing DELETE director request from unauthorized user
        :return 401"""
        tester = app.test_client(self)
        response = tester.delete("/api/directors/21")
        status_code = response.status_code
        self.assertEqual(status_code, 401)


if __name__ == "__main__":
    unittest.main()
