import pandas as pd

tabela_vendas = pd.read_excel("/Users\\12723115582\Desktop\An.Da\Vendas.xlsx")

# print (tabela_vendas.head())

data_maior = tabela_vendas["Valor Unitário"].max()
# print(data_maior)
faturamento = tabela_vendas["Valor Final"].sum()
# print(faturamento)

tipo_produto = tabela_vendas.loc[tabela_vendas["Produto"] == "Bermuda Xadrez"]
valor_tipo_produto = tipo_produto["Valor Final"].sum()
# print  (tipo_produto and valor_tipo_produto)

faturamento_por_loja = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
# print(faturamento_por_loja.head())

faturamento_por_produto = tabela_vendas[["ID Loja", "Produto", "Valor Final"]].groupby(["Produto", "ID Loja"]).sum()
faturamento_por_produto_ordenado = faturamento_por_produto.sort_values(by=["Valor Final"], ascending=False)
# print(faturamento_por_produto_ordenado)

# tabela_formatada_valor_final = faturamento_por_produto_ordenado['Valor Final'].map('R$ {:0,.0f}'.format)
# print(tabela_formatada_valor_final)

print(faturamento_por_produto_ordenado['Valor Final'].map('R$ {:0,.0f}'.format))

maximum = tabela_vendas.max()
# print (max)

average_final_value = tabela_vendas["Valor Final"].min()
# print(average_final_value)
