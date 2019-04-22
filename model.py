from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.sqlite', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Plugin(Base):
    __tablename__ = 'plugin'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)


class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    short = Column(String, nullable=False)


class Plugin_language(Base):
    __tablename__ = 'plugin_language'
    id = Column(Integer, primary_key=True)
    plugin_id = Column(Integer, ForeignKey('plugin.id'))
    language_id = Column(Integer, ForeignKey('language.id'))
    progression = Column(Float)


class Translation(Base):
    __tablename__ = 'translation'
    id = Column(Integer, primary_key=True)
    plugin_id = Column(Integer, ForeignKey('plugin.id'))
    language_id = Column(Integer, ForeignKey('language.id'))
    key = Column(String, nullable=False)
    value = Column(String)
    status = Column(String, nullable=False)


Base.metadata.create_all(engine)
