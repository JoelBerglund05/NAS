@app.route('/news')
def news():
    import pymysql
    import re

    host='localhost'
    user = 'root'
    password = ''
    db = 'skripsi'

    try:
        con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
     except Exception (*as e:
        sys.exit('error',e))

     cur = con.cursor()
     cur.execute("SELECT * FROM dataset")
     data = cur.fetchall()
     
     cur = con.cursor()
     cur.execute("SELECT * FROM dataset")
     data = cur.fetchall()
     render_template('template.html', data=data)


     for row in data:
         id_berita = row[0]
         judul = row[1]
         isi = row[2]
         print('===============================================')
         print('BERITA KE', id_berita)
         print('Judul :', judul)
         print('Isi   :', isi)
         print('===============================================')

return render_template('home.html')