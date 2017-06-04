import psycopg2
from psycopg2 import extras
import login
import connect_db


def db_connector(func):
    def db_wrapper(conn, *args, **kwargs):
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            cursor.execute("BEGIN")
            retval = func(cursor, *args, **kwargs)
            cursor.execute("COMMIT")
        except:
            cursor.execute("ROLLBACK")
            raise
        finally:
            cursor.close()
        return retval
    return db_wrapper


@db_connector
def mentors_list(cursor):
    cursor.execute(
        """SELECT mentors.id as mentor_id, first_name as mentor_first_name, last_name as mentor_last_name,
        schools.name as school_name, schools.country as school_country
        FROM mentors
        JOIN schools ON mentors.city = schools.city
        ORDER BY mentors.id;"""
        )
    return cursor.fetchall()


@db_connector
def schools(cursor):
    cursor.execute(
        """SELECT first_name as mentor_first_name, last_name as mentor_last_name,
        schools.name as school_name, schools.country as school_country
        FROM mentors
        FULL OUTER JOIN schools ON mentors.city = schools.city
        ORDER BY mentors.id;"""
        )
    return cursor.fetchall()


@db_connector
def mentors_by_country(cursor):
    cursor.execute(
        """SELECT COUNT(id), city
        FROM mentors
        GROUP BY city;"""
    )
    return cursor.fetchall()


@db_connector
def contacts(cursor):
    cursor.execute(
        """SELECT schools.name as school_name, mentors.first_name as mentor_first_name, mentors.last_name as mentor_last_name
        FROM mentors
        JOIN schools ON mentors.id = schools.id
        ORDER BY schools.name;"""
    )
    return cursor.fetchall()


@db_connector
def applicants(cursor):
    cursor.execute(
        """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
        FROM applicants
        JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
        WHERE applicants_mentors.creation_date > '2016-01-01'
        ORDER BY applicants_mentors.creation_date;"""
    )
    return cursor.fetchall()


@db_connector
def apps_and_ments(cursor):
    cursor.execute(
        """SELECT applicants.first_name as applicant_first_name,
        applicants.application_code as applicant_application_code,
        mentors.first_name as mentor_first_name
        FROM applicants
        LEFT JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
        LEFT JOIN mentors ON applicants_mentors.mentor_id = mentors.id;"""
    )
    return cursor.fetchall()
