from app.database.utils import get_driver
from app.constants import POSTGRES_URL

if __name__ == "__main__":
    print(POSTGRES_URL)
    print(get_driver("Mika Hakkinen").to_dict())