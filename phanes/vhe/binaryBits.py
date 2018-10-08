from bitstring import Bits

def get_binary_bits(input_data):
    binary_data = Bits(int=abs(input_data), length=64)
    binary_list = []
    for i in range(64):
        binary_list.append(binary_data.bin[i])
    binary_list.reverse()
    for i in range(36):
        binary_list.append(0)
    return binary_list


"""if __name__ == "__main__":
    s1 = Bits(int=abs(50), length=64)
    list = []
    for i in range(64):
        list.append(s1.bin[i])
    list.reverse()
    for i in range(36):
        list.append(0)
    for i in range(100):
        print(list[i],end="",flush=True)"""


        

#0000000000100000100111010000000000000000000000000000000000000000
#0000000000100000100111010000000000000000000000000000000000000000        


#0000000000000000000000000000000000000000101110010000010000000000000000000000000000000000000000000000
#0000000000000000000000000000000000000000101110010000010000000000
#0000000000000000000000000000000000000000101110010000010000000000000000000000000000000000000000000000

# negative 
#0000000000000000000000000000000000000000101110010000010000000000000000000000000000000000000000000000
#0000000000000000000000000000000000000000110001101111101111111111000000000000000000000000000000000000

#0100110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 =50
#011100111111111111111111111111111111111111111111111111111111111100000000000000000000000000000000000
#0100110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000