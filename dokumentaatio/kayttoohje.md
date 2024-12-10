# Käyttöohje

## Asennus

Asenna riippuvuudet komennolla

    poetry install

Asenna tietokanta komennolla

    poetry run invoke init-db

## Käynnistys

Käynnistä ohjelma komennolla 

    poetry run invoke start

Ohjelma aukeaa tekstikäyttöliittymään.

## Päävalikko

Käynnistettäessä ohjelma avautuu päävalikkoon. Käyttäjä voi valita sanakokeen antamalla komennon 1. Komennolla 4 käyttäjä näkee tilastoja.

## Sanakokeen valitseminen

Käyttäjä voi valita minkä sanakokeen hän tekee antamalla sitä vastaavan numeron komentona.

## Sanakoe

Sanakokeesta voi poistua milloin tahansa komennolla x. Muuten käyttäjän tulee antaa oikea suomennos näkyvillä olevasta sanasta. Kun kaikkiin sanakokeen kysymyksiin on vastattu, koe loppuu.