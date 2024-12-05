Dado('que loguei') do
    visit ''
    sleep 10
  end
  
  Quando('eu logar') do
    login_page = LoginPage.new
    login_page.load
  end
  
  Entao('logaremos') do
  end