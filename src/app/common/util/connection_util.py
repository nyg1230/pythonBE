from app.common import util
import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode
from app.common.decorator import decorator

db_info = util.property_util.get_value("database")

class ConnectionUtil():
    @staticmethod
    def __get_conn():
        conn = None

        try:
            conn = psycopg2.connect(**db_info)
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
    def __conn_template(fn: callable):
        result = None
        conn = None
        
        try:
            conn = ConnectionUtil.__get_conn()
            result = fn(conn)
            conn.commit()
        except CustomException as e:
            raise e
        except Exception as e:
            raise CustomException(ExcpetionCode.DB_ERROR)
        finally:
            if (conn is not None):
                ConnectionUtil.__close_conn(conn)
                
        return result

    @staticmethod
    @decorator.sql_logging
    def execute(sql = "", param = ()):       
        def fn(conn):
            result = None
            with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
                cur.execute(sql, param)
                result = cur.fetchall()
            return result
        
        return ConnectionUtil.__conn_template(fn)
    
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
    
    @staticmethod
    def multiple_insert(sql = "", params = [], template = None):
        def fn(conn):
            result = None
            with conn.cursor() as cur:
                result = psycopg2.extras.execute_values(cur, sql, params, template)
            return result
        return ConnectionUtil.__conn_template(fn)