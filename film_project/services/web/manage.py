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
    dir8 = Director("Christopher", "Nolan")
    dir9 = Director("Li", "Chang")
    dir10 = Director("Jhon", "Black")
    dir11 = Director("Mane", "Aston")
    dir12 = Director("Anny", "Stone")
    dir13 = Director("Some", "Dude")
    dir14 = Director("Conrad", "Shield")
    dir15 = Director("Walter", "White")
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
    flm14 = Film(
        user_id=4, name='Mystery Cat', release_date='2016-11-03', rating=8.3,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.ru%2Fpin%2F376261743866615679%2F&'
                    'psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56'
                    'O6l8fECFQAAAAAdAAAAABAD',
        description=''
    )
    flm15 = Film(
        user_id=4, name='Super hero Cat', release_date='2017-04-12', rating=6.5,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F740419994988730339%2F&'
                    'psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56'
                    'O6l8fECFQAAAAAdAAAAABAO',
        description='Super hero cat saves the world'
    )
    flm16 = Film(
        user_id=4, name='Very Big Cat', release_date='2021-04-23', rating=7.5,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.adme.ru%2Fzhizn-zhivotnye%2F17-umoritelnyh-'
                    'dokazatelstv-togo-chto-kotiki-eto-zhidkost-2508881%2F&psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=16268'
                    '58372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56O6l8fECFQAAAAAdAAAAABAU',
        description='Adventures of very big cat', director_id=8
    )
    flm17 = Film(
        user_id=5, name='Kitty Cat', release_date='2013-06-15', rating=6.3,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fsvidok.online%2Fmy-ly-e-koty-ky-v-shapkah-y-z-s'
                    'obstvennoj-shersty%2F&psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe'
                    '&ved=0CAsQjRxqFwoTCJj56O6l8fECFQAAAAAdAAAAABAa',
        description='Kitty Cat Sam life&adventures', director_id=13
    )
    flm18 = Film(
        user_id=1, name='Mystery Things', release_date='2010-07-28', rating=5.4,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fngs.ru%2Ftext%2Ftags%2F%25D0%25BA%25D0%25BE%25D'
                    '1%2582%25D0%25B8%25D0%25BA%25D0%25B8%2F&psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&s'
                    'ource=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56O6l8fECFQAAAAAdAAAAABAg',
        description='Very mystery things in mystery place', director_id=13
    )
    flm19 = Film(
        user_id=1, name='Some Film', release_date='2009-12-03', rating=3.5,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ranak.me%2F2018%2F12%2F02%2Fzacem-nam-koti'
                    'ki%2F&psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqF'
                    'woTCJj56O6l8fECFQAAAAAdAAAAABAm',
        description='Description of film', director_id=13
    )
    flm20 = Film(
        user_id=1, name='Panda Po', release_date='2013-01-03', rating=3.5,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fria.ru%2F20170301%2F1488412994.html&psig=AOvVa'
                    'w2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56O6l8fEC'
                    'FQAAAAAdAAAAABAy',
        description='', director_id=9
    )
    flm21 = Film(
        user_id=1, name='Panda Po 2', release_date='2014-12-12', rating=6.2,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fkotiki.net%2Fstixi-pro-kotikov-anatolij-movshov'
                    'ich%2F&psig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqF'
                    'woTCJj56O6l8fECFQAAAAAdAAAAABAs',
        description="", director_id=9
    )
    flm22 = Film(
        user_id=1, name='Panda Po 3', release_date='2016-08-10', rating=7.1,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D4Z21-XXji5c&p'
                    'sig=AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJ'
                    'j56O6l8fECFQAAAAAdAAAAABA3',
        description="", director_id=9
    )
    flm23 = Film(
        user_id=1, name='Shooting Star', release_date='2019-03-30', rating=7.8,
        poster_link='https://www.google.com/url?sa=i&url=https%3A%2F%2F4lapy.ru%2Fnews%2Fkotiki-ishchut-dom%2F&psig='
                    'AOvVaw2fEOYCnu5fCHVUUw26AmSX&ust=1626858372823000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJj56O6'
                    'l8fECFQAAAAAdAAAAABA8',
        description=""
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
    fg36 = FilmToGenre(1, 15)
    fg37 = FilmToGenre(3, 15)
    fg38 = FilmToGenre(12, 15)
    fg39 = FilmToGenre(7, 17)
    fg40 = FilmToGenre(4, 17)
    fg41 = FilmToGenre(12, 20)
    db.session.add_all([usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8, usr9, usr10,
                        dir1, dir2, dir3, dir4, dir5, dir6, dir7, gnr1, gnr2, gnr3,
                        gnr4, gnr5, gnr6, gnr7, gnr8, gnr9, gnr10, gnr11, gnr12, flm1,
                        flm2, flm3, flm4, flm5, flm6, flm7, flm8, flm9, flm10, flm11,
                        flm12, flm13, fg1, fg2, fg3, fg4, fg5, fg6, fg7, fg8, fg9, fg10,
                        fg11, fg12, fg13, fg14, fg15, fg16, fg17, fg18, fg19, fg20, fg21,
                        fg22, fg23, fg24, fg25, fg26, fg27, fg28, fg29, fg30, fg31, fg32,
                        fg33, fg34, fg35, dir8, dir9, dir10, dir11, dir12, dir13, dir14, dir15,
                        flm14, flm15, flm16, flm17, flm18, flm19, flm20, flm21,
                        flm22, flm23, fg36, fg37, fg38, fg39, fg40, fg41])
    db.session.commit()


if __name__ == "__main__":
    cli()
