import subprocess as sub
import os
os.system("tput setaf 6")
print("         -----------------WELLCOME TO MY AUTOMATION WORLD-----------   ")
os.system("tput setaf 7")

print("""press 1 : configure httpd server 
press 2 : configure docker  
press 3 : create lvm and increase and decraese the size of lvm 
press 4 : yum configuration
press 5 : configure the name  node 
press 6 : configure the data note  
press 7 : configure httpd server top of docker 
press 8 : exit """)
while True:
   print("please enter your choice which type of system you use remote/local : ",end=' ')
   i=input()
   if i=="local":
        x=int(input("enter what you want to do : "))
        def confhttpd():  
                  os.system("sudo yum install httpd")
                  os.system("sudo systemctl start httpd")
                  os.chdir("/var/www/html")
                  x=input("enter the file name eg:vik :  " )
                  os.system("cat > {}.html".format(x))
                  os.system(" ifconfig")
                  c=input("enter the system ip address : " )
                  os.system("curl -I  http://{}/{}.html".format(c,x)) 
        def confdocker():
                  os.system("sudo  dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                  os.system("sudo  dnf install docker-ce --allowerasing  -y")
                  os.system("sudo systemctl start docker")
                  os.system("sudo systemctl enable docker")
                  os.system("sudo systemctl status docker")

             
        def createpv():
                  os.system("fdisk -l")
                  b=int(input("enter how many storage you want to attach:"))
                  c=[]
                  for i in range(b):
                                d=input("enter the name of storage {}".format(i+1))
                                c.append(d)
                                os.system("pvcreate /dev/{}".format(d))
                  e=input("please enter virtual grouph name: ")
                  os.system("vgcreate {} /dev/{}".format(e,c[0]))
                  x = range(b)
                  x.pop(0)
                  for p in x:
                           os.system("vgextend {} /dev/{}".format(e,c[p]))
                  f=int(input("enter partition size: "))
                  g=input("enter your paraition name: ")
                  os.system("lvcreate --size {}G --name {} {}".format(f,g,e))
                  os.system("mkfs.ext4 /dev/{}/{}".format(e,g))
                  h=input("enter a directory name where you want to mount this partition: ")
                  os.system("mkdir {}".format(h))
                  os.system("mount /dev/{}/{} {}".format(e,g,h))
                  print("your partition was created sussfully")
                  a=input("do you want to see details of your storage? (y/n): ")
                  if a in 'y':
                            os.system("lvdisplay {}/{}".format(e,g))
        def extendlv():
                e=input("please enter volume group name: ")
                g=input("enter your partition name (for example sdd2): ")
                l=int(input("enter how much size you want to increase: "))
                os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
                os.system("resize2fs /dev/{}/{}".format(e,g))
        def reducelv():
                e=input("please enter volume group name: ")
                g=input("enter your partition name (for example sdd2): ")
                l=int(input("enter how much size you want to reduce: "))
                os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
        def vgextend():
                y=input("Enter The partition name you want to increase: ")
                os.system("vgextend {} /dev/{}".format(e,y))
		
        def yumconf():  
                sub.getstatusoutput("echo '[dvd1] \n baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream \n gpgcheck=0 \n\n [dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \n gpgcheck=0' > yumconfi.repo | mv yumconfi.repo /etc/yum.repos.d/")
                os.system("sudo yum repolist")
   
       

            
        def namenode():
                z=input("enter the directory name you download hadoop and java software : ")
                os.system("sudo rpm -ivh  {}/jdk-8u171-linux-x64.rpm".format(z))
                os.system("sudo rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(z))          
                dirName = input("enter directory name (for eg: name): ")
                check = sub.getstatusoutput("mkdir /{}".format(dirName))
                while check[0]!=0:
                        print("this directory is exist")
                        dirName = input("enter directory name again (for eg: name): ")
                        os.system("mkdir /{}".format(dirName))
                sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
                ip = (input("enter ip of your pc (for eg: 192.168.32.45): "))
                portNo = int(input("enter a port no (for eg: 9001): "))
                sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(ip,portNo))
                os.system("hadoop namenode -format")
                sub.getoutput("hadoop-daemon.sh start namenode")
                os.system("jps")
        def datanode():
                z=input("enter the directory name you download hadoop and java software : ")
                os.system("sudo rpm -ivh  {}/jdk-8u171-linux-x64.rpm".format(z))
                os.system("sudo rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(z))
                dirName = input("enter directory name (for eg: name): ")
                check = sub.getstatusoutput("mkdir /{}".format(dirName))
                while check[0]!=0:
                        print("this directory is exist")
                        dirName = input("enter directory name again (for eg: name): ")
                        os.system("mkdir /{}".format(dirName))
                sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.data.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
                ip = (input("enter ip of your pc (for eg: 192.168.32.45): "))
                portNo = int(input("enter a port no (for eg: 9001): "))
                sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(ip,portNo))
                os.system("hadoop namenode -format")
                sub.getoutput("hadoop-daemon.sh start namenode")
                os.system("jps")
        
        def httpddocker():
                      os.system("sudo  dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                      os.system("sudo  dnf install docker-ce --allowerasing  -y")
                      os.system("sudo systemctl start docker")
                      os.system("sudo systemctl enable docker")
                      os.system("sudo systemctl status docker")

                      x=input("enter os name : ") 
                      os.system("docker pull {}".format(x))
                      os.system("docker images")
                      y=input("enter conatiner os name : ")
                      z=input("enter image   name : ")
                      t=input("enter the port name : ")
                      os.system("docker run -dit --name {} -p {}:80   {}".format(y,t,z))
                      img=input("enter the os name : ")
                      os.system("docker exec i {} /usr/sbin/httpd".format(img))
                      image=input("enter the container name : ")
                      os.system("docker exec {} yum install httpd -y".format(image))
                      os.system("docker exec {} yum install net-tools -y")

                      os.system("systemctl start  httpd")
                      os.chdir("/var/www/html")
                      x=input("enter the file name : ")
                      os.system("cat > {}.html".format(x))
                      os.system("ifconfig")
                      c=input("enter the system ip addres : ")
                      os.system("curl -I  http://{}/{}.html".format(c,x))



        if x==1:
            confhttpd()
        if x==2:
            confdocker()

       
        if x==3:
            createpv()
            extendlv()
            reducelv()
            vgextend()


        if x==4:
            yumconf()

        if x==5:
            namenode()

        if x==6:
            datanode()

        if x==7:
            httpddocker()
        if x==8:
            exit()






   elif i=="remote":
       print("enter the ip address of remote system : ",end='')
       d=input()
       j=os.system("ssh root@{}".format(d))
       if j!=0:
           exit()
       x=int(input("enter what you want to do : "))
       def confhttpd():
                  os.system("sudo yum install httpd")
                  os.system("sudo systemctl start httpd")
                  os.chdir("/var/www/html")
                  x=input("enter the file name eg:vik :  " )
                  os.system("cat > {}.html".format(x))
                  os.system(" ifconfig")
                  c=input("enter the system ip address : " )
                  os.system("curl -I  http://{}/{}.html".format(c,x))
       def confdocker():
                  os.system("sudo  dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                  os.system("sudo  dnf install docker-ce --allowerasing  -y")
                  os.system("sudo systemctl start docker")
                  os.system("sudo systemctl enable docker")
                  os.system("sudo systemctl status docker")

       def createpv():
                  os.system("fdisk -l")
                  b=int(input("enter how many storage you want to attach:"))
                  c=[]
                  for i in range(b):
                                d=input("enter the name of storage {}".format(i+1))
                                c.append(d)
                                os.system("pvcreate /dev/{}".format(d))
                  e=input("please enter virtual grouph name: ")
                  os.system("vgcreate {} /dev/{}".format(e,c[0]))
                  x = range(b)
                  x.pop(0)
                  for p in x:
                         os.system("vgextend {} /dev/{}".format(e,c[p]))
                  f=int(input("enter partition size: "))
                  g=input("enter your paraition name: ")
                  os.system("lvcreate --size {}G --name {} {}".format(f,g,e))
                  os.system("mkfs.ext4 /dev/{}/{}".format(e,g))
                  h=input("enter a directory name where you want to mount this partition: ")
                  os.system("mkdir {}".format(h))
                  os.system("mount /dev/{}/{} {}".format(e,g,h))
                  print("your partition was created sussfully")
                  a=input("do you want to see details of your storage? (y/n): ")
                  if a in 'y':
                            os.system("lvdisplay {}/{}".format(e,g))
       def extendlv():
                        e=input("please enter volume group name: ")
                        g=input("enter your partition name (for example sdd2): ")
                        l=int(input("enter how much size you want to increase: "))
                        os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
                        os.system("resize2fs /dev/{}/{}".format(e,g))
       def reducelv():
                        e=input("please enter volume group name: ")
                        g=input("enter your partition name (for example sdd2): ")
                        l=int(input("enter how much size you want to reduce: "))
                        os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
       def vgextend():
                        y=input("Enter The partition name you want to increase: ")
                        os.system("vgextend {} /dev/{}".format(e,y))


       def yumconf():
                        sub.getstatusoutput("echo '[dvd1] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream \ngpgcheck=0 \n\n[dvd2] \nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS \ngpgcheck=0' > yumconfi.repo | mv yumconfi.repo /etc/yum.repos.d/")
                        os.system("sudo yum repolist")




       def namenode():
                       z=input("enter the directory name you download hadoop and java software : ")
                       os.system("sudo rpm -ivh  {}/jdk-8u171-linux-x64.rpm".format(z))
                       os.system("sudo rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(z))

                       dirName = input("enter directory name (for eg: name): ")
                       check = sub.getstatusoutput("mkdir /{}".format(dirName))
                       while check[0]!=0:
                                  print("this directory is exist")
                                  dirName = input("enter directory name again (for eg: name): ")
                                  os.system("mkdir /{}".format(dirName))
                       sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
                       ip = (input("enter ip of your pc (for eg: 192.168.32.45): "))
                       portNo = int(input("enter a port no (for eg: 9001): "))
                       sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(ip,portNo))
                       os.system("hadoop namenode -format")
                       sub.getoutput("hadoop-daemon.sh start namenode")
                       os.system("jps")

       def datanode():
                       z=input("enter the directory name you download hadoop and java software : ")
                       os.system("sudo rpm -ivh  {}/jdk-8u171-linux-x64.rpm".format(z))
                       os.system("sudo rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(z))

                       dirName = input("enter directory name (for eg: name): ")
                       check = sub.getstatusoutput("mkdir /{}".format(dirName))
                       while check[0]!=0:
                                  print("this directory is exist")
                                  dirName = input("enter directory name again (for eg: name): ")
                                  os.system("mkdir /{}".format(dirName))
                       sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.data.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirName))
                       ip = (input("enter ip of your pc (for eg: 192.168.32.45): "))
                       portNo = int(input("enter a port no (for eg: 9001): "))
                       sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(ip,portNo))
                       os.system("hadoop namenode -format")
                       sub.getoutput("hadoop-daemon.sh start namenode")
                       os.system("jps")

       def httpddocker():
                      os.system("sudo  dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                      os.system("sudo  dnf install docker-ce --allowerasing  -y")
                      os.system("sudo systemctl start docker")
                      os.system("sudo systemctl enable docker")
                      os.system("sudo systemctl status docker")

                      x=input("enter os name : ")
                      os.system("docker pull {}".format(x))
                      os.system("docker images")
                      y=input("enter conatiner os name : ")
                      z=input("enter image   name : ")
                      t=input("enter the port name : ")
                      os.system("docker run -dit --name {} -p {}:80   {}".format(y,t,z))
                      img=input("enter the os name : ")
                      os.system("docker exec i {} /usr/sbin/httpd".format(img))
                      image=input("enter the container name : ")
                      os.system("docker exec {} yum install httpd -y".format(image))
                      os.system("docker exec {} yum install net-tools -y")

                      os.system("systemctl start  httpd")
                      os.chdir("/var/www/html")
                      x=input("enter the file name : ")
                      os.system("cat > {}.html".format(x))
                      os.system("ifconfig")
                      c=input("enter the system ip addres : ")
                      os.system("curl -I  http://{}/{}.html".format(c,x))

       if x==1:
            confhttpd()
       if x==2:
            confdocker()


       if x==3:
            createpv()
            extendlv()
            reducelv()
            vgextend()


       if x==4:
            yumconf()

       if x==5:
            namenode()

       if x==6:
            datanode()

       if x==7:
            httpddocker()
       if x==8:
            exit()



   else:
       print("Enter A Valid Input")
