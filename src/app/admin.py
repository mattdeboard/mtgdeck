from django.contrib import admin
from app.models import card, card_type, color_identity, converted_mana_cost

admin.site.register(card.Card)
admin.site.register(color_identity.ColorIdentity)
admin.site.register(converted_mana_cost.ConvertedManaCost)

