from weather.models import Weather
from django import forms
from django.core import validators


def tempValidator(value):
    """
    cutom validator for temperature value , it mus be between 19 and 28
    """
    if value not in range(19, 28):
        raise forms.ValidationError(
            "invalid Temperature value , it should be between 19 and 28")


def humidtyValidator(value):
    """
    cutom validator for temperature value , it mus be between 19 and 28
    """
    if value not in range(35, 65):
        raise forms.ValidationError(
            "invalid Humidity value , it should be between 35 and 65")


class WeatherForm(forms.Form):
    """
    weather form class
    """
    temp = forms.FloatField(
        required=True, validators=tempValidator, help_text="Temperature")
    humidity = forms.FloatField(
        required=True, validators=humidtyValidator, help_text="Humidity")
