#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name=="ʯͷ":
     return 0

		
		
     
    elif name=="ʷ����":
     return 1
     
    elif name=="ֽ":
     return 2
     
    elif name=="����":
     return 3
     
    elif name=="����":
     return 4
      
    else:
     print("Error: No Correct Name")
	 
	  	
    


    

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number==0:
     return "ʯͷ"
     
    elif number==1:
     return "ʷ����"
     
    elif number==2:
     return "ֽ"
     
    elif number==3:
     return "����"
     
    elif number==4:
     return "����"
     
    else:
     print("Error: No Correct Name")
     
        
   

    


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("---------------------")
    

    player_choice_number=name_to_number(player_choice)
    
    import random
    
    comp_number=random.randrange(0,4)
    
    comp_choice=number_to_name(comp_number)
    
    print(comp_choice)
    
    s=(player_choice_number-comp_number)%10
    
    if s==0:
     print("���ͼ��������һ����")
    elif s==1 or s==2:
     print("��Ӯ��")
    elif s==3 or s==4:
     pront("�����Ӯ��") 
	
     

		
		 
    
    
    
    
    

    

    

    

    

    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


