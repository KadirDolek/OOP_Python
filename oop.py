import string

class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self._password = None #attribut privé

    def birthday(self):
        self.age += 1
        print(f"{self.username} a maintenant {self.age} ans")

    @property
    def password(self):
        """Getter pour le mot de passe."""
        return self._password
    
    @password.setter
    def password(self, new_password):
        """Setter pour le mot de passe avec validation"""
        # Vérification de la longueur
        if len(new_password) < 8:
            raise ValueError("Le mot de passe doit contenir au moins 8 caractères")
        
        # Vérification d'un caractère spécial
        if not any(c in string.punctuation for c in new_password):
            raise ValueError("Le mot de passe doit contenir au moins un caractère spécial")
        
        # Vérification d'une majuscule
        if not any(c.isupper() for c in new_password):
            raise ValueError("Le mot de passe doit contenir au moins une majuscule")
        
        # Vérification d'un chiffre
        if not any(c.isdigit() for c in new_password):
            raise ValueError("Le mot de passe doit contenir au moins un chiffre")
        
        # Si toutes les vérifications passent -----> self._password = new_password
        print(f"Mot de passe défini pour {self.username}")

    def __repr__(self):
        """Affichage lisible de l'objet User"""
        return f"User(user='{self.username}', email='{self.email}', age='{self.age}')"
    
class Admin(User):
    """Classe Admin qui hérite de User"""

    def __init__(self, username, email, age):
        """Initialisation d'un Admin."""
        super().__init__(username, email, age)
        self.banned_users = [] # Liste des utilisateurs bannis

    def ban_user(self, user):
        """Bannit un utilisateur."""
        if isinstance(user, User):
            self.banned_users.append(user.username)
            print(f"{user.username} a été banni par {self.username}")
        else:
            print("Erreur:le paramètre doit être une instance de User")
    def __repr__(self):
        """Affichage lisible de l'objet Admin."""
        return f"Admin(username='{self.username}', email='{self.email}', age={self.age})"
    

# Et maintenant on test tout ca, sans json, sans pytest, pas la peine : 

if __name__ == "__main__":
    #Création de user
    user1 = User("alice", "alice@email.com",25)
    user2 = User("bob", "bob@email.com",30)

print("---Utilisateurs crées ---")
print(user1)
print(user2)

#test de la méthode birthday()
print ("\n--- Test de birthday() ---")
user1.birthday()

#Test du setter de mot de passe
print("\n--- Test du setter de password ---")
try:
    user1.password = "123" #trop court
except ValueError as e:
    print(f"Erreur : {e}")

user1.password = "Securepass123!" #Valide , passe les 3 vérifs
print(f"Mot de passe: {user1.password}")

print("\n--- Création d'un Admin ---")
admin = Admin("charlie", "charlie@admin.com", 49)
print(admin)


# Test du ban_user()
print("\n--- Test de ban_user() ----")

admin.ban_user(user1)
admin.ban_user(user2)
print(f"Utilisateurs bannis: {admin.banned_users}")