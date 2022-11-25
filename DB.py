import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('DBB.db')
        return con
        print("Соединение работает")
    except Error:
        print(Error)


def sql_party(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE party(id_party integer PRIMARY KEY, "
        "ideology text, charter_program text, attitude_power text)")

    cursorObj.execute(
        "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(1,'Либерализм','Основные сферы жизни:Медицина.Образование.', 'Правящая')")
    cursorObj.execute(
        "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(2,'Консерватизм','Основные сферы жизни:Медицина.Развитие туризма.', 'Правящая')")
    cursorObj.execute(
        "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(3,'Либерализм','Основные сферы жизни:Медицина.Наука.', 'Оппозиционная')")
    cursorObj.execute(
        "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(4,'Консерватизм','Основные сферы жизни:Медицина.Развитие инфраструктуры.', 'Оппозиционная')")
    cursorObj.execute(
        "INSERT INTO party(id_party, ideology , charter_program , attitude_power) VALUES(5,'Либерализм','Основные сферы жизни:Медицина.Поддержка молодым семьям', 'Правящая')")

    con.commit()


def sql_event(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE event(id_event integer PRIMARY KEY, date_event date, "
        "id_party integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE)")

    cursorObj.execute(
        "INSERT INTO event(id_event,date_event, id_party) VALUES(1,'11.09.2021',1)")
    cursorObj.execute(
        "INSERT INTO event(id_event,date_event, id_party) VALUES(2,'10.09.2021',1)")
    cursorObj.execute(
        "INSERT INTO event(id_event,date_event, id_party) VALUES(3,'11.09.2000',2)")
    cursorObj.execute(
        "INSERT INTO event(id_event,date_event, id_party) VALUES(4,'11.09.2020',3)")
    cursorObj.execute(
        "INSERT INTO event(id_event,date_event, id_party) VALUES(5,'11.10.2021',4)")

    con.commit()


def sql_party_members(con):
    cursorObj = con.cursor()
    cursorObj.execute(
      "CREATE TABLE party_members(id_party_members integer PRIMARY KEY, full_name text, position_code real, "
      "id_party integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE)")

    cursorObj.execute(
        "INSERT INTO party_members(id_party_members , full_name , position_code , id_party ) VALUES(1,'Алексеева Оксана Михайловна ', 12, 1)")
    cursorObj.execute(
        "INSERT INTO party_members(id_party_members , full_name , position_code , id_party ) VALUES(2,'Иванов Петр Геннадьевич', 14, 1)")
    cursorObj.execute(
        "INSERT INTO party_members(id_party_members , full_name , position_code , id_party ) VALUES(4,'Осадченко Ирина Валерьяновна', 5, 3)")
    cursorObj.execute(
        "INSERT INTO party_members(id_party_members , full_name , position_code , id_party ) VALUES(3,'Болат Серкан Капибарович', 6, 2)")
    cursorObj.execute(
        "INSERT INTO party_members(id_party_members , full_name , position_code , id_party ) VALUES(5,'Петров Антон Васильевич', 2, 2)")
    con.commit()


def sql_regional_office(con):
    cursorObj = con.cursor()
    cursorObj.execute(
       "CREATE TABLE regional_office(id_regional_office integer PRIMARY KEY, company text)")

    cursorObj.execute(
        "INSERT INTO regional_office(id_regional_office , company) VALUES(1,'Краснодарский край')")
    cursorObj.execute(
        "INSERT INTO regional_office(id_regional_office , company) VALUES(2,'Московская область')")
    cursorObj.execute(
        "INSERT INTO regional_office(id_regional_office , company) VALUES(3,'Ленинградская область')")
    cursorObj.execute(
        "INSERT INTO regional_office(id_regional_office , company) VALUES(4,'Ростовская область')")
    cursorObj.execute(
        "INSERT INTO regional_office(id_regional_office , company) VALUES(5,'Ставропольский край')")
    con.commit()


def sql_main_plot(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE main_plot(id_main_plot integer PRIMARY KEY, title text, id_party integer,"
        " id_regional integer,FOREIGN KEY (id_party) REFERENCES party (id_party) ON DELETE CASCADE ,"
        "FOREIGN KEY (id_regional) REFERENCES regional_office (id_regional) ON DELETE CASCADE)")

    cursorObj.execute(
        "INSERT INTO main_plot(id_main_plot,title ,id_party ,id_regional) VALUES(1,'Центральный Федеральный округ',1, 2)")
    cursorObj.execute(
        "INSERT INTO main_plot(id_main_plot,title ,id_party ,id_regional) VALUES(2,'Южный Федеральный округ',2, 1)")
    cursorObj.execute(
        "INSERT INTO main_plot(id_main_plot,title ,id_party ,id_regional) VALUES(3,'Северно-Западный Федеральный округ',3, 3)")
    cursorObj.execute(
        "INSERT INTO main_plot(id_main_plot,title ,id_party ,id_regional) VALUES(4,'Южный Федеральный округ',4, 4)")
    cursorObj.execute(
        "INSERT INTO main_plot(id_main_plot,title ,id_party ,id_regional) VALUES(5,'Северо_Кавказский Федеральный округ',5, 5)")
    con.commit()


def sql_city(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE city(id_city integer PRIMARY KEY, city_name text, id_regional integer, size real,"
        "FOREIGN KEY (id_regional) REFERENCES regional_office (id_regional) ON DELETE CASCADE)")

    cursorObj.execute(
        "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(1,'Краснодар',1,294)")
    cursorObj.execute(
        "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(2,'Усть-Лабинск',1,37)")
    cursorObj.execute(
        "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(3,'Якутск',10,122)")
    cursorObj.execute(
        "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(4,'Москва',2,2511)")
    cursorObj.execute(
        "INSERT INTO city(id_city , city_name , id_regional , size ) VALUES(5,'Санкт-Петербург',3,1439)")
    con.commit()


def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]


# con = sql_connection()
# sql_party(con)
# sql_party_members(con)
# sql_event(con)
# sql_regional_office(con)
# sql_city(con)
# sql_main_plot(con)

#delete,update