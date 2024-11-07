from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from datetime import datetime, timedelta
from decimal import Decimal



# Create your models here.
class Admin (models.Model):
    admin_id = models.AutoField(primary_key=True, verbose_name='ID Admin')
    username = models.CharField(max_length=50, unique=True, verbose_name='Username')
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(unique=True, verbose_name='email')
    admin_password = models.CharField(max_length=100, verbose_name='Contraseña')
    admin_dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    admin_telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    status = models.BooleanField(default=False)  # admin status (approved/on-hold)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin.username} Perfil Admin'

    class Meta:
        unique_together = ('date_joined', 'time')
        ordering = ['date_joined', 'time']

class ProveedoresSeguros (models.Model):
    proveedor_id = models.AutoField(primary_key=True, verbose_name='ID Proveedor')
    proveedor_nombre = models.CharField(max_length=50, verbose_name='Nombre Proveedor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proveedor_nombre
    
    class Meta:
        verbose_name_plural = "Proveedores de Seguros"
        ordering = ['proveedor_nombre']



class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True, verbose_name='ID Paciente')
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(unique=False, verbose_name='email')
    image = models.ImageField(default="default.png", upload_to="profile_pictures", null=True, blank=True)  # profile picture
    proveedor_nombre = models.ForeignKey(ProveedoresSeguros, on_delete=models.CASCADE)
    plan_seguro = models.CharField(max_length=50, verbose_name='Plan')
    numero_asociado = models.CharField(unique=True, max_length=20, verbose_name='Número de Afiliado')
    HistoriaClinica = models.ForeignKey('HistoriaClinica', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = "Pacientes"
        ordering = ['last_name']


class HistoriaClinica (models.Model):
    historia_id = models.AutoField(primary_key=True, verbose_name='ID')
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    historia_fecha = models.DateTimeField(auto_now_add=True)
    historia_descripcion = models.TextField(verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.historia_id}'

    class Meta:
        verbose_name_plural = "Historias Clínicas"
        ordering = ['historia_fecha']


class Especialidades (models.Model):
    especialidad_id = models.AutoField(primary_key=True, verbose_name='ID Especialidad')
    especialidad_nombre = models.CharField(max_length=50, verbose_name='Especialidad')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.especialidad_nombre

    class Meta:
        verbose_name_plural = "Especialidades"
        ordering = ['especialidad_nombre']



class Profesionales (models.Model):
    profesional_id = models.AutoField(primary_key=True, verbose_name='ID Profesional')
    profesional_nombre = models.CharField(max_length=50, verbose_name='Nombre Profesional')
    profesional_apellido = models.CharField(max_length=50, verbose_name='Apellido Profesional')
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    especialidad_id = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)  # doctor status(approved/on-hold)

    def __str__(self):
        return f'{self.profesional_nombre} {self.profesional_apellido}'

    class Meta:
        verbose_name_plural = "Profesionales"
        ordering = ['profesional_apellido']


class Insumos(models.Model):
    insumo_id = models.AutoField(primary_key=True, verbose_name='ID Insumo')
    insumo_nombre = models.CharField(max_length=50, verbose_name='Nombre Insumo')
    stock_actual = models.IntegerField(verbose_name='Stock Actual')
    stock_minimo = models.IntegerField(verbose_name='Stock Mínimo')
    unidad_medida = models.CharField(max_length=50, verbose_name='Unidad de Medida')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.insumo_id} - {self.insumo_nombre} Información Insumo'

            
    def decrease_stock(self, amount):
        if amount < 0:
            raise ValueError("La cantidad a decrementar no puede ser negativa")
        if self.stock_actual >= amount:
            self.stock_actual -= amount
            self.save()
        else:
            raise ValueError(f"No hay suficiente stock para {self.insumo_nombre}")

    def increase_stock(self, amount):
        if amount < 0:
            raise ValueError("La cantidad a incrementar no puede ser negativa")
        self.stock_actual += amount
        self.save()

    def clean(self):
        if self.stock_actual < 0:
            raise ValueError("El stock actual no puede ser negativo")
        if self.stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo")

    class Meta:
        verbose_name_plural = "Insumos"
        ordering = ['insumo_nombre']


