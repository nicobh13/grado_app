document.addEventListener("DOMContentLoaded", function () {
  const registroForm = document.getElementById("registro-form");
  const pNombre = document.getElementById("p-nombre")

  registroForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Evitar el envío del formulario por defecto

    // Obtener datos del formulario
    const formData = new FormData(registroForm);

    // Realizar una solicitud POST AJAX al servidor
    fetch("/register", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Si la validación es exitosa, redirige o realiza alguna acción
          window.location.href = "/dashboard";
        } else {
          // Si la validación falla, muestra mensajes de error
          mostrarErrores(data.errors);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  function mostrarErrores(errors) {
    // Recorre los errores y agrega los mensajes debajo de los campos correspondientes
    for (const campo in errors) {
      if (errors.hasOwnProperty(campo)) {
        const mensajeError = errors[campo];
        const campoInput = document.getElementById(campo);
        const campoError = document.getElementById(campo + "Error");

        if (campoError) {
          // Si el campo de error ya existe, actualiza su contenido
          campoError.textContent = mensajeError;
        }
      }
    }
  }
});
