import request
from linkedin import linkedin

# Autenticacion de la API con linkedin
API_KEY = "wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl"
API_SECRET = "daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG"
#La URL a la que ser� direccionado luego de identificarse
RETURN_URL = "http://localhost"
#Si la autenticaci�n ha sido exitosa, retorna permisos de usuario, c�digo de autorizaci�n y token
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url
# Se captura la autorizaci�n y el token
application = linkedin.LinkedInApplication(authentication)
authentication.get_access_token()
#Luego de autenticado, se puede obtener acceso a informaci�n del usuario
# Se obtiene la informaci�n de perfil del usuario y se imprime en consola
application.get_profile()
print("Nombre: ".application['firstname'])
print("Apellido: ".application['lastname'])
print("Titular: ".application['headline'])
print("URL de Perfil: ".application['siteStandardProfileRequest'])
