import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória com letras, números e símbolos"""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def menu():
    print("\n=== Gerador de Senhas ===")
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        senha = gerar_senha(tamanho)
        print(f"\n🔒 Sua senha gerada: {senha}\n")
    except ValueError:
        print("❌ ERRO: Digite um número válido!")

if __name__ == "__main__":
    while True:
        menu()
        continuar = input("Gerar outra senha? (s/n): ").strip().lower()
        if continuar != 's':
            print("🚪 Saindo...")
            break