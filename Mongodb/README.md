## MongoDB Exercise

Practical Exercises of MongoDB - all questions in Portuguese (PR-BR).

### Exercício 1 - Aquecendo com os pets

### Inicie com os seguintes comandos

    use petshop

    db.pets.insert({name: "Mike", species: "Hamster"})

    db.pets.insert({name: "Dolly", species: "Peixe"})

    db.pets.insert({name: "Kilha", species: "Gato"})

    db.pets.insert({name: "Mike", species: "Cachorro"})

    db.pets.insert({name: "Sally", species: "Cachorro"})

    db.pets.insert({name: "Chuck", species: "Gato"})

### Adicione outro Peixe e um Hamster com nome Frodo

    db.pets.insert({name: "Frodo", species: "Peixe"})

    db.pets.insert({name: "Frodo", species: "Hamster"})

### Faça uma contagem dos pets na coleção

    db.pets.count()

### Retorne apenas um elemento o método prático possível

    db.pets.findOne()

### Identifique o ID para o Gato Kilha.

    db.pets.find({name: "Kilha"})

### Faça uma busca pelo ID e traga o Hamster Mike

    db.pets.find("5e77a91c1658e8e5dbc5e8ac")

### Use o find para trazer todos os Hamsters

    db.pets.find({species: "Hamster"})

### Use o find para listar todos os pets com nome Mike

    db.pets.find({name: "Mike"})

### Liste apenas o documento que é um Cachorro chamado Mike

    db.pets.find({name: "Mike", species: "Cachorro"})

## Exercício 2 - Mama mia!

### Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.

    db.italians.count({age: 99})

### Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)

    db.italians.find({age: {"$gt": 65}})

### Identifique todos os jovens (pessoas entre 12 a 18 anos).

    db.italians.find({age: {"$gte": 12, "$lte": 18}})

### Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois

    db.italians.count({"cat" : {"$exists" : true} })

    db.italians.count({"dog" : {"$exists" : true} })

    db.italians.count({"dog" : {"$exists" : false}, "cat" : {"$exists": false} })

### Liste/Conte todas as pessoas acima de 60 anos que tenham gato

    db.italians.count({age: {"$gt": 60} , "cat" : {"$exists": true} })

### Liste/Conte todos os jovens com cachorro

    db.italians.count({age: {"$gte": 12, "$lte": 18}, dog : {"$exists": true}})

### Utilizando o $where, liste todas as pessoas que tem gato e cachorro

    db.italians.find({$and: [{$where: "this.cat != null"}, {$where: "this.dog != null"}]})

### Liste todas as pessoas mais novas que seus respectivos gatos.

    db.italians.find({$and: [{$where: "this.cat != null"}, {$where: "this.age < this.cat.age"}]})

### Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)

    db.italians.find({$and: [{$where: "this.cat != null"}, {$where: "this.firstname == this.cat.name"}]}, {$and: [{$where: "this.dog != null"}, {$where: "this.firstname == this.dog.name"}]})

### Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo

    db.italians.find({bloodType : {$exists:  "-"}}, {firstname : true, surname: true})

### Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)

    db.italians.find({}, {_id: false, "dog" : true, "cat": true})

### Quais são as 5 pessoas mais velhas com sobrenome Rossi?

    db.italians.find({"surname" : {$eq : "Rossi"}}).sort({age : -1}).limit(5)

### Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano

    db.italians.insert({"firstname" : "Suzane", "surname" : "Materazzo", "username" : "user919087", "age" : 80, "email" : "Suzane.Materazzo@gmail.com", "bloodType" : "A-", "id_num" : "136325010528", "registerDate" : ISODate("2011-10-09T10:39:29.329Z"), "ticketNumber" : 779111, "jobs" : [ "Programador" ], "favFruits" : [ "Uva" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.64 }, { "title" : "Pulp Fiction: Tempo de Violência (1994)", "rating" : 4.96 }, { "title" : "Coringa (2019)", "rating" : 2.16 }, { "title" : "Os Bons Companheiros (1990)", "rating" : 4.85 }, { "title" : "A Vida é Bela (1997)", "rating" : 4.59 } ], "lion" : { "name" : "Leon", "age" : 12 }})

### Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.

    db.italians.remove("5e77e794a1ffcd036a14c243")

### Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.

    db.italians.updateMany({}, {"$inc": {age: 1} })

    db.italians.updateMany({}, {"$inc": {"dog.age": 1} })

    db.italians.updateMany({}, {"$inc": {"cat.age": 1} })

### O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.

    db.italians.remove({$and: [{"age": 66}, {"cat": {"$exists": true}}]})

### Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

    db.italians.aggregate([
        {$match:
                {$or: [
                    {cat: { $exists: 1 }}, 
                    {dog: {  $exists: 1 }} 
                ]}
        },
        {'$match': { mother: { $exists: 1} }}, 
        {
            '$project': {
                "cat": 1,
                "dog": 1,
                "firstname": 1,
                "mother": 1,
                "isEqual": { "$cmp": ["$firstname","$mother.firstname"]}
            }
        },
        {'$match': { "isEqual": 0 }}
    ])

### Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome

    db.italians.aggregate([
        {$group: {
            _id: "$firstname"
        }},
        {
            '$project': {
                "firstname": 1
            }
        }
    ])

### Agora faça a mesma lista do item acima, considerando nome completo.

    db.italians.aggregate([
        {$group: {
            _id: {firstname: "$firstname", surname: "$surname"}
        }},
        {
            '$project': {
                "firstname": 1,
                "surname": 1
            }
        }
    ])

### Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.

    db.italians.find({
        $and: [
            {age: {"$gt": 20, "$lt": 60}},
            {$or:[
                { dog : {"$exists": 1} },
                { cat : {"$exists": 1} }
            ]},
            {favFruits: {$exists: 1 }},
            {favFruits: {$in: ["Banana", "Maçã"] }}
        ]
    })

## Exercise 3 - Stockbrokers

### Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

    db.stocks.find({
        "Profit Margin" : {$gt: 0.5}
    }).limit(10)

### Liste as ações com perdas (limite a 10 novamente)

    db.stocks.find({
        "Profit Margin" : {$lt: 0}
    }).limit(10)

### Liste as 10 ações mais rentáveis

    db.stocks.find({}).sort({"Profit Margin" : -1}).limit(10)

### Qual foi o setor mais rentável?

    db.stocks.aggregate([
        {"$group": { _id: "$Sector" , total: {$sum: "$Profit Margin" }}},
        {$sort: { total: -1 }}
    ])

### Ordene as ações pelo profit e usando um cursor, liste as ações.

    var cursor = db.stocks.find({
        "Profit Margin" : {$lt: 0}
    }).limit(10)

    cursor.forEach(function(x) {
        print(x.Sector, x["Profit Margin"])
    })

### Renomeie o campo “Profit Margin” para apenas “profit”.

    db.stocks.update({}, {$rename: {"Profit Margin": "profit"}}, false, true)

### Agora liste apenas a empresa e seu respectivo resultado

    db.stocks.find({}, {"Company": 1, "profit": 1})

### Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

    db.stocks.find({}, {"Company": 1, "profit": 1}).sort({profit: -1})

    { "_id" : ObjectId("52853801bb1177ca391c1af3"), "Company" : "BP Prudhoe Bay Royalty Trust", "profit" : 0.994 }

    { "_id" : ObjectId("52853802bb1177ca391c1b69"), "Company" : "Cascade Bancorp", "profit" : 0.994 }

    { "_id" : ObjectId("5285380bbb1177ca391c2c3c"), "Company" : "Pacific Coast Oil Trust", "profit" : 0.99 }

### Liste as ações agrupadas por setor

    db.stocks.aggregate([
        {"$group": { _id: "$Sector"}}
    ])

## Exercício 3.1 - Fraude na Enron

### Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

    db.stocks.aggregate([
        {"$group": { _id: "$sender"}}
    ])

### Contabilize quantos e-mails tem a palavra “fraud”

    db.stocks.count({
        $or: [
            { text: {$regex: /fraud/, $options: 'i'} },
            { subject: {$regex: /fraud/, $options: 'i'} },
        ]
    })
