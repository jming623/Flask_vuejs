from config.db_connector import Database

class testBoard:
   
    def __init__(self):
        self.db_class = Database()

    def getTestBoardList(self):
        result = ''
        sql = '''
            SELECT 
                board_no,
                board_code,
                subject,
                content,
                reg_id,                
                reg_dt,
                update_dt
            FROM testboard
            ORDER BY reg_dt DESC
        '''
        result = self.db_class.executeAll(sql)
    
        return result

