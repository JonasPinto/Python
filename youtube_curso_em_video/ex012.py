#crie um algoritimo que leia o preço de um produto e mostre seu novo preço com desconto de 5% de desconto

preco = float(input('Digite o preço do produto : R$'))
des = preco - (preco * 0.05)
print(f'O preço com desconto é de \033[34mR${des}\033[m')

