fetch('/api/total_expression')
  .then(response => response.json())
  .then(data => {
     document.getElementById('total').innerHTML = 'Total : ' + data.total_expression;
});

fetch('/api/expression_counts')
  .then(response => response.json())
  .then(data => {
    const labels = Object.keys(data.date_counts);
    const counts = Object.values(data.date_counts);

    const ctx = document.getElementById('linechart').getContext('2d');
    new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Expressions',
                    data: counts,
                    backgroundColor: 'rgba(255, 99, 132, 0.6)',
                    borderColor: 'rgba(255, 99, 132, 0.6)',
                }]
            }, 
            options: {
                maintainAspectRatio: false,
                responsive: true,
                scales: {
                    x: {
                        ticks: {
                            autoSkip: false, 
                            maxRotation: 90,
                            minRotation: 0
                        }
                    }
                },
                plugins: {
                    legend: {
                      position: 'top',
                    },
                    title: {
                      display: true,
                      text: 'Monthly Expression'
                    }
                  }
              },

        });
});

function getRandomSample(obj, sampleSize) {
    const keys = Object.keys(obj);
    const randomKeys = keys.sort(() => 0.5 - Math.random()).slice(0, sampleSize);
    const sample = {};
    randomKeys.forEach(key => {
        sample[key] = obj[key];
    });
    return sample;
}

fetch('/api/common_words')
    .then(response => response.json())
    .then(res => {
        const sampleSize = 20;
        const sampledWords = getRandomSample(res.common_words, sampleSize);

        const labels = Object.keys(sampledWords);
        const values = Object.values(sampledWords);

        const freq = document.getElementById('barchart').getContext('2d');

        new Chart(freq, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Sample',
                    data: values,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    },
                    x: {
                        ticks: {
                            autoSkip: false, 
                            maxRotation: 90,
                            minRotation: 0
                        }
                    }
                },
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Common Words'
                    }
                }
            },
        });

    });

fetch('/api/emotion_distribution')
  .then(response => response.json())
  .then(data => {
    const sad = data.distribution['Sad'];
    const joy = data.distribution['Joy'];
    const love = data.distribution['Love'];
    const anger = data.distribution['Anger'];
    const fear = data.distribution['Fear'];
    const surprice = data.distribution['Surprice'];

    const ctx = document.getElementById('doughnutchart').getContext('2d');
    new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Sad', 'Joy', 'Love', 'Anger', 'Fear', 'Surprice'],
                datasets: [{
                    data: [sad, joy, love, anger, fear, surprice],
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.6)',
                        'rgba(255, 206, 86, 0.6)', 
                        'rgba(255, 105, 180, 0.6)',
                        'rgba(255, 99, 132, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)' 
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Emotional Distribution'
                    }
                }
            },
        });
});

fetch('/api/common_words')
   .then(response => response.json())
   .then(data => {
     const word = Object.entries(data.common_words);

     const resizeCanvas = () => {
       const canvas = document.getElementById('word-cloud-canvas');
       const style = getComputedStyle(canvas);
       canvas.width = parseInt(style.width);
       canvas.height = parseInt(style.height);
     };

     const drawWordCloud = () => {
       resizeCanvas();
       const words = word;
       const wordCloudCanvas = document.getElementById('word-cloud-canvas');
       const elements = [wordCloudCanvas];
       const options = {
        list: words,
        gridSize: 12,
        weightFactor: 8,
        fontFamily: "sans-serif",
        color: 'random-dark',
        rotateRatio: 0,
        rotationSteps: 2,
        shape: "square",
        ellipticity: 0.6,
        shrinkToFit: true,
        minSize: 6,
        classes: 'word-cloud-item',
       };
       WordCloud(elements, options);   
     };

    window.addEventListener('resize', drawWordCloud);
    window.addEventListener('load', drawWordCloud);
    drawWordCloud();
});
