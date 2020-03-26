# HBase Exercises

## Prerequisite

- Docker

## Commands to Start

### Pull HBase image

    docker pull dajobe/hbase

### Start with name hbase-furb

    docker run --name hbase-furb dajobe/hbase

### Use other terminal to access the VM

    docker exec -it hbase-furb /bin/bash

### To access the SSH

    hbase shell

## Exercise - Aquecendo com alguns dados

### Copying italians.txt to Docker

    docker cp italians.txt hbase-furb:/tmp

### Create table with 2 column families - personal-data and professional-data

### Create namespace

    create_namespace 'italians_ns'

### Create table

    create 'italians', 'personal-data', 'professional-data'

### Import file italians.txt from command line

    hbase shell /tmp/italians.txt

## Exercise 2 (Portugues only)

### Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;

    put 'italians', '11', 'personal-data:name',  'Gioconda Rezolina'
    put 'italians', '11', 'personal-data:city',  'Veneza'
    put 'italians', '11', 'personal-data:date-nasc',  '01/10/1970'
    put 'italians', '11', 'professional-data:role',  'Analista de Sistemas'
    put 'italians', '11', 'professional-data:salary',  '3055'
    put 'italians', '11', 'professional-data:year-exp',  '5'


    put 'italians', '12', 'personal-data:name',  'Reginaldo Materazzo'
    put 'italians', '12', 'personal-data:city',  'Milao'
    put 'italians', '12', 'personal-data:date-nasc',  '05/02/1990'
    put 'italians', '12', 'professional-data:role',  'Analista de Negocios'
    put 'italians', '12', 'professional-data:salary',  '2700'
    put 'italians', '12', 'professional-data:year-exp',  '3'

### Adicione o controle de 5 versões na tabela de dados pessoais.

    alter 'italians', NAME => 'personal-data', VERSIONS => 5

### Faça 5 alterações em um dos italianos;

    put 'italians', '11', 'personal-data:name',  'Gioconda Rezolina Materazzo'
    put 'italians', '11', 'personal-data:city',  'Milao'
    put 'italians', '11', 'personal-data:city',  'Genova'
    put 'italians', '11', 'personal-data:name',  'Gioconda Rezolina Josefina'
    put 'italians', '11', 'personal-data:date-nasc',  '01/10/1971'

### Com o operador get, verifique como o HBase armazenou o histórico.

    get 'italians', '11', {COLUMN=>'personal-data', VERSIONS=>5}

### Utilize o scan para mostrar apenas o nome e profissão dos italianos.

    scan 'italians', {COLUMNS => ['personal-data:name', 'professional-data:role']}

### Apague os italianos com row id ímpar

    deleteall 'italians', '1'
    deleteall 'italians', '3'
    deleteall 'italians', '5'
    deleteall 'italians', '7'
    deleteall 'italians', '9'
    deleteall 'italians', '11'

### Crie um contador de idade 55 para o italiano de row id 5

    incr 'italians', '5', 'personal-data:age', 55

### Incremente a idade do italiano em 1

    incr 'italians', '5', 'personal-data:age'
