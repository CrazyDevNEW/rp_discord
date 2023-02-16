# Discord
discord_token = "YOUR_DISCORD_TOKEN"

# DateBase
dbHost = "HOST"
dbPort = "3306"
dbUser = "USERNAME_DB"
dbPassword = "PASSWD_USER_DB"
dbDateBase = "NAME_DB"
dbConnector = "mariadb+mariadbconnector"
dbUrl = f"{dbConnector}://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbDateBase}"
