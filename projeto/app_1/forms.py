from django import forms
from .models import Usuario,Tarefa

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'senha']


class UsuarioChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome



class TarefaForm(forms.ModelForm):
    usuario = UsuarioChoiceField(
        queryset=Usuario.objects.all(),
        empty_label="Selecione um usuário"
    )

    
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )

    custo = forms.DecimalField(
        widget=forms.TextInput(attrs={'id': 'id_custo'}),
        max_digits=10,
        decimal_places=2,
        required=True
    )
    class Meta:
        model = Tarefa
        fields = ['usuario', 'descricao', 'data', 'custo']