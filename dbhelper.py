#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Base, Music_Band, Album, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to database
engine = create_engine("postgresql://catalog:topsecret@localhost/catalogdb")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

Music_Bands = session.query(Music_Band).all()
for band in Music_Bands:
	print band.id
	print band.name
	print band.user_id

# Insert Bands
session.add(Music_Band(name='Linkin Park', user_id=1,))
session.commit()

session.add(Music_Band(name='Porcupine Tree', user_id=1,))
session.commit()

session.add(Music_Band(name='Breaking Benajamin', user_id=1,))
session.commit()

session.add(Music_Band(name='Alcest', user_id=1,))
session.commit()

session.add(Music_Band(name='Autumn for the crippled child', user_id=1,))
session.commit()

session.add(Music_Band(name='Steven Wilson', user_id=1,))
session.commit()

session.add(Music_Band(name='Bring me the Horizon', user_id=1,))
session.commit()

session.add(Music_Band(name='Les Discrets', user_id=1,))
session.commit()


# Adding albums for the bands

session.add(Album(name='Hybrid Theory', description="Hybrid Theory is the debut studio album by American rock band Linkin Park, released on October 24, 2000 through Warner Bros. Records. ", music_band_id=1, user_id=1))
session.commit()

session.add(Album(name='In Absentia', music_band_id=1, user_id=1, description="In Absentia is the seventh studio album by British progressive rock band Porcupine Tree, first released on 24 September 2002."))
session.commit()

session.add(Album(name='In Absentia', music_band_id=1, user_id=1, description="In Absentia is the seventh studio album by British progressive rock band Porcupine Tree, first released on 24 September 2002. The album marked several changes for the band"))
session.commit()

session.add(Album(name='Meteora', music_band_id=1, user_id=1, description="Meteora is the second studio album by American rock band Linkin Park. It was released on March 25, 2003 through Warner Bros."))
session.commit()

session.add(Album(name='Deadwing', music_band_id=2, user_id=1, description="Deadwing is the eighth studio album by British progressive rock band Porcupine Tree, released on 28 March 2005."))
session.commit()

session.add(Album(name='Phobia', music_band_id=3, user_id=1, description="Phobia is the third studio album by American rock band Breaking Benjamin. It was recorded at The Barbershop Studios in Hopatcong, New Jersey and released August 8, 2006"))
session.commit()

session.add(Album(name='New Bermuda', music_band_id=5, user_id=1, description="New Bermuda is the third studio album by American blackgaze band Deafheaven. It was released on October 2, 2015 through ANTI- record label."))
session.commit()

session.add(Album(name='To the Bone', music_band_id=6, user_id=1, description="To the Bone is the fifth studio album by English recording artist Steven Wilson, released on 18 August 2017 on Caroline International."))
session.commit()

session.add(Album(name="That's the Spirit", music_band_id=7, user_id=1, description="That's the Spirit is the fifth studio album by British rock band Bring Me the Horizon. The album was released on 11 September 2015,[1] and marks a departure from the group's metalcore roots"))
session.commit()

session.add(Album(name='The sorrow of september', music_band_id=8,user_id=1,description="As as french project, this was the first landmark album from the band"))
session.commit()






