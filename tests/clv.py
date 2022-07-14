from rdflib import XSD, Graph, Literal, Namespace, URIRef

from ontopia_py import ConceptScheme, createGraph, saveGraph
from ontopia_py.ns import CITIES
from ontopia_py.clv import Address, CivicNumbering, StreetToponym, City

# Set namespaces
ANNCSU: Namespace = Namespace("https://w3id.org/sona/data/ANNCSU/")
ONTO_AUTHOR: URIRef = URIRef("https://w3id.org/people/lucamartinelli")

# Create the graph
g: Graph = createGraph()

# Bind the data
g.bind("anncsu", ANNCSU)

# Create a ConceptScheme
ANNCSU_DATA: ConceptScheme = ConceptScheme(ANNCSU)

# Set the properties
ANNCSU_DATA.label = [
    Literal("Anagrafe nazionale numeri civici e strade urbane", lang="it"),
    Literal("Civic Addressing and Street Naming", lang="en")
]
ANNCSU_DATA.creator = [ONTO_AUTHOR]

# And add to graph
ANNCSU_DATA.addToGraph(g)

# Add data
postCode: int = 37060
street: dict = {
    "id": 1,
    "dug": "Via",
    "name": "Roma"
}

civic: dict = {
    "id": 1,
    "street_id": 1,
    "civic": 1,
    "exponent": "A"
}

# Civic full name
civicName: str = "{}/{}".format(civic["civic"], civic["exponent"])
toponymName: str = "{} {}".format(street["dug"], street["name"])
addressName: str = "{}, {} - {}, Sona".format(
    toponymName, civicName, civic["postCode"]
)

# Create CivicNumbering
civicNumbering: CivicNumbering = CivicNumbering(
    id="cv-" + str(civic["id"]),
    baseUri=ANNCSU,
    dataset=ANNCSU_DATA,
    titles=[Literal(civicName, datatype=XSD.string)]
)

# Create StreetToponym
streetToponym: StreetToponym = StreetToponym(
    id="st-" + str(street["id"]),
    baseUri=ANNCSU,
    dataset=ANNCSU_DATA,
    titles=[Literal(toponymName, datatype=XSD.string)]
)
streetToponym.officialStreetName = street["name"]
streetToponym.toponymQualifier = street["dug"]

# Create Address
address: Address = Address(
    id="ad-{}-{}".format(street["id"], civic["id"]),
    baseUri=ANNCSU,
    dataset=ANNCSU_DATA,
    titles=[
        Literal(addressName, datatype=XSD.string)
    ])

# Get city from controlled vocabulary
city: City = City(id="023083-(1975-01-29)", baseUri=CITIES)

address.hasStreetToponym = streetToponym
address.postCode = Literal(postCode, datatype=XSD.int)
address.hasCity = [city]

# Add all to graph
civicNumbering.addToGraph(g, isTopConcept=False)
streetToponym.addToGraph(g, isTopConcept=False)
address.addToGraph(g, isTopConcept=True)

# Finally, save the graph to a file
saveGraph(g, "test")
