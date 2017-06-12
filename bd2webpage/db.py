import sqlite3
import datetime





class BladeDB:


    def __init__(self,db_name):

        self.conn = sqlite3.connect(db_name + '.db')
        self.cursor = self.conn.cursor()
        print("Starting database: " + db_name)
        sql = """create table if not exists results (group_number INTEGER,
                                                      test_date DATE,
                                                      test_id INT,
                                                      wind FLOAT,
                                                      power FLOAT,
                                                      cp FLOAT,
                                                      inner_res INT,
                                                      load_res INT,
                                                      flux FLOAT,
                                                      eqa FLOAT,
                                                      eqb FLOAT,
                                                      eqc FLOAT,
                                                      blade_length FLOAT)"""
        self.cursor.execute(sql)

    def add_record(self,group_number,wind,power,cp,inner_res,load_res,flux,eqa,eqb,eqc,blade_length):


        # Date today
        test_date = datetime.datetime.now()




        sql = """SELECT 
                    test_id
                FROM
                    results
                WHERE
                    group_number = ?"""

        self.cursor.execute(sql, [int(group_number), ])
        # Generate test id
        c_id = self.cursor.fetchall()

        if len(c_id) != 0:
            test_id = max([int(val[0]) for val in c_id]) +1
        else:
            test_id = 1



        sql = """INSERT INTO results (group_number,test_date,test_id,wind,power,cp,inner_res,load_res,flux,eqa,eqb,eqc,blade_length)
                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"""

        for index in range(len(cp)):
            self.cursor.execute(sql, [group_number,test_date,test_id,wind[index],power[index],cp[index],
                inner_res,load_res,flux,eqa,eqb,eqc,blade_length])

        self.conn.commit()

    def fetch_group_params(self,grp_no):

        sql = """SELECT 
                    test_date,inner_res,flux,eqa,eqb,eqc,blade_length
                FROM
                    results
                WHERE
                    group_number = ?
                ORDER BY
                    test_date DESC
                """
        self.cursor.execute(sql,[int(grp_no),])

        params = self.cursor.fetchone()

        return params

    def get_all_graph(self):



        sql = """SELECT
                  group_number,
                  test_id,
                  wind,
                  power,
                  cp
                FROM 
                  results"""



        self.cursor.execute(sql)

        # Create an object with all data
        all_data_dict = {}



        for row in self.cursor.fetchall():
            grp_test_id = "Group-"+str(row[0]) + "-test-" + str(row[1])

            all_data_dict.setdefault(grp_test_id,{'wind':[],'power':[],'cp':[]})['wind'].append(row[2])
            all_data_dict[grp_test_id]['power'].append(row[3])
            all_data_dict[grp_test_id]['cp'].append(row[4])

        return(all_data_dict)


    def get_leaders(self):
        sql = """SELECT * FROM results ORDER BY power DESC LIMIT 1"""
        self.cursor.execute(sql)

        power_winner = self.cursor.fetchone()

        sql = """SELECT * FROM results ORDER BY cp DESC LIMIT 1"""
        self.cursor.execute(sql)

        cp_winner = self.cursor.fetchone()

        return power_winner,cp_winner

    def get_best(self):
        # Appending to this list
        all_best = []
        for i in range(1,9):
            sql = """SELECT
                        test_id, cp, power
                     FROM
                        results 
                    WHERE
                        group_number = ?
                     ORDER BY
                        power
                     DESC LIMIT 1"""

            self.cursor.execute(sql,[i,])
            best_score_p = self.cursor.fetchone()

            sql = """SELECT
                        test_id, cp
                     FROM
                        results 
                    WHERE
                        group_number = ?
                     ORDER BY
                        cp
                     DESC LIMIT 1"""

            self.cursor.execute(sql, [i, ])
            best_score_c = self.cursor.fetchone()

            # Only if the group has data
            if best_score_p != None:
                all_best.append([i,best_score_p[0],best_score_c[0],round(best_score_c[1],4),round(best_score_p[1],5)])

        return all_best