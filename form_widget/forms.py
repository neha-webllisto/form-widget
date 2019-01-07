from django  import forms


CHOICES = (('Select Class','Select Class'),('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'),
	('8th','8th'),('9th','9th'),('10th','10th'),('11th PCM','11th PCM'),('11th Bio','11th Bio'),
	('11th Commerce','11th Commerce'),('12th PCM','12th PCM'),('12th Bio','12th Bio'),('12th Commerce','12th Commerce'))

CATEGORY = (('General','General'),('OBC','OBC'),('SC','SC'),('ST','ST'))


class Widget_form(forms.Form):
	name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Enter name', 'class':'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter Email','class':'form-control'}))
	class1 = forms.ChoiceField(choices=CHOICES,label='Select Class')
	phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Enter Phone','class':'form-control'}))
	category = forms.ChoiceField(choices=CATEGORY, widget=forms.RadioSelect)
	address = forms.CharField(widget=forms.Textarea)

	class1.widget.attrs.update({'class':'form-control','placeholder':'Select Class'})
	category.widget.attrs.update({'class':'form-check-input'})
	address.widget.attrs.update({'class':'form-control green-border-focus','placeholder':'Enter Address'})

	