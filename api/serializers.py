from rest_framework import serializers

from pokemon.models import Pokemon, Type

class PokemonSerializer(serializers.modelSerializer)