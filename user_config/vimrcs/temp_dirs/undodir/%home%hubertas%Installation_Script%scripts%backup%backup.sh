Vim�UnDo� ���
g�e����}©�w���r��L   C   #	git push 1> /dev/null 2> /dev/null   =   #                       f!T1    _�                     !        ����                                                                                                                                                                                                                                                                                                                                                             f&�     �   !   #   8    �   !   "   8    5��    !                      �              O       5�_�                    "        ����                                                                                                                                                                                                                                                                                                                                                             f&�     �   "   $   9    �   "   #   9    5��    "                      �              O       5�_�                    "       ����                                                                                                                                                                                                                                                                                                                                                             f&�     �   !   #   :      Ncp -r ~/.config/rofi/* ~/Installation_Script/user_config/rofi 2>/dev/null || :5��    !                    �                    5�_�                    "   =    ����                                                                                                                                                                                                                                                                                                                                                             f&�     �   !   #   :      Ncp -r ~/.config/nvim/* ~/Installation_Script/user_config/rofi 2>/dev/null || :5��    !   8                 �                    5�_�                    #   =    ����                                                                                                                                                                                                                                                                                                                                                             f&�     �   "   $   :      Ncp -r ~/.config/rofi/* ~/Installation_Script/user_config/rofi 2>/dev/null || :5��    "   8                 ,                    5�_�                    #       ����                                                                                                                                                                                                                                                                                                                                                             f&�    �   "   $   :      Pcp -r ~/.config/rofi/* ~/Installation_Script/user_config/vimrcs 2>/dev/null || :5��    "   	                 �                    �    "                                        �    "                                        5�_�                            ����                                                                                                                                                                                                                                                                                                                                       :           V        f�    �                   �               �              :   #! /bin/bash   &scriptLoc="$(cd $(dirname "$0"); pwd)"       set -e       # Backup script   currentLoc=$(pwd)   YELLOW='\033[1;33m'   GREEN='\033[0;32m'   RED='\033[0;31m'   NC='\033[0m' # No Color   OKBLUE='\033[94m'   OKGREEN='\033[92m'   FAIL='\033[91m'       Backup_Success() {   :	if git status | grep -q 'Your branch is up to date'; then   7		echo -e "${OKGREEN}Backup successful for ${PWD}${NC}"   	else   0		echo -e "${FAIL}Backup failed for ${PWD}${NC}"   	fi   }       PROMPT_COMMAND="Backing up..."       %echo -e "${OKBLUE}Backing up...${NC}"   ,echo -e "${OKBLUE}Copying config files${NC}"   # Backup nvim settings   Vcp ~/.config/nvim/init.lua ~/Installation_Script/user_config/init.lua 2>/dev/null || :   %# Backup polybar, qtile, rofi configs   Tcp -r ~/.config/polybar/* ~/Installation_Script/user_config/polybar 2>/dev/null || :   Pcp -r ~/.config/qtile/* ~/Installation_Script/user_config/qtile 2>/dev/null || :   Ncp -r ~/.config/rofi/* ~/Installation_Script/user_config/rofi 2>/dev/null || :   Ncp -r ~/.config/nvim/* ~/Installation_Script/user_config/nvim 2>/dev/null || :   Ocp -r ~/.vim/vimrcs/* ~/Installation_Script/user_config/vimrcs 2>/dev/null || :   # Backup inputrc   0cp ~/.inputrc ~/Installation_Script/user_config/   # Backup TMUX configuration   Ecp -r ~/.tmux.conf ~/Installation_Script/user_config 2>/dev/null || :   # Backup GNOME settings   $cd ~/Installation_Script/user_config   #dconf dump / > saved_settings.dconf       echo "Starting backup to git"       cd "$scriptLoc"   while read p || [[ -n $p ]];   do   (	echo -e "${OKBLUE}Backing up ${p}${NC}"   	cd $p   	git add . 1> /dev/null   )	git commit -m "Backup" 1> /dev/null || :   #	git push 1> /dev/null 2> /dev/null   	Backup_Success   done < gitlocations.txt       (echo -e "${OKGREEN}Backup complete${NC}"   "PROMPT_COMMAND="Completed backup."5��            :                      �             �                    D                       s      5�_�      	                 J    ����                                                                                                                                                                                                                                                                                                                                                             fLt    �   
      E      T    echo "$0 at line $1 with command $ERROR" >> /home/hubertas/tools/tool_errors.log5��    
   I                 �                     5�_�      
           	   '       ����                                                                                                                                                                                                                                                                                                                                                             fO2     �   &   (   E      Vcp ~/.config/nvim/init.lua ~/Installation_Script/user_config/init.lua 2>/dev/null || :5��    &                                        5�_�   	              
   '   E    ����                                                                                                                                                                                                                                                                                                                                                             fO6     �   &   (   E      Vcp ~/.config/nvim/init.vim ~/Installation_Script/user_config/init.lua 2>/dev/null || :5��    &   B                 D                    5�_�   
                 '   D    ����                                                                                                                                                                                                                                                                                                                                                             fOA     �   &   '          Vcp ~/.config/nvim/init.vim ~/Installation_Script/user_config/init.vim 2>/dev/null || :5��    &                            W               5�_�                    &       ����                                                                                                                                                                                                                                                                                                                                                             fOB    �   %   &          # Backup nvim settings5��    %                      �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             f!T     �         C      exec 2>/tmp/error5��                          =                      5�_�                    <   )    ����                                                                                                                                                                                                                                                                                                                                                             f!T+     �   ;   =   C      )	git commit -m "Backup" 1> /dev/null || :5��    ;                     Z                     5�_�                     =   #    ����                                                                                                                                                                                                                                                                                                                                                             f!T0    �   <   >   C      #	git push 1> /dev/null 2> /dev/null5��    <   	                  d                     5��