###### Os objetivos básicos de um sistema operacional podem ser simplificados a dois conceitos: abstração e gerência de recursos.
###### A abstração de recursos diz respeito a independência do software em relação ao hardware, por exemplo, para salvar um arquivo, o software não precisa saber em qual tipo de disco ele será salvo, se será um HD, um SSD, ou um M2. Isso pode ser visto em nosso programa através da gravação do arquivo e a alteração desses, pois no código não é informado como a gravação deve ser feita, nem se ela mudaria de disco para disco. A abstração também deve atender os seguintes requisitos:

 - ###### Prover interfaces de acesso aos dispositivos, mais simples de usar que as interfaces de baixo nível;
 - ###### Tornar os aplicativos independentes do hardware;
 - ###### Definir interfaces de acesso homogêneas para dispositivos com tecnologias distintas;
 
###### Já a gerência de recursos diz respeito a eventuais disputas de recursos que podem acontecer entre os diferentes softwares que estarão rodando em um computador. Cabe ao sistema operacional definir políticas para gerenciar o uso dos recursos de hardware pelos aplicativos, e resolver eventuais disputas e conflitos. Um sistema operacional visa abstrair o acesso e gerenciar os recursos de hardware, provendo aos aplicativos um ambiente de execução abstrato, no qual o acesso aos recursos se faz através de interfaces simples, independentes das características e detalhes de baixo nível, e no qual os conflitos no uso do hardware são minimizados. Em nosso programa, a gerência de recursos se fez presente através dos processos criados e terminados ao longo do programa. Pois ao criar um processo, recursos são deslocados para ele, e ao terminá-lo, os recursos são “liberados”.



