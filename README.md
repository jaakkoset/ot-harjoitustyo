# Ohjelmistotekniikka, harjoitustyö

[![GHA workflow badge](https://github.com/jaakkoset/ohtuvarasto/workflows/CI/badge.svg)](https://github.com/jaakkoset/ohtuvarasto/actions)

Käyttäjä voi tehdä sovelluksella latinan kieleen liittyiä harjoituksia. Ohjelmassa on tällä hetkellä kaksi sanakoetta. Käyttäjä voi nähdä tilastoista kuinka monta sanaa hän on kääntänyt oikein tai väärin ja kuinka monta sanakoetta hän on suorittanut kokonaisuudessaan.

## Huomio Python-versiosta

Vaatimuksena on Python-versio `3.10`.

## Dokumentaatio

* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

* [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

* [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

* [Changelog](./dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla

    poetry install

Asenna tietokanta komennolla

    poetry run invoke init-db

Käynnistä ohjelma komennolla 

    poetry run invoke start

## Testaus

Suorita testit komennolla

    poetry run invoke test

Luo html-muotoinen testikattavuusraportti komennolla

    poetry run invoke coverage-report

Suorita Pylint-testi

    poetry run invoke lint
