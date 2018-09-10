class SessionsController < ApplicationController
 #protect_from_forgery with: :null_session
 def create
    if params[:password] != nil and params[:username] != nil
    	p = params[:password]
    	u = params[:username]
    	hack =  /union|benchmark|strcmp|locate|STRCMP|position|file|concat|sleep|md5|mid|sub|count|and|left|load|space|instr|pad|conv|right|ascii|cast|reverse|locate|glob|having|like|match|char|regexp|limit|order|group|hex|information/i
    	if u =~ hack or p =~ hack
		flash[:warning] = "hacking detected"
		flash[:danger] = ""
		render :new
		return
    	end
    
        user = User.find_by_sql "SELECT  * from users where username='#{u}' and password='#{p}' LIMIT 1"
        if user.length != 0
     	   session[:user_logged_in] = 1
           redirect_to home_url
        else
	  flash[:warning] = ""
      	  flash[:danger] = "username or password is invalid"
     	  render :new
          return 
        end
   else
	render :new
   end
 end

 def admin
    if params[:password] != nil and params[:username] != nil
        p = params[:password]
        u = params[:username]
    end

     user = User.find_by(username: u, password: p, isadmin:1)
    if user 
          session[:admin] = 1
          redirect_to upload_url
          return
    else
         flash[:warning] = ""
         flash[:danger] = "username or password is invalid"
         render :admin
         return
    end
  
 end


 
 def destroy
    session.clear
    redirect_to login_url
 end
end
