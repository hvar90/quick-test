import pandas as pd
from django.db import connection 


def get_df_from_query(sql_query,*args):
	
	with connection.cursor() as cursor:
		df = pd.read_sql_query(sql_query, connection,params=args)
	return df
	
class QueryService:
	# def __init__(self, nombre):
		# self.nombre = nombre

	def get_df_from_query(self,sql_query,*args):
		with connection.cursor() as cursor:
			df = pd.read_sql_query(sql_query, connection,params=args)
		return df
