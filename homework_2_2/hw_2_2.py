import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")


def find_and_remove():
    db = connection.students
    grades = db.grades

    query = {'type': 'homework'}

    print 'Actual number of grades %s' % grades.count()
    print 'Removing lowest homework for each student...'

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),
                              ('score', pymongo.ASCENDING)])

        current_student = 0

        for doc in cursor:
            if doc['student_id'] == current_student:
                grades.remove(doc)
                current_student += 1

    except Exception as e:
        print "Exception: ", type(e), e

    print 'Done!'
    print 'Final number of grades %s' % grades.count()


find_and_remove()

# Answer: 54
# { "_id" : 54, "average" : 96.19488173037341 }
