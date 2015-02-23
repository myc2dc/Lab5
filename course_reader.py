import csv, sqlite3,
def load_course_database(db_name, csv_filename):
    with open('my_data.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        tuple(reader)
        conn = sqlite3.connect(db_name)

        for row in reader:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            #with conn:
                #cur = conn.cursor()
                #sql_cmd = "insert into course data values(?, ?,1122,'Lecture', 20, 20, 'T. Jefferson')"

if __name__ == "__main__":
    load_course_database("course1.db", "seas-courses-5years.csv")