class Estudios(models.Model):
    estudio_id = models.AutoField(primary_key=True, verbose_name='ID Estudio')
    especialidad = models.ForeignKey('Especialidades', on_delete=models.CASCADE, related_name="estudios", default="Seleccione una opción")
    estudio_nombre = models.CharField(max_length=50, verbose_name='Nombre Estudio')
    estudio_descripcion = models.CharField(max_length=100, verbose_name='Descripción Estudio')
    estudio_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Estudio')
    profesional = models.ForeignKey('Profesionales', on_delete=models.CASCADE, related_name="estudios", default=1)
    app_total = models.IntegerField(verbose_name='Total de turnos', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    insumos = models.ManyToManyField('Insumos', related_name="estudios", blank=True)

    def __str__(self):
        return f'{self.estudio_id} - {self.estudio_nombre} - {self.estudio_precio}'
    
    def update_insumo_stock(self):
        for insumo in self.insumos.all():
            quantity_used = self.get_insumo_quantity(insumo)
            if quantity_used is not None:
                insumo.decrease_stock(quantity_used)

    def get_insumo_quantity(self, insumo):
        # Implement your logic to determine how much of each insumo is used.
        # For example, you might have a field in an intermediate table:
        # return some_quantity_from_intermediate_table
        return 1  # Placeholder implementation

    @receiver(m2m_changed, sender='coreadmin.Estudios_insumos')
    def update_stock_on_insumos_change(sender, instance, action, **kwargs):
        if action in ["post_add", "post_remove", "post_clear"]:
            instance.update_insumo_stock()

            
    def __str__(self):
        return f'{self.estudio_id} - {self.estudio_nombre} - {self.estudio_precio}'

    class Meta:
        verbose_name_plural = "Estudios"
        ordering = ['estudio_nombre']



class Turnos(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='turnos')
    especialidad = models.ForeignKey('Especialidades', on_delete=models.CASCADE, related_name='turnos')
    estudio = models.ForeignKey('Estudios', on_delete=models.CASCADE, related_name='turnos')
    profesional = models.ForeignKey('Profesionales', on_delete=models.CASCADE, related_name='turnos')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('SCHEDULED', 'Programada'),
        ('CONFIRMED', 'Confirmada'),
        ('CHECKED_IN', 'Checked in'),
        ('CHECKED_OUT', 'Checked out'),
        ('CANCELLED', 'Cancelada'),
    ], default='SCHEDULED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.appointment_id} - {self.paciente} - {self.date} {self.time}'
        
    class Meta:
        unique_together = ('profesional', 'date', 'time')
        ordering = ['date', 'time']
        verbose_name_plural = "Turnos"


