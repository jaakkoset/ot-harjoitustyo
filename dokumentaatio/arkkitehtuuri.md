# Ohjelman arkkitehtuuri

## Luokkakaavio

```mermaid
classDiagram
    class Ui {-io}
    class WordTest {word}
    class StatsRepository {-stats}
    IOConsole -- Ui
    Ui -- WordTest
    Ui -- StatsRepository
    WordTest -- WordRepository
    WordTest -- StatsRepository
```

Luokka IOConsole vastaa kommunikoinnista käyttäjän kanssa. Luokassa Ui on käyttöliitymän toiminnot sekä ohjelmasilmukka. WordTest sisältää sanakokeen tarvitsemat metodit. WordRepository hakee sanoja tietokannasta. StatsRepository tallentaa ja hakee tilastoja tietokannasta. WordTest pyytää StatsRepository tallentamaan tiedon jokaisesta oikeasta vastauksesta.
