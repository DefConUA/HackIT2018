class ResumesController < ApplicationController
  before_filter :beforeFilter

  def beforeFilter
     $request = request
  end 
   def index
      if session[:admin]
	require 'digest'
	digest = Digest::SHA256.hexdigest $request.remote_ip + $request.remote_ip
        @resumes = Dir.glob("uploads/resumes/#{digest}/*").map(&File.method(:realpath));
      else 
	redirect_to login_url
      end
   end
   
   def new
     if session[:admin]
       @resume = Resume.new
     else
        redirect_to login_url
     end
   end
   
   def create
    if session[:admin]
      @resume = Resume.new(resume_params)
      
      if @resume.save
         redirect_to resumes_path, notice: "Your resume has been uploaded! :)."
      else
         render "new"
      end
   else
        redirect_to login_url
   end
      
   end
   
   def destroy
     if session[:admin]
      @resume = Resume.find(params[:id])
      @resume.destroy
      redirect_to resumes_path, notice:  "The resume #{@resume.name} has been deleted."
     else
        redirect_to login_url
     end
   end
   
   private
      def resume_params
      params.require(:resume).permit(:name, :attachment)
   end
 

end
