def hamming(input_data):
    length = len(input_data)
    control_bit_cnt = 0
    while (2 ** control_bit_cnt) < (length + control_bit_cnt + 1):
        control_bit_cnt += 1
    
    result = ["0"] * (length + control_bit_cnt) 
    
    index = 0
    for i in range(length + control_bit_cnt):
        if (i + 1) & (i) == 0:
            continue
        result[i] = input_data[index]
        index += 1
    
    for i in range(control_bit_cnt):
        contril_bit_ind = 2 ** i - 1
        check_bits = []
        for j in range(length + control_bit_cnt):
            if (j + 1) & (contril_bit_ind + 1) == (contril_bit_ind + 1):
                check_bits.append(int(result[j]))
        result[contril_bit_ind] = str(sum(check_bits) % 2)
    
    return result


print("After Hamming encoding:", "".join(hamming("00000011100000100010111111101111011010010100111101101000111101011001001101010001100")))
