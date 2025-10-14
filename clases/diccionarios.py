persona = {"Nombre": "Alex", "Edad": 25, "Ciudad": "Guayaquil"}
print("Disccionario Inicial:", persona)

print("Edad:",persona.get("Edad"))

persona ["Profesion"] = "Ingeniero"
print("Persona con profesion:",persona)

print("Claves",persona.keys()) #claves
print("Valores",persona.values()) #Valores

persona["Ciudad"] = "Quito"
print("Ciudad modificada", persona)