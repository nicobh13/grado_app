document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menu-icon'); // Get your SVG element
    const menu = document.getElementById('menu');
    const closeButton = document.getElementById('close-menu'); // Get the close button

    // Function to open/close the menu
    function toggleMenu() {
        // Toggle the menu's right position to show/hide it
        if (menu.style.right === '0px') {
            menu.style.right = '-250px';
        } else {
            menu.style.right = '0px';
        }
    }

    // Toggle the menu when you click the menu icon
    menuIcon.addEventListener('click', toggleMenu);

    // Toggle the menu when you click the close button
    closeButton.addEventListener('click', toggleMenu);

    const talleresElement = document.getElementById('talleres');
    const dulcesElement = document.getElementById('dulces')
    // Obtener el menú desplegable por su clase
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const dulcesMenu = document.querySelector('.dulces-menu');
    // Agregar un controlador de eventos al elemento "Talleres"
    talleresElement.addEventListener('click', () => {
        // Alternar la visibilidad del menú desplegable
        if (dropdownMenu.style.display === 'inline-block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'inline-block';
        }
    });

    dulcesElement.addEventListener('click', () => {
        // Alternar la visibilidad del menú desplegable
        if (dulcesMenu.style.display === 'inline-block') {
            dulcesMenu.style.display = 'none';
        } else {
            dulcesMenu.style.display = 'inline-block';
        }
    });

});

