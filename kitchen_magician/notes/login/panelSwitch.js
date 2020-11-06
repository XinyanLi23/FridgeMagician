const signup = document.querySelector("#signup");
const login = document.querySelector("#login");
const container = document.querySelector("#login-container");

signup.addEventListener("click", () => {
    console.log("SIGNUP BUTTON CLICKED");
    container.classList.add("sign-up-mode");
});

login.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});