markalar={"Audi":10,"Mercedes":20,"Nissan":30,"Mazda":45}

# title="Marka","Adet"
print("            ")
print("{:^10}|{:^10}".format("Marka","Adet"))
print("-"*25)

for marka,adet in markalar.items():
    a="|{:10}|{:^+10.1f}|".format(marka,adet)
    print(a)
    print("-"*25)

    
