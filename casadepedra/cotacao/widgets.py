from django.forms import RadioSelect, TextInput, Select


class RadioSelectButtonGroup(RadioSelect):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """

    template_name = "cotacao/widgets/radio_select_button_group.html"


class FormBootstrap(TextInput):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """
    template_name = "cotacao/widgets/form_control.html"


class SelectOptionBootstrap(Select):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """
    template_name = "cotacao/widgets/form_options_bootstrap.html"


class FormBootstrapHidden(TextInput):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """
    template_name = "cotacao/widgets/input_hidden.html"

class SelectOptionBootstrapAction(Select):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """
    template_name = "cotacao/widgets/form_options_bootstrap_action.html"

class FormBootstrapnoPage(TextInput):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """
    template_name = "cotacao/widgets/form_no_page.html"