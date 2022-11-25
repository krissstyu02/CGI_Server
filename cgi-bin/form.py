#!/usr/bin/env python3
import cgi
import sqlite3
from DB import *

from sqlite3 import Error
def id_find(con, req_id):
    curs = con.cursor()
    curs.execute(f'SELECT * FROM {tbl_name}')
    cc = curs.fetchall()
    for d in range(len(cc)):
        if cc[d][0] == req_id:
            return True

    return False


form = cgi.FieldStorage()
if form.getvalue('table_list') is not None:  # запись в файл
    tbl_name = form.getvalue('table_list')
    file = open("cgi-bin/table.txt", "w")
    file.write(form.getvalue('table_list'))
else:
    inp = open("cgi-bin/table.txt", "r")
    tbl_name = inp.read()
    inp.close()

print("Content-type: text/html\n")
print(f"""<!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Работа с таблицей {tbl_name}</title>
            </head>
            <body>
                <form action="/index.html">
                    <p><input type="submit" value="Вернуться к выбору таблицы"></p>
                </form>
                <form action="/cgi-bin/form.py">
                    <h3>Что Вы хотите сделать с таблицей {tbl_name}?</h3>
                    <p><select name="act_list">
                        <option></option>
                        <option>Добавить запись</option>
                        <option>Обновить запись</option>
                        <option>Удалить запись</option>
                        <option>Вывести все записи</option>
                    </select></p>
                    <p><input type="submit" value="Отправить"></p>
                """)

# if form.getvalue('act_list') is not None:
connection = sql_connection()
table_str = '<table><tr>\n'

act = form.getvalue('act_list')
if form.getvalue('act_list') is not None:  # запись в файл
    act = form.getvalue('act_list')
    file = open("cgi-bin/option.txt", "w")
    file.write(form.getvalue('act_list'))
    file.close()
else:
    inp = open("cgi-bin/option.txt", "r")
    act = inp.readline()
    inp.close()

if act is not None:
    if act == 'Добавить запись':
        print("""
                Введите данные новой записи через пробел: <input type="text" name="new_tran">
                <p><input type="submit" value="Отправить"></p>
                    <style>
                    <meta charset="utf-8">
                    input[type="text"] 
                    {
                        width: 300px;
                    }
                    </style>
               </form>
        """)

        cursorObj = connection.cursor()
        cursor = connection.cursor()
        row = form.getfirst("new_tran").split()
        cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
        headers = [description[0] for description in cursor.description]

        if len(row) < len(headers) - 1 or len(row) >= len(headers):
            print("""Было введено неверное число аргументов -> запись не добавлена в таблицу""")
        elif len(row) == len(headers) - 1:

            fields = ""
            for j in range(len(row)):
                fields += '?, '
            fields = fields[:-2]
            cursorObj.execute(f'INSERT INTO {tbl_name} VALUES(null, {fields})', row)
            connection.commit()
            print("""запись успешно добавлена в таблицу""")

        file = open("cgi-bin/option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Обновить запись':
        print("""
                        Введите id записи, которую хотите обновить: <input type="number" name="update_id"><br /><br />
                        Введите обновленные данные записи через пробел: <input type="text" name="update_tran">
                        <p><input type="submit" value="Отправить"></p>
                            <style>
                            
                            input[name="update_id"]
                            {
                                width:50px;
                            }
                            <meta charset="utf-8">
                            input[name="update_tran"] 
                            {
                                width: 300px;
                            }
                            
                            </style>
                       </form>
                """)

        cursorObj = connection.cursor()
        update_id = int(form.getfirst("update_id"))
        row = form.getfirst("update_tran").split()
        cursorObj.execute(f'SELECT * FROM {tbl_name}')
        headers = [description[0] for description in cursorObj.description]

        find = id_find(connection, update_id)
        sql_str = 'UPDATE ' + tbl_name + ' SET '

        if len(row) < len(headers) - 1 or len(row) >= len(headers):
            print('Было введено неверное число аргументов -> запись не добавлена в таблицу')
        elif not find:
            print('не существует записи с таким id')
        elif len(row) == len(headers) - 1 and find:
            for i in range(len(row)):
                sql_str += headers[i + 1] + ' = "' + row[i] + '", '
            sql_str = sql_str[:-2]
            str3='id_'+str(tbl_name)
            sql_str += ' where '+str3  +' = ' + str(update_id)
            cursorObj.execute(sql_str)
            connection.commit()
            print("запись успешно изменена")

        file = open("cgi-bin/option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Удалить запись':
        print("""
                        Введите id записи, которую хотите удалить: <input type="number" name="delete_id">
                        <p><input type="submit" value="Отправить"></p>
                            <style>
                            input[name="delete_id"]
                            {
                                width:50px;
                            }
                            </style>
                       </form>
                """)

        cursorObj = connection.cursor()
        delete_id = int(form.getfirst("delete_id"))
        find = id_find(connection, delete_id)
        if find:
            cursorObj.execute(f'DELETE from {tbl_name} where id_{tbl_name} = {delete_id}')
            connection.commit()
            print("запись успешно удалена")
        else:
            print('не существует записи с таким id')

    file = open("cgi-bin/option.txt", "w")
    file.write('None')
    file.close()

if act == 'Вывести все записи':
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
    headers = [description[0] for description in cursor.description]
    for i in range(len(headers)):
        table_str += '<th>' + headers[i] + '</th>'
    table_str += '</tr>\n\n'

    for row in cursor.fetchall():
        table_str += '<tr>\n'
        tmp = list(row)
        for i in range(len(tmp)):
            table_str += '<td>' + str(tmp[i]) + '</td>'
        table_str += '</tr>\n'

    table_str += """<style>table {
           border: 1px solid grey;
           border-collapse: collapse;
            }
           td {
           border: 1px solid grey;
           text-align: center;
            }
            th {
           border: 1px solid grey;
           min-width:160px;
            }
        </table>
        </style>"""
    print(table_str)
    print('</table>')
    file = open("cgi-bin/option.txt", "w")
    file.write('None')
    file.close()

print("""</body>
         </html>""")
