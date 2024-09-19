products=[]
# read the file put the products in a list without the new line character
with open("queries/M11215093_queries.txt", "r",encoding="utf-8-sig") as f:
    products = f.read().splitlines()

CHUNK_SIZE = 50
index=1
for i in range(0, len(products), CHUNK_SIZE):
    with open(f"queries/{index}.txt", "w",encoding="utf-8-sig") as f:
        f.write("\n".join(products[i:i+CHUNK_SIZE]))
        index+=1
        f.close()