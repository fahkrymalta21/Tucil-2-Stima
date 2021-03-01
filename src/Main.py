from collections import defaultdict 

# Membaca file teks sebagai file masukkan (input)
berkas = input("Masukkan berkas: ")
baca = open(berkas, "r") # Note: Sebelum dijalankan, Main.py dan file test case disatukan dulu dalam satu folder
arr_baca = baca.readlines()
arr_matkul = ["*" for i in range(len(arr_baca))]

# Menghilangkan char "." dan "\n" pada array arr_baca
for i in range(len(arr_baca)-1):
    arr_matkul[i] = arr_baca[i].replace(".\n", "")
arr_matkul[len(arr_baca)-1] = arr_baca[len(arr_baca)-1].replace(".", "") 

# Memisahkan setiap mata kuliah yang terdapat dalam satu baris (satu indeks list) dengan tanda koma
matriks_matkul = ["*" for i in range(len(arr_matkul))]
for i in range(len(arr_matkul)):
    matriks_matkul[i] = arr_matkul[i].split(", ")

# Kode program untuk menampilkan ke layar (print) topological sorting dari DAG
  
# Class untuk merepresentasikan graf
  
class Graf: 
    def __init__(self, simpul): 
        self.graf = defaultdict(list)  
        self.S = simpul  
  
    # fungsi untuk memasukkan sisi-sisi kedalam graf berdasarkan simpulnya 
    def addSisi(self, u, v): 
        self.graf[u].append(v) 
  
    # Fungsi rekursif Topological Sort 
    def topologicalSortUtil(self, v, dikunjungi, stack): 
  
        dikunjungi[v] = True
   
        for i in self.graf[v]: 
            if dikunjungi[i] == False: 
                self.topologicalSortUtil(i, dikunjungi, stack) 
  
        stack.append(v) 
  
    # Fungsi untuk melakukan Topological Sort 
    # topologicalSortUtil() 
    def topologicalSort(self): 

        dikunjungi = [False]*self.S 
        stack = [] 
  
        for i in range(self.S): 
            if dikunjungi[i] == False: 
                self.topologicalSortUtil(i, dikunjungi, stack) 
        
        return(stack[::-1])  
  

# Array matkul_unik untuk menyimpan mata kuliah dari Array matriks_matkul tetapi secara unik untuk masing-masing matkul
matkul_unik = []
for i in matriks_matkul:
    for j in i:
        if j not in matkul_unik:
            matkul_unik.append(j)

# Array nil_matkul untuk menyimpan integer sebagai nilai unik untuk masing-masing matkul
nil_matkul = [0 for i in range(len(matkul_unik))]
for i in range(len(matkul_unik)):
    nil_matkul[i] = i

# Matriks mat_nil_matkul sebagai matriks yang akan menyimpan matkul pada matriks matriks_matkul dengan nilai integer unik masing-masing
mat_nil_matkul = matriks_matkul
for i in range(len(matriks_matkul)):
    for j in range(len(matriks_matkul[i])):
        for k in range(len(matkul_unik)):
            if matkul_unik[k] == mat_nil_matkul[i][j] :
                mat_nil_matkul[i][j] = nil_matkul[k]

# Implementasi addSisi untuk menyimpan hubungan antara matkul dan prerequisite nya
graf_matkul = Graf(len(matkul_unik))
for i in range(len(mat_nil_matkul)):
    if len(mat_nil_matkul[i]) > 1:
        for j in range(1,len(mat_nil_matkul[i])):
            graf_matkul.addSisi(mat_nil_matkul[i][j], mat_nil_matkul[i][0])

# Array nil_hasil sebagai array yang menyimpan hasil topological sorting akan tetapi masih dalam bentuk integer
nil_hasil = []  
nil_hasil = graf_matkul.topologicalSort()

# Array hasil sebagai array yang menyimpan hasil topological searching dan sudah dalam bentuk susunan matkul
hasil = ["*" for i in range(len(nil_hasil))]
for i in range (len(nil_matkul)):
    for j in range (len(nil_hasil)):
        if nil_hasil[j] == nil_matkul[i]:
            hasil[j] = matkul_unik[i]

for i in range(len(hasil)):
    print("Semester ", i+1, "   : ", hasil[i])


