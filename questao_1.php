<?php

//Primeira Funcao
function convert_to_words($num)
{
    strval($num);
    //numero de digitos
    $len = strlen($num);
 
    // Base cases
    if ($len == 0)
    {
        echo "String vazia\n";
        return;
    }
    if ($len >3)
    {
        echo "Erro: Numero de digitos maior que 3 \n";
        return;
    }
 
    /* The first string is not used,
    it is to make array indexing simple */
    $single_digits = array("zero", "um", "dois",
                           "tres", "quatro", "cinco",
                           "seis", "sete", "oito",
                                           "nove");
 
    /* The first string is not used,
    it is to make array indexing simple */
    $two_digits = array("", "dez", "onze", "doze",
                        "treze", "quatorze", "quinze",
                        "dezesseis", "dezessete","dezoito",
                                               "dezenove");
 
    /* The first two string are not used,
    they are to make array indexing simple*/
    $tens_multiple = array("", "", "vinte", "trinta",
                           "quarenta", "cinquenta", "sessenta",
                           "setenta", "oitenta", "noventa");
 
    $tens_power = array("cento","dozentos", "trezentos","quatrocentos","quinhentos","seissentos",
    "setecentos","oitocentos","novecentos");
 

/* Debugar  */
//    echo $num.": ";
 
    /* Numero com 1 digito */
    if ($len == 1)
    {
        echo $single_digits[$num[0] - '0'] . " \n";
        return;
    }
 
    /* Enquanto num
        nao eh '\0' */
    $x = 0;
    while ($x < strlen($num))
    {
 
        /* Tratamentos do primeiro digito para numero com 3 digitos e numero 100 */
        if ($len >= 3)
        {
            /* Precisa tratar o caso especifico do numero 100 */
            if ($num[$x] - '0' == 1 &&
                     $num[$x + 1] - '0' == 0 &&
                     $num[$x + 2] - '0' == 0)
            {
                echo "cem\n";
                return;
            }

            if ($num[$x]-'0' != 0)
            {
                echo $tens_power[$num[$x] - 1] . " e ";
            
            }
            --$len;
        }
 
        /* Tratamento para os ultimos 2 digitos */
        else
        {
            /* 10-19 */
            if ($num[$x] - '0' == 1)
            {
                $sum = $num[$x] - '0' +
                       $num[$x] - '0';
                echo $two_digits[$sum] . " \n";
                return;
            }
 
            /*  21 ao 99 */
            else
            {
                $i = $num[$x] - '0';
                if($i > 0)
                echo $tens_multiple[$i] . " e ";
                else
                echo "";
                ++$x;
                if ($num[$x] - '0' != 0)
                    echo $single_digits[$num[$x] -
                                     '0'] . " \n";
            }
        }
        ++$x;
    }
}
 
//testes

//convert_to_words("520");
//convert_to_words("856");
//convert_to_words("809");
//convert_to_words("100");
//convert_to_words("21");
//convert_to_words("89");
//convert_to_words("8");

//Gerador aleatorio
 $x=0;
 while ($x < 20)
 {	
    	$nrand = rand(0,999);
        convert_to_words((string)$nrand);
        echo ";\n\n";
        ++$x;
 }



