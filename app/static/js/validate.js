/* Compare fields in register */
const email = document.getElementById('email');
const email2 = document.getElementById('email2');
const pwd = document.getElementById('password');
const pwd2 = document.getElementById('password2');

// Validação//
function validate(item) {
    item.setCustomValidity('');
    item.checkValidity();
    
    if (item == pwd2) {
        if (item.value === pwd.value) item.setCustomValidity('');
        else item.setCustomValidity('As senhas não são iguais')
    }
}

email.addEventListener('input', function () { validate(email)});
email2.addEventListener('input', function () { validate(email2)});
password.addEventListener('input', function () { validate(password)});
password2.addEventListener('input', function () { validate(password2)});