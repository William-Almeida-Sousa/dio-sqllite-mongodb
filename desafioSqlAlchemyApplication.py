import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DECIMAL

Base = declarative_base()

class Client(Base):
    __tablename__ = "client_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(11))
    endereco = Column(String(50))

    conta = relationship(
        "Conta", back_populates="client"
    )

    def __repr__(self):
        return f"Client (id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(30))
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("client_account.id"))
    saldo = Column(DECIMAL)

    client = relationship("Client", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, " \
               f"id_cliente={self.id_cliente}, saldo={self.saldo})"


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

with Session(engine) as session:
    william = Client(
        name="William Almeida",
        cpf="14365476877",
        endereco="Rua do Caixa Prego, 16"
    )

    manu = Client(
        name="Manu Almeida",
        cpf="18465434593",
        endereco="Rua da Panela Torta, 35"
    )

# enviando para o BD (persistência de dados)

session.add_all([william, manu])

session.commit()

stmt_count = select(func.count("*")).select_from(Client)
print("\nTotal de instâncias em Client")
for result in session.scalars(stmt_count):
    print(result)

stmt_order = select(Client).order_by(Client.name.asc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

