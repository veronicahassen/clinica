from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.forms.widgets import SelectDateWidget
from .models import *


estudios = \
    [('Profesionales', 'Profesionales'),
    ('Especialidades', 'Especialidades'),
    ('Estudios', 'Estudios'),
    ('Precio', 'Precio')]


# Admin registration form
class AdminRegistrationForm(UserCreationForm):  # to register an admin
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1960, 2025)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su domicilio'}))
    address.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Pais'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Código postal'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña nuevamente'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode', 'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# Admin details update form
class AdminUpdateForm(forms.ModelForm):  # used to edit an admin instance
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2025)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode', 'image']


# Admin appointment form
class AdminAppointmentForm(forms.ModelForm):  # book an appointment by admin
    Profesionales = forms.TypedChoiceField(label='')  # dcotor is chosen from existing doctors in db
    Profesionales.widget.attrs.update({'class': 'app-form-control'})
    Pacientes = forms.TypedChoiceField(label='')  # patient is chosen from existing patient in db
    Pacientes.widget.attrs.update({'class': 'app-form-control'})
    app_date = forms.DateField(label='', widget=SelectDateWidget(years=range(2024, 2025)))  # appointment date
    app_date.widget.attrs.update({'class': 'app-form-control-date'})
    app_time = forms.TypedChoiceField(label='')  # time of appointment
    app_time.widget.attrs.update({'class': 'app-form-control'})
    description = forms.CharField(max_length=300, label='', widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    def __init__(self, *args, **kwargs):
        super(AdminAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['Profesionales'].choices = [(c.id, c.first_name + " " + c.last_name + " (" + c.especialidades + ")")
                                        for c in Profesionales.objects.filter(status=True).all()]
        # choose doctor from db
        self.fields['Paciente'].choices = [(c.id, c.first_name + " " + c.last_name + " (" + c.proveedor_seguro + ")")
                                        for c in Paciente.objects.filter(status=True).all()]
        # choose patient from db
        self.fields['app_time'].choices = [('8:00 AM', '8:00 AM'),('8:15 AM', '8:15 AM'),('8:30 AM', '8:30 AM'),('8:45 AM', '8:45 AM'), 
                                        ('9:00 AM', '9:00 AM'),('9:15 AM', '9:15 AM'),('9:30 AM', '9:30 AM'),('9:45 AM', '9:45 AM'),
                                        ('10:00 AM', '10:00 AM'),('10:15 AM', '10:15 AM'),('10:30 AM', '10:30 AM'),('10:45 AM', '10:45 AM'),
                                        ('11:00 AM', '11:00 AM'),('11:15 AM', '11:15 AM'),('11:30 AM', '11:30 AM'),('11:45 AM', '11:45 AM'),
                                        ('12:00 PM', '12:00 PM'),('12:15 PM', '12:15 PM'),('12:30 PM', '12:30 PM'),('12:45 PM', '12:45 PM'),
                                        ('13:00 PM', '13:00 PM'),('13:15 PM', '13:15 PM'),('13:30 PM', '13:30 PM'),('13:45 PM', '13:45 PM'),
                                        ('14:00 PM', '14:00 PM'),('14:15 PM', '14:15 PM'),('14:30 PM', '14:30 PM'),('14:45 PM', '14:45 PM'),
                                        ('15:00 PM', '15:00 PM'),('15:15 PM', '15:15 PM'),('15:30 PM', '15:30 PM'),('15:45 PM', '15:45 PM'),
                                        ('16:00 PM', '16:00 PM'),('16:15 PM', '16:15 PM'),('16:30 PM', '16:30 PM'),('16:45 PM', '16:45 PM'),
                                        ('17:00 PM', '17:00 PM'),('17:15 PM', '17:15 PM'),('17:30 PM', '17:30 PM'),('17:45 PM', '17:45 PM'),
                                        ('18:00 PM', '18:00 PM'),('18:15 PM', '18:15 PM'),('18:30 PM', '18:30 PM'),('18:45 PM', '18:45 PM'),
                                        ('19:00 PM', '19:00 PM'),('19:15 PM', '19:15 PM'),('19:30 PM', '19:30 PM'),('19:45 PM', '19:45 PM'),]
        # choices for time slot for appointment

    class Meta:
        model = Turnos
        fields = ['description', 'app_date', 'app_time']


# Patient registration form
class PacienteRegistrationForm(UserCreationForm):  # register patient
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apeliido'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1900, 2025)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    proveedores_seguros = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su proveedor de seguro/obra social'}))
    proveedores_seguros.widget.attrs.update({'class': 'app-form-control'})

    plan_seguro = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese el plan de seguro/obra social'}))
    plan_seguro.widget.attrs.update({'class': 'app-form-control'})

    numero_seguro = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Número de asociado'}))
    numero_seguro.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Pais'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Código Postal'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese nuevamente su contraseña'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = Paciente
        fields = ['username', 'email', 'first_name', 'last_name', 'dob', 'proveedores_seguros', 'plan_seguro', 'numero_seguro', 'city', 'country', 'postcode', 'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# Patient update form
class PacienteUpdateForm(forms.ModelForm):  # update patient details
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1900, 2025)))
    proveedores_seguros = forms.CharField()
    plan_seguro = forms.CharField()
    numero_seguro = forms.IntegerField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Paciente
        fields = ['first_name', 'last_name', 'dob', 'proveedores_seguros', 'plan_seguro', 'numero_seguro', 'city', 'country', 'postcode', 'image']


