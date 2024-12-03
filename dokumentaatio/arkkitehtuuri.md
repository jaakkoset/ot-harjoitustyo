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


## Sekvenssikaavio

Alla oleva sekvenssikaavio kuvaa tapahtumia, kun käyttäjä haluaa tehdä sanakokeen. Alussa käyttäjä on alkuvalikossa ja kaavio loppuu siihen, kun ohjelma odottaa käyttäjältä vastausta ensimmäiseen kysymykseen. WordTestin metodissa choose_word_test() käyttäjä myös valitsee minkä sanakokeen hän haluaa tehdä vaikka sitä ei kaaviossa käydä läpi.

```mermaid
sequenceDiagram
    actor User
    participant Ui
    participant IOConsole
    participant CommandHandler
    participant WordTest
    participant Exercise
    participant ExerciseRepository

    User ->> Ui: enter 1 on terminal
    Ui ->> CommandHandler: get(1)
    CommandHandler ->> Ui: return WordTest
    Ui ->> WordTest: run()
    WordTest ->> WordTest: choose_word_test()
    WordTest ->> Exercise: word_test_id
    Exercise ->> ExerciseRepository: get_exercise_data(exercise_id)
    ExerciseRepository ->> Exercise: return exercise, all_exercise_questions
    WordTest ->> Exercise: question()
    Exercise ->> WordTest: return question
    WordTest ->> IOConsole: write()
    IOConsole ->> User: Suomenna sana: question
    WordTest ->> IOConsole: read()
    IOConsole ->> User: 
```