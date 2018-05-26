#!/bin/bash

#Comprovamos que se executa con privilegios de root o sudo
if ! [ `id -u` -eq 0 ]; then
        echo "You must execute the script with root or sudo privileges!"
        exit 4
fi

#Ruta al fichero de logs
LOG="/var/log/ldapadd.log"

#Creamos un csv donde guardar los usuarios y sus contraseñas para luego mandarlas por carta a los usuarios
FILE_USERS='./users.csv'
echo "NAME,UID,PASSWORD,MAIL" > $FILE_USERS

#Recibimos csv via parametro y hacemos las comprovaciones pertinentes
if ! [ "$#" -eq "1" ]; then
        echo "[`date -u`] [ERROR] No file given to ldapadd script" >> $LOG
        exit 1
elif ! [ -f $1 ]; then
        echo "[`date -u`] [ERROR] The given parameter is not a file for the ldapadd script" >> $LOG
        exit 2
fi

file=$1

#Comprovamos que el fichero de entrada es valido
if ! `cat $file | awk 'BEGIN{FS=OFS=","} NF!=2{exit 1}'`; then
        echo "[`date -u`] [ERROR] The csv input file does not match the correct criteria of two values per line separated by coma" >> $LOG
        exit 3
fi

echo "[`date -u`] [INFO] Starting to transform input file" >> $LOG 
#Eliminamos caracteres con cosas raras
sed -i 'y/āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛñÑ/aaaaeeeeiiiioooouuuuuuuuAAAAEEEEIIIIOOOOUUUUUUUUnÑ/' $file

#Eliminamos el espacio que se genera en caso de no tener segundo apellido
sed -i 's/ ,/,/g' $file
sed -i 's/, /,/g' $file

#Eliminamos lineas vacias
sed -i '/^$/d' $file

echo "[`date -u`] [INFO] Starting to proces file and to load users to ldap domain" >> $LOG
while read i; do
        #Generamos uid para el usuario para consultar si existe en el directorio
        uid=`echo $i | awk -F"," '{ print $2"."$1 }' | tr '[A-Z]' '[a-z]' | awk '{ print $1 }'`

        if ! `slapcat | grep $uid &> /dev/null`; then
                #Sacamos de la base de datos de ldap el ultimo uidNumber
                uidN=`slapcat | awk '{ if ($1 == "uidNumber:") { print $2 } }' | sort -r | head -1`

                # En caso de no tener ningun usuario previo en el ldap
                if [ -z $uidN ]; then
                        uidN="2000"
                fi

                uidN=`echo $((uidN + 1)) | bc -l`

                #Genramos cn y sn
                cn=`echo $i | awk -F"," '{ print $2" "$1 }'`
                sn=`echo $i | awk -F"," '{ print $1 }'`

                #Generamos una password random de seis caracteres y la ciframos con slappasswd
                passwd=`tr -cd '[:alnum:]' < /dev/urandom | fold -w6 | head -n1`
                cipher_pass=`slappasswd -s $passwd`

                #Generamos el ldif para subir el usuario al dominio.
                cat > temporaluser.ldif <<EOL
                dn: uid=$uid,ou=People,dc=elita,dc=local
                objectClass: top
                objectClass: posixAccount
                objectClass: inetOrgPerson
                objectClass: person
                cn: $cn
                uid: $uid
                uidNumber: $uidN
                gidNumber: 2000
                homeDirectory: /home/$uid
                loginShell: /bin/bash
                userPassword: $cipher_pass
                sn: $sn
                mail: $uid@elita.local
EOL

                #Subimos el ldif al domino
                ldapadd -x -D 'cn=admin,dc=elita,dc=local' -f temporaluser.ldif -w 'qwert!"·45' &> /dev/null
                #ldapdelete -x -D 'cn=admin,dc=elita,dc=local' "uid=$uid,ou=People,dc=elita,dc=local" -w 'qwert!"·45'
                echo "[`date -u`] [CORRECT] The user with uid [$uid] was successfully added to the domain" >> $LOG
                rm -rf temporaluser.ldif

                #Una vez subido el usuario al dominio ldap añadimos el uid i la password a un fichero para luego mandar las contraseñas a los usuarios
                echo "$cn,$uid,$passwd,$uid@elita.local" >> $FILE_USERS
        else
                #Buscamos la linea del usuari en el fichero csv
                line=`cat $file | grep "$i" -n | awk -F":" '{ print $1 }'`
                echo "[`date -u`] [ERROR] The user with uid [$uid] in line $line already exists in the domain" >> $LOG
        fi
done < $file

exit 0
