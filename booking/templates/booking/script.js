document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission

        const checkin = document.getElementById("checkin").value;
        const checkout = document.getElementById("checkout").value;
        const guests = document.getElementById("guests").value;

        if (!checkin || !checkout) {
            alert("Please select check-in and check-out dates.");
            return;
        }

        if (new Date(checkout) <= new Date(checkin)) {
            alert("Check-out date must be after check-in date.");
            return;
        }

        if (guests <= 0) {
            alert("Please enter a valid number of guests.");
            return;
        }

        alert("Booking details are valid!");
        // Here we can send data to the backend
    });
});


// login page
document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded successfully!"); // Debugging log

    const loginForm = document.getElementById("loginForm");
    if (!loginForm) {
        console.error("Login form not found!");
        return;
    }

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const emailInput = document.getElementById("email");
        const passwordInput = document.getElementById("password");

        if (!emailInput || !passwordInput) {
            console.error("Email or Password field not found!");
            return;
        }

        const email = emailInput.value;
        const password = passwordInput.value;

        console.log("Email:", email);
        console.log("Password:", password);
        
        if (!email.includes("@")) {
            alert("Please enter a valid email address.");
            return;
        }

        if (password.length < 6) {
            alert("Password must be at least 6 characters long.");
            return;
        }

        alert("Login successful! (Backend connection needed)");
    });
});



// signup page
document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded successfully!");

    const signupForm = document.getElementById("signupForm");

    if (signupForm) {
        signupForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirmPassword").value;

            if (name === "" || email === "" || password === "" || confirmPassword === "") {
                alert("All fields are required!");
                return;
            }

            if (!email.includes("@")) {
                alert("Please enter a valid email address.");
                return;
            }

            if (password.length < 6) {
                alert("Password must be at least 6 characters long.");
                return;
            }

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return;
            }

            alert("Sign-up successful! Redirecting to login...");
            window.location.href = "login.html"; // Redirect to login page
        });
    }
});
