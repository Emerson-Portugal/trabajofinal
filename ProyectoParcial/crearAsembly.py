variable_ar = []
pack = []


def inicioD():  # inicio del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write(".data\n")
    file.close()


def inicioT():  # inicio del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write(".text\n")
    file.close()


def crearMain():  # main del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\nmain:\n")
    file.close()


def fin():  # fin del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\n\njr $ra")
    file.close()


def inicializarVar(variable):
    inicioD()
    valor_res = variable[::-1]
    for i in range(len(valor_res)):
        file = open("ProyectoParcial/variables.txt", "a")
        file.write("var_" + str(valor_res[i])+":    "".word      ""0:1" + "\n")
        file.close()
    inicioT()
    crearMain()

# print(signo)
# print(valor)
# print(variable.lexeme)


def convertir(variable, signo, valor):
    file = open("ProyectoParcial/variables.txt", "a")
    print(variable.lexeme, signo, valor)
    valor_res = valor[::-1]
    pack.append(valor_res)
    signo_res = signo[::-1]
    index = len(signo_res)
    index_signo = 0
    variable_ar.append(variable)

    if len(signo_res) > 0:
        for j in range(len(valor_res)):
            if j == 0:
                # Si la primera posicion de Valor_res == variable_ar -_ solo se asigna
                for i in range(len(variable_ar)):
                    if valor_res[j] == variable_ar[i].lexeme:
                        file.write("\n\nla   $t0," + "   var_" + variable_ar[i].lexeme)
                        file.write("\nlw  " + "$a0," + "  0($t0)")
                        break
                # si la primera varible de VALOR_RES no es IGUAL a VARIABLE_AR -> se Creaera la variable
                else:
                    file.write("\nli $a0,    " + str(valor_res[j]) + "\n")
            if j >= 1:
                for i in range(len(variable_ar)):
                    if valor_res[j] == variable_ar[i].lexeme:
                        file.write("\n\nsw  " + "$a0,  " + "0($sp)")
                        file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")
                        file.write("\n\nla $t0, var_"+variable_ar[i].lexeme)
                        file.write("\nlw  " + "$a0," + "  0($t0)")
                        break

                else:
                    file.write("\n\nsw  " + "$a0,  " + "0($sp)")
                    file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")
                    file.write("\nli $a0,   " + str(valor_res[j]) + "\n")

                if index_signo < index:
                    if signo_res[index_signo] == "+":
                        file.write("\nlw   " + "$t1,   " + "4($sp) \n")
                        file.write("add  " + "$a0,  "   "$a0,  " + "$t1 \n")
                        file.write("\naddiu  " + "$sp  " + "$sp  " + "4")
                        index_signo += 1

        file.write("\n\nla   " + "$t0,  " + "var_"+variable.lexeme)
        file.write("\nsw  " + "$a0,  " + "0($t0)")
        file.close()

    else:
        file.write("\nli $a0,    " + str(valor_res[0]) + "\n")
        file.write("\nla   $t0," + "   var_"+variable.lexeme)
        file.write("\nsw  " + "$a0," + "  0($t0)\n")
        file.close()

# --------------------------------------------------------------------------------


def crearAsemblyIf(numero, simbolo, asig, copia, copia3):
    file = open("ProyectoParcial/variables.txt", "a")
    print(numero, simbolo, asig, copia, copia3)
    # print(print(variable_ar[0].lexeme))
    for i in range(len(variable_ar)):
        file.write("\n\nla $t0, var_"+variable_ar[i].lexeme)
        file.write("\nlw  " + "$a0,  " + "0($t0)")
        file.write("\n\nsw  " + "$a0,  " + "0($sp)")
        file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")

    if len(numero) > 0:

        if copia[1].isdigit():

            file.write("\nli $a0,    " + numero[0] + "\n")

            if simbolo[0] == ">":  # bgt $t0, $t1, mayor 	t0 > t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nbgt  " + "$a0,  " + "$t1,  " + "label_true")

            elif simbolo[0] == "<":  # blt $t0, $t1, menor	# t0 < t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nblt  " + "$a0,  " + "$t1,  " + "label_true")
        else:

            file.write("\nli $a0,    " + numero[0] + "\n")

            if simbolo[0] == ">":  # bgt $t0, $t1, mayor 	t0 > t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nblt  " + "$a0,  " + "$t1,  " + "label_true")

            elif simbolo[0] == "<":  # blt $t0, $t1, menor	# t0 < t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nbgt  " + "$a0,  " + "$t1,  " + "label_true")

    else:

        if copia3[0].isdigit():

            file.write("\nli $a0,    " + copia3[0] + "\n")

            if simbolo[0] == ">":  # bgt $t0, $t1, mayor 	t0 > t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nbgt  " + "$a0,  " + "$t1,  " + "label_true")

            elif simbolo[0] == "<":  # blt $t0, $t1, menor	# t0 < t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nblt  " + "$a0,  " + "$t1,  " + "label_true")

        else:

            if simbolo[0] == ">":  # bgt $t0, $t1, mayor 	t0 > t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nblt  " + "$a0,  " + "$t1,  " + "label_true")

            elif simbolo[0] == "<":  # blt $t0, $t1, menor	# t0 < t1
                file.write("\nlw  " + "$t1,  " + " 4($sp)")
                file.write("\nadd  " + "$sp,  " + "$sp, 4")
                file.write("\nbgt  " + "$a0,  " + "$t1,  " + "label_true")

