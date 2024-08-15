import pymysql

Cursor=pymysql.connect(host='localhost',
                           user='root',
                           password='1#nmnmnm1#',
                           database='booking_system'
                           ).cursor()
dob="11/22/33"
user_id="akash"
user_pass="pass"
queary="INSERT INTO booking_system.user_info (user_id, user_password, date_of_birth) VALUES ('"+user_id+"', '"+user_pass+"','"+dob+"');"
Cursor.execute(queary)
print(queary)




