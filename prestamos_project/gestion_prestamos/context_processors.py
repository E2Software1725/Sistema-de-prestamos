from .models import EmpresaConfiguracion, ImpresoraConfiguracion

def global_settings_processor(request):
    """
    Agrega configuraciones globales al contexto de todas las plantillas.
    """
    empresa_config = EmpresaConfiguracion.objects.first()
    impresora_config = ImpresoraConfiguracion.objects.first()
    
    return {
        'empresa_configuracion': empresa_config,
        'impresora_configuracion': impresora_config,
    }
