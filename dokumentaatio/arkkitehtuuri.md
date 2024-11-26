# Ohjelman arkkitehtuuri

## Luokkakaavio

```mermaid
classDiagram
    class Ui {-io}
    class WordTest {word}
    IOConsole -- Ui
    Ui -- WordTest
    WordTest -- WordRepository
```

Luokka IOConsole vastaa kommunikoinnista käyttäjän kanssa. Luokassa Ui on käyttöliitymän toiminnot sekä ohjelmasilmukka. WordTest sisältää sanakokeen tarvitsemat metodit. WordRepository hakee sanoja tietokannasta.
