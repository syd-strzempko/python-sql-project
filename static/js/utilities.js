function toggleList(turnOn) {
    const list = document.getElementById('listview');
    const map = document.getElementById('mapview');
    const active = document.getElementsByClassName('tog active')?.[0];
    if (turnOn && list.hidden) {
        active.classList.remove('active');
        event.target.classList.toggle('active');
        list.hidden = false;
        map.hidden = true;
    } else if (!turnOn && map.hidden) {
        active.classList.remove('active');
        event.target.classList.toggle('active');
        list.hidden = true;
        map.hidden = false;
    }
};

function loadMap(entries) {
    // Initialize and add the map
    let map;

    async function initMap() {
        // Austin TX centered
        const position = { lat: 30.26, lng: -97.73 };
        // Request needed libraries
        //@ts-ignore
        const { Map } = await google.maps.importLibrary("maps");
        const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

        // The map, centered at Uluru
        map = new Map(document.getElementById("map"), {
            zoom: 6,
            center: position,
            mapId: "DEMO_MAP_ID",
        });

        entries.forEach(entry => {
            const marker = new AdvancedMarkerElement({
                map,
                position: { lat: entry.lat, lng: entry.long},
                title: entry.title,
                content: buildMarker(entry)
            });
            marker.addListener("click", () => toggleDetails(marker));
        });
    }

    try {
        initMap();
    } catch (error) {
        console.log(error);
    }
};

const toggleDetails = (marker) => {
    marker.content.classList.toggle('active');
}

const buildMarker = (entry) => {
    const content = document.createElement("div");
    content.classList.add('markerWrapper');
    content.innerHTML = `
        <div class="markerIcon">
            <img src="static/svg/tp_icon.svg" />
        </div>
        <div class="markerDetail">
            <a href="/${entry.id}">${entry.title}</a>
            by <a href="/${entry.author}">${entry.author}</a> on ${entry.created}
        </div>
    `;
    return content;
}