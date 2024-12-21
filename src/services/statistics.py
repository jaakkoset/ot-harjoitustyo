from repository.stats_repository import stats_repository


class StatisticsService:
    def __init__(
        self,
        stats_repo=stats_repository,
    ):
        self.stats_repo = stats_repo

    def printable_statistics(self):
        stats = self.stats_repo.get_all_stats()
        text = "Sanakokeiden tilastot\n"
        text += f"  Olet kääntänyt oikein {stats['correct_word_test_answers']} sanaa\n"
        text += f"  Olet vastannut väärin {stats['wrong_word_test_answers']} kertaa\n"
        text += f"  Olet suorittanut {stats['word_tests_completed']} sanakoetta kokonaisuudessaan"
        return text
