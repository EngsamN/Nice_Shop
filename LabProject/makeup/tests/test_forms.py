import pytest
from django.contrib.auth.models import User
from makeup.forms import NewUserForm, LoginForm

def test_sample():
    assert 1 + 1 == 2

@pytest.mark.django_db
def test_new_user_form_valid_data():
    form = NewUserForm(data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'strongpassword',
        'password2': 'strongpassword',
    })
    assert form.is_valid()
    user = form.save()
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.check_password('strongpassword')

@pytest.mark.django_db
def test_new_user_form_invalid_data():
    form = NewUserForm(data={})
    assert not form.is_valid()
    assert len(form.errors) > 0

@pytest.mark.django_db
def test_login_form_valid_data():
    user = User.objects.create_user(username='testuser', password='strongpassword')
    form = LoginForm(data={
        'username': 'testuser',
        'password': 'strongpassword',
    })
    assert form.is_valid()
    authenticated_user = form.authentication()
    assert authenticated_user is not None
    assert authenticated_user.username == 'testuser'

@pytest.mark.django_db
def test_login_form_invalid_data():
    form = LoginForm(data={
        'username': 'nonexistentuser',
        'password': 'wrongpassword',
    })
    assert form.is_valid()
    authenticated_user = form.authentication()
    assert authenticated_user is None

@pytest.mark.django_db
def test_editpro_form_valid_data():
    product = Product.objects.create(
        name="Test Product",
        kind="Test Kind",
        description="Test Description",
        price=100,
        expir_date="2025-01-01"
    )
    form = EditproForm(data={
        'name': 'Updated Product',
        'kind': 'Updated Kind',
        'description': 'Updated Description',
        'price': 150,
        'expir_date': '2026-01-01'
    }, instance=product)
    assert form.is_valid()
    updated_product = form.save()
    assert updated_product.name == 'Updated Product'
    assert updated_product.kind == 'Updated Kind'
    assert updated_product.description == 'Updated Description'
    assert updated_product.price == 150
    assert str(updated_product.expir_date) == '2026-01-01'

@pytest.mark.django_db
def test_editpro_form_invalid_data():
    form = EditproForm(data={})
    assert not form.is_valid()
    assert len(form.errors) > 0
