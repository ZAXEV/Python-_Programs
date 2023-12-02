#STORAGE SYSTEM ALEX
#START:23:10
#END: 00:35

class StorageSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def view_inventory(self):
        print("Isi inventory anda adalah:")
        for item in self.inventory:
            print(item)

def main():
    storage = StorageSystem()

    while True:
        print("1. Tambahkan barang")
        print("2. Lihat inventory")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == "1":
            item = input("Masukkan nama barang yang ingin ditambahkan: ")
            storage.add_item(item)
            print(f"{item} telah ditambahkan ke dalam inventory.")
        elif choice == "2":
            storage.view_inventory()
        elif choice == "3":
            print("Terima kasih! Program berakhir.")
            break
        else:
            print("Masukkan pilihan yang valid (1/2/3).")

if __name__ == "__main__":
    main()
