1) create some artists

    >>> from artists.models import Artist
    >>> a1=Artist(Stage_name="Amr",Social_link="https://www.instagram.com/drake/")
    >>> a1.save()
    >>> a2=Artist(Stage_name="Hamaki",Social_link="https://www.instagram.com/Hamaki/")
    >>> a2.save()
    >>> a3=Artist(Stage_name="Tamer",Social_link="https://www.instagram.com/Tamer/")
    >>> a3.save()
    >>> a4=Artist(Stage_name="Adele",Social_link="https://www.instagram.com/Adele/")
    >>> a4.save()
    >>> a5=Artist(Stage_name="z",Social_link="https://www.instagram.com/z/")
    >>> a5.save()

2) list down all artists

    >>> Artist.objects.all()

    <QuerySet [<Artist:  name: Amr Link: https://www.instagram.com/drake/>, <Artist:  name: Hamaki Link: https://www.instagram.com/Hamaki/>, <Artist:  name: Tamer Link: https://www.instagram.com/Tamer/>, <Artist:  name: Adele Link: https://www.instagram.com/Adele/>, <Artist:  name: z Link: https://www.instagram.com/z/>]>

3) list down all artists sorted by name

    >>> Artist.objects.all().order_by("Stage_name") 

    <QuerySet [<Artist:  name: Adele Link: https://www.instagram.com/Adele/>, <Artist:  name: Amr Link: https://www.instagram.com/drake/>, <Artist:  name: Hamaki Link: https://www.instagram.com/Hamaki/>, <Artist:  name: Tamer Link: https://www.instagram.com/Tamer/>, <Artist:  name: z Link: https://www.instagram.com/z/>]>

4) list down all artists whose name starts with `a`

    >>> Artist.objects.all().filter(Stage_name__startswith='a'
    ... )

    <QuerySet [<Artist:  name: Amr Link: https://www.instagram.com/drake/>, <Artist:  name: Adele Link: https://www.instagram.com/Adele/>]>

5) in 2 different ways, create some albums and assign them to any artists

    >>> from albums.models import Album
    >>> from datetime import datetime , timedelta

        -first way:

            >>> artist1=Artist.objects.get(pk=1)
            >>> album1=Album(name="ay7aga",creation_datetime=datetime.now(),release_datetime=datetime.now() + timedelta(days=5),cost=1.5,artist=artist1)
            >>> album1.save()
            >>> artist2=Artist.objects.get(pk=2) 
            >>> album2=Album(name="nothing",creation_datetime=datetime.now(),release_datetime=datetime.now() + timedelta(days=5),cost=15.50,artist=artist2)
            >>> album2.save()
            >>> album5=Album(name="name1",creation_datetime=datetime.now(),release_datetime=datetime(2022,10,30),cost=20.50,artist=artist2)    
            >>> album5.save()
            >>> album3=Album(name="no",creation_datetime=datetime.now(),release_datetime=datetime.now() + timedelta(days=5),cost=1500.50,artist=artist2)    
            >>> album3.save()
            >>> album4=Album(name="noname",creation_datetime=datetime.now(),release_datetime=datetime(2001,5,30),cost=2500.50,artist=artist2)            
            >>> album4.save()
            >>> album4=Album(name="hello world",creation_datetime=timezone.now(),release_datetime=timezone.now() - timedelta(days=5),cost=25.50,artist=artist2)     
            >>> album4.save()

            >>> Album.objects.all()

            <QuerySet [<Album:  name: ay7aga creation date and time: 10/10/2022, 15:05:01 release date and time: 10/10/2022, 15:05:01 cost: 1.50>, <Album:  name: nothing creation date and 
            time: 10/10/2022, 15:18:51 release date and time: 10/10/2022, 15:18:51 cost: 15.50>, <Album:  name: no creation date and time: 10/10/2022, 15:19:45 release date and time: 10/10/2022, 15:19:45 cost: 1500.50>, <Album:  name: hello creation date and time: 10/10/2022, 15:26:59 release date and time: 10/10/2022, 15:26:59 cost: 25.50>, <Album:  name: noname creation date and time: 10/10/2022, 15:30:56 release date and time: 10/10/2022, 15:30:56 cost: 2500.50>, <Album:  name: name1 creation date and time: 10/10/2022, 15:32:04 release date and time: 10/10/2022, 15:32:04 cost: 20.50>, <Album:  name: hello world creation date and time: 10/10/2022, 14:11:34 release date and time: 10/10/2022, 14:11:34 cost: 25.50>]>

        -Second way:

            >>> artist3=Artist.objects.get(pk=3) 
            >>> album4=artist3.album_set.create(name="hello",creation_datetime=datetime.now(),release_datetime=datetime.now() - timedelta(days=5),cost=25.50)

