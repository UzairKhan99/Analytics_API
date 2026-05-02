from decouple import config

DATABASE_URL = config("DATABASE_URL", default="")
DB_TIMEZONE = config("DB_TIMEZONE", default="UTC")
