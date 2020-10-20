/*VALIDAR RUT*/

function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("rut no tiene el largo necesario de 10");
        return false;
    }
    var num = 3;
    var suma = 0;
    for (let index = 0; index < 8; index++) {
        var carac = rut.slice(index, index + 1);
        suma = suma + (carac * num);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut Inválido");
        return false;
    }
    return true;
}

/*VALIDAR FECHA*/

function validarFecha() {
    var fechaForm = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();

    var ano = fechaForm.slice(0, 4);
    var mes = fechaForm.slice(5, 7);
    var dia = fechaForm.slice(8, 10);

    var fechaMia = new Date(ano, (mes - 1), dia);

    if (fechaMia > fechaSistema) {
        alert("Fecha de Nacimiento Incorrecta");
        return false;
    }
    return true;
}

/*VALIDAR TODO*/
function validaNombre() {
    var nom = document.getElementById("txtNombre").value;
    var largo = nom.trim().length;
    if (largo >= 3 && largo <= 80) {
        return true;
    } else {
        return false;
    }
}

function validarTodo() {
    var resp;
    resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validarFecha();
    if (resp == false) {
        return false;
    }
    resp = validaNombre();
    if (resp == false) {
        return false;
    }
    return true;
}