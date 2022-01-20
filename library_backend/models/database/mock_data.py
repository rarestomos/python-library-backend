from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.users_db_model import UsersDBModel

books = [BooksDBModel(name="A song of ice and fire", author="George R.R. Martin",
                      description="Some say it is better than the tv series",
                      cover="https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/A_Song_of_Ice_and_Fire_book_collection_box_set_cover.jpg/220px-A_Song_of_Ice_and_Fire_book_collection_box_set_cover.jpg"),
         BooksDBModel(name="Nightflyers", author="George R.R. Martin",
                      description="On a mission aboard the Nightflyer, the most advanced ship ever built, a team of scientists embark on an expedition to make first contact with alien life. Set in the year 2093, their mission takes them beyond the edge of the solar system, farther than mankind has ever gone before. But when terrifying and violent events start to occur, the team and crew begin to question themselves, each other, and their reclusive captain. They soon come to realize that the true horror isn't waiting for them in outer space -- it's already on their ship.",
                      cover="https://vignette.wikia.nocookie.net/nightflyers8841/images/6/60/Nightflyers_Book_Cover.jpg/revision/latest?cb=20181024125449"),
         BooksDBModel(name="Horus Heresy: Horus Rising", author="Dan Abnett",
                      description="It is the 31st millennium. Under the benevolent leadership of the Immortal Emperor, the Imperium of Man has stretched out across the galaxy. It is a golden age of discovery and conquest. But now, on the eve of victory, the Emperor leaves the front lines, entrusting the great crusade to his favourite son, Horus. Promoted to Warmaster, can the idealistic Horus carry out the Emperor's grand plan, or will this promotion sow the seeds of heresy amongst his brothers? Horus Rising is the first chapter in the epic tale of the Horus Heresy, a galactic civil war that threatened to bring about the extinction of humanity.",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/d/d0/Horusrising.jpg"),
         BooksDBModel(name="Horus Heresy: False Gods", author="Graham McNeil",
                      description="The Great Crusade that has taken humanity into the stars continues. The Emperor of mankind has handed the reins of command to his favoured son, the Warmaster Horus. Yet all is not well in the armies of the Imperium. Horus is still battling against the jealousy and resentment of his brother primarchs and, when he is injured in combat on the planet Davin, he must also battle his inner daemons. With all the temptations that Chaos has to offer, can the weakened Horus resist?",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/4/4c/False_Gods.jpg"),
         BooksDBModel(name="Horus Heresy: Galaxy In Flames", author="Ben Counter",
                      description="Having recovered from his grievous injuries, Warmaster Horus leads the triumphant Imperial forces against the rebel world of Isstvan III. Though the rebels are swiftly crushed, Horus's treachery is finally revealed when the planet is razed by virus bombs and Space Marines turn on their battle-brothers in the most bitter struggle imaginable.",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/thumb/8/84/Galaxy_in_Flames.jpg/330px-Galaxy_in_Flames.jpg"),
         BooksDBModel(name="Horus Heresy: The Flight of The Eisenstein", author="James Swallow",
                      description="Having witnessed the terrible massacre of Imperial forces on Isstvan III, Death Guard Captain Garro seizes a ship and sets a course for Terra to warn the Emperor of Horus's treachery. But when the fleeing Eisenstein is damaged by enemy fire, it becomes stranded in the warp — the realm of the Dark Powers. Can Garro and his men survive the depredations of Chaos and get his warning to the Emperor before Horus's plans reach fruition?",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/thumb/5/5b/Flight-eisenstein.jpg/330px-Flight-eisenstein.jpg"),
         BooksDBModel(name="Horus Heresy: Fulgrim", author="Graham McNeil",
                      description="Under the command of the newly appointed Warmaster Horus, the Great Crusade continues. Fulgrim, Primarch of the Emperor's Children, leads his warriors into battle against a vile alien foe, unaware of the darker forces that have already set their sights upon the Imperium of Man. Loyalties are tested, and every murderous whim indulged as the Emperor's Children take their first steps down the road to true corruption — a road that will ultimately lead them to the killing fields of Isstvan V...",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/thumb/e/ee/Fulgrimnovel.jpg/330px-Fulgrimnovel.jpg"),
         BooksDBModel(name="Horus Heresy: Descent of Angels", author="Mitchell Scanlon",
                      description="The planet of Caliban exists much as it has for thousands of years – the knightly orders protect the common people, fighting back the beasts that lurk in the depths of the seemingly endless forests. Young Zahariel and Nemiel aspire to join the greatest of the orders, led by the example of mighty Lion El'Jonson and his vision of a peaceful and unified world. But the coming of the Imperium brings new concerns and a new destiny for the Lion as part of the Great Crusade, and the sons of Caliban must decide if they will follow him to glory among the stars.",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/thumb/2/2b/Descentofangelscover.jpg/330px-Descentofangelscover.jpg"),
         BooksDBModel(name="Horus Heresy: Legion", author="Dan Abnett",
                      description="A Great War is coming, and it will engulf the Imperium of Man. The Space Marines of the Alpha Legion, the last and most secretive of all the Legiones Astartes brotherhoods, arrive on a heathen world to support the Imperial Army in a pacification campaign against strange and uncanny forces. But what drives the Alpha Legion? Can they be trusted, and what side will they choose when the Great War begins? Loyalties are put to the test, and the cunning schemes of an alien intelligence revealed.",
                      cover="https://wh40k.lexicanum.com/mediawiki/images/thumb/d/d7/Legion.JPG/330px-Legion.JPG"),
         BooksDBModel(name="Horus Heresy: Battle for the Abyss", author="Ben Counter"),
         BooksDBModel(name="Horus Heresy: Mechanicum", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Tales of Heresy ", author="Nick Kyme and Lindsey Preistley"),
         BooksDBModel(name="Horus Heresy: Fallen Angels", author="Mike Lee"),
         BooksDBModel(name="Horus Heresy: A Thousand Sons", author="Graham McNeil"),
         BooksDBModel(name="Horus Heresy: Nemesis", author="James Swallow"),
         BooksDBModel(name="Horus Heresy: The First Heretic", author="Aaron Dembski-Bowden"),
         BooksDBModel(name="Horus Heresy: Prospero Burns", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: Age Of Darkness", author="Christian Dunn"),
         BooksDBModel(name="Horus Heresy: The Outcast Dead", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: Deliverance Lost", author="Gav Thorpe"),
         BooksDBModel(name="Horus Heresy: Know No Fear", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: The Primarchs", author="Christian Dunn"),
         BooksDBModel(name="Horus Heresy: Fear To Tread", author="James Swallow"),
         BooksDBModel(name="Horus Heresy: Shadows Of Treachery",
                      author="Christian Dunn and Nick Kyme"),
         BooksDBModel(name="Horus Heresy: Angel Exterminatus", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: Betrayer", author="Aaron Dembski-Bowden"),
         BooksDBModel(name="Horus Heresy: Mark Of Calth", author="Laurie Goulding"),
         BooksDBModel(name="Horus Heresy: Vulkan Lives", author="Nick Kyme"),
         BooksDBModel(name="Horus Heresy: The Unremembered Empire", author="Dan Abnett"),
         BooksDBModel(name="Horus Heresy: Scars ", author="Chris Wraight"),
         BooksDBModel(name="Horus Heresy: Vengeful Spirit", author="Graham McNeill"),
         BooksDBModel(name="Horus Heresy: The Damnation of Pythos", author="David Annandale")]

users_dict = [
    {
        "email": "ut@ornareIn.co.uk",
        "first_name": "Merrill",
        "last_name": "Mcdonald"
    },
    {
        "email": "tellus.Nunc.lectus@habitantmorbitristique.com",
        "first_name": "Fritz",
        "last_name": "Watts"
    },
    {
        "email": "lorem.luctus.ut@sagittis.com",
        "first_name": "Madison",
        "last_name": "Singleton"
    },
    {
        "email": "Sed.molestie.Sed@duiFuscealiquam.edu",
        "first_name": "Stephanie",
        "last_name": "Salas"
    },
    {
        "email": "orci@Integervitaenibh.net",
        "first_name": "Ethan",
        "last_name": "Larson"
    },
    {
        "email": "erat@PhasellusornareFusce.org",
        "first_name": "Giacomo",
        "last_name": "Mason"
    },
    {
        "email": "eu@mollisnon.net",
        "first_name": "Erica",
        "last_name": "Foley"
    },
    {
        "email": "ultrices@Fuscemollis.edu",
        "first_name": "Len",
        "last_name": "Woodard"
    },
    {
        "email": "risus.quis@quamCurabiturvel.net",
        "first_name": "Preston",
        "last_name": "Norman"
    },
    {
        "email": "gravida.nunc@necquamCurabitur.com",
        "first_name": "Ross",
        "last_name": "Bright"
    },
    {
        "email": "sodales.Mauris.blandit@ipsum.org",
        "first_name": "Nash",
        "last_name": "Munoz"
    },
    {
        "email": "sit.amet@estac.net",
        "first_name": "Jack",
        "last_name": "Rice"
    },
    {
        "email": "Morbi.vehicula@nunc.org",
        "first_name": "Victor",
        "last_name": "Anthony"
    },
    {
        "email": "convallis.erat@necmalesuadaut.org",
        "first_name": "Halee",
        "last_name": "Witt"
    },
    {
        "email": "Vivamus.rhoncus.Donec@acmieleifend.edu",
        "first_name": "Lareina",
        "last_name": "Vang"
    },
    {
        "email": "Vestibulum.ante.ipsum@auctor.co.uk",
        "first_name": "Leslie",
        "last_name": "Galloway"
    },
    {
        "email": "pede.malesuada.vel@nunc.com",
        "first_name": "Jael",
        "last_name": "King"
    },
    {
        "email": "tincidunt.neque.vitae@elitCurabitur.net",
        "first_name": "Nehru",
        "last_name": "Mullins"
    },
    {
        "email": "et.ultrices.posuere@nonloremvitae.com",
        "first_name": "Magee",
        "last_name": "Boone"
    },
    {
        "email": "velit.eu.sem@aliquamadipiscinglacus.org",
        "first_name": "Anika",
        "last_name": "Lott"
    },
    {
        "email": "enim.Curabitur@mauris.net",
        "first_name": "Clarke",
        "last_name": "Atkins"
    },
    {
        "email": "mattis@lobortisquama.co.uk",
        "first_name": "Valentine",
        "last_name": "Sanders"
    },
    {
        "email": "non@tempus.ca",
        "first_name": "Amanda",
        "last_name": "Allen"
    },
    {
        "email": "accumsan.neque.et@Nullasempertellus.edu",
        "first_name": "Vance",
        "last_name": "Brooks"
    },
    {
        "email": "amet.risus@risusquisdiam.com",
        "first_name": "Chelsea",
        "last_name": "Stevenson"
    },
    {
        "email": "Duis.dignissim@estacmattis.net",
        "first_name": "Kamal",
        "last_name": "Jarvis"
    },
    {
        "email": "Sed@velit.org",
        "first_name": "May",
        "last_name": "Bradshaw"
    },
    {
        "email": "Phasellus@Nam.ca",
        "first_name": "Benedict",
        "last_name": "Fletcher"
    },
    {
        "email": "elit@sociisnatoquepenatibus.ca",
        "first_name": "Silas",
        "last_name": "Baker"
    },
    {
        "email": "lacus.Etiam@neque.edu",
        "first_name": "Davis",
        "last_name": "Pugh"
    },
    {
        "email": "orci.consectetuer@nibhdolornonummy.edu",
        "first_name": "Warren",
        "last_name": "Peck"
    },
    {
        "email": "massa.Integer.vitae@quislectusNullam.co.uk",
        "first_name": "Nathaniel",
        "last_name": "Carroll"
    },
    {
        "email": "arcu.Morbi@Quisqueimperdieterat.ca",
        "first_name": "Reuben",
        "last_name": "Huber"
    },
    {
        "email": "odio.Aliquam.vulputate@tortorIntegeraliquam.org",
        "first_name": "Judah",
        "last_name": "Thompson"
    },
    {
        "email": "dolor.dolor@vestibulummassa.ca",
        "first_name": "Nigel",
        "last_name": "Justice"
    },
    {
        "email": "non.lacinia.at@consectetuereuismodest.edu",
        "first_name": "Ryder",
        "last_name": "Jennings"
    },
    {
        "email": "amet@et.com",
        "first_name": "Iliana",
        "last_name": "Le"
    },
    {
        "email": "vitae.velit@Nuncquisarcu.com",
        "first_name": "Kenyon",
        "last_name": "Best"
    },
    {
        "email": "est@necenimNunc.co.uk",
        "first_name": "Grace",
        "last_name": "Raymond"
    },
    {
        "email": "bibendum.ullamcorper@Sedmalesuadaaugue.edu",
        "first_name": "Tara",
        "last_name": "Bradshaw"
    },
    {
        "email": "et.libero@adipiscingfringilla.ca",
        "first_name": "Reece",
        "last_name": "Hanson"
    },
    {
        "email": "Sed.eu@diamPellentesquehabitant.org",
        "first_name": "Rachel",
        "last_name": "Petersen"
    },
    {
        "email": "eget.ipsum@egestas.com",
        "first_name": "Zena",
        "last_name": "Thornton"
    },
    {
        "email": "eleifend@faucibus.com",
        "first_name": "Jaden",
        "last_name": "Bullock"
    },
    {
        "email": "at@utsemNulla.org",
        "first_name": "Jescie",
        "last_name": "Petersen"
    },
    {
        "email": "Fusce.fermentum.fermentum@pharetraNamac.net",
        "first_name": "Orla",
        "last_name": "Evans"
    },
    {
        "email": "eleifend.Cras.sed@eu.org",
        "first_name": "Derek",
        "last_name": "Ryan"
    },
    {
        "email": "Fusce.aliquet@ametconsectetuer.ca",
        "first_name": "Venus",
        "last_name": "Dorsey"
    },
    {
        "email": "odio.semper@orciconsectetuereuismod.ca",
        "first_name": "Kylan",
        "last_name": "Fowler"
    },
    {
        "email": "fermentum.vel.mauris@orciPhasellus.com",
        "first_name": "Lucas",
        "last_name": "Lane"
    },
    {
        "email": "fermentum@a.net",
        "first_name": "Keith",
        "last_name": "Sherman"
    },
    {
        "email": "dui@Maurismolestie.org",
        "first_name": "Abel",
        "last_name": "Dalton"
    },
    {
        "email": "Integer@Mauris.org",
        "first_name": "Quemby",
        "last_name": "Cunningham"
    },
    {
        "email": "Donec.nibh@nonleoVivamus.edu",
        "first_name": "Isadora",
        "last_name": "Graham"
    },
    {
        "email": "aliquam@rutrum.com",
        "first_name": "Nicholas",
        "last_name": "Nielsen"
    },
    {
        "email": "eu@pellentesquea.ca",
        "first_name": "Francis",
        "last_name": "Alvarado"
    },
    {
        "email": "sed@Duis.ca",
        "first_name": "Hillary",
        "last_name": "Mcclure"
    },
    {
        "email": "ornare.libero@fringilla.org",
        "first_name": "Andrew",
        "last_name": "Bean"
    },
    {
        "email": "ut.pellentesque@et.org",
        "first_name": "Colton",
        "last_name": "Matthews"
    },
    {
        "email": "eu.tellus.eu@sagittislobortismauris.edu",
        "first_name": "Shellie",
        "last_name": "Callahan"
    },
    {
        "email": "et.magna@nonante.net",
        "first_name": "Drake",
        "last_name": "Brooks"
    },
    {
        "email": "primis.in.faucibus@sagittis.ca",
        "first_name": "Kimberley",
        "last_name": "Good"
    },
    {
        "email": "adipiscing@luctus.edu",
        "first_name": "Margaret",
        "last_name": "Rutledge"
    },
    {
        "email": "Aliquam.ultrices@milorem.edu",
        "first_name": "Driscoll",
        "last_name": "Burks"
    },
    {
        "email": "id.libero@Vivamus.ca",
        "first_name": "Kato",
        "last_name": "Dixon"
    },
    {
        "email": "ac.arcu.Nunc@nascetur.ca",
        "first_name": "Jared",
        "last_name": "Valencia"
    },
    {
        "email": "est.Nunc@Sedauctorodio.com",
        "first_name": "Cole",
        "last_name": "Quinn"
    },
    {
        "email": "turpis.egestas.Aliquam@molestie.net",
        "first_name": "Adrian",
        "last_name": "Dotson"
    },
    {
        "email": "pede.malesuada.vel@SuspendisseeleifendCras.edu",
        "first_name": "Geoffrey",
        "last_name": "Gould"
    },
    {
        "email": "Nunc@ligulaeu.org",
        "first_name": "Nero",
        "last_name": "Stout"
    },
    {
        "email": "quis.diam@Sed.edu",
        "first_name": "Reuben",
        "last_name": "Velez"
    },
    {
        "email": "Aliquam@temporbibendumDonec.edu",
        "first_name": "Keaton",
        "last_name": "Contreras"
    },
    {
        "email": "ut.cursus@mus.ca",
        "first_name": "Leilani",
        "last_name": "Forbes"
    },
    {
        "email": "faucibus.orci.luctus@Loremipsumdolor.co.uk",
        "first_name": "Kyra",
        "last_name": "Hays"
    },
    {
        "email": "Nunc@vel.ca",
        "first_name": "Merrill",
        "last_name": "Hammond"
    },
    {
        "email": "sapien.gravida.non@sedorcilobortis.com",
        "first_name": "Farrah",
        "last_name": "Daniels"
    },
    {
        "email": "ante.iaculis@aliquamiaculis.co.uk",
        "first_name": "Bruce",
        "last_name": "Gardner"
    },
    {
        "email": "nascetur.ridiculus@non.org",
        "first_name": "Sybil",
        "last_name": "Trevino"
    },
    {
        "email": "Aenean.massa@blandit.co.uk",
        "first_name": "Priscilla",
        "last_name": "Conley"
    },
    {
        "email": "Fusce@metus.org",
        "first_name": "Leslie",
        "last_name": "Hansen"
    },
    {
        "email": "venenatis@venenatislacusEtiam.org",
        "first_name": "Hakeem",
        "last_name": "Everett"
    },
    {
        "email": "non@justonecante.com",
        "first_name": "Rylee",
        "last_name": "Mcleod"
    },
    {
        "email": "eu.arcu.Morbi@semper.edu",
        "first_name": "Oleg",
        "last_name": "Ferrell"
    },
    {
        "email": "semper.auctor.Mauris@lacusQuisqueimperdiet.edu",
        "first_name": "Abel",
        "last_name": "Villarreal"
    },
    {
        "email": "eu.neque.pellentesque@Integer.ca",
        "first_name": "Mohammad",
        "last_name": "Buckner"
    },
    {
        "email": "nascetur@tellusfaucibusleo.com",
        "first_name": "Moses",
        "last_name": "Simpson"
    },
    {
        "email": "ut.odio@arcuSed.co.uk",
        "first_name": "Ryan",
        "last_name": "Cortez"
    },
    {
        "email": "vestibulum.lorem.sit@NullamenimSed.edu",
        "first_name": "Colleen",
        "last_name": "Russo"
    },
    {
        "email": "volutpat@eget.net",
        "first_name": "Keegan",
        "last_name": "Lawrence"
    },
    {
        "email": "ad.litora@nulla.com",
        "first_name": "Neville",
        "last_name": "Leach"
    },
    {
        "email": "euismod@pretium.ca",
        "first_name": "Callie",
        "last_name": "Hess"
    },
    {
        "email": "semper.dui@malesuadaInteger.edu",
        "first_name": "Keith",
        "last_name": "Baldwin"
    },
    {
        "email": "at.pede.Cras@dictum.co.uk",
        "first_name": "Ciara",
        "last_name": "Cunningham"
    },
    {
        "email": "Quisque.fringilla.euismod@sitametorci.edu",
        "first_name": "Claudia",
        "last_name": "Webb"
    },
    {
        "email": "arcu@orciluctus.net",
        "first_name": "Herman",
        "last_name": "Ferrell"
    },
    {
        "email": "Cum@consectetuercursus.net",
        "first_name": "Myles",
        "last_name": "Harvey"
    },
    {
        "email": "sollicitudin@sit.net",
        "first_name": "Lisandra",
        "last_name": "Bates"
    },
    {
        "email": "rhoncus.Donec@aliquetodioEtiam.com",
        "first_name": "Kelly",
        "last_name": "Russell"
    },
    {
        "email": "nunc@vestibulum.net",
        "first_name": "Julian",
        "last_name": "Jackson"
    },
    {
        "email": "egestas.a@pellentesque.com",
        "first_name": "Leandra",
        "last_name": "Case"
    }
]


def get_users_list():
    users = []

    for user_dict in users_dict:
        users.append(UsersDBModel(**user_dict))

    return users
