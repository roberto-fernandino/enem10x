function updateChart(chart, newLabels, newData){
    chart.data.labels = newLabels;
    chart.data.datasets[0].data = newData;
    chart.update();

};

$('#timeFilter').change(function() {
    const selectedFilter = $(this).val();
    $.ajax({
        url: 'filter-graph-time/',
        type: 'GET',
        data: { filter: selectedFilter },
        success: function(response){
            // Grafico de Matematica
            const newLabels1 = response.graph_mat.newLabels;
            const newData1 = response.graph_mat.newData;
            updateChart(myChart1, newLabels1, newData1)

            // Grafico de Nat
            const newLabels2 = response.graph_nat.newLabels;
            const newData2 = response.graph_nat.newData;
            updateChart(myChart2, newLabels2, newData2)

            // Grafico de Lin
            const newLabels3 = response.graph_lin.newLabels;
            const newData3 = response.graph_lin.newData;
            updateChart(myChart3, newLabels3, newData3)

            // Grafico de hum
            const newLabels4 = response.graph_hum.newLabels;
            const newData4 = response.graph_hum.newData;
            updateChart(myChart4, newLabels4, newData4)

        },
        error: function(error) {
            console.log("erro: ", error)
        }

    });
});