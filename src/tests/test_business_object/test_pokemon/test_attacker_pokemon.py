import pytest
from business_object.statistic import Statistic
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestAttackerPokemon:

    def test_attack_coef(self):
        # GIVEN: un Pokémon attaquant avec des stats données
        pikachu = AttackerPokemon(stat_current=Statistic(attack=100, speed=40))

        # WHEN: on calcule le coefficient d'attaque
        multiplier = pikachu.get_pokemon_attack_coef()

        # THEN: on compare avec la formule attendue
        assert multiplier == 1.7
