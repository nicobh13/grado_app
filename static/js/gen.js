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
});

