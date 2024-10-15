import matplotlib.pyplot as plt

# Formatar os inputs de Role e Tag para o padrão do .csv.
def formatarPalavra(palavra):
    palavra = palavra[0].upper()+palavra[1:].lower()
    return palavra

def campeoesWinrateEntre(champions):
    print("Campeões com Winrate entre um valor menor e um maior")
    menorValor = float(input("Insira o menor valor de Winrate: "))
    maiorValor = float(input("Insira o maior valor de Winrate: "))
    # Evitar que insiram o maior valor no menor e vice-versa.
    if menorValor > maiorValor:
        reserva = menorValor
        menorValor = maiorValor
        maiorValor = reserva
    champions_winrate_entre = champions[(champions["winrate"] >= menorValor) & (champions["winrate"] <= maiorValor)]
    champions_winrate_entre = champions_winrate_entre[["id", "key", "name", "title", "role", "tags"]]
    if champions_winrate_entre.empty:
        print("Não há campeões com Winrate entre esses valores.\n")
    else:
        print("Campeões inseridos no arquivo champions_winrate_entre.csv!\n")
        champions_winrate_entre.to_csv("champions_winrate_entre.csv", sep=";", index=False)

def campeoesPorRoleETags(champions):
    print("Campeões por Role e Tags")
    roleEscolhida = input("Insira a Role/Lane que você deseja: ")
    tagEscolhida = input("Insira a Tag/Tipo de Campeão que você deseja: ")
    roleEscolhida = formatarPalavra(roleEscolhida)
    tagEscolhida = formatarPalavra(tagEscolhida)
    champions_role_tag = champions[(champions["role"].str.contains(roleEscolhida) & champions["tags"].str.contains(tagEscolhida))]
    champions_role_tag = champions_role_tag[["id", "key", "name", "title", "role", "tags"]]
    if champions_role_tag.empty:
        print("Não há campeões com essa Role/Lane e Tag/Tipo de Campeão simultaneamente.\n")
    else:
        print("Campeões inseridos no arquivo champions_role_tag.csv!\n")
        champions_role_tag.to_csv("champions_role_tag.csv", sep=";", index=False)

def winrateRole(champions):
    winrate_role = champions.groupby("role")["winrate"].mean().reset_index()
    print("Winrate por Role, baseado no winrate dos campeões, foi inserido no arquivo winrate_role.csv.\n")
    winrate_role.to_csv("winrate_role.csv", index=False)
    plt.figure(figsize=(10, 6))
    plt.bar(winrate_role["role"], winrate_role["winrate"], color="skyblue")
    plt.title("Média de Winrate por Role")
    plt.xlabel("Role/Lane")
    plt.ylabel("Winrate (%)")
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis="y")
    plt.savefig("grafico_winrate_role.png")
    plt.show()

def popularityRole(champions):
    popularity_role = champions.groupby("role")["popularity"].mean().reset_index()
    print("Popularidade por rota, baseado na popularidade dos campeões, foi inserido no arquivo winrate_role.csv.\n")
    popularity_role.to_csv("popularity_role.csv", index=False)
    plt.figure(figsize=(10, 6))
    plt.bar(popularity_role["role"], popularity_role["popularity"], color="skyblue")
    plt.title("Média de Popularidade por Role")
    plt.xlabel("Role/Lane")
    plt.ylabel("Popularidade (%)")
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis="y")
    plt.savefig("grafico_popularity_role.png")
    plt.show()
    
def popularidadeCampeosPorAno(champions):
    champions["ano"] = champions["releasedate"].dt.year
    popularidade_campeoes_ano = champions.groupby("ano")["popularity"].mean().reset_index()
    print("Popularidade dos campeões de cada ano foi inserido no arquivo popularidade_campeoes_ano.csv.\n")
    popularidade_campeoes_ano.to_csv("popularidade_campeoes_ano.csv", index=False)
    plt.figure(figsize=(10, 6))
    plt.plot(popularidade_campeoes_ano["ano"], popularidade_campeoes_ano["popularity"], marker="o", color="skyblue")
    plt.title("Média da Popularidade dos Campeões por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Popularidade")
    plt.grid()
    plt.savefig("grafico_popularidade_campeoes_ano.png")
    plt.show()