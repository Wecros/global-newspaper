"""
Database Models
SQLAlchemy models for PostgreSQL
"""

from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Article(Base):
    """Individual article from scraping"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    content = Column(Text)
    url = Column(String(1000), unique=True)
    source = Column(String(255))
    images = Column(JSON)  # Store as JSON array
    metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class SuperArticle(Base):
    """Generated super-article from multiple sources"""
    __tablename__ = "super_articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    tldr = Column(Text)
    content = Column(Text)
    source_comparison = Column(JSON)  # Compare different sources
    language = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)


class User(Base):
    """User preferences and settings"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    language_prefs = Column(JSON)  # Language preferences
    topic_interests = Column(JSON)  # Topic interests
    created_at = Column(DateTime, default=datetime.utcnow)
