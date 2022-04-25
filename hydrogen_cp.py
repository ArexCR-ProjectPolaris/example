#Hydrogen cp's
#to install package in Py3.10 use py -m pip install (package)

import valispace
import keyring
from thermochem.janaf import Janafdb

username = 'ramir169' # username for valispace
url = 'polarisproject.valispace.com' # url for our Valispace
id_roy = 'experiment' # id of the project that we are pulling from
valispace_API = valispace.API(url=url, username = username, password = keyring.get_password("valispace", username))

T = valispace_API.get_vali(id=20091)["value"]    # temperature [K]
MW = valispace_API.get_vali(id=20092)["value"]   # MW [g/mol]
db = Janafdb()                          # locally intitializes the NIST thermochemical database
hydrogen = db.getphasedata(formula='H2')# hydrogen properties
CP = hydrogen.cp(T)/MW                  # cp [kJ/kg-K]
valispace_API.update_vali(id=20096,formula=str(CP)) # update cp value in Valispace
#does it work?


