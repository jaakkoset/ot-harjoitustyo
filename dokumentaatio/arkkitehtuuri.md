# Ohjelman arkkitehtuuri

## Luokkakaavio

```mermaid
classDiagram
    IOConsole -- Ui
    Ui -- Exercise
    Ui -- StatsRepository
    CommandHandler -- Ui
    IOConsole -- CommandHandler
    CommandHandler -- WordTest
    CommandHandler -- InvalidCommand
    CommandHandler -- Quit
    Exercise -- WordRepository
    Exercise -- StatsRepository
```

Luokka IOConsole vastaa kommunikoinnista käyttäjän kanssa. Luokassa Ui on käyttöliitymän toiminnot sekä ohjelmasilmukka. WordTest sisältää sanakokeen tarvitsemat metodit. WordRepository hakee sanoja tietokannasta. StatsRepository tallentaa ja hakee tilastoja tietokannasta. WordTest pyytää StatsRepositorya tallentamaan tiedon jokaisesta oikeasta vastauksesta.
