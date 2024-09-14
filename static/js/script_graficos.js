document.addEventListener('DOMContentLoaded', function () {
    // Graficos de Boyaca
    if (typeof graficos.Graf_Boyaca !== 'undefined') {
        Plotly.newPlot('torta1Chart1', graficos.Graf_Boyaca[0].data, graficos.Graf_Boyaca[0].layout);
        Plotly.newPlot('torta2Chart1', graficos.Graf_Boyaca[1].data, graficos.Graf_Boyaca[1].layout);
        Plotly.newPlot('barrasChart1', graficos.Graf_Boyaca[2].data, graficos.Graf_Boyaca[2].layout);
        Plotly.newPlot('lineasChart1', graficos.Graf_Boyaca[3].data, graficos.Graf_Boyaca[3].layout);
    }

    // Graficos de Cundinamarca
    if (typeof graficos.Graf_Cundinamarca !== 'undefined') {
        Plotly.newPlot('torta1Chart2', graficos.Graf_Cundinamarca[0].data, graficos.Graf_Cundinamarca[0].layout);
        Plotly.newPlot('torta2Chart2', graficos.Graf_Cundinamarca[1].data, graficos.Graf_Cundinamarca[1].layout);
        Plotly.newPlot('barrasChart2', graficos.Graf_Cundinamarca[2].data, graficos.Graf_Cundinamarca[2].layout);
        Plotly.newPlot('lineasChart2', graficos.Graf_Cundinamarca[3].data, graficos.Graf_Cundinamarca[3].layout);
    }
});