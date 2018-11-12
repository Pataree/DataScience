
import sqlalchemy
from sqlalchemy import create_engine, MetaData, DATE, insert, Float
from sqlalchemy import Table, Column, String, Integer, SMALLINT, BIGINT


def connect(dbtype, host='localhost', port=5432):

    uname = ''
    pwd = ''
    dbname = ''
    host = ''

    if dbtype == 'shares':
        # credential to connect to the aws rds
        uname = 'pataree'
        pwd = 'dbshares'
        dbname = 'dbshares'
        host = 'dbshares.cnee4hwuumob.ap-southeast-2.rds.amazonaws.com'
    elif dbtype == 'twitter':
        uname = 'pataree'
        pwd = 'dbtwitter'
        dbname = 'dbtwitter'
        host = 'dbtwitter.cnee4hwuumob.ap-southeast-2.rds.amazonaws.com'
    else:
        print('No database type has been provided - do not connect')
        return(None, None)

    
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(uname, pwd, host, port, dbname)

    # The return value of create_engine() is our connection object
    con = create_engine(url, client_encoding='utf8', pool_size=5, max_overflow=10)

    # Bind the connection to MetaData()
    meta = MetaData(bind=con) #, reflect=True)

    return (con, meta)

def get_share_table(table_name, metadata):
    # define a table with all its field
    shares_table = Table(table_name, metadata,
    Column('tradedate', DATE(), nullable=False),
    Column('ticker', String(50), nullable=False),
    Column('open', Float(), nullable=False),
    Column('high', Float(), nullable=False),
    Column('low', Float(), nullable=False),
    Column('close', Float(), nullable=False),
    Column('adjclose', Float(), nullable=False),
    Column('volume', Integer(), nullable=False),
    Column('dividend', Float(), nullable=False),
    Column('coef', Float(), nullable=False)
    )
    return shares_table



def get_twitter_table(table_name, metadata):
    twitter_table = Table(table_name, metadata,
    Column('t_id', BIGINT(), primary_key=True),
    Column('t_tweets', String(), nullable=False),
    Column('t_id', BIGINT(), primary_key=True),
    Column('t_tweets', String(), nullable=False),
    Column('t_len', SMALLINT(), nullable=False),
    Column('t_date', DATE(), nullable=False),
    Column('t_source', String(100), nullable=False),
    Column('t_likes', SMALLINT(), nullable=False),
    Column('t_retweet', SMALLINT(), nullable=False),
    Column('t_sentiment', SMALLINT(), nullable=False)
    )
    return twitter_table

