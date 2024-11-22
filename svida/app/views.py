from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, VitalSign, Analysis
from django import forms
from django.contrib import messages
from .forms import VitalSignForm
from django.core.validators import RegexValidator
from .utils import analyze_vital_signs
from itertools import zip_longest
from django.core.exceptions import ValidationError
import re
from django.utils import timezone
from .forms import PatientEditForm



# Formulário para adicionar um paciente
class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact']

# Validador para a pressão arterial no formato "120x80"
def validate_blood_pressure(value):
    # Regex para pression arterial como "120x80"
    if not re.match(r'^\d{2,3}x\d{2,3}$', value):
        raise ValidationError("Pressão arterial inválida. Utilize o formato '120x80'.")
    return value

class VitalSignForm(forms.ModelForm):
    class Meta:
        model = VitalSign
        fields = ['blood_pressure', 'heart_rate', 'breath_rate', 'temperature']
    
    # Campo de Pressão Arterial com o validador personalizado
    blood_pressure = forms.CharField(
        max_length=10,
        validators=[validate_blood_pressure],
        widget=forms.TextInput(attrs={'placeholder': 'Ex: 120x80 mmHg'})
    )

# Função para adicionar um paciente
def add_patient(request):
    if request.method == 'POST':
        form = PatientEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redireciona para a página inicial (ou menu)
    else:
        form = PatientEditForm()
    return render(request, 'app/add_patient.html', {'form': form})



# Função para adicionar sinais vitais
def add_vital_sign(request, patient_id):
    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        form = VitalSignForm(request.POST)
        if form.is_valid():
            vital_sign = form.save(commit=False)
            vital_sign.patient = patient  # Relaciona o paciente com os sinais vitais
            vital_sign.date_recorded = timezone.now()  # Garantir que a data seja salva
            vital_sign.save()  # Salva no banco de dados
            messages.success(request, "Sinais vitais cadastrados com sucesso!")
            return redirect('menu')  # Redireciona após salvar
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = VitalSignForm()

    return render(request, 'app/add_vital_sign.html', {'form': form, 'patient': patient})

# Função para exibir o histórico de sinais vitais de um paciente
def vital_sign_history(request, patient_id):
    # Recupera o paciente e seus sinais vitais
    patient = Patient.objects.get(id=patient_id)
    vital_signs = patient.vitalsign_set.all().order_by('date_recorded')  # Ordem pela data registrada
    
    # Analisa os sinais vitais
    analyzed_signs = Analysis.objects.filter(patient=patient)

    # Combine as duas listas, usando zip_longest para lidar com listas de tamanho diferente
    combined_signs = zip_longest(vital_signs, analyzed_signs, fillvalue=None)

    # Passar o contexto para o template
    context = {
        'patient': patient,
        'combined_signs': combined_signs,  # Passa a lista combinada para o template
    }

    return render(request, 'app/vital_sign_history.html', {'vital_signs': vital_signs, 'patient': patient})

# Função para registrar um novo usuário
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        vital_sign_form = VitalSignForm(request.POST)
        
        if user_form.is_valid() and vital_sign_form.is_valid():
            # Salva o usuário
            user = user_form.save()
           # Supondo que o paciente é criado após o registro do usuário
            patient = user.patient  # Caso você tenha um campo de paciente associado ao usuário
            
            # Cria os sinais vitais para o paciente registrado
            vital_sign = vital_sign_form.save(commit=False)
            vital_sign.patient = patient  # Relaciona os sinais vitais com o paciente
            vital_sign.save()

            return redirect('login')  # Redireciona para a tela de login após o cadastro
    else:
        user_form = UserCreationForm()
        vital_sign_form = VitalSignForm()

    return render(request, 'app/register.html', {
        'user_form': user_form,
        'vital_sign_form': vital_sign_form,
    })
# Função para fazer login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')  # Verifique se a URL 'menu' está configurada corretamente
        else:
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'app/login.html')

# Função para fazer logout
def user_logout(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login

def menu(request):
    patients = Patient.objects.all()  # Obter todos os pacientes
    return render(request, 'app/menu.html', {'patients': patients})

def select_patient_for_vital_signs(request):
    # Obtém todos os pacientes
    patients = Patient.objects.all()
    
    # Renderiza o template e passa a lista de pacientes
    return render(request, 'app/select_patient_for_vital_signs.html', {'patients': patients})

# Função para excluir o paciente
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':  # Confirmação de exclusão
        patient.delete()  # Exclui o paciente
        messages.success(request, "Paciente excluído com sucesso!")
        return redirect('select_patient_for_vital_signs')  # Redireciona de volta à lista de pacientes

    # Exibe uma página de confirmação antes de excluir
    return render(request, 'app/confirm_delete_patient.html', {'patient': patient})

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            # Redireciona para a página de confirmação
            return confirm_edit_patient(request, patient_id)
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = PatientEditForm(instance=patient)

    return render(request, 'app/edit_patient.html', {'form': form, 'patient': patient})

def patient_list(request):
    patients = Patient.objects.all()  # Obtém todos os pacientes do banco de dados
    return render(request, 'patient_list.html', {'patients': patients})


def confirm_edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            # Armazena os dados do formulário em uma sessão para confirmação
            request.session['pending_patient_edit'] = form.cleaned_data
            return render(request, 'app/confirm_edit_patient.html', {
                'form': form,
                'patient': patient
            })

    return redirect('edit_patient', patient_id=patient.id)  # Retorna ao formulário se algo der errado


def save_edit_patient(request, patient_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        # Receber dados do formulário
        patient.name = request.POST.get('name', patient.name)
        age = request.POST.get('age')  # Captura o valor enviado para "age"

        if age:
            patient.age = int(age)  # Converte para inteiro se fornecido
        else:
            patient.age = None  # Define como None para campos nulos

        patient.save() 
        return redirect('success_page')
    
def success_page(request):
    return render(request, 'app/success_page.html', {'message': 'Dados salvos com sucesso!'})
