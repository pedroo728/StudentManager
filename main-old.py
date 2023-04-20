from src.domain.entities.tipo_produto import TipoProduto
from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig
from src.infra.adapters.orm.orm_define import start_mappers
from dotenv import load_dotenv

load_dotenv()
start_mappers()

db_config = DbConfig()

db = DbHandler(db_config)
db.open()
session = db.get_session()

tipo_produto = TipoProduto(2, 'Refrigerante em Latax')
try:
    tipo_produto.validate()
    
    if (session.query(TipoProduto).filter_by(id = tipo_produto.id).first()):
        raise Exception('Ja existe esse tipo de produto')

    if (session.query(TipoProduto).filter_by(descricao = tipo_produto.descricao).first()):
        raise Exception('Ja existe tipo de produto com esse nome')
    
    session.add(tipo_produto)
    session.commit()
    print('Tipo de Produto incluido com sucesso')
except Exception as error:
    print(str(error))

#tipo_produto = session.query(TipoProduto).filter_by(id=1).first()
#print(tipo_produto)

#tipo_produto = session.query(TipoProduto).filter_by(id=1).first()
#tipo_produto.descricao = 'Outra descricao'
#session.commit()

#tipos_produtos = session.query(TipoProduto).all()
#for tipo_produto in tipos_produtos:
#    print(tipo_produto)


#session.query(TipoProduto).filter_by(id = 2).delete()
#session.commit()


#session.query(TipoProduto).delete()
#session.commit()