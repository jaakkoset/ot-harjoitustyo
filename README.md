# Ohjelmistotekniikka, harjoitustyö

Teen **kielenharjoittelusovelluksen**, jossa käyttäjä *ratkoo kieleen liittyviä tehtäviä*.

## Huomio Python-versiosta

Vaatimuksena on Python-versio `3.10`.

## Dokumentaatio

* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

* [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

* [Changelog](./dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla

`poetry install`

Käynnistä ohjelma komennolla 

`poetry run invoke start`

## Testaus

Suorita testit komennolla

`poetry run invoke test`

Luo html-muotoinen testikattavuusraportti komennolla

`poetry run invoke coverage-report`
