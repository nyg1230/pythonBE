from app.common import util
import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode

db_info = util.property_util.get_value("database")

class ConnectionUtil():
    @staticmethod
    def __get_conn():
        conn = None

        try:
            conn = psycopg2.connect(
                dbname = db_info.get("dbname"),
                user = db_info.get("user"),
                password = db_info.get("password"),
                host = db_info.get("host"),
                port = db_info.get("port")
            )
        except Exception as e:
            raise CustomException(ExcpetionCode.CONN_CREATE_ERROR)

        return conn
    
    @staticmethod
    def __close_conn(conn: connection):
        try:
            conn.close()
        except:
            raise CustomException(ExcpetionCode.CONN_CLOSE_ERROR)
            
    @staticmethod
    def execute(sql = "", param = ()):
        result = None
        conn = None

        try:
            conn = ConnectionUtil.__get_conn()
            with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
                cur.execute(sql, param)
                result = cur.fetchall()
            conn.commit()
        except CustomException as e:
            raise e
        except Exception as e:
            print(e)
            raise CustomException(ExcpetionCode.DB_ERROR)
        finally:
            if (conn is not None):
                ConnectionUtil.__close_conn(conn)
                
        return result
    
    @staticmethod
    def select_one(sql = "", param = ()):
        result = ConnectionUtil.execute(sql, param)

        if (util.common_util.is_list(result)):
            len = result.__len__()
            if (len > 1):
                raise CustomException(ExcpetionCode.MANY_RESULTSET)
            elif (len == 0):
                result = None
            else:
                result = result[0]
        
        return result