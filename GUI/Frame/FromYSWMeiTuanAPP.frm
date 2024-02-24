VERSION 5.00
Begin VB.Form FromYSWMeiTuanAPP 
   Caption         =   "美团经营数据读取软件"
   ClientHeight    =   10305
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   17445
   LinkTopic       =   "Form1"
   ScaleHeight     =   10305
   ScaleWidth      =   17445
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame FrameLog 
      Caption         =   "运行日志"
      Height          =   9735
      Left            =   3240
      TabIndex        =   7
      Top             =   240
      Width           =   13815
      Begin VB.ListBox ListLog 
         Height          =   8880
         ItemData        =   "FromYSWMeiTuanAPP.frx":0000
         Left            =   360
         List            =   "FromYSWMeiTuanAPP.frx":0002
         TabIndex        =   8
         Top             =   480
         Width           =   13095
      End
   End
   Begin VB.Frame FrameChromeOptions 
      Caption         =   "浏览器操作"
      Height          =   9735
      Left            =   360
      TabIndex        =   0
      Top             =   240
      Width           =   2655
      Begin VB.CommandButton CommandSaveData 
         Caption         =   "保存数据"
         Height          =   615
         Left            =   360
         TabIndex        =   6
         Top             =   4560
         Width           =   1935
      End
      Begin VB.CommandButton CommandHeadlessChrome 
         Caption         =   "隐藏浏览器"
         Height          =   615
         Left            =   360
         TabIndex        =   5
         Top             =   1200
         Width           =   1935
      End
      Begin VB.CommandButton CommandReadFromCurrent 
         Caption         =   "从当前页读取"
         Height          =   615
         Left            =   360
         TabIndex        =   4
         Top             =   3720
         Width           =   1935
      End
      Begin VB.CommandButton CommandReadData 
         Caption         =   "读取经营数据"
         Height          =   615
         Left            =   360
         TabIndex        =   3
         Top             =   2880
         Width           =   1935
      End
      Begin VB.CommandButton CommandCheckStatus 
         Caption         =   "检查登录状态"
         Height          =   615
         Left            =   360
         TabIndex        =   2
         Top             =   2040
         Width           =   1935
      End
      Begin VB.CommandButton CommandOpenChrome 
         Caption         =   "打开浏览器"
         Height          =   615
         Left            =   360
         TabIndex        =   1
         Top             =   360
         Width           =   1935
      End
   End
End
Attribute VB_Name = "FromYSWMeiTuanAPP"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