# Patient appointment form
class PacienteAppointmentForm(forms.ModelForm):  # make an appointment by patient
    estudios = forms.TypedChoiceField(label='')  # choose estudio from db
    estudios.widget.attrs.update({'class': 'app-form-control'})
    app_date = forms.DateField(label='', widget=SelectDateWidget(years=range(2024, 2025)))  # date of appointment
    app_date.widget.attrs.update({'class': 'app-form-control-date'})
    app_time = forms.TypedChoiceField(label='')  # time of appointment
    app_time.widget.attrs.update({'class': 'app-form-control'})
    description = forms.CharField(max_length=300, label='', widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    def __init__(self, *args, **kwargs):
        super(PacienteAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['estudios'].choices = [(e.id, e.first_name + " " + e.last_name + " (" + e.estudios + ")")
                                        for e in Estudios.objects.filter(status=True).all()]
        # choose estudio from db

        self.fields['app_time'].choices = [('8:00 AM', '8:00 AM'),('8:15 AM', '8:15 AM'),('8:30 AM', '8:30 AM'),('8:45 AM', '8:45 AM'), 
                                        ('9:00 AM', '9:00 AM'),('9:15 AM', '9:15 AM'),('9:30 AM', '9:30 AM'),('9:45 AM', '9:45 AM'),
                                        ('10:00 AM', '10:00 AM'),('10:15 AM', '10:15 AM'),('10:30 AM', '10:30 AM'),('10:45 AM', '10:45 AM'),
                                        ('11:00 AM', '11:00 AM'),('11:15 AM', '11:15 AM'),('11:30 AM', '11:30 AM'),('11:45 AM', '11:45 AM'),
                                        ('12:00 PM', '12:00 PM'),('12:15 PM', '12:15 PM'),('12:30 PM', '12:30 PM'),('12:45 PM', '12:45 PM'),
                                        ('13:00 PM', '13:00 PM'),('13:15 PM', '13:15 PM'),('13:30 PM', '13:30 PM'),('13:45 PM', '13:45 PM'),
                                        ('14:00 PM', '14:00 PM'),('14:15 PM', '14:15 PM'),('14:30 PM', '14:30 PM'),('14:45 PM', '14:45 PM'),
                                        ('15:00 PM', '15:00 PM'),('15:15 PM', '15:15 PM'),('15:30 PM', '15:30 PM'),('15:45 PM', '15:45 PM'),
                                        ('16:00 PM', '16:00 PM'),('16:15 PM', '16:15 PM'),('16:30 PM', '16:30 PM'),('16:45 PM', '16:45 PM'),
                                        ('17:00 PM', '17:00 PM'),('17:15 PM', '17:15 PM'),('17:30 PM', '17:30 PM'),('17:45 PM', '17:45 PM'),
                                        ('18:00 PM', '18:00 PM'),('18:15 PM', '18:15 PM'),('18:30 PM', '18:30 PM'),('18:45 PM', '18:45 PM'),
                                        ('19:00 PM', '19:00 PM'),('19:15 PM', '19:15 PM'),('19:30 PM', '19:30 PM'),('19:45 PM', '19:45 PM'),]
        # choices for time slot for appointment

    class Meta:
        model = Turnos
        fields = ['description', 'app_date', 'app_time']


# Dcctors registration form
class ProfesionalesRegistrationForm(UserCreationForm):  # register doctor
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1900, 2025)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ingrese su domiclio'}))
    address.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Pais'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Código Postal'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    especialidades = forms.CharField(label="", widget=forms.Select(choices=Especialidades))
    especialidades.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese nuevamente su contraseña'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = Profesionales
        fields = ['username', 'email', 'profesional_nombre', 'last_name', 'especialidades', 'dob', 'address', 'city', 'country', 'postcode', 'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

    def check_date(self):  # form date of birth validator
        cleaned_data = self.cleaned_data
        dob = cleaned_data.get('dob')
        if dob < timezone.now().date():
            return True
        self.add_error('dob', 'Invalid date of birth.')
        return False


# Doctor update details form
class ProfesionalesUpdateForm(forms.ModelForm):  # update doctor details
    first_name = forms.CharField()
    last_name = forms.CharField()
    # age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1900, 2025)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    appfees = forms.FloatField()
    admfees = forms.FloatField()

    class Meta:
        model = Profesionales
        fields = ['first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode', 'image',
        'appfees', 'admfees']


# Doctor/Admin confirms attendance appointment form
class AppointmentConfirmationForm(forms.ModelForm):  # doctor/Admin confirms an appointment
    description = forms.CharField(max_length=300, label='', widget=forms.TextInput(attrs={'placeholder': 'DESCRIPCION'}))
    description.widget.attrs.update({'class': 'app-form-control'})
    approval_date = forms.DateField(label='', widget=SelectDateWidget)
    approval_date.widget.attrs.update({'class': 'app-form-control-date'})

    class Meta:
        model = IngresoPaciente
        fields = ['description', 'approval_date']


# Dcotor edit appointment form
class AppointmentUpdateForm(forms.ModelForm):
    # dcotor can edit appointment description field, be it adding new lines or deleting a few of the old one
    description = forms.CharField(max_length=300, label='', widget=forms.TextInput(attrs={'placeholder': 'DESCRIPCION'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = Turnos
        fields = ['description']



class EstudiosAdminForm(forms.ModelForm):
    class Meta:
        model = Estudios
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'especialidad' in self.data:
                pass
        elif self.instance.pk:
            self.fields['profesional'].queryset = self.instance.especialidad.profesionales.all()