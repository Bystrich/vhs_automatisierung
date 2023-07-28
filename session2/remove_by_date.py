import os

from datetime import datetime, timedelta

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

print(os.getcwd())

for f in os.listdir():
    filename, file_type = os.path.splitext(f)

    print(filename)

    m_time = datetime.fromtimestamp(os.path.getmtime(f))

    m_time_string = m_time.strftime('%d-%m-%Y')

    print(m_time_string)

    two_weeks = timedelta(weeks=2)

    earliest_date = datetime.now() - two_weeks

    if m_time < earliest_date:
        print("Die Datei " + filename + " ist älter als zwei Wochen!")
        #os.remove(f)


