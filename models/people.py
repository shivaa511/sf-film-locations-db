from py2neo.ogm import Property, GraphObject, Label, RelatedFrom, RelatedTo

from models.film import Film


class Actor(GraphObject):
    '''
    Represents an actor in the San Francisco Film Locations dataset.
    '''
    __primarykey__ = 'name'

    name = Property()
    person = Label()
    actor = Label()

    person = True
    actor = True

    starred_in = RelatedTo(Film)
    starring = RelatedFrom(Film)


class Writer(GraphObject):
    '''
    Represents a writer in the San Francisco Film Locations dataset.
    '''
    __primarykey__ = 'name'

    name = Property()
    person = Label()
    writer = Label()

    person = True
    actor = True

    wrote = RelatedTo(Film)
    written_by = RelatedFrom(Film)


class Director(GraphObject):
    '''
    Represents a director in the San Francisco Film Locations dataset.
    '''
    __primarykey__ = 'name'

    name = Property()
    person = Label()
    director = Label()

    person = True
    director = True

    directed = RelatedTo(Film)
    directed_by = RelatedFrom(Film)
