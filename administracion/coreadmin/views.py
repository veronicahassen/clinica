from django.conf import settings
from django.core import serializers
from django.core.mail import send_mail, mail_admins
from django.db.models.functions import TruncMonth
from . import forms, models
from datetime import date, time
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect
from xhtml2pdf import pisa # type: ignore
from coreadmin.forms import AdminRegistrationForm, AdminUpdateForm, AdminAppointmentForm, PacienteRegistrationForm, \
    PacienteUpdateForm, PacienteAppointmentForm, ProfesionalesRegistrationForm, ProfesionalesUpdateForm, AppointmentUpdateForm, \
    AppointmentConfirmationForm
from coreadmin.models import Admin, Profesionales, Paciente, Turnos, Estudios, IngresoPaciente
import datetime
from django.shortcuts import render, get_object_or_404
from .models import IngresoPaciente, Paciente, Estudios
from django.http import HttpResponse

def log_patient(request, paciente_id, estudio_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    servicio = get_object_or_404(Estudios, pk=estudio_id)
    ingreso_paciente = IngresoPaciente.objects.create(paciente=paciente, estudio=Estudios)
    ingreso_paciente.log_patient_and_charge_fee()
    return HttpResponse("Paciente ingresado y pago registrado.")


# Home
def home_view(request):  # Homepage
    return render(request, 'coreadmin/home/index.html')


# Account
def login_view(request):  # Login
    return render(request, 'coreadmin/account/login.html')


# Admin
def register_adm_view(request):  # register admin
    if request.method == "POST":
        registration_form = AdminRegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():  # get data from form (if it is valid)
            dob = registration_form.cleaned_data.get('dob')  # get date of birth from form
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # calculate age from dob
            if dob < timezone.now().date():  # check if date of birth is valid (happened the previous day or even back)
                new_user = User.objects.create_user(username=registration_form.cleaned_data.get('username'),
                                                    email=registration_form.cleaned_data.get('email'),
                                                    password=registration_form.cleaned_data.get(
                                                        'password1'))  # create user
                adm = Admin(admin=new_user,
                            first_name=registration_form.cleaned_data.get('first_name'),
                            last_name=registration_form.cleaned_data.get('last_name'),
                            # age=form.cleaned_data.get('age'),
                            dob=registration_form.cleaned_data.get('dob'),
                            address=registration_form.cleaned_data.get('address'),
                            city=registration_form.cleaned_data.get('city'),
                            country=registration_form.cleaned_data.get('country'),
                            postcode=registration_form.cleaned_data.get('postcode'),
                            image=request.FILES['image']
                            )  # create admin
                adm.save()
                group = Group.objects.get_or_create(name='Admin')  # add user to admin group
                group[0].user_set.add(new_user)

                messages.add_message(request, messages.INFO, 'Registration successful!')
                return redirect('login_adm.html')
            else:
                registration_form.add_error('dob', 'Invalid date of birth.')
        else:
            print(registration_form.errors)
            return render(request, 'appointments/admin/register_adm.html', {'registration_form': registration_form})
    else:
        registration_form = AdminRegistrationForm()

    return render(request, 'appointments/admin/register_adm.html', {'registration_form': registration_form})


# Login admin
def login_adm_view(request):  # login admin
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')  # get username
            password = login_form.cleaned_data.get('password')  # get password
            user = auth.authenticate(username=username, password=password)  # authenticate user
            if user is not None and check_admin(user):  # if user exists and is admin
                auth.login(request, user)  # login user
                account_approval = Admin.objects.all().filter(status=True,admin_id=request.user.id)  # if account is approved
                if account_approval:
                    return redirect('profile_adm.html')
                    # return redirect('dashboard_adm.html')
                else:  # if account is not yet approved
                    auth.logout(request)
                    messages.add_message(request, messages.INFO, 'Your account is currently pending. ''Please wait for approval.')
                    return render(request, 'coreadmin/admin/login_adm.html', {'login_form': login_form})
        return render(request, 'coreadmin/admin/login_adm.html', {'login_form': login_form})
    else:
        login_form = AuthenticationForm()

    return render(request, 'coreadmin/admin/login_adm.html', {'login_form': login_form})


# Admin dashboard
@login_required(login_url='login_adm.html')
def dashboard_adm_view(request):
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        adm_det = Admin.objects.all().filter(status=False)
        prof = Profesionales.objects.all().filter(status=False)  # get all on-hold profesionales
        pac = Paciente.objects.all().filter(status=False)  # get all on-hold pacientes
        app = Turnos.objects.all().filter(status=False)  # get all on-hold appointments

        adm_total = Admin.objects.all().count()  # total pacientes
        pac_total = Paciente.objects.all().count()  # total pacientes
        prof_total = Profesionales.objects.all().count()  # get total profesionales
        app_total = Turnos.objects.all().count()  # get total appointments

        pending_adm_total = Admin.objects.all().filter(status=False).count()  # count onhold admins
        pending_pac_total = Paciente.objects.all().filter(status=False).count()  # get total onhold pacientes
        pending_prof_total = Profesionales.objects.all().filter(status=False).count()  # get total onhold profesionales
        pending_app_total = Turnos.objects.all().filter(status=False).count()  # get total onhold appointments

        messages.add_message(request, messages.INFO, 'Hay {0} turnos que requieren ingreso.'.format(pending_app_total))

        context = {'adm': adm, 'prof': prof, 'pac': pac, 'app': app, 'adm_det': adm_det,
                    'adm_total': adm_total, 'pac_total': pac_total, 'prof_total': prof_total, 'app_total': app_total,
                    'pending_adm_total': pending_adm_total, 'pending_pac_total': pending_pac_total,
                    'pending_prof_total': pending_prof_total,
                    'pending_app_total': pending_app_total}  # render information

        return render(request, 'coreadmin/admin/dashboard_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Admin profile
@login_required(login_url='login_adm.html')
def profile_adm_view(request):
    if check_admin(request.user):
        # get information from database
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        dob = adm.dob
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if request.method == "POST":  # profile is updated
            admin_update_form = AdminUpdateForm(request.POST, request.FILES, instance=adm)
            if admin_update_form.is_valid():
                admin_update_form.save()  # save changes in profile

                messages.add_message(request, messages.INFO, 'Profile updated successfully!')
                return redirect('profile_adm.html')
        else:
            admin_update_form = AdminUpdateForm(instance=adm)
        context = {  # render information on webpage
            'admin_update_form': admin_update_form,
            'adm': adm,
            'age': age
        }
        return render(request, 'coreadmin/admin/profile_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Admin book appointment
@login_required(login_url='login_adm.html')
def book_app_adm_view(request):  # book appointment
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        if request.method == "POST":  # if form is submitted
            app_form = AdminAppointmentForm(request.POST)
            if app_form.is_valid():
                profesional_id = app_form.cleaned_data.get('profesionales')  # get profesional id
                paciente_id = app_form.cleaned_data.get('pacientes')  # get paciente id
                est = Estudios.objects.all().filter(id=1).first()
                prof = Profesionales.objects.all().filter(id=profesional_id).first()  # get profesional
                pac = Paciente.objects.all().filter(id=paciente_id).first()  # get paciente

                if check_estudio_availability(est, app_form.cleaned_data.get('app_date'),app_form.cleaned_data.get('app_time')):  # check if appointment is available during that slot
                    app = Turnos(Profesionales=prof, Estudios=est, Paciente=pac,
                                description=app_form.cleaned_data.get('description'),
                                app_date=app_form.cleaned_data.get('app_date'),
                                app_time=app_form.cleaned_data.get('app_time'),
                                status=True)  # create new appointment
                    app.save()
                    messages.add_message(request, messages.INFO, 'Turno creado.')
                    return redirect('book_app_adm.html')
                else:  # if slot is not available, display error
                    messages.add_message(request, messages.INFO, 'No disponible.')
                    return render(request, 'coreadmin/admin/book_app_adm.html', {'app_form': app_form})
            else:
                messages.add_message(request, messages.INFO, 'Error al crear el turno. Por favor, intente nuevamente.')
                print(app_form.errors)
        else:
            app_form = AdminAppointmentForm()
        return render(request, 'coreadmin/admin/book_app_adm.html', {'adm': adm, 'app_form': app_form})
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Admin download summary report
def dl_report_adm_action(request):
    template_path = 'templates/coreadmin/admin/summary_report.html'

    adm = Admin.objects.filter(admin_id=request.user.id).first()
    adm_det = Admin.objects.all().filter(status=False)
    prof = Profesionales.objects.all().filter(status=False)  # get all on-hold profesionales
    pac = Paciente.objects.all().filter(status=False)  # get all on-hold pacientes
    app = Turnos.objects.all().filter(status=False)  # get all on-hold appointments

    adm_total = Admin.objects.all().count()  # total pacientes
    pac_total = Paciente.objects.all().count()  # total pacientes
    prof_total = Profesionales.objects.all().count()  # get total profesionales
    app_total = Turnos.objects.all().count()  # get total appointments

    pending_adm_total = Admin.objects.all().filter(status=False).count()  # count onhold admins
    pending_pac_total = Paciente.objects.all().filter(status=False).count()  # get total onhold pacientes
    pending_prof_total = Profesionales.objects.all().filter(status=False).count()  # get total onhold profesionales
    pending_app_total = Turnos.objects.all().filter(status=False).count()  # get total onhold appointments

    context = {'adm': adm, 'prof': prof, 'pac': pac, 'app': app, 'adm_det': adm_det,
                'adm_total': adm_total, 'pac_total': pac_total, 'prof_total': prof_total, 'app_total': app_total,
                'pending_adm_total': pending_adm_total, 'pending_pac_total': pending_pac_total,
                'pending_prof_total': pending_prof_total,
                'pending_app_total': pending_app_total}

    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clinica-seprice-summary-report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Admin fulfilled appointment
@login_required(login_url='login_adm.html')
def approve_app_adm_action(request, pk):
    if check_admin(request.user):
        # get information from database
        turnos = Turnos.objects.get(id=pk)
        turnos.status = True  # approve appointment
        turnos.save()

        messages.success(request, "Turno completado.")
        return redirect(reverse('view_all_app_adm.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# All appointments: pending, incomplete, completed
@login_required(login_url='login_adm.html')
def all_app_adm_view(request):
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        app = Turnos.objects.all().filter(status=False)
        appointment_app = Turnos.objects.all().filter(status=False).count()
        app_count = Turnos.objects.all().count()
        pending_app_total = Turnos.objects.all().filter(status=False).count()
        approved_app_total = Turnos.objects.all().filter(status=True).count()

        appointment_details = []
        for app in Turnos.objects.filter(status=True).all():  # get approved appointments
            p = app.profesional
            e = app.estudio
            c = app.paciente
            if p and e and c:
                appointment_details.append([p.first_name, p.last_name, e.especialidad,
                                            e.name,
                                            c.first_name, c.last_name, c.proveedor_seguro_name,
                                            app.description, app.app_date, app.app_time,
                                            app.pk, app.completed, app.status])  # render information

        pending_appointment_details = []
        for app in Turnos.objects.filter(status=False).all():  # get pending appointments
            p = app.profesional
            e = app.estudio
            c = app.paciente
            if p and e and c:
                pending_appointment_details.append([p.first_name, p.last_name, e.especialidad,
                                            e.name,
                                            c.first_name, c.last_name, c.proveedor_seguro_name,
                                            app.description, app.app_date, app.app_time,
                                            app.pk, app.completed, app.status])  # render information

        return render(request, 'coreadmin/admin/view_all_app_adm.html',
                        {'adm': adm, 'app': app, 'appointment_app': appointment_app, 'app_count': app_count,
                        'pending_app_total': pending_app_total, 'approved_app_total': approved_app_total,
                        'appointment_details': appointment_details,
                        'pending_appointment_details': pending_appointment_details})
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Admin appointment view
@login_required(login_url='login_adm.html')
def appointment_adm_view(request):
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        app = Turnos.objects.all().filter(status=False)
        appointment_app = Turnos.objects.all().filter(status=False).count()
        app_count = Turnos.objects.all().count()
        pending_app_total = Turnos.objects.all().filter(status=False).count()
        approved_app_total = Turnos.objects.all().filter(status=True).count()
        context = {'adm': adm, 'app': app, 'appointment_app': appointment_app, 'app_count': app_count,
                    'pending_app_total': pending_app_total, 'approved_app_total': approved_app_total}
        return render(request, 'coreadmin/admin/appointment_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approved appointment's details
@login_required(login_url='login_adm.html')
def app_details_adm_view(request, pk):
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()

        app = Turnos.objects.filter(id=pk).first()  # get appointment
        prof = app.profesional
        pac = app.paciente

        app.app_link = pac.first_name

        appointment_details = [prof.first_name, prof.last_name, prof.especialidad,
                                pac.first_name, pac.last_name, pac.proveedor_servicios_name, pac.numero_asociado,
                                app.app_date, app.app_time, app.app_link, app.description,
                                app.status, app.completed, pk]  # render fields

        return render(request, 'appointments/admin/view_app_details_adm.html',
                        {'adm': adm,
                        'prof': prof,
                        'app': app,
                        'pac': pac,
                        'appointment_details': appointment_details})
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Complete appointment action
@login_required(login_url='login_adm.html')
def complete_app_adm_action(request, pk):
    if check_admin(request.user):
        # get information from database and render in html webpage
        app = Turnos.objects.get(id=pk)
        app.completed = True
        app.save()

        messages.add_message(request, messages.INFO, 'Turno finalizado')
        return redirect('view_all_app_adm.html')
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Statistics page
@login_required(login_url='login_adm.html')
def statistics_adm_view(request):
    if check_admin(request.user):
        prof = Profesionales.objects.all().filter(status=False)  # get all on-hold profesionales
        pac = Paciente.objects.all().filter(status=False)  # get all on-hold pacientes

        pac_total = Paciente.objects.all().count()  # total pacientes
        prof_total = Profesionales.objects.all().count()  # get total profesionales
        app_total = Turnos.objects.all().count()  # get total appointments

        pending_pac_total = Paciente.objects.all().filter(status=False).count()  # get total onhold pacientes
        pending_prof_total = Profesionales.objects.all().filter(status=False).count()  # get total onhold profesionales
        pending_app_total = Turnos.objects.all().filter(status=False).count()  # get total onhold appointments

        context = {'prof': prof, 'pac': pac,
                    'pac_total': pac_total, 'prof_total': prof_total, 'app_total': app_total,
                    'pending_pac_total': pending_pac_total, 'pending_prof_total': pending_prof_total,
                    'pending_app_total': pending_app_total}  # render information

        return render(request, 'coreadmin/admin/view_statistics_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# View statistics (pivot data)
@login_required(login_url='login_adm.html')
def pivot_data(request):
    dataset = Turnos.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


# paciente section
@login_required(login_url='login_adm.html')
def paciente_adm_view(request):
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        pac = Paciente.objects.all().filter(status=False)
        pac_approved = Paciente.objects.all().filter(status=True).count()
        pac_pending = Paciente.objects.all().filter(status=False).count()
        pac_count = Paciente.objects.all().count()
        context = {'adm': adm, 'pac': pac, 'pac_pending': pac_pending, 'pac_approved': pac_approved,'pac_count': pac_count}
        return render(request, 'coreadmin/admin/paciente_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approve paciente account
@login_required(login_url='login_adm.html')
def approve_pac_adm_view(request):  # Approve paciente
    # get information from database and render in html webpage
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        pac = Paciente.objects.all().filter(status=False)
        pac_approved = Paciente.objects.all().filter(status=True).count()
        pac_pending = Paciente.objects.all().filter(status=False).count()
        pac_count = Paciente.objects.all().count()

        context = {'adm': adm, 'pac': pac, 'pac_pending': pac_pending, 'pac_approved': pac_approved, 'pac_count': pac_count}

        return render(request, 'coreadmin/admin/approve_pac.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


#  Receive patient action
@login_required(login_url='login_adm.html')
def approve_pac_adm_action(request, pk):
    if check_admin(request.user):
        # get information from database
        pac = Paciente.objects.get(id=pk)
        pac.status = True  # approve paciente
        pac.save()

        messages.add_message(request, messages.INFO, 'Paciente ingresado correctamente')
        return redirect(reverse('approve_pac.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# View all pacientes
@login_required(login_url='login_adm.html')
def all_pac_adm_view(request):  # View all pacientes
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        pac = Paciente.objects.all().filter(status=False)
        pac_approved = Paciente.objects.all().filter(status=True).count()
        pac_pending = Paciente.objects.all().filter(status=False).count()
        pac_count = Paciente.objects.all().count()
        pac_details = []

        for pac in Paciente.objects.filter(status=True).all():
            pac_details.append([pac.id, pac.image.url,
                                pac.first_name, pac.last_name, pac.dob,
                                pac.proveedor_servicio_name, pac.numero_asociado, pac.status])

        context = {'adm': adm, 'pac': pac, 'pac_pending': pac_pending, 'pac_approved': pac_approved,
                    'pac_count': pac_count, 'pac_details': pac_details}

        return render(request, 'coreadmin/admin/view_all_pac.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Profesionales section
@login_required(login_url='login_adm.html')
def profesional_adm_view(request):  # view profesionales
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        prof = Profesionales.objects.all().filter(status=False)
        prof_approved = Profesionales.objects.all().filter(status=True).count()
        prof_pending = Profesionales.objects.all().filter(status=False).count()
        prof_count = Profesionales.objects.all().count()
        context = {'adm': adm, 'prof': prof, 'prof_approved': prof_approved, 'prof_pending': prof_pending,
                    'prof_count': prof_count}
        return render(request, 'coreadmin/admin/profesional_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approve profesional account
@login_required(login_url='login_adm.html')
def approve_prof_adm_view(request):
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        prof = Profesionales.objects.all().filter(status=False)
        prof_approved = Profesionales.objects.all().filter(status=True).count()
        prof_pending = Profesionales.objects.all().filter(status=False).count()
        prof_count = Profesionales.objects.all().count()
        context = {'adm': adm, 'prof': prof, 'prof_approved': prof_approved, 'prof_pending': prof_pending, 'prof_count': prof_count}
        return render(request, 'coreadmin/admin/approve_prof.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approve profesionales action
@login_required(login_url='login_adm.html')
def approve_prof_adm_action(request, pk):
    if check_admin(request.user):
        # get information from database
        prof = Profesionales.objects.get(id=pk)
        prof.status = True  # approve profesionales
        prof.save()

        messages.add_message(request, messages.INFO, 'Profesional aprobado exitosamente.')
        return redirect(reverse('approve_prof.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# View all profesionales
@login_required(login_url='login_adm.html')
def all_prof_adm_view(request):
    # get information from database and render in html webpage
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        prof = Profesionales.objects.all().filter(status=False)
        prof_approved = Profesionales.objects.all().filter(status=True).count()
        prof_pending = Profesionales.objects.all().filter(status=False).count()
        prof_count = Profesionales.objects.all().count()

        prof_details = []
        for p in Profesionales.objects.filter(status=True).all():
            est = Estudios.objects.filter(profesional=p).first()
            prof_details.append(
                [p.id, p.image.url, p.first_name, p.last_name, p.dob, p.address, p.postcode, p.city, p.country, p.especialidad_id, p.status, est.app_total])

        context = {'adm': adm, 'prof': prof, 'prof_approved': prof_approved, 'prof_pending': prof_pending,
                    'prof_count': prof_count, 'prof_details': prof_details}

        return render(request, 'coreadmin/admin/view_all_prof.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# View admin
@login_required(login_url='login_adm.html')
def admin_adm_view(request):
    # get information from database and render in html webpage
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        adm_details = Admin.objects.all().filter()
        adm_approved = Admin.objects.all().filter(status=True).count()
        adm_pending = Admin.objects.all().filter(status=False).count()
        adm_count = Admin.objects.all().count()
        context = {'adm': adm,
                    'adm_details': adm_details,
                    'adm_approved': adm_approved,
                    'adm_pending': adm_pending,
                    'adm_count': adm_count}
        return render(request, 'coreadmin/admin/admin_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approve admin account
@login_required(login_url='login_adm.html')
def approve_adm_adm_view(request):
    if check_admin(request.user):
        # get information from database and render in html webpage
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        adm_details = Admin.objects.all().filter(status=False)
        adm_approved = Admin.objects.all().filter(status=True).count()
        adm_pending = Admin.objects.all().filter(status=False).count()
        adm_count = Admin.objects.all().count()
        context = {'adm': adm,
                    'adm_details': adm_details,
                    'adm_approved': adm_approved,
                    'adm_pending': adm_pending,
                    'adm_count': adm_count}

        return render(request, 'coreadmin/admin/approve_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Approve admin action
@login_required(login_url='login_adm.html')
def approve_adm_adm_action(request, pk):
    if check_admin(request.user):
        # get information from database
        adm = Admin.objects.get(id=pk)
        adm.status = True  # approve admin
        adm.save()
        messages.add_message(request, messages.INFO, 'Admin approved successfully.')
        return redirect(reverse('approve_adm.html'))
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# View all admins
@login_required(login_url='login_adm.html')
def all_adm_adm_view(request):
    if check_admin(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()
        adm_approved = Admin.objects.all().filter(status=True).count()
        adm_pending = Admin.objects.all().filter(status=False).count()
        adm_count = Admin.objects.all().count()

        # get information from database and render in html webpage
        adm_details = []
        for a in Admin.objects.all():
            adm_details.append(
                [a.id, a.image.url, a.first_name, a.last_name, a.dob, a.address, a.city, a.country, a.postcode, a.status])

        context = {'adm': adm, 'adm_approved': adm_approved, 'adm_pending': adm_pending, 'adm_count': adm_count, 'adm_details': adm_details}

        return render(request, 'coreadmin/admin/view_all_adm.html', context)
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Paciente
def register_pac_view(request):  # Register paciente
    if request.method == "POST":
        registration_form = PacienteRegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():  # if form is valid
            dob = registration_form.cleaned_data.get('dob')  # ger date of birth from form
            if dob < timezone.now().date():  # check if date is valid
                new_user = User.objects.create_user(username=registration_form.cleaned_data.get('username'),
                                                    email=registration_form.cleaned_data.get('email'),
                                                    password=registration_form.cleaned_data.get(
                                                        'password1'))  # create use
                c = Paciente(paciente=new_user,
                            first_name=registration_form.cleaned_data.get('first_name'),
                            last_name=registration_form.cleaned_data.get('last_name'),
                            dob=registration_form.cleaned_data.get('dob'),
                            proveedor_seguro_name=registration_form.cleaned_data.get('proveedor_seguro_name'),
                            numero_asociado=registration_form.cleaned_data.get('numero_asociado'),
                            image=request.FILES['image']
                            )  # create patient
                c.save()

                group = Group.objects.get_or_create(name='Paciente')  # add user to patient group
                group[0].user_set.add(new_user)

                messages.add_message(request, messages.INFO, '¡Registro exitoso!')
                return redirect('login_pac.html')
            else:  # if date of birth is invalid
                registration_form.add_error('dob', 'Invalid date of birth.')
                return render(request, 'coreadmin/paciente/register_pac.html', {'registration_form': registration_form})
        else:
            print(registration_form.errors)
    else:
        registration_form = PacienteRegistrationForm()
    return render(request, 'coreadmin/paciente/register_pac.html', {'registration_form': registration_form})


# Login paciente
def login_pac_view(request):  # Login paciente
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():  # if form is valid
            username = login_form.cleaned_data.get('username')  # get username from form
            password = login_form.cleaned_data.get('password')  # get password from form
            user = auth.authenticate(username=username, password=password)  # get user
            if user is not None and check_paciente(user):  # if user exists and is a paciente
                auth.login(request, user)  # login
                account_approval = Paciente.objects.all().filter(status=True, paciente_id=request.user.id)
                if account_approval:  # if account is approved
                    return redirect('profile_pac.html')
                else:  # if not approved, redirect to wait_approval webpage
                    messages.add_message(request, messages.INFO, 'Su cuenta se encuentra pendiente de aprobación. Por favor, espere.')
                    return render(request, 'coreadmin/paciente/login_pac.html', {'login_form': login_form})
        return render(request, 'coreadmin/paciente/login_pac.html', {'login_form': login_form})
    else:
        login_form = AuthenticationForm()

    return render(request, 'coreadmin/paciente/login_pac.html', {'login_form': login_form})


# Paciente profile
@login_required(login_url='login_pac.html')
def profile_pac_view(request):
    if check_paciente(request.user):
        # get information from database and render in html webpage
        pac = Paciente.objects.filter(pac_id=request.user.id).first()
        dob = pac.dob
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # calculate age
        if request.method == "POST":
            paciente_update_form = PacienteUpdateForm(request.POST, request.FILES, instance=pac)
            if paciente_update_form.is_valid():  # if form is valid
                dob = paciente_update_form.cleaned_data.get('dob')  # get date of birth from form
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if dob < timezone.now().date():  # if date of birth is valid
                    paciente_update_form.save()  # save details
                    pac.age = pac  # save age
                    pac.save()

                    messages.add_message(request, messages.INFO, '¡Perfil actualizado exitosamente!')
                    return redirect('profile_pac.html')
                else:
                    paciente_update_form.add_error('dob', 'Invalid date of birth.')
                    context = {
                        'paciente_update_form': paciente_update_form,
                        'pac': pac,
                        'age': age
                    }
                    return render(request, 'coreadmin/paciente/profile_pac.html', context)
            else:
                print(paciente_update_form.errors)
        paciente_update_form = PacienteUpdateForm(instance=pac)
        context = {
            'paciente_update_form': paciente_update_form,
            'pac': pac,
            'age': age
        }
        return render(request, 'coreadmin/paciente/profile_pac.html', context)
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# paciente book appointment
@login_required(login_url='login_prof.html')
def book_app_pac_view(request):
    if check_paciente(request.user):
        pac = Paciente.objects.filter(paciente_id=request.user.id).first()
        app_details = []

        for app in Turnos.objects.filter(paciente=pac, status=False).all():
            p = app.profesional
            if p:
                app_details.append([p.first_name, p.last_name, p.especialidad, app.description, app.app_date, app.app_time, app.status])

        if request.method == "POST":  # if paciente books an appointment
            app_form = PacienteAppointmentForm(request.POST)

            if app_form.is_valid():  # if form is valid
                prof_id = int(app_form.cleaned_data.get('profesional'))  # get profesional id from form
                prof = Profesionales.objects.all().filter(id=prof_id).first()  # get profesional from form
                est = prof.estudio_nombre
                if check_estudio_availability(est,  # check if estudio is available during that slot
                                            app_form.cleaned_data.get('app_date'),
                                            app_form.cleaned_data.get('app_time')):
                    app_date = app_form.cleaned_data.get('app_date')  # get appointment date
                    if timezone.now().date() < app_date:  # check if appointment date is valid
                        app = Turnos(profesional=prof,
                                        estudio=est,
                                        paciente=pac,
                                        description=app_form.cleaned_data.get('description'),
                                        app_date=app_form.cleaned_data.get('app_date'),
                                        app_time=app_form.cleaned_data.get('app_time'),
                                        status=False)  # create appointment instance, which is unapproved
                        app.save()
                        messages.add_message(request, messages.INFO, 'Su turno ha sido reservado.')
                        return redirect('book_app_pac.html')
                    else:
                        app_form.add_error('app_date', 'Invalid date.')
                else:  # if estudio is busy
                    app_form.add_error('app_time', 'No disponible.')
                return render(request, 'coreadmin/paciente/book_app_pac.html', {'app_form': app_form, 'app_details': app_details})
            else:  # if form is invalid
                print(app_form.errors)
        else:
            app_form = PacienteAppointmentForm()
        return render(request, 'coreadmin/paciente/book_app_pac.html',
                        {'est': est, 'pac': pac, 'app_form': app_form, 'app_details': app_details})
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# View paciente appointment dashboard
@login_required(login_url='login_pac.html')
def app_pac_view(request):
    if check_paciente(request.user):
        # get information from database and render in html webpage
        pac = Paciente.objects.filter(paciente_id=request.user.id).first()

        total_app = Turnos.objects.filter(paciente=pac).count()
        total_approved_app =Turnos.objects.filter(status=True, paciente=pac).count()
        total_pending_app = Turnos.objects.filter(status=False, paciente=pac).count()
        # app_total = Appointment.objects.filter(status=True, paciente=pac).all()

        pending_appointment_details = []
        for app in Turnos.objects.filter(status=False, completed=False, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                pending_appointment_details.append(
                    [p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                    app.pk, app.description, app.app_date, app.app_time, app.app_link,
                    app.status, app.completed, app.rating])

        incomplete_appointment_details = []
        for app in Turnos.objects.filter(status=True, completed=False, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                incomplete_appointment_details.append(
                    [p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                    app.pk, app.description, app.app_date, app.app_time, app.app_link,
                    app.status, app.completed, app.rating])

        appointment_details = []
        for app in Turnos.objects.filter(status=True, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                appointment_details.append([p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                                            app.pk, app.description, app.app_date, app.app_time, app.app_link,
                                            app.status, app.completed, app.rating])

        messages.add_message(request, messages.INFO, 'Ustes tiene {0} turnos pendientes.'.format(total_pending_app))

        context = {
            'pac': pac,
            'total_app': total_app,
            'total_approved_app': total_approved_app,
            'total_pending_app': total_pending_app,
            'pending_appointment_details': pending_appointment_details,
            'appointment_details': appointment_details,
            'incomplete_appointment_details': incomplete_appointment_details,
            # 'message': message
        }

        return render(request, 'coreadmin/paciente/view_app_pac.html', context)
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# View all paciente appointments
@login_required(login_url='login_prof.html')
def all_app_pac_view(request):
    if check_paciente(request.user):
        # get information from database and render in html webpage
        pac = Paciente.objects.filter(paciente_id=request.user.id).first()

        total_app = Turnos.objects.filter(paciente=pac).count()
        total_approved_app = Turnos.objects.filter(status=True, paciente=pac).count()
        total_pending_app = Turnos.objects.filter(status=False, paciente=pac).count()
        # app_total = Turnos.objects.filter(status=True, paciente=pac).all()

        pending_appointment_details = []
        for app in Turnos.objects.filter(status=False, completed=False, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                pending_appointment_details.append(
                    [p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                    app.pk, app.description, app.app_date, app.app_time, app.app_link,
                    app.status, app.completed, app.rating])

        incomplete_appointment_details = []
        for app in Turnos.objects.filter(status=True, completed=False, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                incomplete_appointment_details.append(
                    [p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                    app.pk, app.description, app.app_date, app.app_time, app.app_link,
                    app.status, app.completed, app.rating])

        completed_appointment_details = []
        for app in Turnos.objects.filter(status=True, completed=True, paciente=pac).all():  # get all approved appointments
            p = app.profesional
            c = app.paciente
            if p and c:
                completed_appointment_details.append(
                    [p.first_name, p.last_name, p.estudio, c.first_name, c.last_name,
                    app.pk, app.description, app.app_date, app.app_time, app.app_link,
                    app.status, app.completed, app.rating])

        messages.add_message(request, messages.INFO, 'Usted tiene {0} turnos.'.format(total_approved_app))

        context = {
            'pac': pac,
            'total_app': total_app,
            'total_approved_app': total_approved_app,
            'total_pending_app': total_pending_app,
            'pending_appointment_details': pending_appointment_details,
            'completed_appointment_details': completed_appointment_details,
            'incomplete_appointment_details': incomplete_appointment_details,
        }

        return render(request, 'coreadmin/paciente/view_all_app_pac.html', context)
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# Appointment rating
@login_required(login_url='login_prof.html')


# View approved appointment's details
@login_required(login_url='login_prof.html')
def app_details_pac_view(request, pk):
    if check_paciente(request.user):
        app = Turnos.objects.filter(id=pk).first()  # get appointment
        prof = app.profesional
        pac = app.paciente

        app.app_link = pac.first_name

        appointment_details = [prof.first_name, prof.last_name, prof.service_field,
                                pac.first_name, pac.last_name,
                                pac.proveedor_servicio_name, pac.numero_asociado,
                                app.app_date, app.app_time, app.app_link, app.description,
                                app.status, app.completed, pk]  # render fields
        return render(request, 'coreadmin/paciente/view_app_details_pac.html',
                    {'prof': prof,
                    'app': app,
                    'pac': pac,
                    'appointment_details': appointment_details})

    else:
        auth.logout(request)
        return redirect('login_pac.html')


# Join meeting
@login_required(login_url='login_pac.html')
def join_meeting_pac_view(request):
    if check_paciente(request.user):
        # get information from database and render in html webpage
        pac = Paciente.objects.get(paciente_id=request.user.id)
        total_app = Turnos.objects.filter(paciente=pac).count()
        total_approved_app = Turnos.objects.filter(status=True, paciente=pac).count()
        total_pending_app = Turnos.objects.filter(status=False, paciente=pac).count()

        app_details = []
        for app in Turnos.objects.filter(status=True, paciente=pac,app_link__isnull=True).all():  # get all approved appointments with room name
            p = app.profesional
            if p:
                app.app_link = pac.first_name
                app_details.append([app.pk, p.first_name, p.last_name, p.estudio,
                                    app.app_date, app.app_time, app.description, app.app_link, app.status])

        prof_details = []
        for est in Estudios.objects.all():  # get all profesional estudios instances
            e = est.profesional
            dob = e.dob
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if e.status:
                prof_details.append([p.first_name, p.last_name, p.estudio, est.app_total])

        return render(request, 'coreadmin/paciente/join_meeting_pac.html',
                    {'pac': pac, 'total_app': total_app,
                    'total_approved_app': total_approved_app,
                    'total_pending_app': total_pending_app,
                    'app_details': app_details,
                    'prof_details': prof_details})
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# Appointment report
@login_required(login_url='login_prof.html')
def app_report_pac_view(request, pk):
    # get information from database and render in html webpage
    app = Turnos.objects.all().filter(id=pk).first()
    pac = app.paciente
    prof = app.profesional
    app_date = app.calldate
    app_time = app.calltime

    app_details = []

    context = {
        'pac_name': pac.first_name,
        'prof_name': prof.first_name,
        'app_date': app_date,
        'app_time': app_time,
        'app_desc': app.description,
        'pac_proveedor_seguro': app.proveedor_seguro,
        'pac_numero_asociado': app.numero_asociado,
        'app_details': app_details,
        'pk': pk,
    }

    if check_paciente(request.user):
        return render(request, 'coreadmin/paciente/app_report_pac.html', context)
    elif check_profesional(request.user):
        return render(request, 'coreadmin/Doctor/report_apt.html', context)
    elif check_admin(request.user):
        return render(request, 'coreadmin/Admin/report_apt.html', context)
    else:
        return render(request, 'coreadmin/account/login.html')


# paciente feedback
@login_required(login_url='login_prof.html')
def feedback_pac_view(request):
    if check_paciente(request.user):
        pac = Paciente.objects.get(paciente_id=request.user.id)
        feedback_form = forms.FeedbackForm()
        if request.method == 'POST':
            feedback_form = forms.FeedbackForm(request.POST)
            if feedback_form.is_valid():  # if form is valid
                email = feedback_form.cleaned_data['Email']  # get email from form
                name = feedback_form.cleaned_data['Name']  # get name from form
                subject = "You have a new Feedback from {}:<{}>".format(name, feedback_form.cleaned_data[
                    'Email'])  # get subject from form
                message = feedback_form.cleaned_data['Message']  # get message from form

                message = "Subject: {}\n" \
                            "Date: {}\n" \
                            "Message:\n\n {}" \
                    .format(dict(feedback_form.subject_choices).get(feedback_form.cleaned_data['Subject']),
                            datetime.datetime.now(),
                            feedback_form.cleaned_data['Message'])

                try:
                    mail_admins(subject, message)
                    messages.add_message(request, messages.INFO, 'Thank you for submitting your feedback.')

                    return redirect('feedback_pac.html')
                except:
                    feedback_form.add_error('Email',
                                            'Try again.')
                    return render(request, 'coreadmin/paciente/feedback_pac.html', {'email': email,
                                                                                        'name': name,
                                                                                        'subject': subject,
                                                                                        'message': message,
                                                                                        'feedback_form': feedback_form,
                                                                                        'pac': pac})
        return render(request, 'coreadmin/paciente/feedback_pac.html', {'feedback_form': feedback_form,
                                                                                        'pac': pac})
    else:
        auth.logout(request)
        return redirect('login_pac.html')


# Download report
def dl_app_report_action(request, pk):
    # get information from database
    template_path = 'coreadmin/report/app_report_pdf.html'

    app = Turnos.objects.all().filter(id=pk).first()

    pac = app.paciente
    prof = app.profesional

    app_date = app.app_date
    app_time = app.app_time

    app_details = []

    context = {
        'pac_name': pac.first_name,
        'prof_name': prof.first_name,
        'app_date': app_date,
        'app_time': app_time,
        'app_desc': app.description,
        'pac_comp_name': app.company_name,
        'pac_comp_add': app.company_address,
        'app_details': app_details,
    }
    # context = {'myvar': 'this is your templates context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="appointment_report.pdf"'
    # find the templates and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# profesional
def register_prof_view(request):  # Register profesional
    if request.method == "POST":
        registration_form = ProfesionalesRegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():  # if form is valid
            dob = registration_form.cleaned_data.get('dob')  # get date of birth from form
            if dob < timezone.now().date():  # if date of birth is valid
                new_user = User.objects.create_user(username=registration_form.cleaned_data.get('username'),
                                                    email=registration_form.cleaned_data.get('email'),
                                                    password=registration_form.cleaned_data.get(
                                                        'password1'))  # create new user
                prof = Profesionales(profesional=new_user,
                        first_name=registration_form.cleaned_data.get('first_name'),
                        last_name=registration_form.cleaned_data.get('last_name'),
                        especialidad=registration_form.cleaned_data.get('especialidad'),
                        estudio=registration_form.cleaned_data.get('estudio'),
                        dob=registration_form.cleaned_data.get('dob'),
                        address=registration_form.cleaned_data.get('address'),
                        city=registration_form.cleaned_data.get('city'),
                        country=registration_form.cleaned_data.get('country'),
                        postcode=registration_form.cleaned_data.get('postcode'),
                        image=request.FILES['image'])  # create new profesional
                prof.save()

                est = Estudios(profesional=prof) (appfees=200, admfees=2000)
                est.save()

                group = Group.objects.get_or_create(name='profesional')  # add user to doctor group
                group[0].user_set.add(new_user)

                messages.add_message(request, messages.INFO, 'Registro exitoso!')
                return redirect('login_prof.html')
            else:  # if date of birth is invalid
                registration_form.add_error('dob', 'Invalid date of birth.')
                return render(request, 'coreadmin/profesional/register_prof.html',
                            {'registration_form': registration_form})
        else:
            print(registration_form.errors)
    else:
        registration_form = ProfesionalesRegistrationForm()

    return render(request, 'coreadmin/profesional/register_prof.html', {'registration_form': registration_form})


# Login profesional
def login_prof_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and check_profesional(user):
                auth.login(request, user)
                account_approval = Profesionales.objects.all().filter(status=True, profesional_id=request.user.id)
                if account_approval:
                    return redirect('profile_prof.html')
                else:
                    messages.add_message(request, messages.INFO, 'Your account is currently pending. '
                                                                'Please wait for approval.')
                    return render(request, 'coreadmin/profesional/login_prof.html', {'login_form': login_form})
        return render(request, 'coreadmin/profesional/login_prof.html', {'login_form': login_form})
    else:
        login_form = AuthenticationForm()
    return render(request, 'coreadmin/profesional/login_prof.html', {'login_form': login_form})


# profesional profile
@login_required(login_url='login_prof.html')
def profile_prof_view(request):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        prof = Profesionales.objects.filter(profesional_id=request.user.id).first()
        dob = prof.dob
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # calculate age
        if request.method == "POST":
            profesional_update_form = ProfesionalesUpdateForm(request.POST, request.FILES, instance=prof)
            if profesional_update_form.is_valid():  # if form is valid
                dob = profesional_update_form.cleaned_data.get('dob')
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # calculate age
                if dob < timezone.now().date():  # if date of birth is valid
                    profesional_update_form.save()
                    est = Estudios.objects.all().filter(
                        profesional=prof).first()  # get doctor professional details
                    # dp.appfees = p_form.cleaned_data.get('appfees')
                    # dp.admfees = p_form.cleaned_data.get('admfees')
                    est.save()  # save profesional service field data

                    messages.add_message(request, messages.INFO, 'Profile updated successfully!')
                    return redirect('profile_prof.html')
                else:
                    profesional_update_form.add_error('dob', 'Invalid date of birth.')
                    context = {
                        'profesional_update_form': profesional_update_form,
                        'prof': prof,
                        'age': age
                    }
                    return render(request, 'coreadmin/profesional/profile_prof.html', context)
        else:
            # get data from database and put initial values in form
            # age.refresh_from_db()
            est = Estudios.objects.all().filter(profesional=prof).first()
            profesional_update_form = ProfesionalesUpdateForm(instance=prof)
            # profesional_update_form.fields['appfees'].initial = dp.appfees
            # profesional_update_form.fields['admfees'].initial = dp.admfees
            context = {
                'profesional_update_form': profesional_update_form,
                'prof': prof,
                'age': age
            }
            return render(request, 'coreadmin/profesional/profile_prof.html', context)
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# profesional dashboard - approved appointments don't show, WHAT IS WRONG?!
@login_required(login_url='login_prof.html')
def dashboard_prof_view(request):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        prof = Profesionales.objects.get(profesional_id=request.user.id)
        app_completed = Turnos.objects.all().filter(profesional=prof, completed=True).count()
        available_app = Turnos.objects.all().filter(profesional=prof, status=False).count()
        pending_app_count = Turnos.objects.all().filter(profesional=prof, status=False).count()
        app_count = models.Turnos.objects.all().filter(status=True, profesional=prof).count()

        pending_app = []
        for app in Turnos.objects.filter(status=False, profesional=prof.id, app_link__isnull=True,
                                            completed=False).all():  # get unapproved appointments which have links not set and are not yet finished
            c = Paciente.objects.filter(id=app.paciente.id).first()
            if c:
                pending_app.append([app.pk, c.first_name, c.last_name, c.proveedor_seguro_name,
                                    app.app_date, app.app_time, app.description, app.status, app.completed])

        upcoming_app = []
        for app in Turnos.objects.filter(status=True, profesional=prof.id, app_link__isnull=True,
                                            completed=False).all():  # get approved appointments which have links not set and are not yet finished
            c = Paciente.objects.filter(id=app.paciente.id).first()
            app.app_link = c.first_name
            if c:
                upcoming_app.append([app.pk, c.first_name, c.last_name, c.proveedor_seguro_name,
                                    app.app_date, app.app_time, app.description, app.app_link, app.status,
                                    app.completed,
                                    prof.first_name])

        completed_app = []  # approved manually inside
        for app in Turnos.objects.filter(profesional=prof, completed=True).all():  # get all approved appointments
            c = app.paciente
            if c:
                completed_app.append([prof.first_name,
                                    c.first_name,
                                    app.completed, app.pk])

        messages.add_message(request, messages.INFO, 'You have {0} pending appointments to approve.'.format(pending_app_count))

        return render(request, 'coreadmin/profesional/dashboard_prof.html',
                    {'prof': prof,
                    'pending_app': pending_app,
                    'upcoming_app': upcoming_app,
                    'app_completed': app_completed,
                    'available_app': available_app,
                    'completed_app': completed_app,
                    'app_count': app_count})
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# View all profesional appointments
@login_required(login_url='login_prof.html')
def all_app_prof_view(request):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        prof = Profesionales.objects.get(profesional_id=request.user.id)
        app_completed = Turnos.objects.all().filter(profesional=prof.id, completed=True).count()
        available_app = Turnos.objects.all().filter(profesional=prof.id, status=False).count()
        app_count = models.Turnos.objects.all().filter(profesional=prof.id, status=True,).count()

        pending_app = []
        for app in Turnos.objects.filter(status=False, profesional=prof.id, app_link__isnull=True,
                                            completed=False).all():  # get unapproved appointments which have links not set and are not yet finished
            c = Paciente.objects.filter(id=app.paciente.id).first()
            if c:
                pending_app.append([app.pk, c.first_name, c.last_name, c.proveedor_seguro_name,
                                    app.app_date, app.app_time, app.description, app.status, app.completed])

        upcoming_app = []
        for app in Turnos.objects.filter(status=True, profesional=prof.id, app_link__isnull=True,
                                            completed=False).all():  # get approved appointments which have links not set and are not yet finished
            c = Paciente.objects.filter(id=app.paciente.id).first()
            app.app_link = c.first_name
            if c:
                upcoming_app.append([app.pk, c.first_name, c.last_name, c.proveedor_seguro_name,
                                    app.app_date, app.app_time, app.description, app.app_link, app.status,
                                    app.completed,
                                    prof.first_name])

        completed_app = []  # approved manually inside
        for app in Turnos.objects.filter(profesional=prof.id, completed=True).all():  # get all approved appointments
            c = app.paciente
            app.app_link = c.first_name
            if c:
                completed_app.append([app.pk, c.first_name, c.last_name, c.proveedor_seguro_name,
                                    app.app_date, app.app_time, app.description, app.app_link, app.status,
                                    app.completed,
                                    prof.first_name])

        return render(request, 'coreadmin/profesional/view_app_prof.html', {
            'prof': prof,
            'pending_app': pending_app,
            'upcoming_app': upcoming_app,
            'completed_app': completed_app,
            'app_completed': app_completed,
            'app_count': app_count,
            'available_app': available_app, })
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# Add appointment link action - can't seem to save link.... link = app_link?
@login_required(login_url='login_prof.html')
def add_link_prof_action(request, pk, link):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        appointment = Turnos.objects.get(id=pk)
        appointment.app_link = link
        appointment.save()
        return redirect(reverse('view_app_prof.html'))
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# View profesional appointment's details, approve appointment or edit details - save & update doesn't work, complete works
@login_required(login_url='login_prof.html')
def app_details_prof_view(request, pk):
    if check_profesional(request.user):
        adm = Admin.objects.filter(admin_id=request.user.id).first()

        app = Turnos.objects.filter(id=pk).first()  # get appointment
        prof = app.profesional
        pac = app.paciente

        app.app_link = pac.first_name

        appointment_details = [prof.first_name, prof.last_name, prof.service_field,
                                pac.first_name, pac.last_name,
                                pac.proveedor_seguro_name, pac.numero_asociado,
                                app.app_date, app.app_time, app.app_link, app.description,
                                app.status, app.completed, pk]  # render fields

        return render(request, 'coreadmin/profesional/view_app_details_prof.html',
                      {'adm': adm,
                        'prof': prof,
                        'app': app,
                        'pac': pac,
                        'appointment_details': appointment_details})
    else:
        auth.logout(request)
        return redirect('login_adm.html')


# Get an appointment
@login_required(login_url='login_prof.html')
def get_link_prof_action(request, pk):
    if check_profesional(request.user):
        # get information from database
        appointment = Turnos.objects.get(id=pk)
        appointment.status = True  # approve appointment
        appointment.save()

        prof = appointment.profesional
        est = Estudios.objects.filter(profesional=prof).first()
        est.app_total += 1  # add paciente to profesional count
        est.save()

        messages.add_message(request, messages.INFO, 'Appointment approved!')
        return redirect(reverse('dashboard_prof.html'))
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# Complete an appointment - did I even use this?
@login_required(login_url='login_prof.html')
def complete_app_prof_action(request, pk):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        app = Turnos.objects.get(id=pk)
        app.completed = True
        app.save()

        messages.add_message(request, messages.INFO, 'Appointment completed successfully!')
        return redirect('view_app_prof.html')
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# View all approved appointments
@login_required(login_url='login_prof.html')
def approved_app_prof_view(request):
    if check_profesional(request.user):
        prof = Profesionales.objects.get(profesional_id=request.user.id)  # get profesional

        incomplete_appointments = []
        for ip in IngresoPaciente.objects.filter(
                profesional=prof).all():  # get all pacientes approved under this profesional
            pac = ip.paciente
            if pac and not ip.completed_date:
                incomplete_appointments.append([prof.first_name, pac.first_name,
                                                ip.approval_date, ip.completed_date, ip.pk])

        completed_appointments = []
        for ip in IngresoPaciente.objects.filter(
                profesional=prof).all():  # get all pacientes approved under this profesional
            pac = ip.paciente
            if pac and ip.completed_date:
                completed_appointments.append([prof.first_name, pac.first_name,
                                                ip.approval_date, ip.completed_date, ip.pk])
        return render(request, 'coreadmin/profesional/view_approved_app_prof.html',
                    {'incomplete_appointments': incomplete_appointments,
                    'completed_appointments': completed_appointments})
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# View approved appointment's details
@login_required(login_url='login_prof.html')
def approved_app_details_prof_view(request, pk):
    if check_profesional(request.user):
        # get information from database and render in html webpage
        ip = IngresoPaciente.objects.filter(id=pk).first()
        prof_d = Profesionales.objects.get(profesional_id=request.user.id)
        prof_d = prof_d.estudio

        pac = ip.paciente
        prof = ip.profesional
        approved_appointment_details = [ip.pk, prof.first_name,
                                        pac.first_name, ip.approval_date, ip.completed_date, ip.description]
        # med = Medicines.objects.all()
        return render(request, 'coreadmin/profesional/view_approved_app_details_prof.html',
                    {'approved_appointment_details': approved_appointment_details,
                    'prof_d': prof_d, })
        # 'med': med})
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# profesional feedback
@login_required(login_url='login_prof.html')
def feedback_prof_view(request):
    if check_profesional(request.user):
        prof = Profesionales.objects.get(profesional_id=request.user.id)
        feedback_form = forms.FeedbackForm()
        if request.method == 'POST':
            feedback_form = forms.FeedbackForm(request.POST)
            if feedback_form.is_valid():  # if form is valid
                email = feedback_form.cleaned_data['Email']  # get email from form
                name = feedback_form.cleaned_data['Name']  # get name from form
                subject = "You have a new Feedback from {}:<{}>".format(name, feedback_form.cleaned_data[
                    'Email'])  # get subject from form
                message = feedback_form.cleaned_data['Message']  # get message from form

                message = "Subject: {}\n" \
                            "Date: {}\n" \
                            "Message:\n\n {}" \
                    .format(
                    dict(feedback_form.subject_choices).get(feedback_form.cleaned_data['Subject']),
                    datetime.datetime.now(),
                    feedback_form.cleaned_data['Message']
                )

                try:
                    mail_admins(subject, message)
                    messages.add_message(request, messages.INFO, 'Thank you for submitting your feedback.')

                    return redirect('feedback_prof.html')
                except:
                    feedback_form.add_error('Email',
                                            'Try again.')
                    return render(request, 'coreadmin/profesional/feedback_prof.html', {'feedback_form': feedback_form})
        return render(request, 'coreadmin/profesional/feedback_prof.html', {'prof': prof, 'feedback_form': feedback_form})
    else:
        auth.logout(request)
        return redirect('login_prof.html')


# User check
def check_admin(user):  # check if user is admin
    return user.groups.filter(name='Admin').exists()


def check_paciente(user):  # check if user is paciente
    return user.groups.filter(name='paciente').exists()


def check_profesional(user):  # check if user is profesional
    return user.groups.filter(name='profesional').exists()


# Appointment availability check
def check_estudio_availability(profesional, dt, tm):  # check if profesional is available in a given slot
    tm = tm[:-3]  # separate AM/PM
    hr = tm[:-3]  # get hour reading
    mn = tm[-2:]  # get minute reading
    ftm = time(int(hr), int(mn), 0)  # create a time object
    app = Turnos.objects.all().filter(status=True,
                                        profesional=profesional,
                                        app_date=dt)  # get all appointments for a given prof and the given date

    if ftm < time(8, 0, 0) or ftm > time(19, 0, 0):  # if time is not in between 9AM to 5PM, reject
        return False

#    if time(12, 0, 0) < ftm < time(13, 0, 0):  # if time is in between 12PM to 1PM, reject
#        return False

    for a in app:
        if ftm == a.app_time and dt == a.app_date:  # if some other appointment has the same slot, reject
            return False

    return True
