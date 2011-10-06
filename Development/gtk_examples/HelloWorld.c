#include <gtk/gtk.h> 

// by default search in /usr/include
// gcc -g -Wall HelloWorld.c -o test

int main (int argc, char **argv)
{
    GtkWidget *window, *label;

    gtk_init (&argc, &argv); // always necessary
    
    // create graphic components...
    window = gtk_window_new (GTK_WINDOW_TOPLEVEL); // asi se crean los widgets en GTK
    g_signal_connect (window, "delete-event", G_CALLBACK (gtk_main_quit), NULL);

    label = gtk_label_new ("Hello World!"); 

    // attach label to window using pointers...
    //gtk_container_add ((GtkContainer *)window, label);
    gtk_container_add (GTK_CONTAINER (window), label); // secure cast that checks type

    // show window...
    gtk_widget_show_all (window);

    /* All GTK applications must have a gtk_main(). Control ends here
     * and waits for an event to occur (like a key press or
     * mouse event). */
    gtk_main ();

    return 0;
}

// pkg-config --modversion gtk+-2.0
// pkg-config --libs gtk+-2.0
// $ sudo apt-get install libgtk2.0-dev
// gcc -g -Wall `pkg-config --cflags --libs gtk+-2.0` HelloWorld.c -o test
// $devhelp
