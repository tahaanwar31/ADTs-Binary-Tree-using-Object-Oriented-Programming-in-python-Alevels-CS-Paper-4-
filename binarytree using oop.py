#DECLARE ArrayNodes:ARRAY[0:19] OF INTEGER
#DECLARE RootPointer,FreeNode:INTEGER
class Tree():
    #PUBLIC LeftPointer:INTEGER
    #PUBLIC Data:INTEGER
    #PUBLIC RightPointer:INTEGER
    def __init__(self,LeftPointerP,DataP,RightPointerP):
        self.LeftPointer=LeftPointerP
        self.Data=DataP
        self.Rightpointer=RightPointerP
ArrayNodes=[0]*20
RootPointer=-1
FreeNode=0
def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    NodeData=int(input("Please enter the data you want to add: "))
    if RootPointer>19:
        print("Binary Tree is full")
    else:
        ArrayNodes[FreeNode]=Tree(-1,NodeData,-1)
        if RootPointer==-1:
            RootPointer=0
        else:
            placed=False
            CurrentPointer=RootPointer
            while placed==False:
                if NodeData<ArrayNodes[CurrentPointer].Data:
                    if ArrayNodes[CurrentPointer].LeftPointer==-1:
                        ArrayNodes[CurrentPointer].LeftPointer=FreeNode
                        placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer].LeftPointer
                else:
                    if ArrayNodes[CurrentPointer].RightPointer==-1:
                        ArrayNodes[CurrentPointer].RightPointer=FreeNode
                        placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer].RightPointer
        FreeNode=FreeNode+1
def FindItem(SearchItem):
    CurrentPointer=RootPointer
    while CurrentPointer!=-1 and ArrayNodes[CurrentPointer].Data!=SearchItem:
        if SearchItem<ArrayNodes[CurrentPointer].Data:
            CurrentPointer=ArrayNodes[CurrentPointer].Leftpointer
        else:
            CurrentPointer=ArrayNodes[CurrentPointer].RightPointer
    print(CurrentPointer)

