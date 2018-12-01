from py2neo.ogm import Property, GraphObject, Label, RelatedTo

from models.film import Film, FunFact


class Location(GraphObject):
    '''
    Represents a filming location in the San Francisco Film Locations dataset.
    '''
    __primarykey__ = 'name'

    name = Property()
    location = Label()

    location = True

    location_for = RelatedTo(Film)
    has_fact = RelatedTo(FunFact)