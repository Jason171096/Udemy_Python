from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
            label = "Titulo",
            max_length=50, 
            required=False,
            widget = forms.TextInput(
                attrs={
                    'placeholder': 'Titulo',
                    'class': 'Titulo_form_article'
                }
            ),
            validators=[
                validators.MinLengthValidator(4, "Titulo demasiado corto"),
                validators.RegexValidator('^[a-zA-Z0-9ñ ]*$', message='El titulo no acepta caracteres extraños')
            ]
        )

    content = forms.CharField(
        label = "Contenido", 
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(50, "Limite excedido de caracteres")
        ])

    content.widget.attrs.update({
            'placeholder': 'Titulo',
            'class': 'Titulo_form_article'
        }
    )

    public_options = [
        (0, "NO"),
        (1, "SI")
    ]

    public = forms.TypedChoiceField(label="¿Publicado?", choices = public_options)