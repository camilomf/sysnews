from django import forms
from django.contrib.auth.models import User
from .models import News, Source, Tags

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('url', 
                'title',
                'headline',
                'explanation',
                'hash_news',
                'publication_date',
                'tags',
                'image',
                'source',
                'country',
                # 'usuario',
                )
        
        widgets = {
            'url' : forms.URLInput(attrs={'class':'form-control','required':'required','placeholder':'https://'}),
            'title' : forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'headline' : forms.Textarea(attrs={'class':'form-control','rows':3,'required':'required'}),
            'explanation' : forms.Textarea(attrs={'class':'form-control','rows':20,'required':'required'}),
            'hash_news' : forms.TextInput(attrs={'class':'form-control'}),
            'publication_date' : forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control','type':'date','required':'required'}),
            'tags' : forms.SelectMultiple(attrs={'class':'form-control chzn-select','required':'required'}),
            'image' : forms.ClearableFileInput(attrs={'class':'form-control-file','required':'required'}),
            'source' : forms.Select(attrs={'class':'form-control chzn-select','required':'required'}),
            'country' : forms.Select(attrs={'class':'form-control chzn-select','required':'required'}),
        }

class TagsForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ('name', 
                'description',
                )
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'description' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        }

    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get("nombre")
    #     if Tags.objects.filter(nombre=nombre).exists():
    #         raise forms.ValidationError("El Tag ya se ha agregado")
    #     return nombre
    

class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = ('name', 
                'description',
                )
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'description' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
    
    def clean_source(self):
        name =self.cleaned_data.get('name')
        if 'name' in self.changed_data:
            if Source.objects.filter(name=name).exists():
                raise forms.ValidationError("La fuente ya se ha agregado")
        return name