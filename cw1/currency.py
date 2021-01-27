KNUTS_PER_SICKLE = 29  # Knuts
SICKLE_PER_GALLEON = 17  # Sickles

base_knuts = int(input("Enter the currency in knuts: "))

# Divide (and truncate) the knuts into sickles
sickles = base_knuts // KNUTS_PER_SICKLE
# Take off the remaining knuts that were not converted to sickles
knuts = base_knuts % KNUTS_PER_SICKLE
# Divide (and truncate) the sickles into galleons
galleons = sickles // SICKLE_PER_GALLEON
# Take off the remaining sickles that were not converted to galleons
sickles = sickles % SICKLE_PER_GALLEON

print(f"{galleons} galleons {sickles} sickles and {knuts} knuts")
