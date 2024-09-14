function openTab(evt, tabName) {
    // Ocultar todos los contenidos de las pestañas
    var i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Eliminar la clase "active" de todos los botones
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
    }

    // Mostrar el contenido de la pestaña actual y agregar la clase "active" al botón de la pestaña
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function openSubTab(evt, subTabName) {
    // Ocultar todos los contenidos de las subpestañas
    var i, subtabcontent, subtabbuttons;
    subtabcontent = document.getElementsByClassName("subtab-content");
    for (i = 0; i < subtabcontent.length; i++) {
        subtabcontent[i].style.display = "none";
    }

    // Eliminar la clase "active" de todos los botones de subpestañas
    subtabbuttons = document.getElementsByClassName("subtab-button");
    for (i = 0; i < subtabbuttons.length; i++) {
        subtabbuttons[i].className = subtabbuttons[i].className.replace(" active", "");
    }

    // Mostrar el contenido de la subpestaña actual y agregar la clase "active" al botón de la subpestaña
    document.getElementById(subTabName).style.display = "block";
    evt.currentTarget.className += " active "
}
