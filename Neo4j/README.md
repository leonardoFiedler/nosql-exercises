# Neo4J Exercise

## Start Command

:play intro-neo4j-exercises

## Exercise 1

### Retreiving Nodes

MATCH (n) RETURN n

### Examine the data model of the graph

call db.schema.visualization()

### Retrieve all Person nodes

Match (p:Person) RETURN p

### Retrieve all Movie nodes

MATCH (m:Movie) RETURN m

## Exercise 2

### Retrieve all movies that were released in a specific year.

match (m:Movie {released:2003}) return m

### Query the database for all property keys

CALL db.propertyKeys()

### Retrieve all Movies released in a specific year, returning their titles

match (m:Movie {released:2006}) return m.title

### Display title, released, and tagline values for every Movie node in the graph

match (m:Movie) return m.title, m.released, m.tagline

### Display more user-friendly headers in the table

match (m:Movie) return m.title as movieTitle, m.released as releasedDate, m.tagline as tagline

## Exercise 3

### Retrieve all people who wrote the movie Speed Racer

MATCH (p:Person)-[:WROTE]->(:Movie {title: 'Speed Racer'}) RETURN p.name

### Retrieve all movies that are connected to the person, Tom Hanks

MATCH (m:Movie)<--(p:Person {name: 'Tom Hanks'}) RETURN m.title

### Retrieve information about the relationships Tom Hanks has with the set of movies retrieved earlier

MATCH (m:Movie)-[rel]-(p:Person {name: 'Tom Hanks'}) RETURN m.title, type(rel)

### Retrieve information about the roles that Tom Hanks acted in

MATCH (m:Movie)-[rel:ACTED_IN]-(p:Person {name: 'Tom Hanks'}) RETURN m.title, rel.roles

## Exercise 4

### Retrieve all movies that Tom Cruise acted in

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.name = 'Tom Cruise' RETURN m

### Retrieve all people that were born in the 70’s 

MATCH (p:Person) WHERE p.born IN [1970, 1979] RETURN p.name

### Retrieve the actors who acted in the movie The Matrix who were born after 1960

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.title = 'The Matrix' AND p.born > 1960 RETURN p

### Retrieve all movies by testing the node label and a property

MATCH (m:Movie) WHERE m.released = 2000 RETURN m.title

MATCH (m) WHERE m:Movie AND m.released = 2000 RETURN m.title

### Retrieve all people that wrote movies by testing the relationship between two nodes

MATCH (p:Person)-[:WROTE]->(m:Movie) RETURN p.name, m.title

MATCH (p)-[rel]->(m) WHERE p:Person AND type(rel) = 'WROTE' AND m:Movie RETURN p.name as Name, m.title as Movie

### Retrieve all people in the graph that do not have a property

MATCH (a:Person) WHERE NOT exists(a.born) RETURN a.name

### Retrieve all people related to movies where the relationship has a property

MATCH (p:Person)-[rel]->(m:Movie) WHERE exists(rel.rating) RETURN p.name, m.title, rel.rating

### Retrieve all actors whose name begins with James

MATCH (p:Person) WHERE p.name STARTS WITH 'James' RETURN p.name

### Retrieve all REVIEWED relationships from the graph with filtered results

MATCH (p:Person)-[rev:REVIEWED]->(m:Movie) WHERE toLower(rev.summary) CONTAINS 'fun' RETURN m.title, rev.rating, rev.summary

### Retrieve all people who have produced a movie, but have not directed a movie

MATCH (p:Person)-[:PRODUCED]->(m:Movie) WHERE not ((p)-[:DIRECTED]->(:Movie)) RETURN p.name, m.title

### Retrieve the movies and their actors where one of the actors also directed the movie

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p1:Person) WHERE exists((p1)-[:DIRECTED]->(:Movie)) RETURN p.name, p1.name, m.title

### Retrieve all movies that were released in a set of years 

MATCH (m:Movie) WHERE m.released IN [2000, 2004, 2008] RETURN m.title, m.released

### Retrieve the movies that have an actor’s role that is the name of the movie

MATCH (p:Person)-[r:ACTED_IN]->(m:Movie) WHERE m.title IN r.roles RETURN m.title, p.name

## Exercise 5

### Retrieve data using multiple MATCH patterns 

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p1:Person), (p2:Person)-[:DIRECTED]->(m) WHERE p.name = 'Gene Hackman' RETURN m.title, p2.name, p1.name

### Retrieve particular nodes that have a relationship 

MATCH (p1:Person)-[:FOLLOWS]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2

### Modify the query to retrieve nodes that are exactly three hops away

MATCH (p1:Person)-[:FOLLOWS*3]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2

### Modify the query to retrieve nodes that are one and two hops away

MATCH (p1:Person)-[:FOLLOWS*1..2]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2

