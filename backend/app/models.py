from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Date, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    kakao_id = Column(String(100), nullable=False)

    chat_sessions = relationship(
        "ChatSession", back_populates="user", cascade="all, delete-orphan"
    )
    cocktails = relationship(
        "Cocktail", back_populates="user", cascade="all, delete-orphan"
    )
    reviews = relationship(
        "Review", back_populates="user", cascade="all, delete-orphan"
    )

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class ChatSession(Base):
    __tablename__ = 'ChatSessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    title = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="chat_sessions")
    messages = relationship("ChatMessage", back_populates="session", cascade="all, delete-orphan")

class ChatMessage(Base):
    __tablename__ = 'ChatMessages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('ChatSessions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("ChatSession", back_populates="messages")

class Cocktail(Base):
    __tablename__ = 'Cocktail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    registered_date = Column(Date)

    user = relationship("User", back_populates="cocktails")
    tags = relationship("CocktailTag", back_populates="cocktail", cascade="all, delete-orphan")
    recipe = relationship("Recipe", back_populates="cocktail", uselist=False, cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="cocktail", cascade="all, delete-orphan")

class CocktailTag(Base):
    __tablename__ = 'CocktailTag'
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    tag = Column(String(50), primary_key=True)

    cocktail = relationship("Cocktail", back_populates="tags")

class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), unique=True, nullable=False)

    cocktail = relationship("Cocktail", back_populates="recipe")
    ingredients = relationship(
        "RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan"
    )

class Ingredient(Base):
    __tablename__ = 'Ingredient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    tag = Column(String(50))

    recipe_associations = relationship(
        "RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan"
    )

class RecipeIngredient(Base):
    __tablename__ = 'RecipeIngredient'
    recipe_id = Column(Integer, ForeignKey('Recipe.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('Ingredient.id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True)
    amount = Column(String(50))

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_associations")

class Review(Base):
    __tablename__ = 'Review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cocktail_id = Column(Integer, ForeignKey('Cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    review_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    cocktail = relationship("Cocktail", back_populates="reviews")
