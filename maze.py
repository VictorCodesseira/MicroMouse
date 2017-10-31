def main():
    maze = [[9,3,9,5,5,1,7,9,3,9,3,9,5,5,5,3], [10,12,6,9,3,10,9,6,12,6,10,10,9,5,5,6], [10,9,5,6,12,6,12,3,9,2,10,10,10,13,1,3], [10,10,9,5,5,5,5,6,14,8,4,6,10,11,10,10],
            [10,10,8,3,9,3,9,3,9,2,9,3,8,2,10,10], [10,8,6,12,6,12,6,8,6,12,6,12,6,12,6,10], [10,10,9,3,9,5,3,12,7,11,11,11,11,9,5,2], [10,10,10,10,10,9,6,9,1,0,0,0,0,0,7,10],
            [10,10,10,10,10,8,3,12,6,14,14,14,14,12,1,6], [10,10,10,10,10,14,12,5,5,5,5,5,5,5,4,3], [10,10,10,12,6,9,3,9,3,9,3,9,3,9,3,10], [10,10,12,5,1,6,12,6,12,6,12,6,12,6,12,6],
            [10,8,5,1,6,11,9,5,5,5,5,5,5,3,13,3], [10,12,3,12,5,4,6,9,5,1,5,1,5,6,9,2], [8,3,12,5,5,5,5,6,11,12,5,4,5,5,6,10], [14,12,5,5,5,5,5,5,4,5,5,5,5,5,5,6]]


    draw = [['+',' ','+', ' ',' ',' ', '+',' ','+'], ['+','_','+', ' ',' ',' ', '+',' ','+'], 
            ['+',' ','+', ' ',' ','|', '+',' ','+'], ['+','_','+', ' ',' ','|', '+',' ','+'], 
            ['+',' ','+', ' ',' ',' ', '+','_','+'], ['+','_','+', ' ',' ',' ', '+','_','+'], 
            ['+',' ','+', ' ',' ','|', '+','_','+'], ['+','_','+', ' ',' ','|', '+','_','+'], 
            ['+',' ','+', '|',' ',' ', '+',' ','+'], ['+','_','+', '|',' ',' ', '+',' ','+'], 
            ['+',' ','+', '|',' ','|', '+',' ','+'], ['+','_','+', '|',' ','|', '+',' ','+'], 
            ['+',' ','+', '|',' ',' ', '+','_','+'], ['+','_','+', '|',' ',' ', '+','_','+'], 
            ['+',' ','+', '|',' ','|', '+','_','+'], ['x','x','x', 'x','x','x', 'x','x','x']]


    '''     
            Sendo a existência de uma parede = 1 e a não existência = 0,
            "Número" do bloco = 1*(cima) + 2*(direita) + 4*(baixo) + 8*(esquerda)

            0 = + . +    1 = + _ +    2 = + . +   3 = + _ +
                . . .        . . .        . . |       . . |
                + . +        + . +        + . +       + . +

            4 = + . +    5 = + _ +    6 = + . +    7 = + _ +
                . . .        . . .        . . |        . . |
                + _ +        + _ +        + _ +        + _ +

            8 = + . +    9 = + _ +   10 = + . +   11 = + _ +
                | . .        | . .        | . |        | . |
                + . +        + . +        + . +        + . +

            12= + . +   13 = + _ +   14 = + . +   15 = + _ +
                | . .        | . .        | . |        | . |
                + _ +        + _ +        + _ +        + _ +
    '''

    print()

    for line in range(16): # Percorre todas as linhas
        line_part = 0
        while line_part < 3: # Cada linha é dividida em 3 partes individuais
            for row in range(16): # Percorre todas as colunas
                row_part = 0
                while row_part < 3: #Cada coluna é dividida em 3 partes
                    if((line == 0 and line_part == 0) or (row_part == 0 and row == 0) or (row == 15 and row_part == 2) or (line == 15 and line_part == 2)): #Trata dos casos de borda

                        if(row_part == 0 and line == 0 and line_part == 0):
                            row_part = 1
                        elif(row_part == 2 and line == 0 and line_part == 0 and row == 15):
                            print("# ", end = '')

                        if(row_part == 0 and line == 15 and line_part == 2):
                            row_part = 1
                        elif(row_part == 2 and line == 15 and line_part == 2 and row == 15):
                            print("# ", end = '')
                    
                        print("# ", end = '')

                    else:
                        if(row_part == 0): # Se chegou aqui, não está na borda, então ignoramos a primeira parte da linha e coluna, para evitar repetições
                            row_part = 1
                        if(line_part == 0):
                            line_part = 1
                        print(draw[maze[line][row]][row_part + (line_part*3)] + " ", end = '')
                    row_part += 1
            line_part += 1         
                
            print()
        
    return 0

main()
