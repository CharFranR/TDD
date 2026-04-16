from rpg import Personaje

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange (Preparar)
    heroe = Personaje()
    
    # Assert (Verificar)
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True

def test_personaje_recibe_dano():
    heroe = Personaje()
    enemigo = Personaje()
    
    # Act (Actuar)
    enemigo.atacar(heroe, dano=200)
    
    # Assert
    assert heroe.hp == 800