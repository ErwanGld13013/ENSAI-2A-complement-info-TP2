import pytest
from business_object.statistic import Statistic
from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon


class TestAllRounderPokemon:
    def test_multiplier_all_rounder_pokemon(self):
        # GIVEN:
        poketest = AllRounderPokemon(stat_current=Statistic(sp_atk=110, sp_def=60))

        # WHEN:
        multiplier = poketest.get_pokemon_attack_coef()

        # THEN:
        assert multiplier == 1.85
