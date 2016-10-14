key = u'vFm0MBpv8f31byULUm1E415'.encode('utf-16le')

def decrypt(data):
    decrypted = ''
    for i in xrange(0, len(data)):
        decrypted += chr(ord(data[i]) ^ ord((key[i % 0x10])))
        
    return decrypted

def main():
    f = open('pZkapu', 'rb')
    data = f.read()
    f.close()
    f = open('p7kapu.dontrun', 'wb')
    f.write(decrypt(data))
    f.close()
    print 'Done'

if __name__ == '__main__':
    main()
