#!/bin/bash
mkdir Defesa_Cibernetica; cd Defesa_Cibernetica
mkdir hackermindset codeforsecurity linux_windows networking iot computer_architecture security_management
cd hackermindset/
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd codeforsecurity/
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd linux_windows/ 
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd networking/ 
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd iot/ 
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd computer_architecture/ 
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..
cd security_management/ 
echo "A melhor matéria é HackerMindset" > notas.txt; cd ..

cd hackermindset/
echo "usuario: "$(whoami) > file.txt
echo "host: "$(hostname) >> file.txt
echo "SO: "$( systeminfo | grep "Nome do sistema operacional" | cut -d : -f2- | cut -c 2-) >> file.txt
echo "Ip: "$(ipconfig | grep "Endereço IPv4. . . . . . . . . . . :" | awk '{print $14}' | sed '2,14d') >> file.txt
echo "path: "$(pwd) >> file.txt

#Comantario novoooo
