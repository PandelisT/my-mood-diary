from controllers.journals_controller import journal
from controllers.auth_controller import auth
from controllers.profile_images_controller import profile_images
from controllers.client_controller import clients

registerable_controllers = [
    auth,
    journal,
    profile_images,
    clients
]