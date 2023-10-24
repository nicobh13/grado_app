function toggleLoginForm(
  isLoginForm,
  changeButton,
  registrationForm,
  loginForm,
  changeSection,
  inputSection
) {
  console.log(isLoginForm);

  if (
    (changeSection.classList.contains("slide-right") &&
      inputSection.classList.contains("slide-left")) ||
    isLoginForm
  ) {
    changeSection.classList.remove("slide-right");
    inputSection.classList.remove("slide-left");
    changeButton.textContent = "Registrarse";
    registrationForm.style.display = "none";
    loginForm.style.display = "block";
  } else {
    changeSection.classList.add("slide-right");
    inputSection.classList.add("slide-left");
    changeButton.textContent = "Iniciar Sesión";
    registrationForm.style.display = "block";
    loginForm.style.display = "none";
  }

  isLoginForm = !isLoginForm;

  return isLoginForm;
}

document.addEventListener("DOMContentLoaded", function () {
//divs de cada formulario, no el formulario en sí
  const registrationForm = document.getElementById("registration-form");
  const loginForm = document.getElementById("login-form");
  const code = document.getElementById("code");
  const selectRol = document.getElementById("rol");
  const changeButton = document.getElementById("change-button");
  const changeSection = document.querySelector(".change-section");
  const inputSection = document.querySelector(".input-section");

  // Obtener la URL completa
  var urlActual = window.location.href;
  console.log(urlActual);

  var form_type = urlActual.split("form_type=");
  form_type = form_type[1];
  let isLoginForm = true;

  if (form_type == "register") {
    isLoginForm = false;
  }

  isLoginForm = toggleLoginForm(
    isLoginForm,
    changeButton,
    registrationForm,
    loginForm,
    changeSection,
    inputSection
  );

  changeButton.addEventListener("click", function (event) {
    // Llamar a la función para realizar la acción deseada
    isLoginForm = toggleLoginForm(
      isLoginForm,
      changeButton,
      registrationForm,
      loginForm,
      changeSection,
      inputSection
    );

    // Prevenir la acción de envío del formulario predeterminada si está dentro de un formulario
    event.preventDefault();
  });

  code.style.display = "none";

  selectRol.addEventListener("change", function () {
    const rol = selectRol.value;

    if (rol == "docente" || rol == "directivo") {
      code.style.display = "block";
    } else {
      code.style.display = "none";
    }
  });
});
