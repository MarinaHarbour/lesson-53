class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name = Runner('Anna')
        for i in range(1, 11):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name = Runner('Igor')
        for i in range(1, 11):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        name1 = Runner('Vanya')
        name2 = Runner('Sasha')
        for i in range(1, 11):
            name1.run()
            name2.walk()
        self.assertNotEqual(name1.distance, name2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{value}")



    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r1_r3(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        self.all_results[1] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]  # Получаем объект последнего бегуна
        self.assertNotEqual(last_runner.name, 'Ник')  # Проверяем имя

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r2_r3(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results[2] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]
        self.assertNotEqual(last_runner.name, "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r1_r2_r3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results[3] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]
        self.assertNotEqual(last_runner.name, "Ник")



if __name__ == '__main__':
    unittest.main()