document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("navctrl");
    const navbar = document.getElementById("SideNav");
    const main2 = document.getElementById("main2");

    toggleButton.addEventListener("click", function () {
        if (navbar.style.width === "0%") {
            navbar.style.width = "80%";
            main2.style.opacity= "0.2";
        } else {
            navbar.style.width = "0%";
            main2.style.opacity= "1"
        }
    });

});

