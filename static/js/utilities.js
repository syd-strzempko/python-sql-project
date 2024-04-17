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

async function loadMap(entries) {
    // Austin TX centered
    const defaultPosition = { lat: 30.26, lng: -97.73 };
    // Request needed libraries
    //@ts-ignore
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    bounds = new google.maps.LatLngBounds();

    map = new Map(document.getElementById("map"), {
        zoom: 11,
        center: defaultPosition,
        mapId: key,
    });
    if (entries.length) {
        entries.forEach(entry => {
            const position = { lat: entry.lat, lng: entry.long}
            const marker = new AdvancedMarkerElement({
                map,
                position,
                title: entry.title,
                content: buildMarker(entry)
            });
            marker.addListener("click", () => toggleDetails(marker));
            bounds.extend(position);
        });
        map.fitBounds(bounds);
    }
    return map;
};

const toggleDetails = (marker) => {
    marker.content.classList.toggle('active');
}

const buildMarker = (entry) => {
    const content = document.createElement("div");
    content.classList.add('markerWrapper');
    if (entry.verified === 'False') {
        content.classList.add('unverified');
    }
    content.innerHTML = `
        <div class="markerIcon">
            <img src="/static/svg/tp_icon.svg" />
        </div>
        <div class="markerDetail">
            <a href="/entry/${entry.id}">${entry.title}</a>
            by <a href="/user/${entry.user.id}">${entry.user.name}</a> on ${entry.created}
        </div>
    `;
    return content;
}

const updateUserLocation = (geoMarker, map) => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (pos) => {
            let position = {
              lat: pos.coords.latitude,
              lng: pos.coords.longitude,
            };
            geoMarker.position = position;
            map.setCenter(position);
          },
          () => {},
        );
    } else { return null };
};

function initUserLocation(map) {
    async function initLocation() {
        const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
              (pos) => {
                let position = {
                  lat: pos.coords.latitude,
                  lng: pos.coords.longitude,
                };
                geoMarker = new google.maps.marker.AdvancedMarkerElement({
                    map,
                    position,
                    gmpDraggable: (window.location.pathname.includes('new')),
                    title: 'Selected Location'
                });
                map.setCenter(position);
                document.getElementById("geolocation")?.setAttribute("value", `${position.lat.toString()},${position.lng.toString()}`);
                if (window.location.pathname.includes('new')) {
                    geoMarker.addListener("dragend", (event) => {
                        const position = geoMarker.position;
                        map.setCenter(position);
                        document.getElementById("geolocation")?.setAttribute("value", `${position.lat.toString()},${position.lng.toString()}`);
                    });
                }
                return geoMarker;
              },
              () => {
                console.log(error);
              },
            );
        } else {
            // Location not enabled; set to default Austin
            geoMarker = new google.maps.marker.AdvancedMarkerElement({
                map,
                position: { lat: 30.26, lng: -97.73 },
                gmpDraggable: true,
                title: 'Selected Location'
            });
            map.setCenter(position);
            document.getElementById("geolocation")?.setAttribute("value", `${position.lat.toString()},${position.lng.toString()}`);
            geoMarker.addListener("dragend", (event) => {
                const position = geoMarker.position;
                map.setCenter(position);
                document.getElementById("geolocation")?.setAttribute("value", `${position.lat.toString()},${position.lng.toString()}`);
            });
            return geoMarker;
        };
    }
    try {
        initLocation();
    } catch (error) {
        console.log(error);
    }
}