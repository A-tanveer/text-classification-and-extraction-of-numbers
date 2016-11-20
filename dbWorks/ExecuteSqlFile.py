def execute_scripts_from_file(filename):
    import pymysql

    conn = pymysql.Connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    # Execute every command from the input file
    for command in sql_commands:
        try:
            cur.execute(command)
        except:
            print("Command skipped: ")