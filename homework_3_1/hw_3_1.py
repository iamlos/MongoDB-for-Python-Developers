import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")


def remove_lowest_homework():
    db = connection.school
    students = db.students

    query = {}

    print 'Removing lowest homework for each student...'

    try:
        students_docs = students.find(query)

        for student in students_docs:
            student['scores'].sort()
            for score in student['scores']:
                if score['type'] == 'homework':
                    current_student_id = student['_id']
                    students.update({'_id': current_student_id}, {'$pull': {'scores': score}})
                    break

    except Exception as e:
        print "Exception: ", type(e), e

    print 'Done!'


remove_lowest_homework()

# Answer: 13
# { "_id" : 13, "average" : 91.98315917172745 }

