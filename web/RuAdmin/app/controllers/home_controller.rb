class HomeController < ApplicationController

  def index
    if session[:user_logged_in]
     render "index"
    else
     redirect_to login_url
    end
  end

end
