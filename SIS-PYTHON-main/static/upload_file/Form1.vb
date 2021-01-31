Imports System.IO
Imports System.Text

Module Module1
    Sub aaa()
        Dim barcode As OnBarcode.Barcode.Linear
        ' Create linear barcode object
        barcode = New OnBarcode.Barcode.Linear()
        ' Set barcode symbology type to Code-39
        barcode.Type = OnBarcode.Barcode.BarcodeType.CODE39
        ' Set barcode data to encode
        barcode.Data = "0123456789"
        ' Set barcode bar width (X    dimension) in pixel
        barcode.X = 1
        ' Set barcode bar height (Y dimension) in pixel
        barcode.Y = 60
        ' Draw & print generated barcode to png image file
        barcode.drawBarcode("C://vbnet-code39.png")
    End Sub
    Sub dle()
        Dim path As String = "C:\Users\AH\Desktop\MyTest.txt"
        My.Computer.FileSystem.DeleteFile(path)
    End Sub
    Sub aame()
        My.Computer.FileSystem.RenameFile("C:\Users\AH\Desktop\MyTest.txt", "SecondTest.txt")
    End Sub
    Sub create()
        Dim path As String = "C:\Users\AH\Desktop\MyTest.txt"

        ' Create or overwrite the file.
        Dim fs As FileStream = File.Create(path)

        ' Add text to the file.
        Dim info As Byte() = New UTF8Encoding(True).GetBytes("This is some text in the file.")
        fs.Write(info, 0, info.Length)
        fs.Close()
    End Sub

End Module


Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        aaa()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Dim FILE_NAME As String = "C:\Users\AH\Desktop\Cheat Engine.lnk"

        If System.IO.File.Exists(FILE_NAME) = True Then
            Process.Start(FILE_NAME)
        Else
            MsgBox("File Does Not Exist")
        End If
    End Sub

    Private Sub ListBox1_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ListBox1.SelectedIndexChanged
        For Each foundFile As String In My.Computer.FileSystem.GetFiles(My.Computer.FileSystem.SpecialDirectories.MyDocuments, Microsoft.VisualBasic.FileIO.SearchOption.SearchAllSubDirectories, "C:\Users\AH\Desktop\*.txt")
            ListBox1.Items.Add(foundFile)
        Next
    End Sub
End Class


