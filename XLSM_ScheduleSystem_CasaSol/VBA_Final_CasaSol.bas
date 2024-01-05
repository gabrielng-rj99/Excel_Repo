Attribute VB_Name = "Module1"
Sub RectangleRoundedCorners1_Click()
' RectangleRoundedCorners1_Click Macro
' Limpar os Filtros
    ActiveSheet.Unprotect
    
    ChangeBevelEffect1
    
    ActiveWorkbook.SlicerCaches("Slicer_mês").ClearManualFilter
    ActiveWorkbook.SlicerCaches("Slicer_Dia").ClearManualFilter
    ActiveWorkbook.SlicerCaches("Slicer_da_Sem").ClearManualFilter
    ActiveWorkbook.SlicerCaches("Slicer_Horário").ClearManualFilter
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=1
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=2
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=3
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=4
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=5
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=6
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=7
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=8
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=9
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=10
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=11
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=12
    ActiveSheet.ListObjects("TB_Schedule").Range.AutoFilter Field:=13

    ChangeBevelEffect2
    
    ActiveSheet.Protect AllowFiltering:=True
    
End Sub

Sub ChangeBevelEffect1()
    Dim shp As Shape
    Set shp = ActiveSheet.Shapes("Limpar_Filtros_Button")
    
    With shp
        .ThreeD.BevelTopType = msoBevelSoftRound
    End With

    Dim startTime As Double
    startTime = Timer              ' Pause
    Do While Timer < startTime + 0.1
        DoEvents
    Loop

End Sub

Sub ChangeBevelEffect2()
    Dim shp As Shape
    Set shp = ActiveSheet.Shapes("Limpar_Filtros_Button")
    
    With shp
        .ThreeD.BevelTopType = msoBevelCircle
    End With

End Sub

