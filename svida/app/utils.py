from .models import Analysis, VitalSign

def analyze_vital_signs(vital_sign):
    # Realize uma análise com base nos sinais vitais.
    # Este é apenas um exemplo, a análise real pode ser mais complexa.
    analysis_result = ""

    # Exemplo de regras para a análise de sinais vitais
    if vital_sign.blood_pressure > 140:
        analysis_result += "Pressão arterial alta. "
    elif vital_sign.blood_pressure < 90:
        analysis_result += "Pressão arterial baixa. "
    else:
        analysis_result += "Pressão arterial normal. "

    if vital_sign.heart_rate > 100:
        analysis_result += "Frequência cardíaca alta. "
    elif vital_sign.heart_rate < 60:
        analysis_result += "Frequência cardíaca baixa. "
    else:
        analysis_result += "Frequência cardíaca normal. "

    if vital_sign.breath_rate > 20:
        analysis_result += "Frequência respiratória elevada. "
    elif vital_sign.breath_rate < 12:
        analysis_result += "Frequência respiratória baixa. "
    else:
        analysis_result += "Frequência respiratória normal. "

    if vital_sign.temperature > 38:
        analysis_result += "Temperatura corporal alta (febre). "
    elif vital_sign.temperature < 36:
        analysis_result += "Temperatura corporal baixa. "
    else:
        analysis_result += "Temperatura corporal normal. "

    # Cria uma nova análise associada ao paciente
    analysis = Analysis(
        patient=vital_sign.patient,
        analysis=analysis_result,
        vital_sign=vital_sign
    )
    analysis.save()

    return analysis_result
