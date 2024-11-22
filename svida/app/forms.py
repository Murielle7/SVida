from django import forms
from .models import VitalSign
from .models import Patient

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact']  

class VitalSignForm(forms.ModelForm):
    class Meta:
        model = VitalSign
        fields = ['blood_pressure', 'heart_rate', 'breath_rate', 'temperature']

    # Validação para Pressão Arterial
    def clean_blood_pressure(self):
        blood_pressure = self.cleaned_data.get('blood_pressure')

        if blood_pressure:
            # Remove espaços extras e "mmHg" se presente
            blood_pressure = blood_pressure.replace(" ", "").replace("mmHg", "")

            # Verifica se o formato está correto: ex: "120x80"
            if 'x' not in blood_pressure:
                raise forms.ValidationError('A pressão arterial deve seguir o formato "120x80".')

            # Divide a string para separar sistólica e diastólica
            parts = blood_pressure.split('x')

            # Se não houver exatamente 2 partes, é um erro
            if len(parts) != 2:
                raise forms.ValidationError('Formato inválido. A pressão arterial deve ser no formato "120x80".')

            try:
                # Tenta converter as partes para inteiros
                systolic = int(parts[0])
                diastolic = int(parts[1])
            except ValueError:
                raise forms.ValidationError('A pressão arterial deve conter números válidos.')

            # Verifica se os valores da pressão estão dentro de uma faixa razoável
            if not (30 <= systolic <= 250 and 30 <= diastolic <= 150):
                raise forms.ValidationError('A pressão arterial deve estar dentro de uma faixa razoável.')

        else:
            raise forms.ValidationError('A pressão arterial é obrigatória.')

        return blood_pressure

    def clean_heart_rate(self):
        heart_rate = self.cleaned_data.get('heart_rate')
        if heart_rate:
            try:
                heart_rate = int(heart_rate)
            except ValueError:
                raise forms.ValidationError('A frequência cardíaca deve ser um número inteiro.')
        else:
            raise forms.ValidationError('A frequência cardíaca é obrigatória.')
        return heart_rate

    def clean_breath_rate(self):
        breath_rate = self.cleaned_data.get('breath_rate')
        if breath_rate:
            try:
                breath_rate = int(breath_rate)
            except ValueError:
                raise forms.ValidationError('A frequência respiratória deve ser um número inteiro.')
        else:
            raise forms.ValidationError('A frequência respiratória é obrigatória.')
        return breath_rate

    def clean_temperature(self):
        temperature = self.cleaned_data.get('temperature')
        if temperature:
            try:
                temperature = float(temperature)
            except ValueError:
                raise forms.ValidationError('A temperatura deve ser um número decimal.')
        else:
            raise forms.ValidationError('A temperatura é obrigatória.')
        return temperature
