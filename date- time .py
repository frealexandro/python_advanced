
from datetime import datetime 
import pytz

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("ciudad de mexico:",mexico_date.strftime("%d/%m/%Y ,%H : %M : %s "))

from datetime import datetime 
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("bogota:",bogota_date.strftime("%d/%m/%Y ,%H : %M : %s "))