### Modify the query to retrieve particular nodes that are connected no matter how many hops are required

MATCH (p1:Person)-[:FOLLOWS*]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2

### Specify optional data to be retrieved during the query 

MATCH (p:Person) WHERE p.name STARTS WITH 'Tom' OPTIONAL MATCH (p)-[:DIRECTED]->(m:Movie) RETURN p.name, m.title

### Retrieve nodes by collecting a list

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, collect(m.title) as moviesName RETURN p.name, moviesName

### Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie by collecting a list

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p1:Person) WITH p, m, collect(p1.name) as coActors WHERE p.name = 'Tom Cruise' RETURN m.title, coActors

### Retrieve nodes as lists and return data associated with the corresponding lists

MATCH (p:Person)-[:REVIEWED]->(m:Movie) RETURN m.title, count(*), collect(p.name) as reviewers

### Retrieve nodes and their relationships as list

MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p2:Person) RETURN p2.name, count(p1), collect(p1.name) as actorsName

###  Retrieve the actors who have acted in exactly five movies 

MATCH (p1:Person)-[:ACTED_IN]->(m:Movie) WITH count(p1) as movieCount, p1, collect(m.title) as movies WHERE movieCount = 5 RETURN p1.name, movies

### Retrieve the movies that have at least 2 directors with other optional data

MATCH (p1:Person)-[:DIRECTED]->(m:Movie) 
OPTIONAL MATCH (p2:Person)-[:REVIEWED]->(m)
WITH m, collect(p2.name) as reviewersName,count(p1) as directorsNumber WHERE directorsNumber > 1 RETURN directorsNumber, m.title, reviewersName

## Exercise 6

### Execute a query that returns duplicate records.

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >=1990 AND m.released < 2000 RETURN m.released, m.title, collect(p.name)

### Modify the query to eliminate duplication

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >=1990 AND m.released < 2000 RETURN m.released, collect(m.title), collect(p.name)

### Modify the query to eliminate more duplication

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >=1990 AND m.released < 2000 RETURN m.released, collect(DISTINCT m.title), collect(p.name)

### Sort results returned

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >=1990 AND m.released < 2000 RETURN m.released, collect(DISTINCT m.title), collect(p.name) ORDER BY m.released DESC

### Retrieve the top 5 ratings and their associated movies 

MATCH (:Person)-[r:REVIEWED]->(m:Movie) RETURN m.title, r.rating ORDER BY r.rating DESC LIMIT 5

### Retrieve all actors that have not appeared in more than 3 movies

MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, collect(m.title) as movieList ,count(m) as movieCount WHERE movieCount <= 3 RETURN p.name, movieList

## Exercise 7

### Collect and use lists

MATCH (p:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p1:Person)
WITH m, collect(DISTINCT p.name) as actorNames, collect(DISTINCT p1.name) AS producers
RETURN DISTINCT m.title, actorNames, producers
ORDER BY size(actorNames)

### Collect a list

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WITH p, collect(m) as movies
WHERE size(movies) > 5
RETURN p.name, movies

### Unwind a list

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WITH p, collect(m) as movies
WHERE size(movies) > 5
WITH p, movies UNWIND movies AS movie
RETURN p.name, movie.title

### Perform a calculation with the date type

MATCH (m:Movie)-[:ACTED_IN]-(p:Person {name: 'Tom Hanks'}) 
RETURN m.title, m.released, p.born, 2020 - m.released, m.released - p.born

MATCH (m:Movie)-[:ACTED_IN]-(p:Person {name: 'Tom Hanks'}) 
RETURN m.title, m.released, p.born, date().year - m.released, m.released - p.born

## Exercise 8

### Create a Movie node

CREATE(:Movie {title: 'Forrest Gump'})

### Retrieve the newly-created node

MATCH (m: Movie) WHERE m.title = 'Forrest Gump' RETURN m

### Create a Person node

CREATE (:Person {name: 'Robin Wright'})

### Retrieve the Person node you just created by its name

MATCH (p: Person) WHERE p.name = 'Robin Wright' RETURN p

### Add a label to a node

MATCH (m: Movie) WHERE m.released < 2010
SET m:OlderMovie
RETURN DISTINCT labels(m)

### Retrieve the node using the new label

MATCH (m:OlderMovie) RETURN m.title, m.released

### Add the Female label to selected nodes

MATCH (p: Person) WHERE p.name STARTS WITH 'Robin'
SET p:Female
RETURN DISTINCT labels(p)

### Retrieve all Female nodes

MATCH (p: Female) RETURN p.name 

### Remove the Female label from the nodes that have this label

MATCH (p: Female) REMOVE p:Female

### View the current schema of the graph

CALL db.schema.visualization()

### Add properties to a movie

