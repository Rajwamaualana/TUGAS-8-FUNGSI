def fibonachi (n):
    if n<=0: 
        return print ("tidak ada nilai fibonachi")
    elif n==1 or n==2:
        return 1
    else:
        return fibonachi (n-1) + fibonachi (n-2)
a = int (input("masukkan nilai fibonachi :"))
hasil_fibonachi = fibonachi(a)
print (hasil_fibonachi)
