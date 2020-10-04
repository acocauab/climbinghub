Database structure
==================

Definition of the database structure. 

Collections
-----------

- routes: Collection that will store all the analyzed climbing routes with the
  information of the grades.
- webpages: Collection that will store the diferent webpages that contains
  climbing routes. (that people manually introduced) Maybe it can contain also
  contains links to the route collection.

> NOTE: For the MVP we will not contemplate users.

**Route document example:**
```json
{
    "_id": "https://www.rocjumper.com/escalada/via-nuria-serra-sant-joan-boxiols/",
    "name": "Vía de la Núria (V 250 m) Serra de Sant Joan",
    "website": "https://www.rocjumper.com/",
    "grade": {
        "original": "6a+/A0 D+",
        "climbing": 615,
        "Artificial": 4,
        "Difficulty": 7
    },
    "zone": {
        "name": "montserrat",
        "gps": "https://www.rocjumper.com/index.php?mapsmarkerpro=download_gpx&url=https://www.rocjumper.com/wp-content/uploads/2020/09/acceso-via-nuria-serra-sant-joan-boxiols-rocjumper.gpx"
    },
    "tags": {
        "long": true,
        "classic": false,
        "snow": false,
        "ice": false,
        "sportive": false
    },
    "equipment": [
        "Casco", 
        "Arnés", 
        "Bagas de anclaje", 
        "Guantes (opcional)", 
        "Asegurador-Descensor", 
        "Autoseguro", 
        "Cuerdas 2 x 60 m", 
        "Reuniones", 
        "12 x Cintas expresses", 
        "Pies de gato"
    ],
    "photos": [
    "https://www.rocjumper.com/wp-content/uploads/2020/09/030-via-nuria-serra-sant-joan-boixols-rocjumper.jpg", 
    "https://www.rocjumper.com/wp-content/uploads/2020/09/010-via-nuria-serra-sant-joan-boixols-rocjumper-168x300.jpg"
    ]
}
```

> NOTE: Equipment section wont be included MVP

> NOTE: Zone section wont be included for the MVP (it might be changed)

> GRADE: The grade wont be expressed as 6a, D+ or A0 since this will make more
> dificult to query the databse with `<` and `>` expresions instead integers will be
> used. Anyway we will save the original text to avoid missing information.

Climbing grades will consist in 3 numbers: Example: 6b+ -> 625
`<gradenumber><letter><superior>`

Where:
- **gradenumber**: The same as the original grade
- **letter**: a:1, b:2, c:3 no-letter: 0
- **superior**: if + then 5 else 0

Artificial and Difficulty will be correlative numbers.

```json
{
    "_id": "https://www.rocjumper.com,
    "pages": [
        
    ] 
}
```