class IngresoPaciente(models.Model):
    ingreso_id = models.AutoField(primary_key=True, verbose_name='ID Visita')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesionales, on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudios, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha Visita')
    ingreso_hora = models.TimeField(verbose_name='Hora Visita')
    ingreso_tipo = models.CharField(max_length=20, choices=[
        ('SIN_TURNO', 'Ingreso por Guardia'),
        ('CON_TURNO', 'Ingreso con Turno'),
    ], default='CON_TURNO')
    ingreso_gravedad = models.CharField(max_length=10, choices=[
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ], null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('Esperando', 'Esperando'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ])
    HistoriaClinica = models.ForeignKey('HistoriaClinica', on_delete=models.CASCADE, null=True, blank=True)
    fecha_hora_completado = models.DateTimeField(verbose_name='Fecha y Hora Completado', null=True, blank=True)
    insumos = models.ManyToManyField(Insumos, related_name='appointments')
    SalaEspera = models.ManyToManyField('SalaEspera', related_name='appointments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Ingreso"
        ordering = ['fecha_ingreso']

    def __str__(self):
        return f'{self.ingreso_id} - {self.paciente} - {self.estado}'

    def create_payment_record(self):
        """
        Creates a payment record for the patient's service.
        """
        try:
            Pagos.objects.create(
                ingreso_paciente=self,
                monto=self.estudios.precio
            )
            return True
        except Exception as e:
            # Log the error
            print(f"Error creating payment record: {str(e)}")
            return False

    def log_patient_and_charge_fee(self):
        # Create payment record
        Pagos.objects.create( ingreso_paciente=self, monto=self.servicio.precio )

    def get_insumo_quantity(self, insumo):
        """
        Returns the quantity of the given insumo used for this appointment.
        Assumes each insumo is used once per appointment if it's associated.
        """
        if self.insumos.filter(id=insumo.id).exists():
            return 1
        return 0

    def add_insumo(self, insumo):
        """
        Adds an insumo to this appointment.
        """
        self.insumos.add(insumo)

    def remove_insumo(self, insumo):
        """
        Removes an insumo from this appointment.
        """
        self.insumos.remove(insumo)

    def get_all_insumos(self):
        """
        Returns all insumos associated with this appointment.
        """
        return self.insumos.all()

    def get_total_insumos_count(self):
        """
        Returns the total count of insumos used in this appointment.
        """
        return self.insumos.count()


class SalaEspera(models.Model):
    sala_id = models.AutoField(primary_key=True, verbose_name='ID Sala')
    sala_nombre = models.CharField(max_length=50, verbose_name='Nombre Sala')
    IngresoPaciente = models.ForeignKey('IngresoPaciente', on_delete=models.CASCADE, verbose_name='Ingreso Paciente')
    profesional = models.ForeignKey('Profesionales', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Profesional')
    estudio = models.ForeignKey('Estudios', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Estudio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sala_id} - {self.sala_nombre} - {self.IngresoPaciente}'

    class Meta:
        verbose_name = 'Sala de Espera'
        verbose_name_plural = 'Salas de Espera'


class Pagos(models.Model):
    ingreso_paciente = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago de {self.ingreso_paciente.paciente} por {self.monto} el {self.fecha_pago}"
    
    class Meta:
        verbose_name_plural = "Pagos"


class Facturas (models.Model):
    factura_id = models.AutoField(primary_key=True, verbose_name='ID Factura')
    factura_numero = models.IntegerField(unique=True, verbose_name='Número Factura')
    factura_fecha = models.DateField(verbose_name='Fecha Factura')
    pago_id = models.ForeignKey(Pagos, on_delete=models.CASCADE, verbose_name='ID Pago')    
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.factura_numero}'

    class Meta:
        verbose_name_plural = "Facturas"
        ordering = ['factura_numero']



class SolicitudesInsumos(models.Model):
    ESTADO_SOLICITUD_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Completada', 'Completada'),
    ]
    estado_solicitud = models.CharField(max_length=20, choices=ESTADO_SOLICITUD_CHOICES, default='Pendiente')
    solicitud_id = models.AutoField(primary_key=True, verbose_name='ID Solicitud')
    solicitud_fecha = models.DateField(verbose_name='Fecha Solicitud')
    insumo_id = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    cantidad_solicitada = models.CharField(max_length=5, verbose_name='Cantidad Solicitada')
    solicitado_por = models.CharField(max_length=50, verbose_name='Solicitado por')
    fecha_completada = models.DateField(verbose_name='Fecha Completada', null=True, blank=True)
    fecha_actualizacion = models.DateField(verbose_name='Fecha Actualización', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.solicitud_id} - {self.insumo_id} - {self.estado_solicitud}'
    
    class Meta:
        verbose_name_plural = "Solicitudes de Insumos"
        ordering = ['solicitud_fecha', 'estado_solicitud']



class ResultadoLaboratorio (models.Model):
    resultado_id = models.AutoField(primary_key=True, verbose_name='ID Resultado')
    visita_id = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE)
    estudio_id = models.ForeignKey(Estudios, on_delete=models.CASCADE)
    resultado_detalle = models.CharField(max_length=200, verbose_name='Detalle Resultado')
    created_at = models.DateTimeField(auto_now_add=True)
    resultado_fecha = models.DateField(verbose_name='Fecha Resultado')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.resultado_id} - {self.resultado_fecha}'
    
    class Meta:
        verbose_name_plural = "Resultados"
        ordering = ['resultado_fecha']

