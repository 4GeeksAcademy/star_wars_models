from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Float, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    nombre: Mapped[str] = mapped_column(String(30))
    apellido: Mapped[str] = mapped_column(String(30))
    fecha_subscripcion: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now, nullable=False)

class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    genero: Mapped[str] = mapped_column(String(20))
    altura: Mapped[float] = mapped_column(Float)
    color_ojos: Mapped[str] = mapped_column(String(50))
    color_cabello: Mapped[str] = mapped_column(String(50)) 

class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    diametro: Mapped[int] = mapped_column(Integer)
    clima: Mapped[str] = mapped_column(String(50))
    terreno: Mapped[str] = mapped_column(String(50))
    poblacion: Mapped[int] = mapped_column(BigInteger)

PersonajeFavorito = Table(
    "personajeFavorito",
    db.metadata,
    Column("usuario_id", ForeignKey("user.id")),
    Column("personaje_id", ForeignKey("personaje.id"))
)  

PlanetaFavorito = Table(
    "planetaFavorito",
    db.metadata,
    Column("usuario_id", ForeignKey("user.id")),
    Column("planeta_id", ForeignKey("planeta.id"))
)


def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