6) get the latest released album
    
    >>> Album.objects.all().order_by("release_datetime").reverse()[0]

    <Album:  name: name1 creation date and time: 10/10/2022, 15:32:04 release date and time: 10/10/2022, 15:32:04 cost: 20.50>

7) get all albums released before today

    >>> from django.utils import timezone
    >>> Album.objects.all().filter(release_datetime__lt=timezone.now())

    <QuerySet [<Album:  name: hello creation date and time: 10/10/2022, 15:26:59 release date and time: 10/10/2022, 15:26:59 cost: 25.50>, <Album:  name: noname creation date and time: 10/10/2022, 15:30:56 release date and time: 10/10/2022, 15:30:56 cost: 2500.50>, <Album:  name: hello world creation date and time: 10/10/2022, 14:11:34 release date and time: 10/10/2022, 14:11:34 cost: 25.50>]>

8) get all albums released today or before but not after today

    >>> Album.objects.all().filter(release_datetime__lte=timezone.now()) 

    <QuerySet [<Album:  name: hello creation date and time: 10/10/2022, 15:26:59 release date and time: 10/10/2022, 15:26:59 cost: 25.50>, <Album:  name: noname creation date and time: 10/10/2022, 15:30:56 release date and time: 10/10/2022, 15:30:56 cost: 2500.50>, <Album:  name: hello world creation date and time: 10/10/2022, 14:11:34 release date and time: 10/10/2022, 14:11:34 cost: 25.50>]>

9) count the total number of albums (hint: count in an optimized manner)

    >>> Album.objects.count()

    7

10) in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)

    - first way:

        >>> for i in range(Artist.objects.count()):Artist.objects.get(pk=i+1), Album.objects.all().filter(artist=(i+1)) 
        ... 

        (<Artist:  name: Amr Link: https://www.instagram.com/drake/>, <QuerySet [<Album:  name: ay7aga creation date and time: 10/10/2022, 15:05:01 release date and time: 10/10/2022, 15:05:01 cost: 1.50>]>)
        (<Artist:  name: Hamaki Link: https://www.instagram.com/Hamaki/>, <QuerySet [<Album:  name: nothing creation date and time: 10/10/2022, 15:18:51 release date and time: 10/10/2022, 15:18:51 cost: 15.50>, <Album:  name: no creation date and time: 10/10/2022, 15:19:45 release date and time: 10/10/2022, 15:19:45 cost: 1500.50>, <Album:  name: noname creation date and time: 10/10/2022, 15:30:56 release date and time: 10/10/2022, 15:30:56 cost: 2500.50>, <Album:  name: name1 creation date and time: 10/10/2022, 15:32:04 release date and time: 10/10/2022, 15:32:04 cost: 20.50>, <Album:  name: hello world creation date and time: 10/10/2022, 14:11:34 release date and time: 10/10/2022, 14:11:34 cost: 25.50>]>)
        (<Artist:  name: Tamer Link: https://www.instagram.com/Tamer/>, <QuerySet [<Album:  name: hello creation date and time: 10/10/2022, 15:26:59 release date and time: 10/10/2022, 
        15:26:59 cost: 25.50>]>)
        (<Artist:  name: Adele Link: https://www.instagram.com/Adele/>, <QuerySet []>)
        (<Artist:  name: z Link: https://www.instagram.com/z/>, <QuerySet []>)

    -second way:

        


11) list down all albums ordered by cost then by name (cost has the higher priority)

    >>> Album.objects.all().order_by("cost","name") 

    <QuerySet [<Album:  name: ay7aga creation date and time: 10/10/2022, 15:05:01 release date and time: 10/10/2022, 15:05:01 cost: 1.50>, <Album:  name: nothing creation date and 
    time: 10/10/2022, 15:18:51 release date and time: 10/10/2022, 15:18:51 cost: 15.50>, <Album:  name: name1 creation date and time: 10/10/2022, 15:32:04 release date and time: 10/10/2022, 15:32:04 cost: 20.50>, <Album:  name: hello creation date and time: 10/10/2022, 15:26:59 release date and time: 10/10/2022, 15:26:59 cost: 25.50>, <Album:  name: hello world creation date and time: 10/10/2022, 14:11:34 release date and time: 10/10/2022, 14:11:34 cost: 25.50>, <Album:  name: no creation date and time: 10/10/2022, 15:19:45 release date and time: 10/10/2022, 15:19:45 cost: 1500.50>, <Album:  name: noname creation date and time: 10/10/2022, 15:30:56 release date and time: 10/10/2022, 15:30:56 cost: 2500.50>]>


