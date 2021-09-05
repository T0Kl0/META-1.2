email = input("CUAL ES TU CORREO ELECTRONICO: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = "EL NOMBRE DE USUARIO ES '{}' Y EL NOMBRE DEL DOMINIO ES '{}'".format(user_name,domain_name)

# Display output message
print(output)