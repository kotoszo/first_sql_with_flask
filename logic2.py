import connect_db
import psycopg2
import logic


@logic.db_connector
def példa(cursor):
    cursor.execute(
        """SELECT {last}, {first}, {id} FROM {people}""".format(last='last_name', first=False, id=False)
    )
    a = cursor.fetchall()
    return a


@logic.db_connector
def get_people(cursor, people, info_tuple):
    if len(info_tuple) == 1:
        cursor.execute("""SELECT %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 2:
        cursor.execute("""SELECT %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 3:
        cursor.execute("""SELECT %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 4:
        cursor.execute("""SELECT %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 5:
        cursor.execute("""SELECT %s, %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 6:
        cursor.execute("""SELECT %s, %s, %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 7:
        cursor.execute("""SELECT %s, %s, %s, %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 8:
        cursor.execute("""SELECT %s, %s, %s, %s, %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    elif len(info_tuple) == 9:
        cursor.execute("""SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s FROM {people};""".format(people=people) % info_tuple)
    data = cursor.fetchall()
    return data


def tuple_maker(dictionary):
    info_list = [value for key, value in dictionary.items()]
    info_tuple = tuple(info_list)
    return info_tuple


@logic.db_connector
def search_helper(cursor, group_to_search, key_for_search, what_to_search):
    if key_for_search == 'id':
        cursor.execute("""SELECT * FROM %s WHERE %s = %s;""" % (group_to_search, key_for_search, what_to_search))
    else:
        what_to_search = "%" + what_to_search + "%"
        cursor.execute("""SELECT * FROM %s WHERE %s LIKE '%s';""" % (group_to_search, key_for_search, what_to_search))
    data = cursor.fetchall()
    return data
