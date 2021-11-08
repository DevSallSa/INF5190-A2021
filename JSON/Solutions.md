# Solutions

## Exercice 1 :

Après correction :

```
{
	"numero_employe": 884,
	"numero_semaine": 4,
	"annee": 2012,
	"lundi": [{
			"code_de_projet": 200,
			"minutes": 90
		},
		{
			"code_de_projet": 125,
			"minutes": 45
		},
		{
			"code_de_projet": 990,
			"minutes": 180
		},
		{
			"code_de_projet": 166,
			"minutes": 100
		}
	],
	"mardi": [{
		"code_de_projet": 125,
		"minutes": 420
	}],
	"mercredi": [{
		"code_de_projet": 125,
		"minutes": 420
	}],
	"jeudi": [{
			"code_de_projet": 125,
			"minutes": 420
		},
		{
			"code_de_projet": 116,
			"minutes": 50
		}
	],
	"vendredi": [{
		"code_de_projet": 166,
		"minutes": 420
	}],
	"samedi": [],
	"dimanche": [{
		"code_de_projet": 990,
		"minutes": 30
	}]
}

```

## Exercice 2

```
{
  "numero_employe": 884,
  "numero_semaine": 4,
  "annee": 2012,
  "jours": [
    [{
      "code_de_projet": 200,
      "minutes": 90
    }, {
      "code_de_projet": 125,
      "minutes": 45
    }, {
      "code_de_projet": 990,
      "minutes": 180
    }, {
      "code_de_projet": 166,
      "minutes": 100
    }],
    [{
      "code_de_projet": 125,
      "minutes": 420
    }],
    [{
      "code_de_projet": 125,
      "minutes": 420
    }],
    [{
      "code_de_projet": 125,
      "minutes": 420
    }, {
      "code_de_projet": 116,
      "minutes": 50
    }],
    [{
      "code_de_projet": 166,
      "minutes": 420
    }],
    [],
    [{
      "code_de_projet": 990,
      "minutes": 30
    }]
  ]
}
```

## Exercice 3

Version atelier :
```
{
  "nom": "Steeve",
  "prenom": "Steeve",
  "assurance_maladie": "STV0979636r36r",
  "naissance": "1998-02-12",
  "medecin_famille": {
    "nom": "Pas Steeve",
    "prenom": "Docteur",
    "identifiant": "DRALMAUR8907645",
    "ville": "Bruxelles"
  },
  "visites": [{
    "date": "2020-03-15",
    "sujet": "COVID-19",
    "description": "Testé positif à la COVID-19, aucun médicament n'est prescrit. Patient encore vivant."
  }, {
    "date": "2021-02-09",
    "sujet": "Grippe",
    "description": "Le patient hallucine, il pense qu'il a COVID-19. Il tousse mais il est pas mort."
  }]
}
```

Version Jacques :

```
{
  "nom": "Berger",
  "prenom": "Jacques",
  "assurance_maladie": "BERJ12052304",
  "naissance": "1912-05-23",
  "medecin_famille": {
    "nom": "Stevenson",
    "prenom": "Steven",
    "identifiant": "234F3",
    "ville": "Sherbrooke"
  },
  "visites": [{
    "date": "2016-09-01",
    "sujet": "Suivi annuel",
    "description": "Rien à signaler. Renouvellement de la prescription de morphine."
  }, {
    "date": "2016-09-03",
    "sujet": "Blessure au dos",
    "description": "Entorse lombaire. Prescription d'anti-inflammatoires."
  }]
}
```

## Exercice 4

Version atelier :
 ```
[{
  "sigle": "INF3190",
  "groupe": 20,
  "trimestre": 2,
  "annee": 2020,
  "enseignant": "François-Xavier Guillemette",
  "note": "A+"
}, {
  "sigle": "INF2050",
  "groupe": 30,
  "trimestre": 1,
  "annee": 2019,
  "enseignant": "Jacques Berger",
  "note": "C+"
}, {
  "sigle": "INF4500",
  "groupe": 10,
  "trimestre": 3,
  "annee": 2021,
  "enseignant": "Vladimir",
  "note": "A"
}]
```

Version Jacques :

```
[{
  "sigle": "INF4375",
  "groupe": 50,
  "trimestre": 3,
  "annee": 2016,
  "enseignant": "Jacques Berger",
  "note": "A+"
}, {
  "sigle": "INF2015",
  "groupe": 30,
  "trimestre": 1,
  "annee": 2016,
  "enseignant": "Jacques Berger",
  "note": "A-"
}, {
  "sigle": "INF1256",
  "groupe": 21,
  "trimestre": 2,
  "annee": 2015,
  "enseignant": "François-Xavier Guillemette",
  "note": "A"
}]
```

