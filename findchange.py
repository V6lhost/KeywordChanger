import argparse, sys
from changer import change

parser = argparse.ArgumentParser(usage="findchange.py -if kaynak dosya -f aranacak kelime -c yerleştirilecek kelime - seçenekler")

parser.add_argument("-sfile",help="Düzenlenecek metinin bulunduğu dosya", required=True)
parser.add_argument("-f", help="Aranacak kelime", required=True)
parser.add_argument("-c", help="Yerleştirilecek kelime", required=True)
parser.add_argument("-k", help="Kelime olarak ara", action="store_true")
parser.add_argument("-b", help="Sadece baştan ayrı olarak ara", action="store_true")
parser.add_argument("-s", help="Sadece sondan ayrı olarak ara", action="store_true")
parser.add_argument("-be", help="Baştan hariç tutulacak karakterler. Örnek: (-be :;=')")
parser.add_argument("-se", help="Sondan hariç tutulacak karakterler. Örnek: (-se :;=')")

args = parser.parse_args()

if args.s or args.b and args.k:
    print("b ve s parametreleri k parametresi ile kullanılamaz!")
    sys.exit(1)

changed = 0

with open(args.sfile, "r") as src:
    srcText = src.read()

if args.k:
    fword = " " + args.f + " "
    changed_text = change(srcText, fword, args.c)
    changed = 1

if args.b:
    fword = " " + args.f
    if changed == 1:
        changed_text = change(changed_text, fword, args.c)
    else:
        changed_text = change(srcText, fword, args.c)
        changed = 1

if args.s:
    fword = args.f + " "
    if changed == 1:
        changed_text = change(changed_text, fword, args.c)
    else:
        changed_text = change(srcText, fword, args.c)
        changed = 1

if args.be:
    for arg in args.be:
        fword = arg + args.f
        if args.s:
            fword = fword + " "
        
        if changed == 1:
            changed_text = change(changed_text, fword, args.c)
        else:
            changed_text = change(srcText, fword, args.c)
            changed = 1

if args.se:
    for arg in args.se:
        fword = args.f + arg
        if args.b:
            fword = " " + fword
        
        if changed == 1:
            changed_text = change(changed_text, fword, args.c)
        else:
            changed_text = change(srcText, fword, args.c)
            changed = 1
if changed != 1:
    changed_text = change(srcText, args.f, args.c)
print(changed_text, "\nKaydetmek istiyor musunuz?(e/h)")
secim = input()
if secim.upper() == "E":
    dosya = input("Kaydetmek istediğiniz dosya adı:(Aynı dosyaya kaydetmek için boş bırakın.)")
    if dosya == "":
        with open(args.sfile, "w") as file:
            file.write(changed_text)
    else:
        with open(dosya, "w") as file:
            file.write(changed_text)