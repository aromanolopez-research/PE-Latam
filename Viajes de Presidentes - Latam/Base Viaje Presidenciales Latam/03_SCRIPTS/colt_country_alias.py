# Alias de nombres de pais: nuestra base -> nomenclatura de COLT.
# Detectado 2026-08-15 durante la verificacion de links COLT (Argentina Turkey/Vatican,
# luego confirmado sistematicamente en Brasil/Chile/Paraguay/Uruguay).
# Usar SIEMPRE al cruzar Destination_Country (nuestro) contra CountryVisited (COLT).
COLT_COUNTRY_ALIAS = {
    "Turkey": "Turkiye",
    "Vatican City": "Holy See",
    "Cape Verde": "Cabo Verde",
    "East Timor": "Timor Leste",
    "Timor-Leste": "Timor Leste",
    "Republic of the Congo": "Congo-Brazzaville",
    "Democratic Republic of the Congo": "Congo-Kinshasa",
}
# Nota: "Puerto Rico" (aparece en Uruguay) NO tiene equivalente en el vocabulario de
# paises de COLT (no lo codifican como pais separado) -no es un alias, es una
# ausencia real de su esquema, tratar como colt_unico/verificacion propia sin
# esperar encontrar una fila de COLT equivalente-.
