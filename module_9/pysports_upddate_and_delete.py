# import statements
import mysql.connector
from mysql.connector import errorcode

# database config object
config = {
    "user": "pysports_user",
    "password": "pysp0rts",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def display(cursor, title):

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n -- {} --".format(title))

    for player in players:
        print(" Player ID: {}\n First Name {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                  "VALUES('Jack', 'Fosgate', '1')")

    cursor.execute(add_player)

    db.commit()

    display(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    update_player = ("UPDATE player SET team_id = 2, first_name = 'George', last_name = 'Ramero' WHERE first_name= 'Jack'")

    cursor.execute(update_player)

    db.commit()

    display(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'George'")

    cursor.execute(delete_player)

    db.commit()

    display(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n This is the end, please press enter to exit")

except mysql.connector.Error as err:
    """ handle errors """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()