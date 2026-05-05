# ================== CLASSE BASE ==================
class Animal:
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, x, y):
        self._nome = nome
        self._cor = cor
        self._sexo = sexo
        self._velocidade = velocidade
        self._peso = peso
        self._estamina = estamina
        self._x = x
        self._y = y
        self._direcao_x = 1
        self._direcao_y = 1
        self._vivo = True

    # ===== GETTERS E SETTERS =====
    def get_nome(self): return self._nome
    def set_nome(self, nome): self._nome = nome

    def get_cor(self): return self._cor
    def set_cor(self, cor): self._cor = cor

    def get_sexo(self): return self._sexo
    def set_sexo(self, sexo): self._sexo = sexo

    def get_velocidade(self): return self._velocidade
    def set_velocidade(self, v):
        if v > 0:
            self._velocidade = v

    def get_peso(self): return self._peso
    def set_peso(self, p):
        if p > 0:
            self._peso = p

    def get_estamina(self): return self._estamina
    def set_estamina(self, e):
        if e >= 0:
            self._estamina = e

    def get_posicao(self): return (self._x, self._y)
    def set_posicao(self, x, y):
        self._x = x
        self._y = y

    def get_vivo(self): return self._vivo
    def set_vivo(self, v): self._vivo = v

    # ===== MÉTODOS =====
    def andar(self, rodada, limite):
        if not self._vivo or self._estamina <= 0:
            return

        if rodada % 2 == 0:
            # eixo X
            for _ in range(self._velocidade):
                self._x += self._direcao_x
                if self._x >= limite or self._x <= 0:
                    self._direcao_x *= -1
                    self._x += self._direcao_x
        else:
            # eixo Y
            for _ in range(self._velocidade):
                self._y += self._direcao_y
                if self._y >= limite or self._y <= 0:
                    self._direcao_y *= -1
                    self._y += self._direcao_y

        self._estamina -= 1

    def imprimir_caracteristicas(self):
        if self._vivo:
            print(f"{self._nome} | Pos: ({self._x},{self._y}) | Peso: {self._peso} | Estamina: {self._estamina}")
        else:
            print(f"{self._nome} está morto.")

    # ===== COLISÃO =====
    def checar_colisao(self, outro):
        if not self._vivo or not outro._vivo:
            return

        if self._x == outro._x and self._y == outro._y:
            print(f"\n💥 {self._nome} encontrou {outro._nome}")

            # Leão mata todos
            if isinstance(self, Leao) and not isinstance(outro, Leao):
                self.rugir()
                outro._vivo = False
                self._peso += 1

            elif isinstance(outro, Leao) and not isinstance(self, Leao):
                outro.rugir()
                self._vivo = False
                outro._peso += 1

            # Leão vs Leão
            elif isinstance(self, Leao) and isinstance(outro, Leao):
                if self.idade > outro.idade:
                    outro._vivo = False
                    self._peso += 1
                else:
                    self._vivo = False
                    outro._peso += 1

            # Cachorro mata gato
            elif isinstance(self, Cachorro) and isinstance(outro, Gato):
                self.latir()
                outro._vivo = False
                self._peso += 1

            elif isinstance(outro, Cachorro) and isinstance(self, Gato):
                outro.latir()
                self._vivo = False
                outro._peso += 1


# ================== CLASSES FILHAS ==================

class Leao(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, x, y, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, x, y)
        self.idade = idade

    def rugir(self):
        print(f"{self._nome}: ROAAAR!")


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, x, y, raca, idade):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, x, y)
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self._nome}: AU AU!")


class Gato(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, x, y)
        self.raca = raca

    def miar(self):
        print(f"{self._nome}: MIAU!")


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, velocidade, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, velocidade, peso, estamina, x, y)
        self.raca = raca

    def mugir(self):
        print(f"{self._nome}: MUUU!")


# ================== ANIMAIS EXTRAS ==================

class Tigre(Animal):
    def atacar(self):
        print(f"{self._nome}: ataque feroz!")


class Coelho(Animal):
    def fugir(self):
        print(f"{self._nome}: fugindo!")


# ================== PROGRAMA PRINCIPAL ==================

def main():
    limite = 10
    rodada = 1

    animais = [
        Leao("Leão", "amarelo", "M", 2, 150, 10, 0, 0, 10),
        Cachorro("Dog", "marrom", "M", 2, 20, 10, 5, 5, "vira-lata", 5),
        Gato("Gato", "preto", "F", 1, 5, 10, 3, 3, "siamês"),
        Vaca("Vaca", "branco", "F", 1, 200, 10, 7, 7, "holandesa"),
        Tigre("Tigre", "laranja", "M", 2, 180, 10, 2, 2),
        Coelho("Coelho", "branco", "F", 1, 3, 10, 8, 8)
    ]

    while True:
        print("\n1 - Andar")
        print("2 - Mostrar animais")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            for a in animais:
                a.andar(rodada, limite)

            # checar colisões
            for i in range(len(animais)):
                for j in range(i + 1, len(animais)):
                    animais[i].checar_colisao(animais[j])

            for a in animais:
                a.imprimir_caracteristicas()

            rodada += 1

        elif op == "2":
            for a in animais:
                a.imprimir_caracteristicas()

        elif op == "0":
            break

        else:
            print("Opção inválida!")


main()