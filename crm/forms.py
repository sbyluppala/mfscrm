
from django import forms
from .models import Customer, Service, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 'city', 'state',
                  'zipcode', 'email')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time',
                  'service_charge')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('cust_name', 'p_product', 'p_description', 'p_quantity', 'p_pickup_time',
                  'p_charge')
