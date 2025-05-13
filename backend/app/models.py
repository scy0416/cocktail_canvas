from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Float, SmallInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    kakao_id = Column(String(100), nullable=False)

    sessions = relationship('ChatSession', back_populates='user', cascade='all, delete-orphan')
    cocktails = relationship('Cocktail', back_populates='user', cascade='all, delete-orphan')
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class ChatSession(Base):
    __tablename__ = 'ChatSessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    title = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    user = relationship('User', back_populates='sessions')
    messages = relationship('ChatMessage', back_populates='session', cascade='all, delete-orphan')

class ChatMessage(Base):
    __tablename__ = 'ChatMessages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('ChatSessions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    session = relationship('ChatSession', back_populates='messages')

class Cocktail(Base):
    __tablename__ = 'Cocktail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    registered_date = Column(Date)
    alcohol = Column(Float, nullable=False)
    image_url = Column(String(100))
    user_review = Column(Text)

    user = relationship('User', back_populates='cocktails')
    tags = relationship('CocktailTag', back_populates='cocktail', cascade='all, delete-orphan')
    recipes = relationship('Recipe', back_populates='cocktail', cascade='all, delete-orphan')
    recipe_ingredients = relationship('RecipeIngredient', back_populates='cocktail', cascade='all, delete-orphan')
    reviews = relationship('Review', back_populates='cocktail', cascade='all, delete-orphan')

class CocktailTag(Base):
    __tablename__ = 'CocktailTag'
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    tag = Column(String(50), primary_key=True)

    cocktail = relationship('Cocktail', back_populates='tags')

class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    recipe = Column(Text, nullable=False)

    cocktail = relationship('Cocktail', back_populates='recipes')

class Ingredient(Base):
    __tablename__ = 'Ingredient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    tag = Column(String(50))

    recipe_ingredients = relationship('RecipeIngredient', back_populates='ingredient', cascade='all, delete-orphan')

class RecipeIngredient(Base):
    __tablename__ = 'RecipeIngredient'
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('Ingredient.id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True)
    amount = Column(String(50))

    cocktail = relationship('Cocktail', back_populates='recipe_ingredients')
    ingredient = relationship('Ingredient', back_populates='recipe_ingredients')

class Review(Base):
    __tablename__ = 'Review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    rating = Column(SmallInteger, nullable=False)
    comment = Column(Text)
    review_date = Column(DateTime, server_default=func.now(), nullable=False)

    user = relationship('User', back_populates='reviews')
    cocktail = relationship('Cocktail', back_populates='reviews')
