import sqlite3
import datetime





class BladeDB:


    def __init__(self,db_name):

        self.conn = sqlite3.connect(db_name + '.db')
        self.cursor = self.conn.cursor()
        print(" * Starting database: " + db_name)
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

        sql = """create table if not exists graphs (group_number INTEGER,
                                                              data_name DATE,
                                                              wind FLOAT,
                                                              power FLOAT,
                                                              resistance FLOAT)"""
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
                  results
                ORDER BY
                  test_date"""



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

    def fetch_names(self):
        sql = """SELECT
                   group_number,data_name
                FROM
                   graphs
               """
        self.cursor.execute(sql)

        name_dict = {}
        name_list = [[],[],[],[],[],[],[],[]]

        for row in self.cursor.fetchall():

            if row[1] not in name_list[row[0] - 1]:
                name_list[row[0] - 1].append(row[1])

            name_dict.setdefault(str(row[0]),[])

            # Only append name once. This is not a noSQL
            if row[1] not in name_dict[str(row[0])]:
                name_dict[str(row[0])].append(row[1])



        return name_dict,name_list





    def is_name_valid(self,name,group_number):
        sql = """SELECT
                     data_name
                  FROM
                     graphs
                 WHERE
                     data_name = ? AND group_number = ?
                 """

        self.cursor.execute(sql,[name,group_number])

        if len(self.cursor.fetchall()) > 0:
            return False
        else:
            return True


    def add_graph(self,wind,res,power,name,grp_num):


        sql = """INSERT INTO graphs (group_number,data_name,wind,power,resistance)
                         VALUES(?,?,?,?,?)"""

        for index in range(len(wind)):
            self.cursor.execute(sql, [grp_num,name,wind[index], power[index], res[index]])

        self.conn.commit()



    def get_data_by_id(self,name,group_number):


        sql = """SELECT
                     wind,power,resistance
                  FROM
                     graphs
                 WHERE
                     data_name = ? AND group_number = ?
                 """

        self.cursor.execute(sql, [name, group_number])

        data_dict = {"wind":[],
                     "power":[],
                     "res":[]}

        for row in self.cursor.fetchall():

            data_dict["wind"].append(row[0])
            data_dict["power"].append(row[1])
            data_dict["res"].append(row[2])

        return data_dict