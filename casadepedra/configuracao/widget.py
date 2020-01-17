from django.forms import CheckboxInput, Textarea


class Texto_Area_WppWidget(Textarea):
    
    template_name = "configuracao/widgets/TextoAreaWpp.html"
    
class CheckBox_HiddenWidget(CheckboxInput):
    
    template_name = "configuracao/widgets/checkboxhidden.html"