# ----------------------------------------------------------------------------------------------------------
    # file.write("\n\nlabel_false:")
    # for h in range(len(pack)):
    #     file.write("\nli $a0,    "  + str(pack[h][0]) + "\n")
    #     file.write("\nla   $t0," + "   var_"+variable_ar[h].lexeme)
    #     file.write("\nsw  " + "$a0," + "  0($t0)\n")
    # file.write("\nb  " + "label_end\n")

    # file.write("\nlabel_true:")
    # for h in range(len(asig)):
    #     for f in range(len(variable_ar)):
    #         if asig[h][1] == variable_ar[f].lexeme:
    #             file.write("\nli $a0,    "  + (asig[h][0]) + "\n")
    #             file.write("\nla   $t0," + "   var_"+variable_ar[f].lexeme)
    #             file.write("\nsw  " + "$a0," + "  0($t0)\n")

    # file.write("\n\nlabel_end:")
    file.close()

# ------------------------------------------------------------------------------------------


def deficionIf(asig):
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\nlabel_true:")
    for h in range(len(asig)):
        for f in range(len(variable_ar)):
            if asig[h][1] == variable_ar[f].lexeme:
                file.write("\nli $a0,    " + (asig[h][0]) + "\n")
                file.write("\nla   $t0," + "   var_"+variable_ar[f].lexeme)
                file.write("\nsw  " + "$a0," + "  0($t0)\n")
    file.write("\n\nlabel_end:")
    file.close()


def deficionElse(asig):
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\n\nlabel_false:")
    for h in range(len(asig)):
        for f in range(len(variable_ar)):
            if asig[h][1] == variable_ar[f].lexeme:
                file.write("\nli $a0,    " + (asig[h][0]) + "\n")
                file.write("\nla   $t0," + "   var_"+variable_ar[f].lexeme)
                file.write("\nsw  " + "$a0," + "  0($t0)\n")
    file.write("\nb  " + "label_end\n")
    file.close()

# ----------------------------------------------------------------------------------------------


def invocationFuction(valor, variable, nameFuction):
    file = open("ProyectoParcial/variables.txt", "a")
    # int x; solo actualizamos la tabla de simbolos

    # x = f1(5); $ invocacion a una funcion
    file.write("\nsw  " + "$fp  " + "0($sp)")
    file.write("\naddiu  " + "$sp  " + "$sp-4")

    # generamos codigo para cada parametro
    for i in valor:
        file.write("\n\nli  " + "$a0,  " + i)

    # metemos el parametro a la pila
        file.write("\n\nsw  " + "$a0  " + "0($sp)")
        file.write("\naddiu  " + "$sp  " + "$sp-4")

    file.write("\n\njal  " + nameFuction[0])  # invocamos a la funcion

    # actualizamos la variable x en memoria   ##########################
    # el registro $t0, sera el puntero a la varaible en memoria
    file.write("\n\nla  " + "$t0,  " + "var_"+variable)
    file.write("\nsw  " + "$a0,  " "0($t0)")

    # ##################################################################

    # mostramos lo que tenemos en el acumulador
    # li $v0, 1
    # syscall
    file.write("\n\nli $v0, 1")
    file.write("\nsyscall")

    # # terminamos el codigo
    # li $v0, 10
    # syscall
    file.write("\n\nli $v0, 10")
    file.write("\nsyscall")






# ------------------------------------------------------------------------------------------------

def createFuction(valor, signo, nombreFuncion):
    file = open("ProyectoParcial/variables.txt", "a")

    file.write("\n\nmove  " + "$fp  " + "$sp  ")

    file.write("\n\n" + nombreFuncion + ":")

    file.write("\n\nsw  " + "$ra,  " + "0($sp)")
    file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")

    file.write("\nlw  " + "$a0,  " + "8($sp)")

    file.write("\n\nsw  " + "$a0,  " + "0($sp)")
    file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")

    # for
    # # 10
    if len(signo) > 2:
        print("Espera")
    else:

        for i in valor:
            # li $a0, 10
            file.write("\nli $a0,    " + i + "\n")
            if signo[0] == "+":
                # # suma
                # lw $t1, 4($sp)
                # add $a0, $a0, $t1
                file.write("\nlw   " + "$t1,   " + "4($sp) \n")
                file.write("add  " + "$a0,  "   "$a0,  " + "$t1 \n")

        # # li $a0, 10
        # file.write("\nli $a0,    " + valor + "\n")
        # #file.write("\nli $a0,    " + valor + "\n")
        # if signo == "+":
        #     # # suma
        #     # lw $t1, 4($sp)
        #     # add $a0, $a0, $t1
        #     file.write("\nlw   " + "$t1,   " + "4($sp) \n")
        #     file.write("add  " + "$a0,  "   "$a0,  " + "$t1 \n")

        # # pop
        file.write("\n\naddiu  " + "$sp,  " + "$sp,  4")

    # # fin expresion de la funcion ###############################################

    file.write("\n\nlw  " + "$ra  " + "4($sp)\n")
    file.write("addiu  " + "$sp  " + "$sp  12\n")  # 12 = 4*num_param + 8
    file.write("\nlw  "  + "$fp  " + "0($sp)\n")
    file.write("jr  " + "$ra")

    file.close()


# ----------------------------------------------------------------------------------------------------
def terminar():
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\n\nli $v0, 1")
    file.write("\nsyscall")
    file.write("\n\njr $ra ")
    file.close()
