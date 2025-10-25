
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

class Product:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __repr__(self):
        """Affichage lisible de l'objet User"""
        return f"Product(nom='{self.nom}', prix='{self.prix}')"
    
class Order:
    def __init__(self, user:User, products: list):
        self.user = user
        self.products = products  # Liste simple (ex: [p1, p2, p2, p3] pour les quantités)

    def total_price(self):
        """Retourne la somme des prix de tous les produits (avec répétition pour quantités)"""
        return sum(product.prix for product in self.products)
    

user = User("Bob", "bob@test.com", 25)
p1 = Product("Livre", 10.50)
p2 = Product("Stylo", 2.30)
order = Order(user, [p1, p2, p1])  # Stylo acheté 2x

print(order.user.username)  # "Bob"
print(order.products)       # [Product(nom='Livre', prix=10.5), Product(nom='Stylo', prix=2.3), ...]
print(f"Total : {order.total_price()} €")  # "Total : 15.1 €"

