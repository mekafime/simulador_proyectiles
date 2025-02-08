function generarGrafica() {
    let u0 = document.getElementById("u0").value;
    let theta1 = document.getElementById("theta1").value;
    let theta2 = document.getElementById("theta2").value;

    let graph = document.getElementById("grafico");

    let url = `/plot?u0=${u0}&theta1=${theta1}&theta2=${theta2}`;
    graph.src = url;
    graph.style.display = "block"; // Muestra la imagen después de generarla
}
