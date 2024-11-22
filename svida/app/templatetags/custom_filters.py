from django import template
from app.utils import analyze_vital_signs  # Supondo que você tenha essa função

register = template.Library()

# @register.filter
# def analyze_vital_signs(value):
#      # Exemplo simples de análise
#      if value.heart_rate > 100:
#         return "Frequência cardíaca elevada"
#      elif value.temperature > 37.5:
#          return "Temperatura elevada"
        
#      else:
#         return "Sinais vitais normais"
#         register = template.Library()

@register.filter
def zip_lists(list1, list2):
    """Retorna uma lista de tuplas combinando dois iteráveis (listas)."""
    return zip(list1, list2)