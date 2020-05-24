
import vozatexto
import sintetizador
import auto
import time
from win10toast import ToastNotifier

duracion = "None" 
modoPrueba = True
menuAyuda = True
tiempo = {'uno':1,'1':1,'dos':2,'2':2,'tres':3,'3':3,'cuatro':4,'4':4,'cinco':5,'5':5,'seis':6,'6':6,'siente':7,'7':7,'ocho':8,'8':8,'nueve':9,'9':9,'diez':10,'10':10}
a = True
toaster = ToastNotifier()
toaster.show_toast("Python ",
                   "Iniciando asistente de voz",
                   duration=3)
sintetizador.hablar("iniciando asistente de voz")

while True:
    try:
        texto = ""
        toaster.show_toast("Python ",
                   "Microfono Activo",
                   duration=1.5)
        texto = vozatexto.reconocer(duracion).lower()

        if ("modo" in texto and ("desactivar" in texto or "fin" in texto)  and "prueba" in texto):
            modoPrueba = True
        elif ("modo" in texto and ("activar" in texto or "iniciar" in texto) and "prueba" in texto):
            modoPrueba = False

        if (modoPrueba == False):
            sintetizador.hablar("modo de prueba activo, usted dijo: "+texto)


        if (("ajustar" in texto or "cambiar" in texto) and ("tiempo" in texto or "duracion" in texto)):
            if (duracion == "Mone"):
                actual = "es automatico por el sistema, a la espera que dejes de hablar,"
            else:
                actual = "es de "+duracion+" segundos,"
           
            sintetizador.hablar("el tiempo actual es de "+actual+" diga el nuevo valor, recuerde que el tiempo esta dado en segundos y debe ser entero, por favor diga un numero entre uno y diez")
            texto = vozatexto.reconocer("2").lower()
            aux2 = str(tiempo[texto])
            if (int(aux2) > 0 and int(aux2) < 11):
                sintetizador.hablar("el nuevo tiempo de escucha cambio a "+aux2+ " segundos.")
                duracion = aux2
            else:
                sintetizador.hablar("el numero dicho no fue entendido correctamente, queda definido forma automatica.")
                duracion = "None"

        if ("modo" in texto  and "ayuda" in texto):
            tex = 'Este es el modo ayuda, en este usted podrá mirar los diferentes módulos y se le dirán como son los comandos, ¿por favor diga que ayuda necesita?  Puede elegir entre navegación, configuración o escritura.'
            sintetizador.hablar(tex)   
            while menuAyuda:
                texto = vozatexto.reconocer("None").lower()
                sintetizador.hablar('muy bien, ')
                if ("navegación" in texto or "navegacion" in texto): 
                    tex = 'En el módulo de navegación puede realizar las siguientes acciones, como primer comando esta, abrir WhatsApp, que sirve para abrir la aplicación, de igual manera esta el comando, cerrar WhatsApp, que cierra el aplicativo, otra funcionalidad  es ,minimizar, con esta ocultas tus conversaciones, si quieres volverla a abrir esta el comando, maximizar, o tembien puedes decir , restaurar, y volverá a aparecer tu ventana de WhatsApp, también están los comandos de scroll los cuales deberá decir, bajar, en caso de querer hacer un scroll hacia abajo o deberá decir, subir, en caso de querer hacer un scroll hacia arriba. ¿Desea preguntar sobre otro modulo? Responde con sí o no.'
                    sintetizador.hablar(tex) 
                    texto = vozatexto.reconocer("None").lower()
                    if ("si" in texto or "sí" in texto):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False
                elif ("configuración" in texto or "configuracion" in texto): 
                    tex = 'En el módulo de configuración puede realizar las siguientes acciones, como primer comando puedes tener un modo de prueba con el siguiente comando, activar modo de prueba, con este podrás probar el micrófono y dirá todo lo que tú le hables, también  está el comando para cambiar el tiempo de escucha y se activa diciendo, ajustar tiempo de escucha, donde  te pregunta el nuevo valor en segundos de 1 a 10 y lo parametriza. ¿Desea preguntar sobre otro modulo? Responde con sí o no'
                    sintetizador.hablar(tex) 
                    texto = vozatexto.reconocer("None").lower()
                    if ("si" in texto or "sí" in texto):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False 
                elif ("escritura" in texto):
                    tex = 'En el módulo de escritura básicamente tiene los comandos necesarios para escribir o iniciar un chat nuevo,  como primer comando esta, nuevo, con este abre el panel de los contactos y posteriormente con el comando, escribir, puedes escribir el nombre del contacto, luego con el comando, enter o aceptar,  podrás enviar la petición para crear el chat nuevo, y con los mismo anteriores comandos podrás escribir una vez ya dentro del chat, si quieres enviar un mensaje a un contacto especifico de manera rápida podrás hacerlo con el siguiente comando, enviar mensaje a, y al final le añades el nombre el contacto, un ejemplo puede ser, enviar mensaje a Daniel, el aplicativo reconocerá el contacto y luego te pedirá que digas tu mensaje y luego lo enviara. ¿Desea preguntar sobre otro modulo? Responde con sí o no'  
                    sintetizador.hablar(tex) 
                    texto = vozatexto.reconocer("None").lower()
                    if ("si" in texto or "sí" in texto):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False


        if ("abrir" in texto and modoPrueba):
            aux = "abriendo whatsapp"
            sintetizador.hablar(aux)
            auto.abrir()
        elif ("cerrar" in texto and modoPrueba):
            sintetizador.hablar("cerrando whatsapp")
            auto.cerrarVentana()                
        elif (("bajar" in texto or "scroll down" in texto or "scrolldown" in texto) and modoPrueba) :
            sintetizador.hablar('bajando')
            auto.scrollDown()
        elif (("abajo" in texto  or "siguiente" in texto) and modoPrueba):
            sintetizador.hablar('bajando siguiente chat') 
            auto.siguienteChat()   
        elif ("arriba" in texto and modoPrueba):
            sintetizador.hablar('subiendo al siguiente chat') 
            auto.anteriorChat()   
        elif (("subir" in texto or "scroll up" in texto or "scrollup" in texto) and modoPrueba) :
            sintetizador.hablar('subiendo') 
            auto.scrollUp()     
        elif ("minimi" in texto and modoPrueba):
            sintetizador.hablar('minimizando whatsapp')
            auto.minimizar()
        elif ((("restaurar" in texto) or ("maximi" in texto)) and modoPrueba):
            sintetizador.hablar('abriendo whatsapp')
            auto.abrir1()
        elif ((("aumen" in texto and  "letra" in texto) or  "acercar" in texto) and modoPrueba):
            sintetizador.hablar('aumentando letra')
            auto.acercar()
        elif ((("reducir" in texto and  "letra" in texto) or  "alejar" in texto) and modoPrueba):
            sintetizador.hablar('reduciendo letra')
            auto.alejar()
        elif ("nuevo" in texto and modoPrueba):
            sintetizador.hablar('creando nuevo chat')
            auto.nuevo()
        elif ("perfil" in texto and modoPrueba):
            sintetizador.hablar('mostrando perfil')
            auto.foto()
        elif ("escribir" in texto and modoPrueba):
            sintetizador.hablar('claro')
            texto = texto[texto.find("escribir")+9:]
            sintetizador.hablar('escribiendo '+texto)
            auto.escribir(texto)
        elif ("buscar" in texto and modoPrueba):
            sintetizador.hablar("buscando")
            texto = texto[texto.find("buscar")+7:]
            sintetizador.hablar('buscando '+texto)
        elif (("atras" in texto or "atrás" in texto or "escape" in texto) and modoPrueba):
            sintetizador.hablar('atras')
            auto.escape()
        elif (("elimin" in texto and "conver" in texto) and modoPrueba):
            sintetizador.hablar('eliminando conversacion')
            auto.borrar()
        elif ("finali" in texto and modoPrueba):
            sintetizador.hablar("finalizando prueba")
            auto.cerrarVentana()    
        elif (("aceptar" in texto or "enter" in texto) and modoPrueba):
            sintetizador.hablar("aceptar")
            auto.enter() 
        elif (("enviar" in texto and  "mensaje a" in texto) and modoPrueba): 
            aux = texto[texto.find("mensaje a")+10:]
            tex = 'que mensaje desea darle a ',aux,'?'
            sintetizador.hablar(tex)   
            texto = vozatexto.reconocer("None").lower()
            sintetizador.hablar('muy bien, enviando mensaje')
            auto.nuevo()
            auto.escribir(aux)
            time.sleep(1)
            auto.enter() 
            time.sleep(1)
            auto.escribir(texto)
            auto.enter() 
        elif (( "chat de" in texto) and modoPrueba): 
            aux = texto[texto.find("chat de")+7:]
            sintetizador.hablar('muy bien')
            auto.buscarChat()
            auto.escribir(aux)
            time.sleep(1)
            auto.enter()   
        elif (( "borrar" in texto and "todo" in texto) and modoPrueba): 
            sintetizador.hablar('muy bien')
            auto.borrarTodo()
        elif (( "borrar" in texto) and modoPrueba): 
            auto.borrarTexto()

    except Exception as e:
        print('Ocurrio un error', e)