MATCH (m: Movie)
WHERE m.title = 'Forrest Gump'
SET m.released = 1994,
    m.tagline = "m.lengthInMinutes = 142",
    m.lengthInMinutes = 142,
    m:OlderMovie

### Retrieve an OlderMovie node to confirm the label and properties

MATCH (m:OlderMovie) WHERE m.title = 'Forrest Gump' RETURN m

### Add properties to the person, Robin Wright

MATCH (p: Person) WHERE p.name = 'Robin Wright'
SET p.born = 1996,
    p.birthPlace = 'Dallas'

### Retrieve an updated Person node 

MATCH (p: Person) WHERE p.name = 'Robin Wright' RETURN p

### Remove a property from a Movie node

MATCH (m: Movie) WHERE m.title = 'Forrest Gump' SET m.lengthInMinutes = null

### Retrieve the node to confirm that the property has been removed

MATCH (m: Movie) WHERE m.title = 'Forrest Gump' RETURN m

### Remove a property from a Person node

MATCH (p: Person) WHERE p.name = 'Robin Wright' SET p.birthPlace = null

### Retrieve the node to confirm that the property has been removed

MATCH (p: Person) WHERE p.name = 'Robin Wright' RETURN p

## Exercise 9

### Create ACTED_IN relationships

MATCH (m: Movie) WHERE m.title = 'Forrest Gump'
MATCH (p: Person)
WHERE p.name = 'Tom Hanks' or p.name = 'Robin Wright' or p.name = 'Gary Sinise'
CREATE (p)-[:ACTED_IN]->(m)

### Create DIRECTED relationships

MATCH (m: Movie) WHERE m.title = 'Forrest Gump'
MATCH (p: Person)
WHERE p.name = 'Robert Zemeckis'
CREATE (p)-[:DIRECTED]->(m)

### Create a HELPED relationship

MATCH (p: Person) WHERE p.name = 'Tom Hanks'
MATCH (p1: Person) WHERE p1.name = 'Gary Sinise'
CREATE (p)-[:HELPED]->(p1)

### Query nodes and new relationships

MATCH (p: Person)-[rel]-(m: Movie)
WHERE m.title = 'Forrest Gump'
RETURN p, rel, m

### Add properties to relationships

MATCH (p: Person)-[rel: ACTED_IN]->(m: Movie)
WHERE m.title = 'Forrest Gump'
SET rel.roles =
CASE p.name
    WHEN 'Tom Hanks' THEN ['FORREST GUMP']
    WHEN 'Robin Wright' THEN ['Jenny Curran']
    WHEN 'Gary Sinise' THEN ['Lieutenant Dan Taylor']
END

### Add a property to the HELPED relationship

MATCH (p: Person)-[rel:HELPED]->(p1: Person)
WHERE p.name = 'Tom Hanks' AND p1.name = 'Gary Sinise'
SET rel.research = 'war history'

###  View the current list of property keys in the graph 

CALL db.propertyKeys()

### View the current schema of the graph

CALL db.schema.visualization()

### Retrieve the names and roles for actors

MATCH (p: Person)-[rel:ACTED_IN]->(m: Movie)
WHERE m.title = 'Forrest Gump'
RETURN p.name, rel.roles

### Retrieve information about any specific relationships 

MATCH (p: Person)-[rel:HELPED]->(p1: Person)
RETURN p.name, rel, p1.name

### Modify a property of a relationship

MATCH (p: Person)-[rel:ACTED_IN]->(m: Movie)
WHERE m.title = 'Forrest Gump' AND p.name = 'Gary Sinise'
SET rel.roles = ['Lt. Dan Taylor']

### Remove a property from a relationship

MATCH (p: Person)-[rel:HELPED]->(p1: Person)
WHERE p.name = 'Tom Hanks' AND p1.name = 'Gary Sinise'
REMOVE rel.research

### Confirm that your modifications were made to the graph 

MATCH (p: Person)-[rel:ACTED_IN]->(m: Movie)
WHERE m.title = 'Forrest Gump'
RETURN p, rel, m

## Exercise 10

### Delete a relationship

MATCH (p: Person)-[rel:HELPED]->(p1: Person) DELETE rel

### Confirm that the relationship has been deleted 

MATCH (p: Person)-[rel:HELPED]->(p1: Person)
RETURN rel

### Retrieve a movie and all of its relationships

MATCH (p: Person)-[rel]->(m: Movie)
WHERE m.title = 'Forrest Gump'
RETURN p, rel, m

### Try deleting a node without detaching its relationships 

MATCH (m: Movie)
WHERE m.title = 'Forrest Gump'
DELETE m

### Delete a Movie node, along with its relationships 

MATCH (m: Movie)
WHERE m.title = 'Forrest Gump'
DETACH DELETE m

### Confirm that the Movie node has been deleted 

MATCH (m: Movie) WHERE m.title = 'Forrest Gump' RETURN m