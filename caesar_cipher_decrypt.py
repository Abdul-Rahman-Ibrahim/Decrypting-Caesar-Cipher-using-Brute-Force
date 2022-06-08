class CaeserCipher:
    def __init__(self):
        words_file = open("words.txt")
        self.words = words_file.readlines()
        self.delimeter = "\n"
        self.alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        words_file.close()
    def decrypt(self, filename):
        enc_file = open(filename)
        f_line = enc_file.readline().strip().split()
        counter = 0
        key = 0
        print("Decrypting text. Please wait...\n")
        for i in range(26):
            tmp_counter = 0
            for enc_word in f_line:
                if len(enc_word) > 1:
                    dec_word = ""
                    for enc_ch in enc_word:
                        if enc_ch in self.alphabets:
                            k = (self.alphabets.index(enc_ch.lower()) - i)%26
                            dec_ch = self.alphabets[k]
                            dec_word += dec_ch
                        else:
                            dec_word += enc_ch
                    if (dec_word+self.delimeter) in self.words:
                        tmp_counter += 1
            if tmp_counter > counter:
                counter = tmp_counter
                key = i
        enc_file.close()
        enc_file = open(filename)
        decrypted_msg = ""
        for line in enc_file:
            for enc_ch in line:
                if enc_ch.lower() in self.alphabets:
                    i = (self.alphabets.index(enc_ch.lower()) - key)%26
                    dec_ch = self.alphabets[i]
                    if enc_ch.isupper():
                        dec_ch = dec_ch.upper()
                    decrypted_msg += dec_ch
                else:
                    decrypted_msg += enc_ch
        print(decrypted_msg)
        enc_file.close()
c = CaeserCipher()
c.decrypt("enc.txt")
