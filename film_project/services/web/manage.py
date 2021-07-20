"""Module that allows to give flask app commands through command line interface"""

from flask.cli import FlaskGroup

from project import app
from project.models import User, Genre, Film, Director, FilmToGenre, db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """Command to create a database"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """Command to seed database with data"""
    usr1 = User("Oleg97", "pbf312*", True)  # admin
    usr2 = User("Alina555", "gw#11drp", False)
    usr3 = User("Max8000", "bweuhb$09", False)
    usr4 = User("Semen21", "yyslf888@", False)
    usr5 = User("Marina05", "passcode!", True)  # admin
    usr6 = User("Viktor29", "test444**", False)
    usr7 = User('Alex33', '##rot1', False)
    usr8 = User('Mariia209', 'tot_123', True)  # admin
    usr9 = User('Nikolai28', 'ehfu00&', False)
    usr10 = User('Dasha01', 'erj@w2', False)
    dir1 = Director('Joel', 'Coen')
    dir2 = Director('Robert', 'Zemeckis')
    dir3 = Director('David', 'Fincher')
    dir4 = Director('Hayao', 'Miyazaki')
    dir5 = Director('Todd', 'Phillips')
    dir6 = Director('Guy', 'Ritchie')
    dir7 = Director('Martin', 'Scorsese')
    gnr1 = Genre('Crime')
    gnr2 = Genre('Drama')
    gnr3 = Genre('Thriller')
    gnr4 = Genre('Comedy')
    gnr5 = Genre('Biography')
    gnr6 = Genre('Animation')
    gnr7 = Genre('Adventure')
    gnr8 = Genre('Family')
    gnr9 = Genre('Sport')
    gnr10 = Genre('Romance')
    gnr11 = Genre('Mystery')
    gnr12 = Genre('Action')
    flm1 = Film(
        user_id=2, name='Joker', release_date='2019-10-02', rating=8.4,
        poster_link='https://www.imdb.com/title/tt7286456/mediaviewer/rm3353122305/',
        description='In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. '
                    'He then embarks on a downward spiral of revolution and bloody crime. '
                    'This path brings him face-to-face with his alter-ego: the Joker.',
        director_id=5
    )
    flm2 = Film(
        user_id=4, name='Snatch', release_date='2000-08-23', rating=8.3,
        poster_link='https://www.imdb.com/title/tt0208092/mediaviewer/rm1248859904/',
        description='Unscrupulous boxing promoters, violent bookmakers, a Russian gangster, '
                    'incompetent amateur robbers and supposedly Jewish jewelers fight'
                    ' to track down a priceless stolen diamond.',
        director_id=6
    )
    flm3 = Film(
        user_id=8, name='The wolf of Wall Street', release_date='2013-02-06', rating=8.2,
        poster_link='https://www.imdb.com/title/tt0993846/mediaviewer/rm2842940160/',
        description='Based on the true story of Jordan Belfort, '
                    'from his rise to a wealthy stock-broker living the high life to his '
                    'fall involving crime, corruption and the federal government.',
        director_id=7
    )
    flm4 = Film(
        user_id=3, name='Spirited away', release_date='2001-07-20', rating=8.6,
        poster_link='https://www.imdb.com/title/tt0245429/mediaviewer/rm4207852801/',
        description='During her family''s move to the suburbs, '
                    'a sullen 10-year-old girl wanders into a world ruled by gods, '
                    'witches, and spirits, and where humans are changed into beasts.',
        director_id=4
    )
    flm5 = Film(
        user_id=4, name='Howls moving castle', release_date='2004-11-20', rating=8.6,
        poster_link='https://www.imdb.com/title/tt0347149/mediaviewer/rm2848505089/',
        description='When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance '
                    'of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions'
                    ' in his legged, walking castle.',
        director_id=4
    )
    flm6 = Film(
        user_id=6, name='The Big Lebowski', release_date='1998-03-06', rating=8.1,
        poster_link='https://www.imdb.com/title/tt0118715/mediaviewer/rm318364928/',
        description='Jeff "The Dude" Lebowski, mistaken for a millionaire of the same name, '
                    'seeks restitution for his ruined rug and enlists his bowling buddies to help get it.',
        director_id=1
    )
    flm7 = Film(
        user_id=1, name='Forrest Gump', release_date='1994-06-23', rating=8.8,
        poster_link='https://www.imdb.com/title/tt0109830/mediaviewer/rm1954748672/',
        description='The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and '
                    'other historical events unfold from the perspective of an Alabama man with an IQ of 75, '
                    'whose only desire is to be reunited with his childhood sweetheart.',
        director_id=2
    )
    flm8 = Film(
        user_id=10, name='Gone Girl', release_date='2014-09-26', rating=8.1,
        poster_link='https://www.imdb.com/title/tt2267998/mediaviewer/rm2766521344/',
        description='With his wife''s disappearance having become the focus of an intense media circus, '
                    'a man sees the spotlight turned on him when it''s suspected that he may not be innocent.',
        director_id=3
    )
    flm9 = Film(
        user_id=10, name='Fight Club', release_date='1999-10-15', rating=8.8,
        poster_link='https://www.imdb.com/title/tt0137523/mediaviewer/rm1412004864/',
        description='An insomniac office worker and a devil-may-care soap maker'
                    ' form an underground fight club that evolves into much more.',
        director_id=3
    )
    flm10 = Film(
        user_id=10, name='The Girl with the Dragon Tattoo', release_date='2011-12-12', rating=7.8,
        poster_link='https://www.imdb.com/title/tt1568346/mediaviewer/rm1878306816/',
        description='Journalist Mikael Blomkvist is aided in his search for a woman who'
                    ' has been missing for forty years by Lisbeth Salander, a young computer hacker.',
        director_id=3
    )
    flm11 = Film(
        user_id=4, name='Goodfellas', release_date='1990-09-12', rating=8.7,
        poster_link='https://www.imdb.com/title/tt0099685/mediaviewer/rm2091797760/',
        description='The story of Henry Hill and his life in the mob, covering his relationship '
                    'with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito '
                    'in the Italian-American crime syndicate.',
        director_id=7
    )
    flm12 = Film(
        user_id=5, name='Lock, Stock and Two Smoking Barrels', release_date='1998-08-28', rating=8.2,
        poster_link='https://www.imdb.com/title/tt0120735/mediaviewer/rm1138956032/',
        description='Eddy persuades his three pals to pool money for a vital poker game against a '
                    'powerful local mobster, Hatchet Harry. Eddy loses, after which Harry gives him'
                    ' a week to pay back 500,000 pounds.',
        director_id=6
    )
    flm13 = Film(
        user_id=6, name='Sherlock Holmes', release_date='2009-12-25', rating=7.6,
        poster_link='https://www.imdb.com/title/tt0988045/mediaviewer/rm4059794944/',
        description='Detective Sherlock Holmes and his stalwart partner Watson engage in'
                    ' a battle of wits and brawn with a nemesis whose plot is a threat to all of England.',
        director_id=6
    )
    fg1 = FilmToGenre(1, 1)
    fg2 = FilmToGenre(2, 1)
    fg3 = FilmToGenre(3, 1)
    fg4 = FilmToGenre(1, 2)
    fg5 = FilmToGenre(4, 2)
    fg6 = FilmToGenre(5, 3)
    fg7 = FilmToGenre(1, 3)
    fg8 = FilmToGenre(2, 3)
    fg9 = FilmToGenre(6, 4)
    fg10 = FilmToGenre(7, 4)
    fg11 = FilmToGenre(8, 4)
    fg12 = FilmToGenre(6, 5)
    fg13 = FilmToGenre(7, 5)
    fg14 = FilmToGenre(8, 5)
    fg15 = FilmToGenre(4, 6)
    fg16 = FilmToGenre(1, 6)
    fg17 = FilmToGenre(9, 6)
    fg18 = FilmToGenre(2, 7)
    fg19 = FilmToGenre(10, 7)
    fg20 = FilmToGenre(2, 8)
    fg21 = FilmToGenre(11, 8)
    fg22 = FilmToGenre(3, 8)
    fg23 = FilmToGenre(2, 9)
    fg24 = FilmToGenre(1, 10)
    fg25 = FilmToGenre(2, 10)
    fg26 = FilmToGenre(11, 10)
    fg27 = FilmToGenre(5, 11)
    fg28 = FilmToGenre(1, 11)
    fg29 = FilmToGenre(2, 11)
    fg30 = FilmToGenre(12, 12)
    fg31 = FilmToGenre(4, 12)
    fg32 = FilmToGenre(1, 12)
    fg33 = FilmToGenre(12, 13)
    fg34 = FilmToGenre(7, 13)
    fg35 = FilmToGenre(11, 13)
    db.session.add_all([])
    db.session.commit()


if __name__ == "__main__":
    cli()
