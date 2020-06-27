@echo off
:Start
cls
echo Escolha um programa para rodar
echo.
echo 01. Aula_01_0_QtApp                       25. Aula_17_1_App_Webview (bad)
echo 02.                                       26. Aula_17_2_App_Webview (Ok NotaFiscal)
echo 03.                                       27. Aula_17_3_App_Webview (Ok Google)
echo 04.                                       28. Aula_17_4_App_Webview
echo 05.                                       29.
echo 06.                                       30. Aula_18_1_Cons_ServerRMI
echo 07.                                       31. Aula_18_1_Cons_ClientRMI
echo 08. Aula_01_0_QtApp_Event                 32.
echo 09.                                       33.
echo 10. Aula_10_1_App_Thread                  34.
echo 11. Aula_10_2_App_Thread                  35.
echo 12. Aula_10_3_App_Thread                  36.
echo 13. Aula_13_1_App_ServerSocket            37.
echo 14. Aula_13_1_App_ClientSocket            38.
echo 15.                                       39.
echo 16. Aula_14_1_Cons_Report_Xhtml2Pdf       40.
echo 17. Aula_14_2_Cons_Report_Xhtml2Pdf       41.
echo 18. Aula_14_3_Cons_Report_Xhtml2Pdf_Tag   42.
echo 19. Aula_14_4_Cons_Report_Xhtml2Pdf_Pie   43.
echo 20. Aula_14_5_Cons_Report_Xhtml2Pdf_Hist  44.
echo 21. Aula_14_6_Cons_Report_Xhtml2Pdf_Sig   45.
echo 22. Aula_14_7_Cons_Report_Xhtml2Pdf_3D    46.
echo 23.                                       47.
echo 24.                                       48.
echo qq. Sair
echo.

set /p x="Escolha: "
IF '%x%' GEQ '01' (IF '%x%' LEQ '09' GOTO Item_%x%)
IF '%x%' GEQ '10' (IF '%x%' LEQ '19' GOTO Item_%x%)
IF '%x%' GEQ '20' (IF '%x%' LEQ '29' GOTO Item_%x%)
IF '%x%' GEQ '30' (IF '%x%' LEQ '31' GOTO Item_%x%)
IF '%x%' EQU 'qq' GOTO Item_%x%
IF '%x%' EQU 'QQ' GOTO Item_%x%

echo.
echo Favor digitar valores entre 01 e 28 ou qq para sair
GOTO Continue

:Item_01
cls
"C:\ProgramData\Anaconda3\python" Aula_01_0_QtApp.py
GOTO Continue

:Item_02
cls
"C:\ProgramData\Anaconda3\python" Aula_03_2_App_Pack.py
GOTO Continue

:Item_03
cls
"C:\ProgramData\Anaconda3\python" Aula_03_3_App_Place.py
GOTO Continue

:Item_04
cls
"C:\ProgramData\Anaconda3\python" Aula_06_1_App_Event.py
GOTO Continue

:Item_05
cls
"C:\ProgramData\Anaconda3\python" Aula_06_2_App_1Cam.py
GOTO Continue

:Item_06
cls
"C:\ProgramData\Anaconda3\python" Aula_06_3_App_2Cam.py
GOTO Continue

:Item_07
cls
"C:\ProgramData\Anaconda3\python" Aula_09_1_App_Frame.py
GOTO Continue

:Item_08
cls
"C:\ProgramData\Anaconda3\python" Aula_09_2_App_Frame.py
GOTO Continue

:Item_09
cls
"C:\ProgramData\Anaconda3\python" Aula_09_3_App_Menu.py
GOTO Continue

:Item_10
cls
"C:\ProgramData\Anaconda3\python" Aula_10_1_App_Thread.py
GOTO Continue

:Item_11
cls
"C:\ProgramData\Anaconda3\python" Aula_10_2_App_Thread.py
GOTO Continue

:Item_12
cls
"C:\ProgramData\Anaconda3\python" Aula_10_3_App_Thread.py
GOTO Continue

:Item_13
cls
"C:\ProgramData\Anaconda3\python" Aula_13_1_App_ServerSocket.py
GOTO Continue

:Item_14
cls
"C:\ProgramData\Anaconda3\python" Aula_13_1_App_ClientSocket.py
GOTO Continue

:Item_15
cls
"C:\ProgramData\Anaconda3\python" zzzzzzzzzzzzzzzzzzz.py
GOTO Continue

:Item_16
cls
"C:\ProgramData\Anaconda3\python" Aula_14_1_Cons_Report_Xhtml2Pdf.py
GOTO Continue

:Item_17
cls
"C:\ProgramData\Anaconda3\python" Aula_14_2_Cons_Report_Xhtml2Pdf.py
GOTO Continue

:Item_18
cls
"C:\ProgramData\Anaconda3\python" Aula_14_3_Cons_Report_Xhtml2Pdf_Tag.py
GOTO Continue

:Item_19
cls
"C:\ProgramData\Anaconda3\python" Aula_14_4_Cons_Report_Xhtml2Pdf_Pie.py
GOTO Continue

:Item_20
cls
"C:\ProgramData\Anaconda3\python" Aula_14_5_Cons_Report_Xhtml2Pdf_Hist.py
GOTO Continue

:Item_21
cls
"C:\ProgramData\Anaconda3\python" Aula_14_6_Cons_Report_Xhtml2Pdf_Sig.py
GOTO Continue

:Item_22
cls
"C:\ProgramData\Anaconda3\python" Aula_14_7_Cons_Report_Xhtml2Pdf_3D.py
GOTO Continue

:Item_23
cls
"C:\ProgramData\Anaconda3\python" zzzzzzzzzzzzzzzzzzz.py
GOTO Continue

:Item_24
cls
"C:\ProgramData\Anaconda3\python" zzzzzzzzzzzzzzzzzzz.py
GOTO Continue

:Item_25
cls
"C:\ProgramData\Anaconda3\python" Aula_17_1_App_Webview.py
GOTO Continue

:Item_26
cls
"C:\ProgramData\Anaconda3\python" Aula_17_2_App_Webview.py
GOTO Continue

:Item_27
cls
"C:\ProgramData\Anaconda3\python" Aula_17_3_App_Webview.py
GOTO Continue

:Item_28
cls
"C:\ProgramData\Anaconda3\python" Aula_17_4_App_Webview.py
GOTO Continue

:Item_29
cls
"C:\ProgramData\Anaconda3\python" zzzzzzzzzzzzzzzzzzz.py
GOTO Continue

:Item_30
cls
"C:\ProgramData\Anaconda3\python" Aula_18_1_Cons_ServerRMI.py
GOTO Continue

:Item_31
cls
"C:\ProgramData\Anaconda3\python" Aula_18_1_Cons_ClientRMI.py
GOTO Continue

:Item_qq
cls
exit

:Item_QQ
cls
exit

:Continue
pause
GOTO Start