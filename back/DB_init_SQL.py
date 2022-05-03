from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


# ONE SHELL MAKE DB BEFORE INITign IT  ! 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123123@localhost/STORE'

db=SQLAlchemy(app)


#entities 

#table'dan sonraki siralar: table'in adi, columnlar, column adi degeri ve aldigi deger
#customer_product = db.Table('customer_product',
  #db.Column('Cid', db.Integer, db.ForeignKey('Customers.cid')),
  #db.Column('email', db.String(100), db.ForeignKey('Customers.email')),
  #db.Column('name', db.String(100), db.ForeignKey('Customers.name')),
  #db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid'))
#)

under = db.Table('under',
  db.Column('Pcid', db.Integer, db.ForeignKey('Product_Category.Pcid')),
  db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid'))
  #db.Column('email', db.String(100), db.ForeignKey('Customers.email')),
  #db.Column('name', db.String(100), db.ForeignKey('Customers.name')),
  #db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid'))
)

wishes = db.Table('wishes',
  db.Column('email', db.String(100), db.ForeignKey('Customers.email')),
  db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid')),
  db.Column('date', db.DateTime(timezone=True), server_default=func.now())
  #db.Column('email', db.String(100), db.ForeignKey('Customers.email')),
  #db.Column('name', db.String(100), db.ForeignKey('Customers.name')),
  #db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid'))
)

shopping_cart = db.Table('shopping_cart',
  db.Column('email', db.String(100), db.ForeignKey('Customers.email')),
  db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid')),
  db.Column('date', db.DateTime(timezone=True), server_default=func.now()),
  db.Column('quantity', db.Integer)

)


change_price = db.Table('change_price',
  db.Column('Sid', db.Integer, db.ForeignKey('Sales_Manager.Sid')),
  db.Column('Pid', db.Integer, db.ForeignKey('Products.Pid'))

)


class Customers(db.Model):
  __tablename__='Customers'
  #Cid=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100))
  pass_hash=db.Column(db.String(512))
  email=db.Column(db.String(100), primary_key=True)
  homeadress=db.Column(db.String(100))
  wishes = db.relationship('Products', secondary = wishes)
  shopping_cart_= db.relationship('Products', secondary = shopping_cart)
  #bought_products = db.relationship('Products', secondary = customer_product, backref = 'owned')

  def __init__(self,name,pass_hash,email,homeadress):
    self.name=name
    self.pass_hash=pass_hash
    self.email=email
    self.homeadress=homeadress

class Products(db.Model):
  __tablename__='Products'
  Pid=db.Column(db.Integer,primary_key=True, autoincrement=True )
  name=db.Column(db.String(100))
  model=db.Column(db.String(50))
  description=db.Column(db.String(1000))
  edition_number=db.Column(db.Integer  )
  quantity =db.Column(db.Integer)
  amount_sold=db.Column(db.Integer)
  price =db.Column(db.Integer )
  raiting = db.Column(db.Integer) 
  warranty=db.Column(db.String(1000))
  distributor_Information =db.Column(db.String(1000))
  author=db.Column(db.String(1000))
  sale=db.Column(db.REAL )
  picture_url0=db.Column(db.String(1000))
  picture_url1=db.Column(db.String(1000))
  picture_url2=db.Column(db.String(1000))
  date =  db.Column(db.String(1000))




  def __init__(self,name,model,description,edition_number
              ,quantity, amount_sold, price, raiting, warranty, distributor_Information, author, sale,
              picture_url0,picture_url1,picture_url2):
    self.name=name
    self.model=model
    self.description=description
    self.edition_number=edition_number
    self.quantity=quantity
    self.amount_sold=amount_sold
    self.price=price
    self.raiting=raiting
    self.warranty=warranty
    self.distributor_Information=distributor_Information
    self.author=author
    self.sale=sale
    self.picture_url0=picture_url0
    self.picture_url1=picture_url1
    self.picture_url2=picture_url2
    self.sale=sale
    self.date = str(datetime.now()) 

    

class Product_Category(db.Model):
  __tablename__='Product_Category'
  Pcid=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100))
  under_ = db.relationship('Products', secondary = under, backref = 'pcid')

  def __init__(self,name):
    self.name=name


class Product_Manager(db.Model):
  __tablename__='Product_Manager'
  Pmid=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100))
  pass_hash=db.Column(db.String(512))

  def __init__(self,name, pass_hash):
    self.name=name
    self.pass_hash=pass_hash

class Sales_Manager(db.Model):
  __tablename__='Sales_Manager'
  Sid=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100))
  pass_hash=db.Column(db.String(512))
  change_price_= db.relationship('Products', secondary = change_price)

  def __init__(self,name, pass_hash):
    self.name=name
    self.pass_hash=pass_hash

class Purchased(db.Model):
  __tablename__='Purchased'
  purcid=db.Column(db.Integer,primary_key=True)
  price=db.Column(db.Integer)
  sale=db.Column(db.REAL)
  quantity=db.Column(db.Integer)
  shipment=db.Column(db.String(100))

  def __init__(self,price, sale, quantity, shipment):
    self.price = price
    self.sale = sale
    self.quantity = quantity
    self.shipment = shipment
    
class Comment(db.Model):
  __tablename__='Comment'
  cid=db.Column(db.Integer,primary_key=True)
  text=db.Column(db.String(250))
  

  def __init__(self,text):
    self.text=text
    


















if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  db.create_all()
  


