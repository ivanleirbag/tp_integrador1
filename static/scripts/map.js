const map = L.map('map').setView([-34.6037, -58.3816], 5); // Centrado en Argentina

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

let marker;

map.on('click', function (e) {
    /**
     * @brief Handles click events on the map to place a marker and fetch location info.
     * @param {Object} e - The Leaflet event object containing click coordinates.
     */
    const { lat, lng } = e.latlng;
    if (marker) marker.setLatLng(e.latlng);
    else marker = L.marker(e.latlng).addTo(map);

    fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lng}&format=json`)
        .then(res => res.json())
        .then(data => {
            const display_name = data.display_name;
            document.getElementById('cityInput').value = display_name;
        })
        .catch(err => console.error("Error al obtener datos de ubicación:", err));
});
