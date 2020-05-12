from django import forms


class InputForm(forms.Form):
    x_coordinate = forms.CharField(max_length=50,label = "Enter X(x-axis coordinate (1-9)")
    y_coordinate = forms.CharField(max_length=50, label = "Enter Y(y-axis coordinate(1-9)")
    month = forms.CharField(max_length=50, label = "Enter month(Jan-Dec)")
    day = forms.CharField(max_length=50, label = "Enter Day of week(Monday to Sunday)")
    ffmc = forms.CharField(max_length=50, label = "Enter FFMC code")
    dmc = forms.CharField(max_length=50, label = "Enter DMC code")
    dc = forms.CharField(max_length=50, label = "Enter DC code")
    isi = forms.CharField(max_length=50, label = "Enter ISI index")
    temp = forms.CharField(max_length=50, label = "Enter temp(in Celsius)")
    rh = forms.CharField(max_length=50, label = "Enter RH(relative humidity in %)")
    wind = forms.CharField(max_length=50, label = "Enter wind speed(Km/h)")
    outside = forms.CharField(max_length=50, label = "Enter Outside rain(mm/m^2)")
