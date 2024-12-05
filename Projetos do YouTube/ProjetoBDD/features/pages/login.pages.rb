class LoginPage < SitePrism::Page
    set_url "https://www.linkedin.com/login/pt"

    element :emailField, :id, "username"
    element :passwordField, :id, "password"
    element :loginButton, :xpath, "//*[@id="organic-div"]/form/div[4]/button"

    def userLogin
        clickemail.click
        emailField.set "contatojp30@gmail.com"
        passwordField.set "@JulioCadelca9898*"
        loginButton.click
    end
    
end