from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone  # Importante para definir o valor default


# Model de Paciente
class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)  # Permite nulos
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=10)
    heart_rate = models.IntegerField()
    breath_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateTimeField(default=timezone.now)  # Define a data de registro automaticamente

    def __str__(self):
        return f'{self.patient.name} - {self.date_recorded}'

# Função para verificar a pressão arterial
def verificar_pressao_arterial(vital_sign):
    blood_pressure = vital_sign.blood_pressure.split('/')
    systolic = int(blood_pressure[0])  # Pressão sistólica
    diastolic = int(blood_pressure[1])  # Pressão diastólica
    
    if systolic > 130 or diastolic > 90:
        return "Hipertensão"
    if systolic < 100 and diastolic < 60:
        return "Hipotensão"
    return "Normotensão"

# Função para verificar a temperatura corporal
def verificar_temperatura(vital_sign):
    temperature = vital_sign.temperature
    if temperature < 36:
        return "Hipotermia"
    elif 36 <= temperature <= 37.3:
        return "Afebril"
    elif 37.4 <= temperature <= 38.5:
        return "Febril"
    elif temperature > 38.5:
        return "Hipetermia"
    return "Normotermia"

# Função para verificar a frequência respiratória
def verificar_frequencia_respiratoria(vital_sign):
    frequencia = vital_sign.breath_rate
    if frequencia < 12:
        return "Bradipneia"
    elif 12 <= frequencia <= 20:
        return "Eupneia"
    elif frequencia > 20:
        return "Taquipneia"
    
    return "Frequência respiratória normal"

# Função para verificar a frequência cardíaca
def verificar_frequencia_cardiaca(vital_sign):
    frequencia = vital_sign.heart_rate
    if frequencia < 60:
        return "Bradicardia"
    elif 60 <= frequencia <= 100:
        return "Normocardia"
    elif frequencia > 100:
        return "Taquicardia"
    
    return "Frequência cardíaca normal"



def vital_sign_history(request, patient_id):
    """
    Função que exibe o histórico de sinais vitais de um paciente específico.
    Obtém o paciente e os sinais vitais associados e os renderiza na página.
    """
    # Obtém o paciente específico
    patient = Patient.objects.get(id=patient_id)
    
    # Obtém todos os sinais vitais associados ao paciente
    vital_signs = VitalSign.objects.filter(patient=patient).order_by('-date_recorded')  # Ordena do mais recente para o mais antigo

    # Agora, vamos aplicar as funções de verificação para cada sinal vital
    analyzed_signs = []
    for sign in vital_signs:
        # Para cada sinal vital, chamamos o método 'descricao_completa' para obter a análise detalhada
        analysis = sign.descricao_completa()
        analyzed_signs.append(analysis)

    # Passa os sinais vitais e as análises para o template
    return render(request, 'app/vital_sign_history.html', {'patient': patient, 'vital_signs': vital_signs})
 

# Função que analisa os sinais vitais
def analyze_vital_signs(vital_sign):
    return {
        'pressao_arterial': verificar_pressao_arterial(vital_sign),
        'temperatura': verificar_temperatura(vital_sign),
        'frequencia_respiratoria': verificar_frequencia_respiratoria(vital_sign),
        'frequencia_cardiaca': verificar_frequencia_cardiaca(vital_sign),
    }

class Analysis(models.Model):
    # Exemplo de campos para o modelo, ajuste conforme necessário
    pressao_arterial = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    frequencia_respiratoria = models.CharField(max_length=100)
    frequencia_cardiaca = models.CharField(max_length=100)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def __str__(self):
        return f'Análise de {self.patient.name}'