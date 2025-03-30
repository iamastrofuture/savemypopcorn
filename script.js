const seriesList = [
    { name: 'Family Guy', url: 'family-guy-season-1' },
    { name: 'The Simpsons', url: 'the-simpsons-season-1' },
    { name: 'South Park', url: 'south-park-season-1' }
    // Add more series here
];

// Sort series alphabetically
seriesList.sort((a, b) => a.name.localeCompare(b.name));

const seriesContainer = document.getElementById('series-list');
seriesList.forEach(series => {
    const link = document.createElement('a');
    link.href = `/${series.url}/index.html`;  // Link to the season page
    link.innerText = series.name;
    seriesContainer.appendChild(link);
});

document.getElementById('search').addEventListener('input', (event) => {
    const query = event.target.value.toLowerCase();
    const filteredSeries = seriesList.filter(series => 
        series.name.toLowerCase().includes(query)
    );
    seriesContainer.innerHTML = ''; // Clear previous list
    filteredSeries.forEach(series => {
        const link = document.createElement('a');
        link.href = `/${series.url}/index.html`;
        link.innerText = series.name;
        seriesContainer.appendChild(link);
    });
});