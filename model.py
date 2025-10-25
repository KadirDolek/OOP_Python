
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
    def add_product(self, product: Product, quantity: int = 1):
        """Ajoute un produit à la commande (quantité par défaut : 1)"""
        for _ in range(quantity):
            self.products.append(product)

    def remove_product(self, product: Product, quantity: int = 1):
        """Retire un produit de la commande (quantité par défaut : 1)"""
        for _ in range(quantity):
            if product in self.products:
                self.products.remove(product)
            else:
                raise ValueError(f"Produit {product.nom} non trouvé dans la commande")
    


    
# testons ca 



user = User("Alice", "alice@test.com", 30)
p1 = Product("T-shirt", 25.0)
p2 = Product("Socks", 5.0)
order = Order(user, [p1, p2, p2])  # +1 T-shirt et +2 Socks

print("Initial :", order.products)  # [Product(nom='T-shirt', prix=25.0), ...]

# Ajoutorder.add_product(p1)             
order.add_product(p1, quantity=2)  
print("Après ajout :", order.products)

# Retrait
order.remove_product(p2)          
order.remove_product(p1, quantity=2)  
print("Après retrait :", order.products)
print("Total :", order.total_price(), "€")

