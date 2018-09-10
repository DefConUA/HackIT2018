Rails.application.routes.draw do
  resources :resumes, only: [:index, :new, :create, :destroy]
  get "/upload", to: "resumes#index"

  get '/', to: 'sessions#create', as: 'login'
  match '/admin', to: 'sessions#admin', via: :all
  get '/logout', to: 'sessions#destroy', as: 'logout'
  get '/home', to: 'home#index', as: 'home'
  resources :sessions
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
