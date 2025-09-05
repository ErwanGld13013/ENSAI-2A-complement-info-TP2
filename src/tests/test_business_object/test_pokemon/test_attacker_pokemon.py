import pytest
from business_object.statistic import Statistic
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestAttackerPokemon:

    def test_attack_coef(self):
        # GIVEN: un Pokémon attaquant avec des stats données
        stat_max = Statistic(hp=100, attack=80, defense=50, sp_atk=40, sp_def=30, speed=70)
        stat_current = Statistic(hp=100, attack=80, defense=50, sp_atk=40, sp_def=30, speed=70)
        pikachu = AttackerPokemon(stat_max=stat_max, stat_current=stat_current, level=5, name="Pikachu")

        # WHEN: on calcule le coefficient d'attaque
        coef = pikachu.get_pokemon_attack_coef()

        # THEN: on compare avec la formule attendue
        expected = 1 + (pikachu.speed_current + pikachu.attack_current) / 200
        assert coef == pytest.approx(expected)
