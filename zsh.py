# -- encoding: utf-8 --
# encode as 'UTF8'
import os
import sys,time
m="\033[5;31m"
mm="\033[0;31m"
m1="\033[1;31m"
gt="\033[1;32m"
c="\033[1;36m"
y="\033[1;33m"
w="\033[1;37m"
ban = '''
    %sZsh Theme Installer for termux
    %sCoded by :  %s-=Mr_msdv=-%s'''%(gt,c,m,mm)
tema = """%s
 ╔════════════════════════╗
 ║%s    Pilih Salah satu %s   ║
 ╠═══╦════════════════════╣
 ║%s 1%s ║%s robbyrussell       %s║
 ║%s 2%s ║%s af-magic           %s║
 ║%s 3%s ║%s afowler            %s║
 ║%s 4%s ║%s agnoster           %s║
 ║%s 5%s ║%s alanpeabody        %s║
 ║%s 6%s ║%s amuse              %s║
 ║%s 7%s ║%s arrow              %s║
 ║%s 8%s ║%s aussiegeek         %s║
 ║%s 9%s ║%s avit               %s║
 ║%s10%s ║%s awesomepanda       %s║
 ╚═══╩════════════════════╝"""%(c,y,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c,w,c,gt,c)
 
print(ban).center(64,'=')
print(c+' Instaling ZSH Themes').center(45)
os.system("mv $HOME/.termux $HOME/.termux.bak")
os.system("curl -fsLo $HOME/.termux/colors.properties --create-dirs https://raw.githubusercontent.com/mrmsdv/zsh-theme-OnTermux/master/.setings/colors.properties")
time.sleep(2)
print(m1+" Loading 35%").center(45)
os.system("curl -fsLo $HOME/.termux/font.ttf --create-dirs https://raw.githubusercontent.com/mrmsdv/zsh-theme-OnTermux/master/.setings/font.ttf")
time.sleep(1)
print(m1+" Loading 63%")
os.system("curl -fsLo $HOME/.termux/termux.properties --create-dirs https://raw.githubusercontent.com/mrmsdv/zsh-theme-OnTermux/master/.setings/termux.properties")
time.sleep(2)
print(m1+" Loading 100% Completed !")
os.system("git clone git://github.com/robbyrussell/oh-my-zsh.git $HOME/.oh-my-zsh --depth 1")
os.system("cp $HOME/.oh-my-zsh/templates/zshrc.zsh-template $HOME/.zshrc")
os.system('''sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' $HOME/.zshrc''')
print(m+" Setting Complete !"+m1)
time.sleep(2)
os.system('termux-reload-settings')
time.sleep(2)
print(ban)