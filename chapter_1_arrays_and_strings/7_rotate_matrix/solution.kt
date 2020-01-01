/* PROBLEM
   Given an image represented by an NxN matrix, where each pixel in the image is 4
   bytes, write a method to rotate the image by 90 degrees. Can you do this in place? */


/* ALGORITHM
   [eng]
   Rotation in place.
   We rotate the matrix starting from the outer ring, the considering the inner rings one
   after the other.
   For each ring we take each element of the top side, put it in the final position in the
   right side, take the relative element and put in the final position in the bottom side,
   take the relative element and put it in the final position in the left side. */

fun main() {
    val n = 4
    val matrix = Array(n, {i -> Array(n, {j -> (i * n + (j + 1))})})

    println("Orig matrix:")
    for (i in 0..n-1) {
        for (j in 0..n-1) {
            print("${matrix[i][j]} ")
        }
        println()
    }

    rotateMatrix(matrix)
    println("Dest matrix:")
    for (i in 0..n-1) {
        for (j in 0..n-1) {
            print("${matrix[i][j]} ")
        }
        println()
    }
}

fun rotateMatrix(matrix: Array<Array<Int>>) {
    val n: Int = matrix[0].size
    val end: Int = n / 2

    for (i in 0..end) {
        for (j in i..n-1-(i+1)) {
            rotate(i, j, matrix, n)
        }
    }
}

fun rotate(startRow: Int, startCol: Int, matrix: Array<Array<Int>>, n: Int) {
    var row = startRow
    var col = startCol
    var nextRow = col
    var nextCol = n - 1 - row

    var saved1 = matrix[startRow][startCol]
    var saved2 = 0
    for (i in 0..3) {
        saved2 = matrix[nextRow][nextCol]
        matrix[nextRow][nextCol] = saved1

        row = nextRow
        col = nextCol
        nextRow = col
        nextCol = n - 1 - row

        saved1 = saved2
    }

}
