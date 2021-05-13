import sqlite3

conn = sqlite3.connect("week8.db")
c = conn.cursor()
# c.execute("CREATE TABLE video (id text,playlistName text,url text);")
# c.execute("DROP TABLE video;")
# c.execute("SELECT url FROM video WHERE id='해성' AND playlistName='일번';")
# conn.commit()
a = c.fetchall()
print(a)