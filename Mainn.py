from Core import *
menu()
option=int(input("Enter your option: "))


while option !=0:
    if option==1:
        input_list_changeset=input('Please input ur changesets separated by comma: ')
        changesets=input_list_changeset.split(',')
        print('Changeset      Distance')
        
        core(changesets)




    elif option==2:
        input_list_way=input('Please input your ways id separated by comma: ')
        Per_way=input_list_way.split(',')
        print('Way id       Distance')
        for j in Per_way:
            Dist=0
            node=Take_nodes_from_ways(j)    
            latlong=Take_latlong_from_node(node)
            Dist01=Calculate_Distance_Way(latlong)
            Dist= Dist01+Dist
            if Dist ==0:
                Dist=0.2
            
            print(f'{j}\t{Dist}')
            
            

    elif option==3:
        User=input('Please input your user name on OSMCha: ')
        Token=input('Please copy and paste your Token on OSMCha: ')
        StartDate=input('Please input Start date for query following format YYYY-MM-DD: ')
        EndDate=input('Please input End date for query following format YYYY-MM-DD: ')
        Info=OSMCha_name_query(StartDate,EndDate,User,Token)
        print('Changeset      Distance')
        core(Info)
    
    
    
    else:
        print('Invalid option')  
        print("")


    menu()        
    option=int(input("Enter your option: "))  


print('\n')
print('Thanks for using my tool. See you soon!!!') 