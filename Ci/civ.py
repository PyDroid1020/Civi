import sqlite3
from colorama import Fore
import math
import os

class Civi:
    def __init__(self):
        self

    @classmethod
    def setup(self):
        try:
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'database')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)
                sqlite3.connect('./database/level.db')
                sqlite3.connect('./database/welcome.db')
            print(Fore.YELLOW + "✅ | levels database connected") 
            print(Fore.YELLOW + "✅ | welcome database connected")
        except:
            return print(Fore.RED + "Something went wrong ❓")

    @classmethod
    def update_level_data(self , message):
        guild_id = message.guild.id
        member_id = message.author.id
        db = sqlite3.connect('./database/level.db' , isolation_level=None)
        cursor = db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS guild (guild_id int, user_id int, exp int, PRIMARY KEY (guild_id, user_id))"
        )
        cursor = cursor.execute("INSERT OR IGNORE INTO guild(guild_id , user_id , exp) VALUES (?,?,?)" , (guild_id , member_id , 1))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE guild SET exp = exp + 1 WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))


    @classmethod
    def get_user_xp(self, guild_id , member_id):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur = db.cursor()
        cur.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur.fetchone()
        exp = data[0]
        return exp
    @classmethod
    def get_user_level(self, guild_id , member_id):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cursor = db.cursor()
        cursor.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cursor.fetchone()
        exp = data[0]
        lvl = int(math.sqrt(exp)//1)
        return lvl
    @classmethod
    def get_user_rank(self , guild_id , member_id):
        db1 = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur1 = db1.cursor()
        cur1.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur1.fetchone()
        exp = data[0]
        db2 = sqlite3.connect("./database/level.db")
        cur2 = db2.cursor()
        cur2.execute("SELECT exp FROM guild WHERE guild_id = ?", (guild_id,))
        rank = 1
        for value in cur2:
            if exp < value[0]:
                rank += 1
        return rank
    @classmethod
    def set_user_xp(self , guild_id , member_id , xp):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur = db.cursor()
        cur.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur.fetchone()
        if data is None:
            return print("This user has no exp")
        else:
            cur.execute("UPDATE guild SET exp = ? WHERE guild_id = ? AND user_id = ?", (xp , guild_id, member_id))
    @classmethod
    def add_user_xp(self , guild_id , member_id , xp):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur = db.cursor()
        cur.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur.fetchone()
        if data is None:
            return print("This user has no exp")
        else:
            cur.execute("UPDATE guild SET exp = exp +? WHERE guild_id = ? AND user_id = ?", (xp , guild_id, member_id))

    @classmethod
    def decrease_user_xp(self , guild_id , member_id , xp):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur = db.cursor()
        cur.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur.fetchone()
        if data is None:
            return print("This user has no exp")
        else:
            cur.execute("UPDATE guild SET exp = exp - ? WHERE guild_id = ? AND user_id = ?", (xp , guild_id, member_id))
    @classmethod
    def reset_member_xp(self , guild_id , member_id):
        db = sqlite3.connect("./database/level.db" , isolation_level=None)
        cur = db.cursor()
        cur.execute("SELECT exp FROM guild WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
        data = cur.fetchone()
        if data is None:
            return print("This user has no exp")
        else:
            cur.execute("UPDATE guild SET exp = 0 WHERE guild_id = ? AND user_id = ?", (guild_id, member_id))
            

        
    class settings:
        class guild:
            def reset_guild_data(self , guild_id:int):
                db = sqlite3.connect('./database/level.db' , isolation_level=None)
                cur = db.cursor()
                cur.execute("SELECT * FROM guild WHERE guild_id = ?" , (guild_id,))
                data = cur.fetchone()
                if data is None:
                    return print("No data for this server")
                if data is not None:
                    cur.execute("DELETE FROM guild WHERE guild_id = ?" , (guild_id,))
                    db.commit()
                    print("Data reseted")
        def repair():
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'database')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)
                sqlite3.connect('./database/level.db')
                sqlite3.connect('./database/welcome.db')
                print(Fore.GREEN + "Fixed")
            if os.path.exists(final_directory):
                os.makedirs(final_directory)
                sqlite3.connect('./database/level.db')
                sqlite3.connect('./database/welcome.db')
                print(Fore.GREEN + "Files dirs well")   
