class CaesarCipher:
    def __init__(self):
        with open("words.txt") as words_file:
            self.words = [word.strip() for word in words_file.readlines()]
        self.delimeter = "\n"
        self.alphabets = list("abcdefghijklmnopqrstuvwxyz")

    def decrypt(self, filename):
        with open(filename) as enc_file:
            encrypted_lines = enc_file.readlines()
        
        encrypted_text = " ".join([line.strip() for line in encrypted_lines])
        encrypted_words = encrypted_text.split()
        max_match_count = 0
        best_key = 0
        
        print("Decrypting text. Please wait...\n")
        
        # Attempt all possible shifts (from 0 to 25)
        for key in range(26):
            match_count = 0
            
            for enc_word in encrypted_words:
                dec_word = self._decrypt_word(enc_word, key)
                if dec_word in self.words:
                    match_count += 1
            
            if match_count > max_match_count:
                max_match_count = match_count
                best_key = key
        
        print(f"Best key found: {best_key} with {max_match_count} matches.\n")
        
        # Decrypt the entire text using the best key
        decrypted_msg = ""
        for line in encrypted_lines:
            decrypted_msg += self._decrypt_line(line, best_key)
        
        print("Decrypted Message:\n")
        print(decrypted_msg)

    def _decrypt_word(self, word, key):
        dec_word = ""
        for enc_ch in word:
            if enc_ch.lower() in self.alphabets:
                k = (self.alphabets.index(enc_ch.lower()) - key) % 26
                dec_ch = self.alphabets[k]
                dec_word += dec_ch
            else:
                dec_word += enc_ch
        return dec_word

    def _decrypt_line(self, line, key):
        dec_line = ""
        for enc_ch in line:
            if enc_ch.lower() in self.alphabets:
                k = (self.alphabets.index(enc_ch.lower()) - key) % 26
                dec_ch = self.alphabets[k]
                if enc_ch.isupper():
                    dec_ch = dec_ch.upper()
                dec_line += dec_ch
            else:
                dec_line += enc_ch
        return dec_line
        
c = CaesarCipher()
c.decrypt("encoded.txt")
