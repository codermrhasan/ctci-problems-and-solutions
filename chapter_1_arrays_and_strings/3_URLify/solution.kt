fun main() {
    val origArray = Array<Char>(7) { ' ' }
    origArray[0] = 'p'
    origArray[1] = ' '
    origArray[2] = 'r'
    origArray[3] = 'o'
    origArray[4] = 'v'

    println("Final string: ${replaceSpaces(origArray, 5)}")
}

fun replaceSpaces(origArray: Array<Char>, origLen: Int): String {
    var spaces = 0
    for (i in 0 until origLen) {
        if (origArray[i] == ' ') spaces++
    }
    val finalLen = origLen + 2 * spaces

    var pos = finalLen - 1
    for (i in (origLen-1) downTo 0) {
        if (origArray[i] == ' ') {
            origArray[pos--] = '0'
            origArray[pos--] = '2'
            origArray[pos--] = '%'
        } else {
            origArray[pos--] = origArray[i]
        }
    }

    return origArray.joinToString("")
}


