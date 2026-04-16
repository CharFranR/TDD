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

def test_personaje_muere_si_hp_llega_a_cero():
    heroe = Personaje()
    enemigo = Personaje()
    
    enemigo.atacar(heroe, dano=1500)
    
    assert heroe.hp == 0 
    assert heroe.esta_vivo == False

def test_curar_personaje():
    p = Personaje()
    p.atacar(p, 200) 
    
    p.heal(p, 100)
    assert p.hp == 900

def test_no_curar_mas_del_maximo():
    p = Personaje()
    p.hp = 900  
        
    p.heal(p, 200)
    assert p.hp == 1000

def test_los_muertos_no_se_curan():
    p = Personaje()
    p.hp = 0
    p.is_alive = False
    
    p.heal(p, 500)
    assert p.hp == 0
    assert p.is_alive is False