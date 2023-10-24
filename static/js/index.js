document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".t-slide");

    slides.forEach((slide) => {
        slide.addEventListener("click", function () {
            if (!this.classList.contains("expanded")) {
                slides.forEach((s) => s.classList.remove("expanded"));
                this.classList.add("expanded");
            } else {
                this.classList.remove("expanded");
            }
        });
    });
});

// Function to apply your styles
function applyInitialStyles() {
    var banner = document.querySelector(".banner");
    var menuIcon = document.querySelector(".menu_icon");
    var name = document.querySelector(".name");
    var line = document.querySelector(".line");

    // Apply your initial styles here
    banner.style.backgroundColor = "transparent";
    menuIcon.style.fill = "#e9eceb";
    name.style.color = "#e9eceb";
    line.style.backgroundColor = "#e9eceb";
}

// Add an event listener for the DOMContentLoaded event
document.addEventListener("DOMContentLoaded", function () {
    // Call your function to apply initial styles when the DOM is ready
    applyInitialStyles();

    // Add the scroll event listener to handle changes when scrolling
    window.addEventListener("scroll", function () {
        var banner = document.querySelector(".banner");
        var menuIcon = document.querySelector(".menu_icon");
        var name = document.querySelector(".name");
        var line = document.querySelector(".line");

        // Get the scroll position
        var scrollPosition = window.scrollY;

        // Define the scroll threshold where changes occur (e.g., 14vh)
        var scrollThreshold = 14 * window.innerHeight / 100;

        // Check if the user has scrolled past the threshold
        if (scrollPosition < scrollThreshold) {
            // Apply changes when scrolled past the threshold
            banner.style.backgroundColor = "transparent";
        } else {
            // Revert to initial styles when above or at the threshold
            banner.style.backgroundColor = "#171b1a";
            menuIcon.style.fill = "#e9eceb";
            name.style.color = "#e9eceb";
            line.style.backgroundColor = "#e9eceb";
        }
    });

    // Trigger the scroll event once to apply the initial styles when the page loads
    window.dispatchEvent(new Event("scroll"));
});

